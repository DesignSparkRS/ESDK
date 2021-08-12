#!/usr/bin/env python3

# Copyright (c) 2021 RS Components Ltd
# SPDX-License-Identifier: MIT License

'''
Python SVM40 Reader
'''

import time, argparse, csv, os
from smbus2 import SMBus, i2c_msg

SVM_ADDRESS = 0x6A

DEFAULT_READ_INTERVAL = 5

FILE_MODE = 'w'

FILE_HEADER = ['timestamp', 'voc', 'temperature', 'humidity']

def read_sensor_data(bus):
	write = i2c_msg.write(SVM_ADDRESS, [0x03, 0xA6])
	read = i2c_msg.read(SVM_ADDRESS, 9)
	bus.i2c_rdwr(write)
	time.sleep(0.001) # Delay necessary due to response time of microcontroller on SVM40
	bus.i2c_rdwr(read)
	return list(read)

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

	with open(file, FILE_MODE) as handle:
		# Write the CSV file header
		csv_writer = csv.writer(handle, delimiter=',')
		csv_writer.writerow(FILE_HEADER)
		print("{0},{1},{2},{3}".format(FILE_HEADER[0], FILE_HEADER[1], FILE_HEADER[2], FILE_HEADER[3]))

		# Spin in a while loop until terminated

		try:
			# Reset device
			i2c_bus.write_i2c_block_data(SVM_ADDRESS, 0xD3, [0x04])
		except Exception as e:
			print("Could not reset device, reason {0}".format(e))

		time.sleep(1)

		try:
			# Start periodic measurement mode
			i2c_bus.write_i2c_block_data(SVM_ADDRESS, 0x00, [0x10])
		except Exception as e:
			print("Could not start periodic measurements, reason {0}".format(e))

		while True:
			try:
				sensor_data = read_sensor_data(i2c_bus)
				voc = round(((sensor_data[0] << 8) + sensor_data[1]) / 10, 1)
				humidity = round(((sensor_data[3] << 8) + sensor_data[4]) / 100, 1)
				temperature = round(((sensor_data[6] << 8) + sensor_data[7]) / 200, 1)

				timestamp = str(int(time.time()))

				csv_writer.writerow([timestamp, voc, temperature, humidity])
				print("{0},{1},{2},{3}".format(timestamp, voc, temperature, humidity))

				time.sleep(interval)

			except KeyboardInterrupt:
				exit()

			except Exception as e:
				print("Caught exception {0}".format(e))

if __name__ == '__main__':
	main()
