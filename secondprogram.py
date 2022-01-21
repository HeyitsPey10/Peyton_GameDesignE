#Peyton Jacobe, 1/19/22

#other operators +-*/     **exponent  %modulus Format printing 
# Format printing escape character

#Program creating an equation, asking user input, and formatting the output
import os
os.system('cls')
#Declare variables:
var1=10
var2=2
var3=2.9
var4=5

#calculate equation given 
# print(2**4)

#print format
result= (3*var1 - 2*(var2)**2/var3)/var4
print("Var1 = %5d"% var1)
print("Var2 = %5d"% var2)
print("Var3 = %8.2f"% var3)
print("Var4 = %5d"% var4)
print("Result = %6.2f"% result, end=" ---")