#!/usr/bin/env python

import sys

def arg_check():
	if len(sys.argv) < 2:
		print 'You did not enter a file name to parse!'
		exit

	return

def ingest(file_location):
	lines = [line.split() for line in open(file_location).read().split('\n') if line ]

	return(lines)

def print_msg(correct, total, alg):
	print alg, ':', correct, '/', total	

	return

def fixed_true(lines):
	correct = 0
	total = 0

	for line in lines:
		path = str(line[1])
		if path == "@":
			 correct += 1

		total += 1	

	return(correct, total)

def static_first(lines):
	total = 0
	correct = 0
	table = [[0, 0, 0]] * 1024
	for line in lines:
	#slot with mask of 10 bits will give us 1024 slots

		path = str(line[1])
		branch = int(line[0], 0)
		slot = branch & ~(~0 << 10)
		tag = branch >> 10
		pred = (1 << 0)
		dirty = 1

		if not (table[slot][1]):
		#adds new entry
			table[slot] = [tag, dirty, pred]

		elif (table[slot][0] != tag):
		#adds new address entry to slot
			table[slot] = [tag, dirty, pred]

		elif (table[slot][0] == tag):
			#print 'we use this prediction'
			pass

		else:
			#print 'should never happen....'
			pass
		

		pred = table[slot][2] & ( 0 | (1 << 0) )
		#print pred
		if (pred) and (path == '@'):
			correct += 1

		elif not(pred) and (path == '.'):
			correct += 1

		else:
			table[slot][2] += 1										
						
		total += 1
	#print table
	return(correct, total)

def bimodal(lines):
#
#implement ttl and dirty bit
	correct = 0
	total = 0
	table = [[0, 0, 0]] * 1024
	for line in lines:
	#slot with mask of 10 bits will give us 1024 slots

		path = str(line[1])
		branch = int(line[0], 0)
		slot = branch & ~(~0 << 10)
		tag = branch >> 10
		pred = (1 << 1) | (1 << 0)
		dirty = 1

		if not (table[slot][1]):
		#adds new entry
			table[slot] = [tag, dirty, pred]

		elif (table[slot][0] != tag):
		#adds new address entry to slot
			table[slot] = [tag, dirty, pred]

		elif (table[slot][0] == tag):
			pass

		else:
			pass
		

		pred = table[slot][2] & ( 0 | (1 << 1) )
		if (pred) and (path == '@'):
			correct += 1
			table[slot][2] = table[slot][2] & ((1 << 1) | (0 << 0))

		elif not(pred) and (path == '.'):
			correct += 1
			table[slot][2] = table[slot][2] & ((1 << 1) | (0 << 0))

		else:
			table[slot][2] += 1										
						
		total += 1


	return(correct, total)

