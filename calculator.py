import arithmetic

def main():
   
    symbols = {"+": arithmetic.add, "-": arithmetic.subtract, 
    "*": arithmetic.multiply, "/": arithmetic.divide, "square": arithmetic.square,
    "cube": arithmetic.cube, "pow": arithmetic.power, "mod": arithmetic.mod}

    while True:
        user_input = raw_input("> ")
        user_tokens = user_input.split()

        if user_tokens[0] == "q":
            break

        sym = symbols[user_tokens[0]]
        num1 = float(user_tokens[1])

        if len(user_tokens) == 2 and (user_tokens[0] == "square" or user_tokens[0] == "cube"):
            print sym(num1)            

        elif len(user_tokens) == 3:
            num2 = float(user_tokens[2])
            print sym(num1, num2)

        else:
            print "Wrong input!"


if __name__ == '__main__':
    main()