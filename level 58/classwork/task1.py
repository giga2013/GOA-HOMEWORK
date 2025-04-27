names = ["გიგა", "გიგი", "საბა", "ირკალი", "ანდრია", "ნიკოლოზი", "ალექსი", "სანდრო", "დავითი", "თომა"]

renewed = [n for n in names if len(n) < 6 or n.startswith("ა")]

print(renewed)
