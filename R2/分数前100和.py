from fractions import Fraction
fz=2;fm=1;sum=Fraction(0)
for i in range(100):
    x = Fraction(fz , fm)
    sum+=x
    fm, fz = fm + fz, fm
print(float(sum))