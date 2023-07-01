from gf2 import *

# Chinese Remainder Theorem
# use CRT to solve two linear congruences in gf(2)
# https://www.omnicalculator.com/math/chinese-remainder
# https://github.com/ZeroBone/chrem/blob/master/chrem.py
# still dont fully know how this works tbh

# solve 3 linear congruences in gf(2)
def chrem_solve3_mod(n1,n2,n3, a1,a2,a3):
  (sol, mod) = chrem_solve2_mod(n1, n2, a1, a2)
  return chrem_solve2_mod(mod, n3, sol, a3)

# solve 2 linear congruences in gf(2)
def chrem_solve2_mod(n1,n2,a1,a2):
  (mod_gcd, u, v) = gf2_extended_gcd(n2, n1)
  
  N = gf2_mul(n1, n2)
  
  m1 = gf2_div(N, n1)
  m2 = gf2_div(N, n2)
  
  (r1,u1,v1) = gf2_extended_gcd(m1, n1)
  (r2,u2,v2) = gf2_extended_gcd(m2, n2)
  
  e1 = gf2_mul(v1, m1)
  e2 = gf2_mul(v2, m2)
  
  if mod_gcd == 1: # n1,n2 are coprime
    sol = gf2_mod(gf2_mul(a1,e1) ^ gf2_mul(a2,e2), N)
    mod = gf2_mul(n1, n2)
    return (sol, mod)
  elif (a2 ^ a1) % mod_gcd == 0:
    return None
  else: # n1,n2 aren't coprime
    mod_lcm = gf2_div(gf2_mul(n1,n2), mod_gcd)
    
    k = gf2_div(a2 ^ a1, mod_gcd)
    sol = gf2_mod(a1 ^ gf2_mul(n1, gf2_mul(u,k)), mod_lcm)
    
    return (sol, mod_lcm)
