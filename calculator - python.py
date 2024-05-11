# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:34:56 2024

@author: harip
"""

# SIMPLE CALCULATOR
import math
def add():
    a = float(input("Enter 1st number : "))
    b = float(input("Enter 2nd Nnumber : "))
    c = a+b
    print(f"\nsum of {a} and {b} is {c}")

def subtract():
    a = float(input("Enter 1st number : "))
    b = float(input("Enter 2nd Nnumber : "))
    c = a-b
    print(f"\ndifference of {a} and {b} is {c}")
    
def multiply():
    a = float(input("Enter 1st number : "))
    b = float(input("Enter 2nd Nnumber : "))
    c = a*b
    print(f"\nproduct of {a} and {b} is {c}")
    
def division():
    a = float(input("Enter 1st number : "))
    b = float(input("Enter 2nd Nnumber : "))
    c = a/b
    d = a//b 
    e = a%b
    print (f"\ndivision of {a} and {b} is {c} , floor division is {d} and remainder is {e}")

def exponential_power():
    a = float(input("Enter 1st number : "))
    b = float(input("Enter 2nd Nnumber : "))
    c = a**b
    print(f"\n{a} power {b} is {c} | {a} exponential {b} is {c} ")

def root():
    a = float(input("Enter 1st number : "))
    c= math.sqrt(a)
    print(f"\nsquare root of {a} is {c}")

def main():
    while True:
        print("\n********* WELCOME TO CALCULATOR *********")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponential / Power (^)")
        print("6. Nth Root")
        print("7. Exit Calculator")
        ch = int(input("Enter your choice of operation : "))
        
        if ch == 1: add()
        elif ch == 2: subtract()
        elif ch == 3: multiply()
        elif ch == 4: division()
        elif ch == 5: exponential_power()
        elif ch == 6: root()
        elif ch == 7: 
            print("\nThank you for using CALCULATOR !!!")
            break
        else:
            print("\nInvalid choice ! please enter appropriate choice")

        
if __name__ ==  '__main__':
    main()