p=int(input('Enter principal amount: '))
r=int(input('Enter percentages of rate: '))
t=int(input('Enter period of time: '))
def simple_interest(principal,time,rate):
	A=p*(1+r*t)
	print 'Total value of interest = ',A
simple_interest(principal=p,time=t,rate=r)
