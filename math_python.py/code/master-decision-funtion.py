import numpy as np
import matplotlib.pyplot as plt

def main():
  cost = tution()
  calculation(cost)

def tution():
	x = float(input("how much is tution? "))
	return x

def calculation(x):
	p = 15000
	c = 50000

	n = float(input("how many year is your program? "))

	product = (n * x)-5000
	print(product)

main()



