# Uses python3
# python3 aplusb.py <<< "3 5"
import sys
#input = sys.stdin.read()
input = input("input: ")
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
