def funk(stry):
    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False


    def add(x, y):
        if is_number(x) == True & is_number(y) == True:
            return str(int(x) + int (y))
        else:
            return "ERR"


    def sub(x, y):
        if is_number(x) == True & is_number(y) == True:
            return str(int(x) - int(y))
        else:
            return "ERR"


    def mul(x, y):
        if is_number(x) == True & is_number(y) == True:
            return str(int(x) * int(y))
        else:
            return "ERR"


    def dif(x, y):
        if is_number(x) == True & is_number(y) == True:
            if y =='0':
                return "ERR"
            else:

                return str(int(x) / int(y))
        else:
            return "ERR"


    def porw(x, y):
        if x.isdigit() == True & y.isdigit() == True:
            return str(pow(int(x), int(y)))
        else:
            return "ERR"


    s = []
    handle = open(stry+".txt", "r")
    asd = ""
    file = open('answers.txt', "w")
    for line in handle:
        s.append(line)
    for i in range(0, len(s)):

        a, b, c = s[i].split()

        if b == "add":
            asd = asd + add(a, c) + '\n'
        elif b == "sub":
            asd = asd + sub(a, c) + '\n'

        elif b == "mul":
            asd = asd + mul(a, c) + '\n'

        elif b == "div":
            asd = asd + dif(a, c) + '\n'

        elif b == "pow":
            asd = asd + porw(a, c) + '\n'

        else:
            asd = asd + "ERR" + '\n'

    file.write(asd)
    file.close()
    handle.close()
