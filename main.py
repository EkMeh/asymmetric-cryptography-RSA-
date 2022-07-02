import rsa
import os

message=input("Enter the encryption text: ")
rsa.Encrypt(message,rsa.PublickKey()[0],rsa.PublickKey()[1])
print("Decrypted text: " + rsa.Decrypt(rsa.PrivateKey()[0],rsa.PrivateKey()[1]))