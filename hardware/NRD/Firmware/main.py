import gc
import time
import _thread
import math
import machine
from i2c_responder import I2CResponder
from machine import Pin, Timer

sensor = Pin(4, Pin.IN)
led = Pin(2, Pin.OUT)
event_gpio = Pin(3, Pin.OUT)
scl = Pin(1, Pin.IN)

count = 0
event = False

cpm_averaging_time = 10 # CPM averaging time in seconds
current_cpm = 0
last_cpm_count = 0
current_cps = 0
last_cps_count = 0
i2c_data = [0]
led_enabled = True
gpio_output_enabled = False
counter_reset = False

def calculate_moving_average(new_data_point, data_list, average_size):
    # Add fresh data
    data_list.insert(0, new_data_point)
    try:
        # Remove nth item in list
        data_list.pop(average_size)
    except Exception as e:
        pass
    total = 0
    total = sum(data_list)
        
    value = math.ceil(total / len(data_list))
    if(value == None):
        return 0
    else:
        return value

def i2c_thread():
    global current_cps
    global current_cpm
    global led_enabled
    global gpio_output_enabled
    global counter_reset

    i2c = I2CResponder(0, sda_gpio=0, scl_gpio=1, responder_address=0x60)

    i2c_data = [0x0, 0x0]
    i2cTrafficTime = 0
    i2cWdtEnabled = False
    write_data = []
    replyByteCounter = 0

    while True:
        while not i2c.read_is_pending():
            gc.collect()
            
            # Check I2C WDT and reset if necessary
            if(i2cWdtEnabled and time.ticks_diff(time.ticks_ms(), i2cTrafficTime) > 10000):
                print("No I2C traffic with I2C WDT enabled! Resetting")
                machine.reset()
                
            if i2c.write_data_is_available():
                i2cTrafficTime = time.ticks_ms()
                replyByteCounter = 0
                i2c_data = i2c.get_write_data(max_size=2)
                
                if(len(i2c_data) >= 2):
                    # Update LED control variable
                    if(i2c_data[0] == 0x04):
                        if(i2c_data[1] == 0x01):
                            led_enabled = True
                            i2c_data.clear()
                        elif(i2c_data[1] == 0x00):
                            led_enabled = False
                            i2c_data.clear()
                    
                    # Reset all counters
                    if(i2c_data[0] == 0x05 and i2c_data[1] == 0x01):
                        counter_reset = True
                    
                    # Update GPIO event detection output control
                    if(i2c_data[0] == 0x06):
                        if(i2c_data[1] == 0x01):
                            gpio_output_enabled = True
                        elif(i2c_data[1] == 0x00):
                            gpio_output_enabled = False
                    
                    # Update I2C watchdog timeout control
                    if(i2c_data[0] == 0x07):
                        if(i2c_data[1] == 0x01):
                            i2cWdtEnabled = True
                        elif(i2c_data[1] == 0x00):
                            i2cWdtEnabled = False
                        
        i2cTrafficTime = time.ticks_ms()
        # Requested CPS data
        if(i2c_data[0] == 0x01):
            i2c.put_read_data(current_cps)

        # Requested CPM data
        if(i2c_data[0] == 0x02):
            i2c.put_read_data(bytearray(current_cpm.to_bytes(2, 'big'))[replyByteCounter])
            replyByteCounter += 1
        
        # Requested total count
        if(i2c_data[0] == 0x03):
            if(count > 4,294,967,295):
                count_capped = 4,294,967,295
            else:
                count_capped = count
            i2c.put_read_data(bytearray(count_capped.to_bytes(4, 'big'))[replyByteCounter])
            replyByteCounter += 1

        # Return LED enabled status
        if(i2c_data[0] == 0x04):
            i2c.put_read_data(led_enabled)
        
        # Return GPIO output enabled status
        if(i2c_data[0] == 0x06):
            i2c.put_read_data(gpio_output_enabled)
        
        # Return I2C WDT enabled status
        if(i2c_data[0] == 0x07):
            i2c.put_read_data(i2cWdtEnabled)
        
        # Check I2C WDT and reset if necessary
        if(i2cWdtEnabled and time.ticks_diff(time.ticks_ms(), i2cTrafficTime) > 10000):
            print("No I2C traffic with I2C WDT enabled! Resetting")
            machine.reset()

def count_thread():
    global event
    global count
    global cpm_averaging_time
    global current_cpm
    global current_cps
    global led_enabled
    global gpio_output_enabled
    global counter_reset

    ledOnTime = 0
    lastCpsCount = 0
    cpsStartTime = 0
    cpmStartTime = 0

    cps_sma_list = []
    cpm_sma_list = []
    while True:
        # Check to see if sensor has detected radiation
        if(sensor.value() == True):
            event = True
            count = count + 1

        # Turn on LED if event detected
        if(event and led_enabled and led.value() == False):
            ledOnTime = time.ticks_ms()
            event = False
            led.value(1)
            if(gpio_output_enabled):
                event_gpio.value(1)

        # Turn off LED after 5ms timeout (to make a blink)
        if(led.value() and time.ticks_diff(time.ticks_ms(), ledOnTime) > 5):
            led.value(0)
            if(gpio_output_enabled):
                event_gpio.value(0)

        # Calculate CPS & CPM every second
        if(time.ticks_diff(time.ticks_ms(), cpsStartTime) > 1000):
            current_cps = calculate_moving_average((count - lastCpsCount), cps_sma_list, 5)
            print("CPS: ", current_cps)
            
            # Calculate CPM from CPS * 60, averaged
            current_cpm = calculate_moving_average((current_cps * 60), cpm_sma_list, 5)
            print("CPM: ", current_cpm)
            # Reset tracking variables
            lastCpsCount = count
            cpsStartTime = time.ticks_ms()
        
        # Reset all counters
        if(counter_reset == True):
            current_cps = 0
            lastCpsCount = 0
            count = 0
            cps_sma_list.clear()
            cpm_sma_list.clear()
            counter_reset = False

i2c_thread_handle = _thread.start_new_thread(i2c_thread, ())
count_thread()
