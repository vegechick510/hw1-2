def my_pow(a, b):
    print("a: {}, b: {} \nCalculating a^b...".format(a, b))
    if a==0 and b==0:
        return -1
    c = 1
    for i in range(b):
        c = c * a
    return c
my_pow(2, "3")