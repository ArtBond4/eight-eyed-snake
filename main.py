"""BAD CHOICE"""
# file = open("../../my_file.txt")
# file = open("C:/Users/Art/Desktop/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

"""GOOD CHOICE"""
# mode = r - read, w - write and del(create new file), a - append
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
with open("../../my_file.txt", mode="a") as file:
    file.write("\nHello")
