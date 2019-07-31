#Write a function which takes in an integer n and 
# returns a one-argument function. 
# This function should take in some value x and 
# return n + x the first time it is called, similar to make_adder.
#  The second time it is called, however, 
# it should return n + x + 1, then n + x + 2 the third time, and so on.

def make_adder_inc(n):
    def adder(x):
        nonlocal n
        value = n + x
        n = n + 1
        return value
    return adder
   
   
   
   
adder1 = make_adder_inc(5)
adder2 = make_adder_inc(6)
adder1(2) 