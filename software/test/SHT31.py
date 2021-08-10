#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# Copyright (c) 2021 RS Components Ltd
# SPDX-License-Identifier: MIT License

'''
Python SHT31 CSV logger
'''

import time, smbus, argparse, csv, os

SHT_ADDRESS = 0x44

DEFAULT_READ_INTERVAL = 5

FILE_MODE = 'w'

FILE_HEADER = ['timestamp', 'temperature', 'humidity']

def main():
	parser = argparse.ArgumentParser(description='Reads an SHT31 sensor to a CSV file every n seconds.')
	parser.add_argument('-i', '--interval', metavar='interval', type=int, help='The sensor read interval (in seconds)', default=DEFAULT_READ_INTERVAL)
	parser.add_argument('-f', '--filename', metavar='filename', type=str, help='The CSV file name', default=os.devnull)

	args = parser.parse_args()

	if args.interval < 1:
		parser.error("Minimum interval is 1s")
	
	'''
	Sit in a loop and read the SHT31 at the specified interval, then print to the CSV file
	'''

	# Try open I2C bus
	try:
		i2c_bus = smbus.SMBus(1)
	except Exception as e:
		print("Could not open I2C bus! Reason {0}".format(e))

	file = args.filename
	interval = args.interval

	with open(file, FILE_MODE) as handle:
		# Write the CSV file header
		csv_writer = csv.writer(handle, delimiter=',')
		csv_writer.writerow(FILE_HEADER)
		print("{0},{1},{2}".format(FILE_HEADER[0], FILE_HEADER[1], FILE_HEADER[2]))

		# Spin in a while loop until terminated
		while True:
			try:
				# Send measurement command (0x2C) and ask for high repeatability measurement (0x06)
				i2c_bus.write_i2c_block_data(SHT_ADDRESS, 0x2C, [0x06])

				# Delay for 0.5s, in high repeatability this is how long it takes to get a measurement
				time.sleep(0.5)

				'''
				Read 6 bytes of sensor data
				Temperature MSB, temperature LSB, temperature CRC, humidity MSB, humidity LSB, humidity CRC
				'''
				raw_data = i2c_bus.read_i2c_block_data(SHT_ADDRESS, 0x00, 6)

				# Calculate temperature & humidity values
				raw_temperature = raw_data[0] * 256 + raw_data[1]
				temperature = round(-45 + (175 * raw_temperature / 65535.0), 1)
				humidity = round(100 * (raw_data[3] * 256 + raw_data[4]) / 65535.0, 1)

				timestamp = str(int(time.time()))

				csv_writer.writerow([timestamp, temperature, humidity])
				print("{0},{1},{2}".format(timestamp, temperature, humidity))

				time.sleep(interval - 0.5)

			except KeyboardInterrupt:
				exit()

			except Exception as e:
				print("Caught exception {0}".format(e))

if __name__ == '__main__':
	main()
