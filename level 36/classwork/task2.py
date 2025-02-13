def iscapitalized(user_str):
    print(user_str[0].isuper() and user_str[1:].islower())

text = input("enter centence: ")
iscapitalized(text)