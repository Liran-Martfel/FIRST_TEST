word = []
while True:
    user_input = input("Enter string: ")
    user_input = user_input.lower()
    if user_input == 'quit':
        break
    word.append(user_input)

duplicates = False
for item in word:
    if word.count(item) > 1:
        duplicates = True
        break

if duplicates:
    print("There were duplicates")
else:
    print("There were no duplicates")