import pyfiglet

def convert(text):
    ascii_text = pyfiglet.figlet_format(text)
    return ascii_text

input_text = input("Enter text to convert: ")
output_text = convert(input_text)
print(output_text)
