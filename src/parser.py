# Functions ----------------------------------------

# 1. Parser using CYK
def parse(tokens, cnf):
    
    nTokens = len(tokens)
    encodedCode = [[set([]) for j in range(nTokens)] for i in range(nTokens)]

    for j in range(0, nTokens):
        for product, rule in cnf.items():
            for grammar in rule:
                if len(grammar) == 1 and grammar[0] == tokens[j]:
                    encodedCode[j][j].add(product)

        for i in range(j, -1, -1):
            for k in range(i, j):
                for product, rule in cnf.items():
                    for grammar in rule:
                        if len(grammar) == 2 and grammar[0] in encodedCode[i][k] and grammar[1] in encodedCode[k + 1][j]:
                            encodedCode[i][j].add(product)
    
    if 'S' in encodedCode[0][nTokens - 1]:
        return 1
    else:
        return 0

    