def two_layer(lines):
	correct = 0
	total = 0
	table = [[0, 0, 0, 0, 0, 0, 0]] * 1024
	for line in lines:
	#slot with mask of 10 bits will give us 1024 slots

		path = str(line[1])
		branch = int(line[0], 0)
		slot = branch & ~(~0 << 10)
		tag = branch >> 10
		dirty = 1
		hist = (0 << 1) | (0 << 0)
		spot00 = (0 << 3) | (0 << 2) | (0 << 1) | (0 << 0)
		spot01 = (0 << 3) | (1 << 2) | (1 << 1) | (1 << 0)
		spot10 = (1 << 3) | (0 << 2) | (0 << 1) | (1 << 0)
		spot11 = (1 << 3) | (1 << 2) | (1 << 1) | (0 << 0)

		if not (table[slot][1]):
		#adds new entry
			table[slot] = [tag, dirty, hist, spot00, spot01, spot10, spot11]

		elif (table[slot][0] != tag):
		#adds new address entry to slot
			table[slot] = [tag, dirty, hist, spot00, spot01, spot10, spot11]

		elif (table[slot][0] == tag):
			pass

		else:
			pass

		check_hist = table[slot][2] & ((1 << 1) | (1 << 0))
		save_bit = table[slot][2] & (0 | (1 << 0))

		if check_hist == ((0 << 1) | (0 << 0)):
		#table[spot][3]

			pred = table[slot][3] & ( 0 | (1 << 1))
			if (pred) and (path == '@'):
				correct += 1
				table[slot][3] = table[slot][3] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))

			if not (pred) and (path == '.'):
				correct += 1
				table[slot][3] = table[slot][3] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))

			else:
				table[slot][3] += 1
				table[slot][3] = table[slot][3] & ((0 << 3) | (0 << 2) | (1 << 1) | (1 << 0))

			if path == '@':
				table[slot][2] = (0 | ((save_bit << 1) | (1 << 0)) )
			else:
				table[slot][2] = (0 | ((save_bit << 1) | (0 << 0)) )
				
		elif check_hist == ((0 << 1) | (1 << 0)):
		#table[spot][4]

			pred = table[slot][4] & (0 | (1 << 1))
			if (pred) and (path == '@'):
				correct += 1
				table[slot][4] = table[slot][4] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))
			if not (pred) and (path == '.'):
				correct += 1
				table[slot][4] = table[slot][4] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))
				
			else:
				table[slot][4] += 1
				table[slot][4] = table[slot][4] & ((0 << 3) | (0 << 2) | (1 << 1) | (1 << 0))

			if path == '@':
				table[slot][2] = (0 | ((save_bit << 1) | (1 << 0)) )
			else:
				table[slot][2] = (0 | ((save_bit << 1) | (0 << 0)) )
				
			
								
		elif check_hist == ((1 << 1) | (0 << 0)):
		#table[spot][5]

			pred = table[slot][5] & (0 | (1 << 1))
			if (pred) and (path == '@'):
				correct += 1
				table[slot][5] = table[slot][5] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))

			if not (pred) and (path == '.'):
				correct += 1
				table[slot][5] = table[slot][5] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))

			else:
				table[slot][5] += 1
				table[slot][5] = table[slot][5] & ((0 << 3) | (0 << 2) | (1 << 1) | (1 << 0))

			if path == '@':
				table[slot][2] = (0 | ((save_bit << 1) | (1 << 0)) )
			else:
				table[slot][2] = (0 | ((save_bit << 1) | (0 << 0)) )
				
			
		elif check_hist == ((1 << 1) | (1 << 0)):
		#table[spot][6]

			pred = table[slot][6] & (0 | (1 << 1))
			if (pred) and (path == '@'):
				correct += 1
				table[slot][6] = table[slot][6] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))

			if not (pred) and (path == '.'):
				correct += 1
				table[slot][6] = table[slot][6] & ((1 << 3) | (1 << 2) | (1 << 1) | (0 << 0))

			else:
				table[slot][6] += 1
				table[slot][6] = table[slot][6] & ((0 << 3) | (0 << 2) | (1 << 1) | (1 << 0))

			if path == '@':
				table[slot][2] = (0 | ((save_bit << 1) | (1 << 0)) )
			else:
				table[slot][2] = (0 | ((save_bit << 1) | (0 << 0)) )
				
			
			
		else:
			print 'what the hell was the history??'

		total += 1
	return(correct, total)

if __name__ == "__main__":

	try:
		arg_check()
		lines = ingest(sys.argv[1])

		correct, total = fixed_true(lines)
		print_msg(correct, total, 'Fixed')

		correct, total = static_first(lines)
		print_msg(correct, total, 'Static')

		correct, total = bimodal(lines)
		print_msg(correct, total, 'Bimodal')

		correct, total = two_layer(lines)
		print_msg(correct, total, '2-Layer')

	except:
		print("Unexpected error:", sys.exc_info()[0])
		print("Unexpected error:", sys.exc_info()[1])
