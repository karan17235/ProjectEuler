target = 999

def find_multiple(n):
    p = target // n
    return n*(p*(p+1)) // 2

output = find_multiple(3) + find_multiple(5) - find_multiple(15)
print(output)