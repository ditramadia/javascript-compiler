# Token Expression ---------------------------------

tokenExpression = [
    # Not token
    (r'[ \t]+',                                     None),
    (r'#[^\n]*',                                    None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'', None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"', None),
    (r'\n',                                         "NEWLINE"),
    
    # Operator
    (r'\=(?!\=)', "EQUAL"),
    (r'\==',      "ISEQ"),
    (r'\===',     "SISEQ"),
    (r'!=',       "NEQ"),
    (r'!==',      "SNEQ"),
    (r'<',        "L"),
    (r'>',        "G"),
    (r'<=',       "LE"),
    (r'>=',       "GE"),
    (r'\:',       "COLON"),
    (r'\;',       "SEMICOLON"),
    (r'\+=',      "SUMEQ"),
    (r'-=',       "SUBTREQ"),
    (r'\*=',      "MULEQ"),
    (r'/=',       "DIVEQ"),
    (r'\+',       "ADD"),
    (r'\-',       "SUBTR"),
    (r'\*',       "MUL"),
    (r'/',        "DIV"),
    (r'\%',       "MOD")
    (r'\,',       "COMMA"),
    (r'\.',       "DOT"),
    (r'\w+[.]\w', "DOTBETWEEN"),
    (r'\->',      "ARROW"),
    (r'\&&',      "AND"),
    (r'\||',      "OR"),
    (r'\!',       "NOT"),

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
    (r'\blet\b',               "TYPE"),
    (r'\bvar\b',               "TYPE"),
    (r'\bconst\b',             "TYPE"),

    # Variable
    (r'[A-Za-z_][A-Za-z0-9_]*', "VAR"),




]