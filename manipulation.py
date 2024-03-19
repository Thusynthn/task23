str_manip = input("Enter your sentence:\n")
length_str_manip = len(str_manip)
print("Length of the given sentence: ", length_str_manip)
last_letter = str_manip[-1]
str_manip_replaced = str_manip.replace(last_letter, '@')
print("String with replaced last letter:\n", str_manip_replaced)
last_three_reverse = str_manip[-1:-4:-1]
print("Last three characters in reverse:\n", last_three_reverse)
five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five letter word:\n", five_letter_word)
