import re

"""
Returns the two's complement binary representation of the given number
using the given number of bits
"""
def tc_bin(n, num_bits):
    return bin(2 ** num_bits + n)[-num_bits:]

"""
Returns the binary representation of the given number
Precondition: 0 <= n < 1
"""
def frac_bin(n, max_sig_figs):
    b = ""
    sf = 0 # significant figures
    while sf < max_sig_figs:
        t = n * 2.0
        if t == 0:
            break
        elif t >= 1:
            b = b + "1"
            sf += 1
        else:
            b = b + "0"
            if sf > 0:
                sf += 1
        print "{} x 2 = {} --> {}".format(n,t,b)
        if t >= 1:
            n = round(t - 1.0,2)
        else:
            n = t
    return b

MANTISSA_BITS=9
EXPONENT_BITS=4

i=float(input("enter the float:"))
w=abs(int(i))
f=abs(i) - w
neg = (i < 0)
print("whole num:", w, " fractional part:", f, " negative:", neg)
wb = bin(w)[2:]
if (w > 0):
    e=len(wb)
else:
    e = 0
print("whole part:{} exponent:{}".format(wb,e))
fb = frac_bin(f, MANTISSA_BITS)
print("fractional part:", fb)
print("e:", e)
print("fixed point rep:" + wb + "." + fb)
# normalizing for numbers less than 1
if (w == 0):
    e = (re.search('1', fb).start())
    fb = fb[e:]
    e = -e
    print("shifted for small numbers fb:" + fb)
fpb = "0"
if w > 0:
    fpb += wb + fb
else:
    fpb += fb
fpb = (fpb + "0" * MANTISSA_BITS) [:MANTISSA_BITS]
if (neg):
    fp = (int(fpb,2)*-1)
    fpb = tc_bin(fp, MANTISSA_BITS)
print "--- Floating Point Representation is ---"
print("mantissa:" + fpb + " exponent:" + tc_bin(e, EXPONENT_BITS))