while True:
    user_input = input()
    if user_input == 'quit' or user_input == 'Quit' or user_input == 'q':
        break
    print(user_input[::-1])
