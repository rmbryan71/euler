

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?


September 30, 2018 1:51:01 PM : I could make a list of pairs that represent all the reduced proper fractions, add to the list as I go up to 1 million, then return the length of the list.

September 30, 2018 2:01:41 PM : I guess technically what I want is a set, not a list.
September 30, 2018 2:04:05 PM : and I can store the floats, since they'll be unique
September 30, 2018 2:12:17 PM : I have a brute force solution running, and it bogs down pretty quickly.
September 30, 2018 2:48:10 PM : Oh, wait... each new number will add exactly phi elements to the set.
September 30, 2018 2:48:50 PM : All I have to do is find the sum of phi for all integers up to 1000000
September 30, 2018 2:55:37 PM : That made it easy. correct answer in about 33 seconds.