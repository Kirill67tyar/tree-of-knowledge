from pprint import pprint as pp

# pp(dir(int))
# help(int)
# print(int.__doc__)

# base=2 - двоичная система исчисления
d = int('1101', base=2)
# значение нашего двоичного числа 1101 - 13
print(d) # 13
print(bin(13)) # 0b1101

s = 7
pp(dir(s))
"""
методы int

 'as_integer_ratio',
 'bit_length',
 'conjugate',
 'denominator',
 'from_bytes',
 'imag',
 'numerator',
 'real',
 'to_bytes'
"""
s = 7
print(s.as_integer_ratio()) # (7, 1)
print(s.bit_length()) # 3
print(s.conjugate()) # 7
print(s.denominator) # 1
print(s.from_bytes) # <built-in method from_bytes of type object at 0x00007FFA9D799FD0>
print(s.imag) # 0
print(s.numerator) # 7
print(s.real) # 7
print(s.to_bytes) # <built-in method to_bytes of int object at 0x0000025E105F69F0>



