#!/usr/bin/env python

def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2

operators = {
	'+': add,
	'-': subtract,
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
			operator = operators[operand]
			result = operator(arg1, arg2)
			stack.append(result)			
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print ("Result:", result)

if __name__ == '__main__':
	main()
