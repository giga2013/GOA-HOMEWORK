while True:
    user_input = input("შეიყვანეთ ტექსტი: ")
    if user_input.lower() == "გასასვლელი":
        print("პროგრამა დასრულდა. ნახვამდის!")
        break
    else:
        print(f"თქვენ შეიყვანეთ: {user_input}")
