'''write a python program to find the sum of natural numbers upto N. 
sample input : 16
sample output : the sum of natural numbers upto 16 is 136'''

N=int(input("enter the value for N:"))
number=0
for i in range(1,N+1):
    number+=i
print(f"the sum of natural number upto {N} is {number}")


Declare
f NUMBER=1;
n NUMBER=16;-- compute16!
BEGIN 
   FOR i IN 1..n LOOP
f:=f*i;
END LOOP
print( 'Factorial of'||n||'is'||f);
END;
