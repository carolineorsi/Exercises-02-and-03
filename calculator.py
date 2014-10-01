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
        else:
            sym = symbols[user_tokens[0]]
            num1 = int(user_tokens[1])
            num2 = int(user_tokens[2])
            print sym(num1, num2)


if __name__ == '__main__':
    main()