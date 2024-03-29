#############################
# Lexer
#############################
from tokens import Token, TokenType

WHITESPACE = " \n\t"
DIGITS = "0123456789"
OPERATORS = "+-/*!=<>^"
SEPARATORS = "();{}"
KEYWORDS = ["return","if","else","function","while","for","do"]

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
    
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in DIGITS:
                current_token = Token(TokenType.INTEGER, self.current_char)
                self.advance()
                yield current_token
            elif self.current_char in OPERATORS:
                if self.current_char == "/" and next(self.text, None) == "/":
                    self.skip_comment()
                current_token = Token(TokenType.OPERATOR, self.current_char)
                self.advance()
                yield current_token
            elif self.current_char in SEPARATORS:
                current_token = Token(TokenType.SEPARATOR, self.current_char)
                self.advance()
                yield current_token
            else:
                yield self.generate_phrase()

    # function to generate identifier and keyword tokens
    def generate_phrase(self):
        print(self.current_char)
        phrase = self.current_char
        self.advance()

        while self.current_char != None and self.current_char not in (WHITESPACE + SEPARATORS + OPERATORS):
            phrase += self.current_char
            self.advance()
            if phrase in KEYWORDS:
                return Token(TokenType.KEYWORD, phrase)

        if self.current_char == None or self.current_char in (WHITESPACE + SEPARATORS):
            return Token(TokenType.IDENTIFIER, phrase)
        else:
            raise Exception(f"Illegal character '{self.current_char}' after declaration of phrase '{phrase}'")
    
    # skips a single line of text until newline is reached
    def skip_comment(self):
        while(self.current_char != None and self.current_char != "\n"):
            self.advance()
