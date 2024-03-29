#############################
# Read Input
#############################
from lexer import Lexer

inputFile = open("input.txt", "r")
inputText = inputFile.read()
inputFile.close()

lexer = Lexer(inputText)
tokens = lexer.generate_tokens()
print(list(tokens))