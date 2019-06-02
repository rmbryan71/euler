September 29, 2018 7:06:04 AM : Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n 	Relatively Prime 	φ(n) 	n/φ(n)
2 	1 	1 	2
3 	1,2 	2 	1.5
4 	1,3 	2 	2
5 	1,2,3,4 	4 	1.25
6 	1,5 	2 	3
7 	1,2,3,4,5,6 	6 	1.1666...
8 	1,3,5,7 	4 	2
9 	1,2,4,5,7,8 	6 	1.5
10 	1,3,7,9 	4 	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

September 29, 2018 7:10:03 AM : https://en.wikipedia.org/wiki/Euclidean_algorithm explains dude's quick way of finding the gcd between two numbers, then Bezout's identity to speed that up even more.

Brute force plan is:
 to write a gcd function that takes two integers
 put that in a loop that checks the gcd for a number and every number less than it
 count the cases where gcd = 1 and divide that count by 1.
 
 September 30, 2018 7:38:30 AM : I have a brute force solution that uses the math.gcd function to find the gcd for every pair of numbers, if that's 1, it counts that in the totient. It's been running overnight and it's on 440,000. So it's not half way done, and of course it's slowing down because each number takes longer to calculate than the number before it. This is the perfect project euler problem.
 
 My best idea for speeding this up is making use of the multiplicative property of euler totients (phi).
 If gcd(m,n) == 1, then phi(mn) * phi(m) * phi(n)
 
Euler's product formula was the answer here.
I didn't think of it myself.
I found it here.
https://www.geeksforgeeks.org/eulers-totient-function/

I wrote the code while looking at their code.
I don't think I could have written the code myself just from the equation.

