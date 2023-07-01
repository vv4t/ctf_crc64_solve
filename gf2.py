
# GF(2) implementation
#
# TLDR;
# a+b = a^b
# a-b = a^b
#
# a*b: polynormial division mod 2
# a/b: polynomial division mod 2
#
# http://www.ee.unb.ca/cgi-bin/tervo/calc.pl
# https://en.wikipedia.org/wiki/GF(2)
# 
# scuffed implementation of stuff from GF(2) calculator

show = False

def gf2_mul(a, b):
  res = 0
  
  if b > a:
    tmp = a
    a = b
    b = tmp
  
  i = 0
  while a > 0:
    res ^= ((a & 1) * b) << i
    a >>= 1
    i += 1
  
  return res

def gf2_div_mod(a, b):
  r = a
  q = 0
  
  # long division in GF(2)
  
  n = 0
  while (b >> n) > 0:
    n += 1
  
  while True:
    i = 0
    while (r >> i) > 0:
      i += 1
    
    if i < n:
      break
    
    q |= (1 << (i-n))
    r ^= (b << (i-n))
  
  return (q,r)

def gf2_div(a, b):
  (q,r) = gf2_div_mod(a, b)
  return q

def gf2_mod(a, b):
  (q,r) = gf2_div_mod(a, b)
  return r

def gf2_gcd(a, b):
  if b == 0:
    return a
  
  return gf2_gcd(b, gf2_mod(a, b))

def gf2_extended_gcd(a, b):
  if b == 0:
    if show:
      print()
      print("Now working backwards to obtain Bezout's identity")
    
    return (a,0,1)
  
  # gcd
  if show:
    print("{} = {}*({}) + {}".format(a, gf2_div(a,b), b, gf2_mod(a,b)))
  
  (r,x1,y1) = gf2_extended_gcd(b, gf2_mod(a, b))
  
  x = y1 ^ gf2_mul(gf2_div(a,b), x1)
  y = x1
  
  # reverse gcd
  if show:
    print("{} = {}*{} + {}*{}".format(r, a, y, b, x))
  
  return (r,x,y)

def gf2_lcm(a, b):
  return gf2_div(gf2_mul(a,b), gf2_gcd(a,b))

if __name__ == "__main__":
  show = True
  
  a = 4073
  b = 107
  
  print("Extended Euclidean algorithm in GF(2)")
  (r,x,y) = gf2_extended_gcd(a, b)
  print("gcd({},{})".format(a, b))
  print()
  print("Hence we have")
  print("{} = {} (mod {})".format(r, b, a))
