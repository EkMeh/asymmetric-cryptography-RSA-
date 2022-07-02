import os
import random
import math
import ast
import primeNumbers
import os
# Create a text file to save Exponents
def CreateTxtFile():
    exponents=open("resources\\exponents.txt",'w')
    # generate the exponent // p //
    num1 = primeNumbers.GeneratePrimeNumber()
    # generate the exponent // q //
    num2 = primeNumbers.GeneratePrimeNumber()
    exponents=open("resources\\exponents.txt",'a')
    # save the exponent // p //
    exponents.write("The value of p is: "+str(num1)+str("\n"))
    # save the exponent // q //
    exponents.write("The value of q is: " + str(num2) + str("\n"))
    exponents.close()
# Function to generate the exponent // p //
def ExponentP():
    exponents=open("resources\\exponents.txt",'r')
    exponentsRead=exponents.readlines()
    exponents.close()
    return int(exponentsRead[0][19:-1])
# Function to generate the exponent // q //
def ExponentQ():
    exponents = open("resources\\exponents.txt", 'r')
    exponentsRead = exponents.readlines()
    exponents.close()
    return int(exponentsRead[1][19:-1])
# Function to generate the exponent // fi //
def ExponentFi(exp1,exp2):
    fi = (exp1 - 1) * (exp2 - 1)
    exponents=open("resources\\exponents.txt",'a')
    # save the exponent // fi //
    exponents.write("The value of fi is: "+str(fi)+str("\n"))
    exponents.close()
    return fi
# Function to generate the exponent // n //
def ExponentN(exp1,exp2):
    n = exp1*exp2
    exponents=open("resources\\exponents.txt",'a')
    # save the exponent // fi //
    exponents.write("The value of n is: "+str(n)+str("\n"))
    exponents.close()
    return n
# Function to generate the exponent // e //
def ExponentE():
    exponents=open("resources\\exponents.txt",'r')
    exponentsRead=exponents.readlines()
    exp3=int(exponentsRead[2][19:-1])
    exponents.close()
    while True:
        num2=random.randint(2,exp3)
        if(num2<exp3):
            for e in range(num2,exp3):
                if(e%num2==1 and exp3%e==1):
                    exponents = open("resources\\exponents.txt", 'a')
                    # save the exponent // e //
                    exponents.write("The value of e is: " + str(e) + str("\n"))
                    exponents.close()
                    return e
                    break
# Function to generate the exponent // e //
def ExponentD():
    exponents = open("resources\\exponents.txt", 'r')
    exponentsRead = exponents.readlines()
    exp3=int(exponentsRead[2][19:-1])
    exp5=int(exponentsRead[4][19:-1])
    exponents.close()
    for d in range(1, exp3, 1):
        if (((d * exp5) - 1) % exp3 == 0):
            exponents = open("resources\\exponents.txt", 'a')
            # save the exponent // d //
            exponents.write("The value of d is: " + str(d) + str("\n"))
            exponents.close()
            return d
# Function to generate the exponents of the Public Key(n,e)
def PublickKey():
    global E
    global N
    exponents = open("resources\\exponents.txt", 'r')
    exponentsRead = exponents.readlines()
    return int(exponentsRead[3][19:-1]),int(exponentsRead[4][19:-1])
# Function to generate the exponents of the Private Key(n,d)
def PrivateKey():
    exponents = open("resources\\exponents.txt", 'r')
    exponentsRead = exponents.readlines()
    return int(exponentsRead[3][19:-1]), int(exponentsRead[5][19:-1])
# Encryption function
def Encrypt(Text, KeyN,KeyE):
    msg = open("resources\\RSA.txt", "w")
    msg.close()
    global RSAencrypt
    RSAencrypt=""
    for i in Text:
        RSAencrypt=chr((pow(ord(i),KeyE)%KeyN))
        msg = open("resources\\RSA.txt", "a+")
        msg.write(str(RSAencrypt.encode()) + "\n")
    msg.close()
# Decryption function
def Decrypt(n,d):
    with open("resources\\RSA.txt", "r") as msgEnc:
        msg = msgEnc.readlines()
    global dec_mes
    text = [ast.literal_eval(line) for line in msg]
    dec_mes=""
    for lam in text:
        text_message = (lam.decode("utf-8"))
        text_message = pow(ord(text_message), int(d)) % int(n)
        dec_mes = dec_mes+chr(text_message)
        msgEnc.close()
    return dec_mes

CreateTxtFile()
ExponentP()
ExponentQ()
ExponentFi(ExponentP(),ExponentQ())
ExponentN(ExponentP(),ExponentQ())
ExponentE()
ExponentD()
PublickKey()[0],PublickKey()[1]
PrivateKey()[0],PrivateKey()[1]




