# Import Modules -----------------------------------

import os
import sys
import re

# Data ---------------------------------------------

# 1. Token Expression 
tokenExpression = [
    # Not token
    (r'[ ]+',                      None),
    (r'[\t]+',                     None),
    (r'//[^\n]*',                  None),
    (r'(\/)([\*])+(.|\n)+?(\2\1)', None),
    (r'\n',                        None),
    
    # Keyword
    (r'\bif\b',          "IF"),
    (r'\belse\b',        "ELSE"),
    (r'\bfor\b',         "FOR"),
    (r'\bwhile\b',       "WHILE"),
    (r'\bin\b',          "IN"),
    (r'\bswitch\b',      "SWITCH"),
    (r'\bcase\b',        "CASE"),
    (r'\bbreak\b',       "BREAK"),
    (r'\bdefault\b',     "DEFAULT"),
    (r'\bcontinue\b',    "CONTINUE"),
    (r'\bfunction\b',    "FUNCTION"),
    (r'\breturn\b',      "RETURN"),
    (r'\bdelete\b',      "DELETE"),
    (r'\bfrom\b',        "FROM"),
    (r'\bimport\b',      "IMPORT"),
    (r'\bas\b',          "AS"),
    (r'\btry\b',         "TRY"),
    (r'\bcatch\b',       "CATCH"),
    (r'\bthrow\b',       "THROW"),
    (r'\bfinally\b',     "FINALLY"),


    # Operator
    (r'\=>',       "ARROW"),
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
    (r'\+\+',      "INCREMENT"),
    (r'\-\-',      "DECREMENT"),
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
    (r'\{', "LCB"),
    (r'\}', "RCB"),

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
    print(f"   Illegal character '{char}' found at {line}:{pos}.")
    print()
    print("-----=========  ############ =========-----")
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
        
        isMatch = None
        for tokenEx in tokenExs:
            pattern, label = tokenEx

            regEx = re.compile(pattern)
            isMatch = regEx.match(text, globalPos)

            if isMatch:
                if label:
                    tokens.append(label)
                break
        
        if not isMatch:
            displayIllegal(text[globalPos], curLine, linePos)
            sys.exit(1)
        else: 
            globalPos = isMatch.end(0)

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