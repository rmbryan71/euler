

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.


September 30, 2018 8:09:19 AM : Well, this is certainly going to take advantage of the fast phi function I wrote in euler 69.
I'll need an is_permutation function.

September 30, 2018 8:31:57 AM : To get more timing, profiling and other help, I downloaded and installed the pycharm professional license I won at the PHASE meetup back in May.
Now I can see call graphs and exactly how long execution of code takes.
If I JUST call my phi function on every integer up to 10^7, that takes... almost 16 minutes.
dang.

Okay, that's fast enough. So I just need to check, for each one, if the totient ration would be a global minimum if it's a permutation, then check if it's a permutation.

Instead of really checking for permutations, I'm just sorting the digits of the two numbers, then seeing if they're equal.
I can already tell it's going to be interesting to see which condition I apply first:
A. Is the totient lower than the global lowest totient so far
or
B. Is the totient a permutation of the input

My guess is that A will be faster.

September 30, 2018 11:00:25 AM : I have to correct answer now, and everything from here forward is just checking for efficiency.


