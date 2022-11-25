import sys

sys.getrecursionlimit

def hello():
    print("hello world")
    hello()
hello()