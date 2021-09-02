from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import csv
from . import number_check
import logging

logger = logging.getLogger(__file__)
    
def index(request):
    
    return HttpResponse('''Congratulations, 
		You have created a web application
		using django''')


def first(request):
    print('hello')
    # logger = logging.getLogger(__name__)
    
    print(logger)
    logger.debug("This logs a debug message.")
    logger.info("This logs an info message.")
    logger.warn("This logs a warning message.")
    logger.error("This logs an error message.")
    logger.debug('Log whatever you want')
    logger.info('Log whatever info you want')
    logging.warning('You have got a warning')
    return HttpResponse("hello")


@api_view(['GET'])
def firstApi(request):
    message = 'Congratulations, you  have created an API'
    return Response(message)


@api_view(['GET'])
def addNos(request):
    """ Here is a program for
    finding out the sum of two numbers """
    # Get value of n1 from the request object
    n1 = request.GET.get('n1')
    # Get value of n2 from the request object
    n2 = request.GET.get('n2')
    # find sum
    total = int(n1) + int(n2)
    # Return the result
    return Response(total)




@api_view(['GET'])
def fileApi(request):
    'Read data from file as list and send it as response'
    fil = open('app1/data.txt', 'r+')
    data = fil.read().splitlines()
    fil.close()
    print(data)
    return Response(data)

@api_view(['GET'])
def checkPassword(request):
    password = request.POST.get('password')
    status = 'Invalid password'
    l, u, p, d = 0, 0, 0, 0
    if (len(password) >= 8): 
        for letter in password: 
            # counting lowercase alphabets  
            if (letter.islower()): 
                l+=1            
            # counting uppercase alphabets 
            if (letter.isupper()): 
                u+=1            
            # counting digits 
            if (letter.isdigit()): 
                d+=1            
            # counting special characters 
            if(letter=='@'or letter=='$' or letter=='_'): 
                p+=1       
    print(l, u, p, d)    
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)): 
        print("Valid Password")
        status = "Valid password"
    else: 
        print("Invalid Password") 
        status = "Invalid password"
    return Response(status) 


@api_view(['GET'])
def checkUsername(request):
    username = request.GET.get('username')
    fil = open('app1/users.txt', 'r+')
    users = fil.read().splitlines()
    fil.close()
    print(users)
    status = 'Invalid username'
    if username in users:
        status = 'Valid username'
    return Response(status)


@api_view(['GET'])
def saveUsername(request):
    username = request.GET.get('username')
    fil = open('app1/users.txt', 'a+')
    status = 'User not saved'
    if fil.write('\n'+username):
        status = 'User saved'
    fil.close()
    return Response(status)

@api_view(['GET'])
def viewProducts(request):
    csv_file = open('app1/users.csv')
    # Read dat in the file to a variable
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: # Print header
            print(f'{row[1]}\t{row[2]}\t{row[3]}')
            line_count += 1
        else: # Print product details
            print(f'{row[1]} \t {row[2]} \t {row[3]}')
            line_count += 1
    return Response(f'Found {line_count-1} products.')



@api_view(['GET'])
def viewAllProducts(request):
    csv_file = open('app1/users.csv')
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    products = list()
    props = []
    for row in csv_reader:
        if line_count == 0:
            props = [row[0], row[1], row[2], row[3], row[4] ]
            line_count += 1
        else:
            product = dict.fromkeys(props)
            index = 0
            for p in props:
                product[p] = row[index]
                index += 1
            products.append(product)
            line_count += 1
    print(products)
    print(f'Processed {line_count} lines.')
    # return Response(f'Found {line_count-1} products.')
    return Response(json.dumps(products))

@api_view(['GET'])
def sum_of_numbers(request):
    num = int(request.GET.get('number'))
    # initialize total and counter
    total = 0
    i = 1
    while i <= num:
        total = total + i
        i = i+1    # update counter
    print("The sum is", total) 
    return Response(total)



@api_view(['GET'])
def sum_of_numbers_with_log(request):
    total = 0
    try:
        logger.info("Processing your request")
        num = int(request.GET.get('number'))
        # initialize total and counter
        i = 1
        while i <= num:
            total = total + i
            i = i+1    # update counter
        logger.info("The sum is :"+str(total))
    except Exception as err:
        logger.error("Error occurred: "+ str(err))
        return Response('Error')
    return Response(total)


@api_view(['GET'])
def check_prime(request):
    n1 = int(request.GET.get('number'))
    number_check.prime(n1)
    result = number_check.odd_even(n1)
    return Response(result)




# Request print hello
# Request print post data
# Request print get data
# Request check number, string
# Request check valid passowrdcount number, aplpahbets, uppercase, lowercase, speicial characters
# Write post/get data to file
# Read text file, csv file
# Process mark data from csv file
# List and Write object as binary file
# Loops - Pattern printing
# Decision making - Password checking
# OOP - Save object in file may be binary
# OOP Create object form post/get data
# JSON response
# Function, recursion - Factorial of post data





