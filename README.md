# Rookie Code Rumble CTF: Ancient Aliens

[Rookie Rumble](https://ctf.secso.cc/)

> WARNING!!! THIS CHALLENGE IS HARD (i think)!!!
> 
> We have been intercepting the alien communications, and it seems they are using an old, cryptographically insecure hashing function with constraints as a means of encrypting their messages... Using the intercepted data, we have created a small testing program. Using the source code for this program, determine which input string will pass the checks in place.
>
> Author: @captainboggle

Source: `crc.c`

This is my implementation of yellowsubmarine's solution

> Chinese Remainder Theorem over polynomials in GF(2)
>
> CRC is polynomial division with some divisor which returns a remainder. Since this was applied to multiple different remainders, and GF(2) polynomials form what's called a mathematical "ring", properties like factoring, multiplication etc. allow CRT to apply.
@yellowsubmarine

I thought this was interesting so I gave a shot at implementing it

### Scripts
Solve the ctf
```
> python ctf_solve.c
```

Example solving a known message
```
> python known_solve.c
```

Example solving integers instead of text
```
> python num_solve.py
```

GF(2) demonstration of extended euclidean algorithm
```
> python gf2.py
```

### Useful Stuff
[Detailed rundown of how CRC works](https://sar.informatik.hu-berlin.de/research/publications/SAR-PR-2006-05/SAR-PR-2006-05_.pdf)

[Chinese Remainder Theorem](https://www.omnicalculator.com/math/chinese-remainder)

[CRT Solver in python](https://github.com/ZeroBone/chrem/blob/master/chrem.py)

[GF(2) Demonstration](http://www.ee.unb.ca/cgi-bin/tervo/calc.pl)
