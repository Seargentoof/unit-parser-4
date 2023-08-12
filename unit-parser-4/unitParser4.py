"""
Functions and algorithms for parsing medical Units of Measure. 
Fourth version of UnitParser where all unit information is compiled into one Excel 
file and a dictionary is implemented, hopefully resulting in more efficient and user-friendly
code. Beginning of unit rate implementation. 

Dawson Lin, 7/27/2023
"""

import pandas as pd
import math
import numpy
import utilities as util



#### Functions

### Loading

"""
Opens an xml file storing unit information. Returns a dictionary consisting of:
key = unit expressions
value = tuple of the corresponding context (index 0) and value (index 1)
"""
def load_unit_xlsx_info(filepath = "information/Units.xlsx", column1 = "Expression", 
			column2 = "Context", column3 = "Value") -> dict:
	
	SPACE = " " # CONSTANTS

	# load the file into a variable df
	df = pd.read_excel(filepath)
    
	# create a new dictionary result
	result = dict()

    
	# for each row in the spreadsheet from index 1 onwards 
	#	key = the expression
	#	value = tuple consisting of context (index 0) and value (index 1)
	#	add key, value to the dictionary
	for index, row in df.iterrows():
		#format the expression by converting to lowercase and stripping it of spaces
		key = str(row[column1]).strip().lower().replace(SPACE, "")
		value = (str(row[column2]), float(row[column3]))
		result.update({key: value})

	#return result
	return result
	

#load in all unit and prefix data at once
allUnitsInfo = load_unit_xlsx_info()
# print(allUnitsInfo)


### Parsing

"""
Takes in a string order in the form "Value Unit" and returns 
a tuple consisting of float value and str unit
"""
def parse_order(order: str) -> tuple:
	# value = everything before the space in order
	# unit = everything after the space in order
	# return (value, unit)
	indexOfFirstSpace = order.index(" ")
	value = order[:indexOfFirstSpace]
	unit = order[indexOfFirstSpace+1:]

	try: return (float(value), str(unit))
	except ValueError: return (float(util.remove_commas(value)), str(unit))


### Single Units

"""
Takes a str unit and determines its context (e.g, mass, length, time)
"""
def unit_context(unit: str, unitInfo = allUnitsInfo) -> str:  
	CONTEXT = 0 # CONSTANTS
	SPACE = " "

	#format the unit by converting to lowercase and stripping of spaces
	# if unit is included in one of the tuples of expressions
	# 	return the corresponding context					
	try: 
		unit = unit.strip().lower().replace(SPACE, "")
		return unitInfo.get(unit)[CONTEXT]

	# print "Context not found."
	except: print("Context for", unit, " not found.")
    
	# return None
	return None


"""
Takes a str unit and determines its value relative to the baseUnit
"""
def unit_value(unit: str, unitInfo = allUnitsInfo) -> float:
	VALUE = 1 # CONSTANTS
	SPACE = " "
    
	#format the unit by converting to lowercase and stripping of spaces
	# if unit is included in one of the tuples of expressions
	# 	return the corresponding value
	try: 
		unit = unit.strip().lower().replace(SPACE, "")
		return unitInfo.get(unit)[VALUE]

	# print "Value not found."
	except: print("Value for", unit, "not found.")
    
	# return None
	return None


### Rate Units

"""
Takes a str unitRate and determines its context in the form of:
topUnitContext/bottomUnitContext
"""
def rate_unit_context(unitRate: str, unitInfo = allUnitsInfo) -> str:
	SLASH = "/" # CONSTANTS

	#1. topUnit = everything before the "/"
	topUnit = unitRate[:unitRate.find(SLASH)]

	#2. bottomUnit = everything after the "/"
	bottomUnit = unitRate[unitRate.find(SLASH)+1:]

	#3. return unit_context(topUnit) + "/" + unit_context(bottomUnit)
	return unit_context(topUnit, unitInfo) + SLASH + unit_context(bottomUnit, unitInfo)

"""
Takes a str unitRate and determines its value relative to the baseUnits
"""
def rate_unit_value(unitRate: str, unitInfo = allUnitsInfo) -> float:
	SLASH = "/" # CONSTANTS

	#1. topUnit = everything before the "/"
	topUnit = unitRate[:unitRate.find(SLASH)]

	#2. bottomUnit = everything after the "/"
	bottomUnit = unitRate[unitRate.find(SLASH)+1:]

	#3. return unit_value(topUnit)/unit_value(bottomUnit)
	return (float(unit_value(topUnit))/float(unit_value(bottomUnit)))


#### Implementation

"""
Takes two string orders in the form "Value Unit" and determines whether 
the two are equivalent
"""
def orders_are_equal(order1: str, order2: str, tolerance = 0.01) -> bool:
    # CONSTANTS
	MEASURE = 0; UNIT = 1
	SLASH = "/"

	try: 
		#Algorithm: 
		#1. info1 = order1 parsed, info2 = order2 parsed
		info1 = parse_order(order1); info2 = parse_order(order2)

		#2. measure1 = info1[0], measure2 = info2[0]
		measure1 = info1[MEASURE]; measure2 = info2[MEASURE]	

		#3. unit1 = info1[1], unit2 = info2[1]
		unit1 = info1[UNIT]; unit2 = info2[UNIT]
		# print("Units: ", unit1, unit2)

		# if the units contain a slash, find unit rate contexts and values
		# otherwise
		# 	context1, context2 = the context of unit1 and unit2, respectively
		#	unitValue1, unitValue2 = the unit values of unit1 and unit2, respectively
		# if context1 and context2 are the same
		#	i. if measure1*unitValue1 == measure2*unitValue2 (or are close enough due to 
		# 	presence of float values), return true
		if SLASH in unit1 or SLASH in unit2:
			context1 = rate_unit_context(unit1)
			context2 = rate_unit_context(unit2)
			# print("Contexts: ", context1, context2)

			unitValue1 = rate_unit_value(unit1)
			unitValue2 = rate_unit_value(unit2)
		else:
			context1 = unit_context(unit1)
			context2 = unit_context(unit2)
			# print("Contexts: ", context1, context2)

			unitValue1 = unit_value(unit1)
			unitValue2 = unit_value(unit2)
			# print("Values: ", unitValue1, unitValue2)

		if context1 == context2:
			if math.isclose(measure1*unitValue1 ,measure2*unitValue2, 
		   	rel_tol=tolerance): return True

	except: pass # print("Orders", order1, ",", order2, "are not comparable.")

	#6. return false
	return False


