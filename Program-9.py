a=int(input('Marks of 1st subject: '))
b=int(input('Marks of 2nd subject: '))
c=int(input('Marks of 3rd subject: '))
d=int(input('Marks of 4th subject: '))
e=int(input('Marks pf 5th subjectL '))
mean=(a+b+c+d+e)/5.0
prc=((a+b+c+d+e)*100)/250
print prc
if prc<35.0:
	print 'Fail'
else:
	print 'Pass'

