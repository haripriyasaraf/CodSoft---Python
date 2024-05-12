# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:41:16 2024

@author: harip
"""

import random
character_set = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                 'p','q','r','s','t','u','v','w','x','y','z',
                 '0','1','2','3','4','5','6','7','8','9',
                 '!','@','#','$','%','^','&','*','(',')','_',':',';','"',',','?','/','<','>']



def pswd(n):
    password = ""
    for i in range (1, n+1):
        char = random.choice(character_set)
        password = password + char
    print (f"Password Generated is : {password}")
    ch = input("Do you wish to change password ? y/n ?")
    if ch.lower() == 'y':
        pswd(n)

def main():
    while True:
        print("1. Generate Password")
        print("2. exit")
        choice = int(input("Enter your choice : "))
        if choice ==1 :
            n = int(input("Enter the length of password desired : "))
            pswd(n)
        elif choice == 2:
            print ("Thank you !!")
            break
        else:
            print("Inavlid choice !")

if __name__ == '__main__':
    main()
    