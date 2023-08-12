"""
Entry point for the unitParser 3 program. 

Dawson Lin, 7/25/2023
"""

import unitParser4 as parser
import utilities as util
import time


def check_for_correctness(data1Num, data2Num, num = 0): 
	#1. orders1 = read input/01.data 
	#2. orders2 = read input/02.data
	#3. for i from 0 to the end of orders1
	#	a. print orders1[i], orders2[i], are equal: orders_are_equal(orders1[i], orders2[i]) 
	orders1 = util.read_file_lines("input/" + data1Num + ".data")
	orders2 = util.read_file_lines("input/" + data2Num + ".data")
	if num == 0: num = len(orders1)
	for i in range(0, num): 
		if "tag" not in orders1[i] and "tag" not in orders2[i]:
			print(orders1[i] + ", " + orders2[i] + ": Equal? " + 
			str(parser.orders_are_equal(orders1[i], orders2[i])))
	
def time_operation(data1Num, data2Num):
	orders1 = util.read_file_lines("input/" + data1Num + ".data")
	orders2 = util.read_file_lines("input/" + data2Num + ".data")

	num = len(orders1)

	startTime = time.time()

	for i in range(0, num): 
		try:
			parser.orders_are_equal(orders1[i], orders2[i])
		except: 
			continue

	endTime = time.time()
	elapsedTime = endTime - startTime

	print("Elapsed time:", elapsedTime, "seconds")
	print("Order pairs compared: " +  str(num))

#### BUGS

## Normal units
print("Single Units: ")
print("Check for correctness 1:", parser.orders_are_equal("1000 mmol", "1 mole"))
print("Check for correctness 2:", parser.orders_are_equal("1 l", "1000 cc"))
print("Check for correctness 3:", parser.orders_are_equal("1,000,000 units", "1 milli units"))
print("Check for correctness 4:", parser.orders_are_equal("1,000,000 MCG", "1 g"))
print("Check for correctness 5:", parser.orders_are_equal("1 l", "1000 milliliter(s)"))
print()
print()

## Rates
print("Rates: ")
print("Check for correctness 1:", parser.orders_are_equal("100 mg/day", "100 mg/day"))
print("Check for correctness 2:", parser.orders_are_equal("100 mg/day", "100 mg/day"))
print("Check for correctness 3:", parser.orders_are_equal("100 mg/day", "0.1 g/day"))
print("Check for correctness 4:", parser.orders_are_equal("100 mg/day", "0.00000116 g/sec"))
print("Check for correctness 5:", parser.orders_are_equal("100 ml/day", "0.1 L/day"))
print()
print()


#### Trials

## Trial 1
# check_for_correctness("01a", "01b", 10)
print()
print()
time_operation("01a", "01b")

## Trial 2
print()
print()
time_operation("01aa", "01bb")
print()

## Trial 3
# check_for_correctness("02a", "02b", 10)
print()
print()
time_operation("02a", "02b")
print()

## Trial 4
print()
print()
time_operation("02aa", "02bb")
print()

## Trial 5
# check_for_correctness("01a", "01b", 10)
print()
print()
time_operation("01a", "01b")
print()

## Trial 6
# check_for_correctness("01aaa", "01bbb", 10)
print()
print()
time_operation("01aaa", "01bbb")
print()

## Trial 7
print()
print()
time_operation("03a", "03a")
print()

## Trial 8
print()
print()
time_operation("03a", "03b")
print()

