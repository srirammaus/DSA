
# << means adding left 0 in binary if 11 << 1 = 22,11 < 2 =44 its doubling means each values are multiplied by 2 ,
a = 120
b=  a << 1
c = a << 2
d = a << 3
print(format(a,'08b'))
print(format(b,'08b'))
print(format(c,'08b'))
print(format(d,'08b'))



print(b)
print(c)
print(d)

# each values are divided by 2
a = 123
b=  a >> 1
c = a >> 2
d = a >> 3
print(format(a,'08b'))
print(format(b,'08b'))
print(format(c,'08b'))
print(format(d,'08b'))



print(b)
print(c)
print(d)

# AND operator & , is gennerally used to find odd or even , how becuase comparing anythin with shows which is oddd or even if & shows the last bit of binary  if anythin comapred with 1 if odd then last bit is 1 if even last bit even
a = 1
n = 11

result = a & n
print(f"{a:08b}")      # prints a in 8-bit binary
print(f"{n:08b}")      # prints b in 8-bit binary
print(f"{result:08b}") # prints result in 8-bit binary