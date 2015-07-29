"""
A set of matimatical functions
"""
import math
# Check for an even number
def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Check  for a modulus ( 7.777 etc )
def isodd(num):
    if float(num) % 2 == 0:
        return False
    else:
        return True

#Multiplier for the prime number multiplication.
def multiplylist(numlist):
    total = 1
    for pnum in numlist:
        total = total * pnum
    return total

def squarelist(numlist):
    total = 0
    for value in numlist:
        total += value ** 2
    return total

def isprime(n):

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes,
    #rejects other even numbers.
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range (3,int (n**0.5)+1, 2):

            if n % x == 0:
                n = n+ 1
                return False
    return True

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def primes(n):
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def gen_x(x,generator):
    """
    Generate "x" amount of items from "generator"
    """
    z = 0
    result = []
    for i in generator():
        result.append(i)
        z += 1
        if z == x:
            break
    return result

def divisors(n):
    """
    Find all divisors of n by trial division
    """
    divisors = set([1])
    for i in range(1, math.ceil(n ** 0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n/i)
    return divisors

def stufftoint(stuff):
    return list(map(int, stuff))

#fibonacci generator (to 1000 adjustable)
def fibonacci_gen(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

def listadd(l):
    result = list(l)            # Make a duplicate of d called result
    for key, value in enumerate(l):        # loop through d
        result[key] += 1        # Add one to result[key]
    return result

def count_chk(ltrs, count, prim, divcount, trigger):
    """
    Computes the number of divisors
    """
    ltrsnew = listadd(ltrs)
    divcount = multiplylist(ltrsnew)
    if divcount > trigger:
        return (ltrs, divcount)
    return (ltrs, divcount)

def int_gen ():
    i = 0
    while True:
        yield i
        i = i + 1



def count_2_variable(c2v_config, prim, count):
    result = False
    which = False
    for key, value in enumerate(c2v_config):
        if prim == value:
            which = key
            result = count
            break
    return (which, result)

# Returning a tuple from a function
def doingit(v):
  a = v+10
  b= v*20
  c = 56/v
  return c,a,b; # returns a tuple

class TriangleNum():
    """
        Thread-Safe Triangular number generator
    """
    def __init__(self):
        self.currentTri = 0 # Starting values
        self.step = 1

    def __iter__(self):
        return self  # Simplest iterator

    def next(self):
        try:
            self.currentTri+=self.step # Generate a triangular number
            self.step+=1 # update the step
            return self.currentTri # return the triangular number
        except:
            pass

def zeromaker(curnum, length):
    numofzero = length - len(str(curnum))
    string = "0" * numofzero
    return string + str(curnum)





