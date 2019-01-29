#!/usr/bin/python

"""
Author: 		David Selassie Opoku
Description:	A Python program that takes a polynomial in standard algebraic
				notation and outputs the required derivative.
Use:			Interactive or batch mode
				
Interactive mode 	: 	python derivative.py 
batch mode 		 	:	python derivative.py 'polynomial expr' 'n'
expr: 			Polynomial expression. e.g: 5x^4+3x^2
n:				n-th derivative to calculate i.e 1 for 1st derivative, 2 for 2nd and so on.
"""

import sys

def main():
	# Get user expression input
	# Check validity of input
	# Parse input to determine various terms
	# Derive derivative for each term
	# Combine derivatives of each term
	# Return final derivative

	if len(sys.argv) < 2:	# sys.argv is list storing command-line parameters
		interactive_mode()
	else:
		batch_mode()

def interactive_mode():
	"""Runs program in interactive mode. Type quit to exit.
	"""
	expr = input('Enter polynomial expression: ').strip()
	while expr.lower() != 'quit':
		n = int(input('Enter 1 or 2 for 1st and 2nd derivative respectively: ').strip())
		expr = check_expression(expr)
		expr = expr.strip()
		answer = solve_derivative(expr, n)
		print('Derivative: %s' % (answer))
		print('')
		expr = input('Enter polynomial expression: ').strip()
	print('Hope this was helpful! Bye :)')


def batch_mode():
	"""Runs program in batch mode."""
	expr = str(sys.argv[1])
	n = int(sys.argv[2])
	print(solve_derivative(expr, n))


def check_expression(expr):
	""" Returns TRUE if user input is valid expression and FALSE otherwise
	expr 	polynomial expression entered by user
	"""

	expr = str(expr)

	while len(expr) < 1:
		print('INVALID ENTRY! Need to enter an expression')
		expr = input('Enter polynomial expression: ')
	return expr


def get_terms(expr):
	"""Return individual terms of polynomial expression
	expr  	standard polynomial expression 
	"""

	terms = expr.split('+')

	return terms


def derivative(term):
	"""Return the derivative of a given term
	term 	unit term of expression e.g. x^3
	"""

	coeff, variable, power = get_coeff_var_power(term)

	# calculate new coefficient, variable and power for  derivative
	deriv_coeff = coeff * power
	deriv_power = power - 1

	# return zero if derivative coefficient is zero
	if deriv_coeff == 0:
		deriv = 0

	# just return coefficient if derivative power is zero
	elif deriv_power == 0:
		deriv = deriv_coeff

	# just return term with coefficient and variable if derivative power is one
	elif deriv_power == 1:
		deriv = '%s%s' % (deriv_coeff, variable)

	else:
		deriv = '%s%s^%s' % (deriv_coeff, variable, deriv_power)

	return str(deriv)


def get_coeff_var_power(term):
	"""Returns the coefficient,variable and power for a given term."""
	
	term_split = term.split('^')
	base_term = term_split[0]

	# get coeff and variable
	if len(base_term) == 1:
		if base_term[-1].isdigit():
			coeff = int(base_term[-1])
			variable = ''
		else:
			coeff = 1
			variable = base_term[-1]
	else:
		variable = base_term[-1]
		coeff = int(base_term[:-1])

	# get power
	if len(term_split) == 2:
		power = int(term_split[-1])

	elif len(term_split) == 1 and variable.isalpha():
		power = 1
	else:
		power = 0
	return coeff, variable, power

def solve_derivative(expr, n):
	""" Returns solved derivative of polynomial expression
	expr 	expression to calculate derivative of
	n 		n-th derivative to calculate
	e.g: 	solve_derivative('5x^4+3x^2', 1) --> 20x^3+6x
			solve_derivative('5x^4+3x^2', 2) --> 60x^2+6
	"""

	if n == 0:
		return expr
	else:
		terms = get_terms(expr)
		list_derv = []

		for term in terms:
			derv = derivative(term.strip())
			list_derv.append(derv)

		answer = '+'.join(list_derv)
		return solve_derivative(answer, n - 1)


if __name__ == '__main__':
	main()
	#term = '5x^2'
	#print(get_coeff_var_power(term))
