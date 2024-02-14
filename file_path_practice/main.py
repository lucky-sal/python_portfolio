# Create a letter to send to a list of names from included files

# open the invited names, create a list from the file and strip the unwanted characters
with open("../file_path_practice/Input/Names/invited_names.txt") as file_names:
    names_list = file_names.readlines()
    modified_list = [item.strip() for item in names_list]

# open the letter template and save the format to a variable
with open("../file_path_practice/Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()

# loop through each name in the new list and create the letter
for name in modified_list:
    new_letter_content = letter_contents.replace('[name]', name)
    new_file = f'letter_for_{name}.txt'

    # in the loop, create a new letter into a file
    with open(f"../file_path_practice/Output/ReadyToSend/{new_file}", mode='w') as output_letter:
        output_letter.write(new_letter_content)