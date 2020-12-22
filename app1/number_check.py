def prime(number):
   if number > 1:
   # check for factors
       for i in range(2,number):
           if (number % i) == 0:
               print(number,"is not a prime number")
               print(i,"times",number//i,"is",number)
               break
       else:
           print(number,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
   else:
       print(number,"is not a prime number")

def odd_even(number):
   'Checks whether the number is even or odd'
   if number%2 == 0:
       return "Even"
   else:
       return "Odd"