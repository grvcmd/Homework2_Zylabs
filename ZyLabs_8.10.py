user_input = input()

first_word = ""
for x in user_input:
    if x != ' ':
        first_word += x

backwards = ""
for x in first_word:
    backwards = x + backwards
if (first_word==backwards):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")