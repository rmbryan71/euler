

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

October 1, 2018 7:09:10 PM : This is a lot like problem 39.
October 1, 2018 7:14:37 PM : I've read this : https://en.wikipedia.org/wiki/Pythagorean_triple
October 1, 2018 7:17:11 PM : I got distracted and read this: https://en.wikipedia.org/wiki/Andrew_Wiles
October 1, 2018 7:23:35 PM : I'm just going to write a method that generates all the triplets first.
October 1, 2018 7:29:12 PM : Okay, that was pretty easy. Now, I guess put all their sums in a list and return the count of sums that occur only once.