import arithmetic

def main():
   
    symbols = {"+": arithmetic.add, 
    "-": arithmetic.subtract, 
    "*": arithmetic.multiply,
    "/": arithmetic.divide, 
    "square": arithmetic.square,
    "cube": arithmetic.cube, 
    "pow": arithmetic.power, 
    "mod": arithmetic.mod}

    while True:
        user_input = raw_input("> ")
        user_tokens = user_input.split()
       
        if user_tokens[0] == "q":
            break
        if user_tokens[0] not in symbols:
            print "Not a valid operation"
            continue

        sym = symbols[user_tokens[0]]

        try:
            num1 = float(user_tokens[1])
        except ValueError:
            print("Not a valid input. Enter numbers.")
            continue

        if len(user_tokens) == 2 and (user_tokens[0] == "square" or user_tokens[0] == "cube"):
            print sym(num1)            

        elif len(user_tokens) >= 3:
            input_list = []
            for item in user_tokens[1:]:
                try:
                    input_list.append(float(item))
                except ValueError:
                    print("Not a valid input. Enter numbers.")
                    continue
            print sym(*input_list)




if __name__ == '__main__':
    main()