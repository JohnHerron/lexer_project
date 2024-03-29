#############################
# Tokens
#############################
from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
        KEYWORD = 0
        IDENTIFIER = 1
        OPERATOR = 2
        INTEGER = 3
        SEPARATOR = 5


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
          return (f"\"{self.value}\" = " if self.value != None else "") + self.type.name