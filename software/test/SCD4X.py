#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# Copyright (c) 2021 RS Components Ltd
# SPDX-License-Identifier: MIT License

'''
Python SCD4x Reader
'''

import time, argparse, csv, os
from smbus2 import SMBus, i2c_msg

SCD_ADDRESS = 0x62

FILE_MODE = 'w'

FILE_HEADER = ['timestamp', 'co2', 'temperature', 'humidity']

def get_data_ready(bus):
	write = i2c_msg.write(SCD_ADDRESS, [0xE4, 0xB8])
	read = i2c_msg.read(SCD_ADDRESS, 3)
	bus.i2c_rdwr(write, read)
	state = (list(read)[0] << 8) + list(read)[1]
	if state != 0x8000:
		return True
	else:
		return False

def read_sensor_data(bus):
	write = i2c_msg.write(SCD_ADDRESS, [0xEC, 0x05])
	read = i2c_msg.read(SCD_ADDRESS, 9)
	bus.i2c_rdwr(write, read)
	return list(read)

def main():
	parser = argparse.ArgumentParser(description='Reads an SCD4x sensor to a CSV file every 5 seconds.')
	parser.add_argument('-i', '--interval', metavar='interval', type=int, help='The sensor read interval (in seconds) - not used in this application')
	parser.add_argument('-f', '--filename', metavar='filename', type=str, help='The CSV file name', default=os.devnull)

	args = parser.parse_args()

	# Try open I2C bus
	try:
		i2c_bus = SMBus(1)
	except Exception as e:
		print("Could not open I2C bus! Reason {0}".format(e))

	file = args.filename

	with open(file, FILE_MODE) as handle:
		# Write the CSV file header
		csv_writer = csv.writer(handle, delimiter=',')
		csv_writer.writerow(FILE_HEADER)
		print("{0},{1},{2},{3}".format(FILE_HEADER[0], FILE_HEADER[1], FILE_HEADER[2], FILE_HEADER[3]))

		# Spin in a while loop until terminated

		try:
			# Start periodic measurement mode, update interval is 5s as per datasheet
			i2c_bus.write_i2c_block_data(SCD_ADDRESS, 0x21, [0xB1])

		except Exception as e:
			print("Could not start periodic measurements, reason {0}".format(e))

		while True:
			try:
				if get_data_ready(i2c_bus):
					sensor_data = read_sensor_data(i2c_bus)
					co2 = (sensor_data[0] << 8) + sensor_data[1]
					temperature = round(-45 + (175 * ((sensor_data[3] << 8) + sensor_data[4]) / 65535.0), 1)
					humidity = round(100 * ((sensor_data[6] << 8) + sensor_data[7]) / 65535.0, 1)

					timestamp = str(int(time.time()))

					csv_writer.writerow([timestamp, co2, temperature, humidity])
					print("{0},{1},{2},{3}".format(timestamp, co2, temperature, humidity))

				time.sleep(0.25)

			except KeyboardInterrupt:
				exit()

			except Exception as e:
				print("Caught exception {0}".format(e))

if __name__ == '__main__':
	main()