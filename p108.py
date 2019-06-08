#Import time so we can time this program
import time

#Define primes (17 is sufficient for this problem)
primes = [2, 3, 5, 7, 11, 13, 17]

#Define a function that returns the exponents 
#of all the factors of the input n in its simplest
#factored form
def exponentsOfFactors(n):
    exp = []
    counter = 0
    for i in range(0, len(primes)):
        while n % primes[i] == 0:
            n = n / primes[i]
            counter += 1
        if counter > 0:
            exp.append(counter)
            counter = 0
    return exp

#Define a function that returns the number 
#of divisors for a given n
def d(n):
    exp = exponentsOfFactors(n)
    total = 1
    for i in range(0, len(exp)):
        total *= exp[i] + 1
    return total

#Put everything into a run function so we can
#see how long it takes to run
def run():
    #Start the timer
    start = time.time()

    #Solve the problem
    i = 1
    while d(i**2) / 2 <= 1000:
        i += 1

    #Print the result
    print(i)
    print('This took ' + str(time.time() - start) + ' seconds to run.')

#Run the program
run()