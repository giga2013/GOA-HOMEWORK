def manual_capitalize(user_str):
    capitalize_str = user_str[0].upper() + user_str[1:].lower()
    return capitalize_str

user_input = input("შემოიტანეთ სტრინგი: ")

rersult = manual_capitalize(user_input)
print("capitalize  სტრინგი:", rersult)