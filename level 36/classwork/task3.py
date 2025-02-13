def manual_isdigit(user_str):
    digist = (9876543210)
    valid = True

    for char in user_str:
        if char in digist:
            print("corect charater")

    else:
        valid = False
        print("incorect charter")

    print("valid")

manual_isdigit("123d")