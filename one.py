import os 
import sys

# Comment

print(sys.path)

help("modules")

days = 7
def say_hello(person):
    print(f'Hello, world! Hello {person}')
    return person

say_hello('Ulrik')