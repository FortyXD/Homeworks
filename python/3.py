print("введите end чтобы закончить последовательность")
x = input()
if not x.isdigit():
    print("это не число")
max_elem = 0
while x != "end":
    if not x.isdigit():
        print("это не число")
    else:
        e = int(x)
        if e > max_elem:
            max_elem = e
    x = input()
print(max_elem)
