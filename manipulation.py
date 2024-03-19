
# Prompt the user to enter a sentence
str_manip = input("Enter your sentence:\n")

# Calculate and print the length of the input sentence
length_str_manip = len(str_manip)
print("Length of the given sentence: ", length_str_manip)

# Find the last letter of the input sentence
last_letter = str_manip[-1]

# Replace the last letter of the input sentence with '@' and print the modified sentence
str_manip_replaced = str_manip.replace(last_letter, '@')
print("String with replaced last letter:\n", str_manip_replaced)

# Extract the last three characters of the input sentence in reverse order
last_three_reverse = str_manip[-1:-4:-1]

# Print the last three characters in reverse order
print("Last three characters in reverse:\n", last_three_reverse)

# Form a new word by concatenating the first three characters and the last two characters of the input sentence
five_letter_word = str_manip[:3] + str_manip[-2:]

# Print the newly formed five-letter word
print("Five letter word:\n", five_letter_word)
