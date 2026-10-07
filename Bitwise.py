
"""
BITWISE OPERATORS :
     AND (&) :- Result bit is 1 only if both bits are 1
     Or  (|) :- Result bit is 1 if atleasr one bit is 1
     XOR (^) :- Result bit is 1 if bits are different(cross - T/F, F/T)
     NOT (~) :- Flips every bit
     LEFT SHIFT (<<) :- Moves bits left
     RIGHT SHIFT (>>) :- Moves bits right
"""

a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(~ b)
print(a << b)
print(a >> b)   #---> Data get lost due to right shift