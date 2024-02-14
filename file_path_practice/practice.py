# Reading a file in read mode
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# Write to a file in write mode, w writes over the contents, a = appends and adds to the contents
# with open('my_file.txt', mode='a') as file:
#     file.write('\nNew Text.')
#
# # if file doesnt exist, it creates a new one in the active directory
# with open('new_file.txt', mode='a') as file:
#     file.write('\nNew Text.')

with open(r"\Users\salba\OneDrive\Desktop\new_file.txt") as file:
    contents = file.read()
    print(contents)
