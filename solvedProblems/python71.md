

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.


September 30, 2018 11:08:21 AM : what is the greatest reduced proper fraction less than 3/7 with a denomonator less than a million?

For every number  x less than a million
 start y one less than 3/7 of x
  is y/x greater than global_max?
   is y/x greater than 3/7?
   
September 30, 2018 11:21:47 AM : This was trivial.
Wrote all the code myself and got the answer right on the first pass.
Code executes in just over a second.