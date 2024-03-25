#############################
# Read Input
#############################
from lexer import Lexer

inputText = ""

while True:
    inputText = input("basic-b > ")
    if inputText == "EXIT":
        break
    lexer = Lexer(inputText)
    tokens = lexer.generate_tokens()
    print(list(tokens))

print("\n-----------------------------------------------\n Exitted Basic-Barrel interpreter successfully.\n-----------------------------------------------\n")