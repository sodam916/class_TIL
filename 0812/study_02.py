def itoa(num):
    c = [0] * 10
    while num:
        digit = num % 10
        print(digit)
        num = num // 10
        for i in digit:
            return chr(i)

val = itoa(12345)
print(type(val), val)