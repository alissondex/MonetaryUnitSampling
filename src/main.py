import sys
import csv

import mus


if len(sys.argv) > 1:
	arguments = list(sys.argv)

	if arguments[1] == '--help':
		print('Write help ....')
	else:
		print('\'' + arguments[1] + '\'' + ' is not valid')

	quit()

path_to_file = input('Path to file: ')

try:
	with open(path_to_file, 'r') as csv_file:
		reader = csv.reader(csv_file, delimiter=';')
		columns = next(reader)

		for i in range(len(columns)):
			print(str(i) + ' - ' + columns[i])

		while True:
			try:
				monetary_unit = int(input('Chose the number of column for calculated: '))
				break
			except ValueError:
				continue

		print(monetary_unit)

		sampling = mus.execute(reader, monetary_unit)

except FileNotFoundError:
	print('file ' + path_to_file + ' not found')
	quit()