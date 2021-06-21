a = int(input())
b = int(input())
c = int(input())
if a > b:
    if b < c:
        print(b)
if a > c:
    if c < b:
        print(c)
if a < b:
    if a < c:
        print(a)

if a < b:
    if a == c:
        print(a)
if b < a:
    if b == c:
        print(b)
if a < c:
    if a == b:
        print(a)
if a == b:
    if b == c:
        print(c)
