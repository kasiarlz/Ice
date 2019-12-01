# Python program to check if the input number is prime or not

# take input from the user
# num = int(input("Enter a number: "))
# prime numbers are greater than 1

num=5

if num > 1:
    for A in range  (2,num):
        if (num % A)==0:
            print(num, 'number is not prime')
            print(A, 'times',num//A ,'is', num)
            break
    else:
        print(num, ' is a prime number')   
else:
    print(num,'is not a prime number')   
        



