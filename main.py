import math

def unique_elements(lst):
    return list(set(lst))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(minimum, maximum):
    primes = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            primes.append(num)
    return primes

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def get_coordinates(self):
        return (self.x, self.y)
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

def sort_strings(strings):
    return sorted(strings, key=lambda x: (len(x), x)), sorted(strings, key=lambda x: (len(x), x), reverse=True)

