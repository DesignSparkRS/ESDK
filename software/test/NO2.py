#!/usr/bin/env python3

# Copyright (c) 2021 RS Components Ltd
# SPDX-License-Identifier: MIT License

'''
Python NO2 Click Reader
'''

import time, argparse, csv, os
from smbus2 import SMBus, i2c_msg

LMP_ADDRESS = 0x48
ADC_ADDRESS = 0x4D

DEFAULT_READ_INTERVAL = 5

FILE_MODE = 'w'

FILE_HEADER = ['timestamp', 'no2']

def set_defaults(bus):
	# Datasheet defaults
	bus.write_byte_data(LMP_ADDRESS, 0x12, 0x00) # Deep sleep mode
	bus.write_byte_data(LMP_ADDRESS, 0x01, 0x00) # Unlock registers
	bus.write_byte_data(LMP_ADDRESS, 0x10, 0x03) # TIACN - External resistance, 100R
	bus.write_byte_data(LMP_ADDRESS, 0x11, 0x20) # REFCN - internal ref, 50% int. zero, negative, 0% bias


def get_no2_ppm(bus):
	read = i2c_msg.read(ADC_ADDRESS, 2)
	bus.i2c_rdwr(read)
	read = list(read)
	raw_value = (read[0] << 8) + read[1]
	no2 = round((raw_value / 4095.0) * 1000)
	return no2

def main():
	parser = argparse.ArgumentParser(description='Reads an SVM40 eval board to a CSV file every n seconds.')
	parser.add_argument('-i', '--interval', metavar='interval', type=int, help='The sensor read interval (in seconds)', default=DEFAULT_READ_INTERVAL)
	parser.add_argument('-f', '--filename', metavar='filename', type=str, help='The CSV file name', default=os.devnull)

	args = parser.parse_args()

	if args.interval < 1:
		parser.error("Minimum interval is 1s")

	# Try open I2C bus
	try:
		i2c_bus = SMBus(1)
	except Exception as e:
		print("Could not open I2C bus, reason {0}".format(e))

	file = args.filename
	interval = args.interval

	'''
	The default settings in the AFE are suitable for the SPEC sensor
	Nothing needs to be changed, hence the lack of configuration
	'''

	try:
		# Enable AFE
		set_defaults(i2c_bus)

	except Exception as e:
		print("Could not start AFE, reason {0}".format(e))

	with open(file, FILE_MODE) as handle:
		# Write the CSV file header
		csv_writer = csv.writer(handle, delimiter=',')
		csv_writer.writerow(FILE_HEADER)
		print("{0},{1}".format(FILE_HEADER[0], FILE_HEADER[1]))

		# Spin in a while loop until terminated

		while True:
			try:

				no2 = get_no2_ppm(i2c_bus)

				timestamp = str(int(time.time()))

				csv_writer.writerow([timestamp, no2])
				print("{0},{1}".format(timestamp, no2))

				time.sleep(interval)

			except KeyboardInterrupt:
				exit()

			except Exception as e:
				print("Caught exception {0}".format(e))

if __name__ == '__main__':
	main()
