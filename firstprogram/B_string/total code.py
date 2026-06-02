x = 1   
y = 2.8 
z = 1j  
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))



a = int(input("enter first number : "))
b = int(input("enter second number : "))
print("sum is :",a+b)
print("subtraction is :",a-b)
print("multiple is :",a*b)
print("division is :",a/b)
print("reminder is :",a%b)




str1 = input("enter first string :")
str2 = input("enter second string :")
str = str1 + str2
print("str after concate :",str)
strsli = str[2:6]
print("string slicing from idx2 to 5 :", strsli)





number = int(input("enter a number :"))
if(number>0): print("number is positive")
else : print("number is negative")




a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))
if(a>b and a>c):
    print(a,"is the greatest number")
if(b>a and b>c):
    print(b,"is the greatest number")
if(c>a and c>b):
    print(c,"is the greatest number")




sum = 0
for n in range(1 , 51):
    if(n%2==0): 
        print(n)
        sum = sum+n
print("sum is ",sum)





for i in range(21,50) :
    root = int(i**.5)
    isprime = True
    for j in range(2,root+1):
        if (i%j==0):
            isprime = False
    if(isprime) : print(i)




def swap():
    a=int(input("enter number 1 :"))
    b= int(input("enter number 2 :"))
    print("Before swapping:")
    print("a=",a,"b=",b)
    a=a+b
    b=a-b
    a=a-b
    print("After swapping:")
    print("a = ",a,"b=",b)
swap()




###################################.  9
def calculation(a,b):
    if(a>b):
        return a
    elif(a==b):
        return a,b
    else:
        return b
print("greatest number is :",
    calculation(6,5)
)




###################################.  10
def factorial(a):
    if(a==0):
        return 1
    return a*factorial(a-1)
print(factorial(int(input("enter a number : "))))




###################################.  11
import time
t = time.localtime()
strform = time.asctime(t)
print("current time is :",strform)



###################################.  11
from datetime import datetime
import pytz
def time():
    ist_timezone = pytz.timezone('asia/kolkata')
    current = datetime.now(ist_timezone)
    return current
ist_time = time()
print(f"{ist_time.strftime('%a %d %H:%M:%S %Z %Y')}")


###################################.  12
print("enter your required unit of temperature :")
def function(i):
    if(i=='c' or i=='C'):
        f = float(input("enter temperature in fahrenheit :"))
        c = (f-32)*5/9
        print("temperature in celsius is :",c)
    elif(i=='f' or i=='F'):
        c = float(input("enter temperature in celsius :"))
        f = (c*9/5)+32
        print("temperature in fahrenheit is :",f)
    else:
        print("invalid input")
function(input("enter : c for celsius & f for fahrenheit :"))



###################################.  13
def prime():
    for i in range(1,20) :
        root = int(i**.5)
        isprime = True
        for j in range(2,root+1):
            if (i%j==0):
                isprime = False
        if(isprime) : print(i)
prime()



###################################.  14
for n in range (1,5):
    print("*"* n)



###################################.  15
print("Multiplication table of 8 is :\n")
for n in range(1,11):
   print("8 x",n,"=",n*8)
print("Multiplication table of 15 is :\n")
for n in range(1,11):
   print("15 x",n,"=",n*15)
print("Multiplication table of 69 is :\n")
for n in range(1,11):
   print("69 x",n,"=",n*69)



###################################.  16
lowercase = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
             "r","s","t","u","v","w","x","y","z")
uppercase = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
             "R","S","T","U","V","W","X","Y","Z")
number = ("0","1","2","3","4","5","6","7","8","9")
symbol = ("!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]",
          "|",":",";","<",">",",",".","?","/")
vaishnavi = input("enter {symbol} or {number} or {lowercase} or {uppercase} :")
if(vaishnavi in lowercase):
    print("it is lowercase")
if(vaishnavi in uppercase):
    print("it is uppercase")
if(vaishnavi in symbol):
    print("it is symbol")
if(vaishnavi in number):
    print("it is number")
if(len(vaishnavi)>1):
    print("you have entered more then one characters")




vaishnavi = int(input("enter the lenth of series : "))
n = 1
number = 0
i=1
while(i<=vaishnavi):
    print(number)
    number=number+n
    i+=1