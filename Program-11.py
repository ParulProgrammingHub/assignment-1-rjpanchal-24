p=int(input('Enter principal amount: '))
r=float(input('Enter rate in percentagel: '))
t=int(input('Enter time period in years: '))
n=float(input('No. of times interest is compounded: '))
def compound_interest(principal,rate,time,node):
	A=p*((1+r/n)**(n*t))
	print 'Interest value = ',A
compound_interest(principal=p,rate=r,time=1,node=n)

