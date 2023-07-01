# Example solving the CRC using known values

from gf2 import *
from chrem import *

def solve():
  flag = "BEGINNER{0123456789abcdef}"
  num = str_to_int(flag)
  
  print("==== TARGET ====")
  print("plaintext:", flag)
  print("hex:", hex(num))
  print()
  
  # polynomials in crc.c
  p1 = 0x42f0e1eba9ea3693
  p2 = 0xad93d23594c935a9
  p3 = 0x1337C0DE15BAAAAD
  
  a1 = crc64(num, p1)
  a2 = crc64(num, p2)
  a3 = crc64(num, p3)
  
  print("crc1:", hex(a1))
  print("crc2:", hex(a2))
  print("crc3:", hex(a3))
  print()
  
  n1 = p1 | (1<<64)
  n2 = p2 | (1<<64)
  n3 = p3 | (1<<64)
  
  print("GF(2) Divisors")
  print("n1:", hex(n1))
  print("n2:", hex(n2))
  print("n3:", hex(n3))
  print()
  
  print("=== SOLUTION ===")
  
  (sol, mod) = chrem_solve3_mod(n1,n2,n3, a1,a2,a3)
  
  print("x =", hex(sol))
  print()
  print("x satisfies the linear congruences")
  print("x = {} (mod {})".format(hex(a1), hex(n1)))
  print("x = {} (mod {})".format(hex(a2), hex(n2)))
  print("x = {} (mod {})".format(hex(a3), hex(n3)))
  print()
  print("incrementing x to find an integer which matches the flag...")
  
  flag_start = "BEGINNER{"
  start = str_to_int(flag_start)
  
  i = 0
  ans = sol
  
  while ans >> 17*8 != start:
    ans = sol ^ gf2_mul(mod, i)
    i += 1
  
  print("Found:", int_to_str(ans))

# 64-bit crc
def crc64(num, poly):
  crc = 0
  
  # convert number to binary
  b = bin(num)[2:]
  
  for data in b:
    bit = crc & 0x8000000000000000
    crc = (crc << 1) & 0xffffffffffffffff | int(data)
    
    if bit:
      crc ^= poly
  
  return crc

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
