# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

m = 0
result = 0

def is_one_digit(v):
    if -10 < int(v) < 10 and v == int(v):
        return True
    else:
        return False

def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    return msg

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
            print(check(float(m), float(y), oper))
            print(result)
            print(check(m, y, oper))
        elif oper == "+" and not (x == "M" or y != "M"):
            result = float(x) + float(m)
            print(check(float(x), float(m), oper))
            print(result)
        #----------------------------------------
        elif oper == "-" and not(x == "M" or y == "M"):
            result = float(x) - float(y)
            print(result)
        elif oper == "-" and x == "M":
            result = float(m) - float(y)
            print(check(float(m), float(y), oper))
            print(result)
        elif oper == "-" and y == "M":
            result = float(x) - float(m)
            print(check(float(x), float(m), oper))
            print(result)
        #----------------------------------------
        elif oper == "*" and x == "0":
            result = float(0) * float(y)
            print(check(float(0), float(y), oper))
            print(result)
        elif oper == "*" and y == "0" and not x == "M":
            result = float(x) * float(0)
            print(check(float(x), float(0), oper))
            print(result)
        elif oper == "*" and x == "1" and not y == "M":
            result = float(1) * float(y)
            print(check(float(1), float(y), oper))
            print(result)
        elif oper == "*" and y == "1":
            result = float(x) * float(1)
            print(check(float(x), float(1), oper))
            print(result)
        elif oper == "*" and not(x == "M" or y == "M"):
            result = float(x) * float(y)
            print(result)
        elif oper == "*" and x == "M" and y == "1":
            result = float(m) * float(y)
            print(check(float(m), float(y), oper))
            print(result)
        elif oper == "*" and y == "M" and x == "1":
            result = float(x) * float(m)
            print(check(float(x), float(m), oper))
            print(result)
        elif oper == "*" and x == "M":
            result = float(m) * float(y)
            print(check(float(m), float(y), oper))
            print(result)
        elif oper == "*" and y == "M":
            result = float(x) * float(m)
            print(check(float(x), float(m), oper))
            print(result)
        #----------------------------------------
        elif oper == "/" and x == "M":
            result = float(m) / float(y)
            print(check(float(m), float(y), oper))
            print(result)
        elif oper == "/" and y == "M":
            if m == 0:
                print(check(float(x), float(m), oper))
                print(msg_3)
                continue
            else:
                print(check(float(x), float(m), oper))
                print(result)
        elif (oper == "/" and float(y) != 0) and (x != "M" or y != "M"):
            result = float(x) / float(y)
            print(result)
        elif oper == "/" and float(y) == 0:
            print(msg_3)
            continue
        #----------------------------------------
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
