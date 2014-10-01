import arithmetic

def main():
   
   while True:
    user_input = raw_input()
    user_tokens = user_input.split()
    if user_tokens[0] == "q":
        break
    else:
        num1 = int(user_tokens[1])
        num2 = int(user_tokens[2])
        print arithmetic.add(num1, num2)


if __name__ == '__main__':
    main()