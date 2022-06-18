# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

m = 0
result = 0

while True:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split(" ")
    if (x.isalpha() or y.isalpha()) and not (x == "M" or y == "M"):
        print(msg_1)
    elif oper == "+" or oper == "-" or oper == "*" or oper == "/":
        if oper == "+" and not(x == "M" or y == "M"):
            result = float(x) + float(y)
            print(result)
        elif oper == "+" and not (x != "M" or y == "M"):
            result = float(m) + float(y)
            print(result)
        elif oper == "+" and not (x == "M" or y != "M"):
            result = float(x) + float(m)
            print(result)
        #----------------------------------------
        elif oper == "-" and not(x == "M" or y == "M"):
            result = float(x) - float(y)
            print(result)
        elif oper == "-" and x == "M":
            result = float(m) - float(y)
            print(result)
        elif oper == "-" and y == "M":
            result = float(x) - float(m)
            print(result)
        #----------------------------------------
        elif oper == "*" and not(x == "M" or y == "M"):
            result = float(x) * float(y)
            print(result)
        elif oper == "*" and x == "M":
            result = float(m) * float(y)
            print(result)
        elif oper == "*" and y == "M":
            result = float(x) * float(m)
            print(result)
        #----------------------------------------
        elif oper == "/" and x == "M":
            result = float(m) / float(y)
            print(result)
        elif oper == "/" and y == "M":
            if m == 0:
                print(msg_3)
                continue
            else:
                print(result)
        elif (oper == "/" and float(y) != 0) and (x != "M" or y != "M"):
            result = float(x) / float(y)
            print(result)
        #----------------------------------------
        elif oper == "/" and float(y) == 0:
            print(msg_3)
            continue
        print(msg_4)
        answer1 = input()
        if answer1 == "y":
            m += result
            print(msg_5)
            answer2 = input()
            if answer2 == "y":
                continue
            elif answer2 == "n":
                break
        elif answer1 == "n":
            print(msg_5)
            answer3 = input()
            if answer3 == "y":
                continue
            elif answer3 == "n":
                break

    else:
        print(msg_2)
