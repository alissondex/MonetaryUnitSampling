# implement monetary unit sampling algorithm

from random import uniform

def execute(reader, index):

	unit_values = [{}]
	lines = []
	total = 0
	size = 0

	for row in reader:
		value = float(row[index])
		total += value
		lines.append({'Value': value, 'Accumulated': total})

		size += 1

	interval = float(total / size)

	sampling = []
	next_value = uniform(1, interval);

	print('Total.....: ' + str(total))
	print('Lenght....: ' + str(size))
	print('Interval..: ' + str(interval))
	print('Random....: ' + str(next_value))

	register = 0
	for line in lines:
		if line['Accumulated'] > next_value:
			sampling.append(register)
			next_value += interval
		register += 1

	for s in sampling:
		print('Index of sampling: ' + str(s))

	return sampling