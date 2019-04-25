#=W= for math problem
import math

def Expection_For_Uniform_Distribution(lowerbound, upperbound):
	ans = (lowerbound + upperbound) / 2
	return ans

def Variance_For_Uniform_Distribution(lowerbound, upperbound):
	ans = upperbound - lowerbound
	ans = ans*ans / 12
	return ans

def Central_Limit_Theorem(expection, variance, amount, num):
	new_expection = expection*amount
	new_variance = variance*amount
	ans = (num - new_expection) / (new_variance ** 0.5)
	ans = Guessian_Distribution(new_expection, new_variance,num)
	return ans

def Guessian_Distribution(expection, variance, num):
	ans = 1/((3.14159265359*2)**0.5)*(variance**0.5)
	print(ans)
	ans = ans * math.exp( -( (num-expection)**2 / (2 * variance) ) )
	return ans


upperbound_question = 0.5
lowerbound_question = -0.5

expection_ans = Expection_For_Uniform_Distribution(lowerbound_question, upperbound_question)
variance_ans  = Variance_For_Uniform_Distribution(lowerbound_question, upperbound_question)
ans = Central_Limit_Theorem(expection_ans, variance_ans, 100, 10)

print(expection_ans)
print('%0.2f' %variance_ans)
print('%0.5f' %ans)