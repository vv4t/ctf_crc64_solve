# Solve the ctf

from gf2 import *
from chrem import *

def solve():
  # polynomials in crc | the divisor in gf(2)
  # insert bit at the end since crc64 assumes it exists 
  n1 = 0x42f0e1eba9ea3693 | (1<<64)
  n2 = 0xad93d23594c935a9 | (1<<64)
  n3 = 0x1337C0DE15BAAAAD | (1<<64)
  
  # target CRCs | modulo in gf(2)
  a1 = 0x8d264fc84bbeede9
  a2 = 0x714ceac2d7a3aaa8
  a3 = 0x780486b31ee4df55
  
  # solve the three congruences using CRT
  #
  # x = a1 (mod n1)
  # x = a2 (mod n2)
  # x = a3 (mod n3)
  #
  (solution, mod) = chrem_solve3_mod(n1,n2,n3, a1,a2,a3)
  
  # not the flag yet
  #
  # to generate more solutions to the congruences
  # add multiples of the moduli from the previous solution
  #
  # (x + N*i) = a1 (mod n1)
  # (x + N*i) = a2 (mod n2)
  # (x + N*i) = a3 (mod n3)
  
  flag_start = "BEGINNER{"        # known plaintext
  start = str_to_int(flag_start)  # convert to integer for quick flag validation
  
  i = 0
  ans = solution
  
  # the last 9 bytes of the integer will be flag_start
  # quick way to check if it's the flag is to shift out the unknown 17 bytes
  # then check for flag_start
  while ans >> 17*8 != start:
    ans = solution ^ gf2_mul(mod, i)
    i += 1
  
  print(int_to_str(ans))

# get string bytes as a long integer
def str_to_int(s):
  x = 0
  for i in range(len(s)):
    x = (x << 8) | ord(s[i])
  return x

# convert bytes in integer to string
def int_to_str(n):
  s = ""
  while n > 0:
    s += chr(n & 0xff)
    n >>= 8
  
  return s[::-1]

solve()
