#!/usr/bin/env python3

import readline
import operator
import sys

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
}

def calculate(arg):
	stack = list()
	for operand in arg.split():	
		try:
			operand = float(operand)	
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator = OPERATORS[operand]
			result = operator(arg1, arg2)
			stack.append(result)			
	return stack.pop()

def main():
	while True:
		try:
			read = input('rpn calc> ')
			if read == 'q':
				break
			result = calculate(read)
			print ("Result:", result)
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			print ("could not handle input please retry")


if __name__ == '__main__':
	main()
