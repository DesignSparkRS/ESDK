#!/usr/bin/env python3

# Copyright (c) 2021 RS Components Ltd
# SPDX-License-Identifier: MIT License

'''
Python SPS30 Reader
'''

import time, argparse, csv, os
from smbus2 import SMBus, i2c_msg

SPS_ADDRESS = 0x69

DEFAULT_READ_INTERVAL = 5

FILE_MODE = 'w'

FILE_HEADER = ['timestamp', 'pm1.0', 'pm2.5', 'pm4.0', 'pm10']

def calculateCRC(input):
	'''
	Taken from https://github.com/feyzikesim/sps30
	'''
	crc = 0xFF
	for i in range (0, 1):
		crc = crc ^ input[i]
		for j in range(7, 0, -1):
			if crc & 0x80:
				crc = (crc << 1) ^ 0x31
			else:
				crc = crc << 1
	crc = crc & 0x0000FF
	return crc

def start_measurement(bus):
	# This command asks for measurements in u16 values
	command = [0x00, 0x10, 0x05, 0x00]
	crc = calculateCRC(command[2:4])
	command.append(crc)
	write = i2c_msg.write(SPS_ADDRESS, command)
	bus.i2c_rdwr(write)

def data_ready(bus):
	write = i2c_msg.write(SPS_ADDRESS, [0x02, 0x02])
	read = i2c_msg.read(SPS_ADDRESS, 3)
	bus.i2c_rdwr(write)
	time.sleep(0.001)
	bus.i2c_rdwr(read)
	if list(read)[1] == 0x01:
		return True
	else:
		return False

def get_data(bus):
	write = i2c_msg.write(SPS_ADDRESS, [0x03, 0x00])
	read = i2c_msg.read(SPS_ADDRESS, 30)
	bus.i2c_rdwr(write)
	time.sleep(0.001)
	bus.i2c_rdwr(read)
	raw_data = list(read)

	# Convert to integer values
	pm10 = (raw_data[0] << 8) + raw_data[1]
	pm25 = (raw_data[3] << 8) + raw_data[4]
	pm40 = (raw_data[6] << 8) + raw_data[7]
	pm100 = (raw_data[9] << 8) + raw_data[10]

	data = {
	"pm1.0": pm10,
	"pm2.5": pm25,
	"pm4.0": pm40,
	"pm10": pm100
	}

	return data

def main():
	parser = argparse.ArgumentParser(description='Reads an SPS30 to a CSV file every n seconds.')
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

	with open(file, FILE_MODE) as handle:
		# Write the CSV file header
		csv_writer = csv.writer(handle, delimiter=',')
		csv_writer.writerow(FILE_HEADER)
		print("{0},{1},{2},{3},{4}".format(FILE_HEADER[0], FILE_HEADER[1], FILE_HEADER[2], FILE_HEADER[3], FILE_HEADER[4]))

		try:
			start_measurement(i2c_bus)
		except Exception as e:
			print("Could not start periodic measurements, reason {0}".format(e))

		while True:
			try:
				if data_ready(i2c_bus):
					data = get_data(i2c_bus)

					timestamp = str(int(time.time()))

					csv_writer.writerow([timestamp, data["pm1.0"], data["pm2.5"], data["pm4.0"], data["pm10"]])
					print("{0},{1},{2},{3},{4}".format(timestamp, data["pm1.0"], data["pm2.5"], data["pm4.0"], data["pm10"]))

				time.sleep(0.25)

			except KeyboardInterrupt:
				exit()

			except Exception as e:
				print("Caught exception {0}".format(e))

if __name__ == '__main__':
	main()