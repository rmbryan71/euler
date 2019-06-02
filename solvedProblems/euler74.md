

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?


September 30, 2018 8:03:15 PM : well, I'm going to need an efficient way of calculating the factorial of a numbers digits. I'll start with that.
September 30, 2018 8:12:34 PM : okay, I have a working fac_sum function. Now... I'm going to make a list of all the numbers in a chain until there's a repeat.
October 1, 2018 6:28:41 AM : solved. Not much clever from me here, I just made one function to do a sum of factorials of digits and another function to build a list, make a chain and return the results of the chain.
Execution took 115 seconds and seemed to run in linear time.
October 1, 2018 6:31:56 AM : yeah, I made a timer, it's linear.