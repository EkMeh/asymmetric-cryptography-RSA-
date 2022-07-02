import random

# A function to generate a random number
def GenerateNumber():
        return random.randrange(2 ** (6 - 1) + 1, 2 ** 6 - 1)

# Function to check if the generated number is a prime number
def CheckPrimrNumbers(number):
        global is_prime
        is_prime=False
        if number > 1:
                for i in range(2, number):
                        if (number % i) == 0:
                                is_prime = True
                                break

# A function to generate a prime number
def GeneratePrimeNumber():
        while True:
                genNumber=GenerateNumber()
                CheckPrimrNumbers(genNumber)
                if is_prime==False:
                        return genNumber
                        break


