
text = True

while text:
    text_with_h = input("Please enter some text with 'h' letter: ")
    for letter in text_with_h:
        if letter == 'h' or letter == 'H':
            text = False