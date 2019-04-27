#bacteria problem
#suppose this is a bacteria OwO
#i want it to be 1/4 for split 0,1,2,3
#so what is the prob that it eventually die
import numpy
from random import randint

def bacteria_generator(num):
	guess = num
	for x in range(0,1000):
		factor = randint(0,3)
		if(factor != 0):
			guess += factor
		else:
			guess = guess-1
			if(guess == 0):
				return guess
	return guess

def main():
	print("hello=W=, here is a small program")

	prob_stat = []

	for k in range(1,10):
		k = []
		for z in range(1,1000):
			initalize = 1
			#follow rule to generator
			sum = bacteria_generator(initalize)
			k.append(sum)
		b = 0
		for x in k:
			if(x == 0):
				b = b + 1
		ans = b/1000
		prob_stat.append(ans)

	#for showing the average of the ans
	#btw it answer is ~0.25, i dont why OWO
	test = 0
	for e in prob_stat:
		test += e

	print(test/10)

if __name__ == "__main__":
	main()
