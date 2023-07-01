from gf2 import *
from chrem import *

# CRC example using normal integers
# math in GF(2)

def num_solve():
  num = 439259 # unknown dividend (flag)
  
  print("==== TARGET ====")
  print("num:", num)
  
  # non co-prime divisors (polynomials)
  p1 = gf2_mul(4723, 5)
  p2 = 3037
  p3 = gf2_mul(2371, 5)
  
  # remainders (crc)
  c1 = gf2_mod(num, p1)
  c2 = gf2_mod(num, p2)
  c3 = gf2_mod(num, p3)
  print("x = {} (mod {})".format(c1, p1))
  print("x = {} (mod {})".format(c2, p2))
  print("x = {} (mod {})".format(c3, p3))
  
  (sol,mod) = chrem_solve3_mod(p1,p2,p3, c1,c2,c3)
  
  print("=== SOLUTION ===")
  print("x =", sol)

num_solve()
