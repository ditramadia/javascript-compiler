# Import Modules -----------------------------------

import os
import sys
import re

# Data ---------------------------------------------

# 1. Token Expression 
tokenExpression = [
    # Not token
    (r'[ \t]+',                                     None),
    (r'//[^\n]*',                                   None),
    (r'\n',                                         "NEWLINE"),
    
    # Keyword
    (r'\bif\b',                 "IF"),
    (r'\belse\b',               "ELSE"),
    (r'\bfor\b',                "FOR"),
    (r'\bwhile\b',              "WHILE"),
    (r'\bbreak\b',              "BREAK"),
    (r'\bcontinue\b',           "CONTINUE"),
    (r'\bfrom\b',               "FROM"),
    (r'\bimport\b',             "IMPORT"),
    (r'\bas\b',                 "AS"),
    (r'\bfunction\b',           "FUNCTION"),
    (r'\breturn\b',             "RETURN"),
    (r'\bclass\b',              "CLASS"),
    (r'\bconsole.log\b',        "PRINT"),

    # Operator
    (r'\=(?!\=)',  "EQUAL"),
    (r'\==',       "ISEQ"),
    (r'\===',      "SISEQ"),
    (r'!=',        "NEQ"),
    (r'!==',       "SNEQ"),
    (r'<',         "L"),
    (r'>',         "G"),
    (r'<=',        "LE"),
    (r'>=',        "GE"),
    (r'\:',        "COLON"),
    (r'\;',        "SEMICOLON"),
    (r'\+=',       "SUMEQ"),
    (r'-=',        "SUBTREQ"),
    (r'\*=',       "MULEQ"),
    (r'/=',        "DIVEQ"),
    (r'\+',        "ADD"),
    (r'\-',        "SUBTR"),
    (r'\*',        "MUL"),
    (r'/',         "DIV"),
    (r'\%',        "MOD"),
    (r'\,',        "COMMA"),
    (r'\.',        "DOT"),
    (r'\w+[.]\w',  "DOTBETWEEN"),
    (r'\->',       "ARROW"),
    (r'\&&',       "AND"),
    (r'\|\|',       "OR"),
    (r'\!',        "NOT"),
    (r'\btrue\b',  "TRUE"),
    (r'\bfalse\b', "FALSE"),

    # Brackets
    (r'\(', "LB"),
    (r'\)', "RB"),
    (r'\[', "LSB"),
    (r'\]', "RSB"),
    (r'\}', "LCB"),
    (r'\{', "RCB"),
    (r'\{', "RCB"),

    # Type
    (r'[\+\-]?[0-9]*\.[0-9]+', "INT"),
    (r'[\+\-]?[1-9][0-9]+',    "INT"),
    (r'[\+\-]?[0-9]+',         "INT"),
    (r'\"[^\"\n]*\"',          "STRING"),
    (r'\"[^\'\n]*\"',          "STRING"),
    (r'\bnull\b',              "NULL"),
    (r'\bundefined\b',         "UNDEFINED"),
    (r'\blet\b',               "TYPE"),
    (r'\bvar\b',               "TYPE"),
    (r'\bconst\b',             "TYPE"),

    # Variable
    (r'[A-Za-z_][A-Za-z0-9_]*', "VAR"),
]

# Functions ----------------------------------------

# 1. Display Illegal Character Result
def displayIllegal(char, line, pos):
    print()
    print("-----=========  SYNTAX ERROR =========-----")
    print()
    print(f"Illegal character '{char}' found at {line}:{pos}.")
    print()    

# 2. Tokenizer
def tokenizer(text, tokenExs):

    # Initialization
    globalPos = 0
    linePos = 1
    curLine = 1
    totalChar = len(text)
    tokens = []

    # Checking characters
    while globalPos < totalChar:

        if text[globalPos] == '\n':
            curLine += 1
            linePos = 1
        
        isNErr = None
        for tokenEx in tokenExs:
            pattern, label = tokenEx

            regEx = re.compile(pattern)
            isNErr = regEx.match(text, globalPos)

            if isNErr:
                if label:
                    tokens.append(label)
                break
        
        if not isNErr:
            displayIllegal(text[globalPos], curLine, linePos)
            sys.exit(1)
        else: 
            globalPos = isNErr.end(0)

        linePos += 1
    
    return tokens

# 3. Create Token
def createToken(text):

    # Read file
    file = open(text, encoding="utf8")
    content = file.read()
    file.close()

    # Create token
    tokensResult = tokenizer(content, tokenExpression)

    # Write file
    path = os.getcwd()
    fileWrite = open(path + "/result/tokenResult.txt", 'w')

    for token in tokensResult:
        fileWrite.write(str(token) + " ")
    fileWrite.close()

    return tokensResult