# Import Modules -----------------------------------

import keyword

# Global variables ---------------------------------

# 1. List of terminal
terminal = ['newline',
'if', 'else', 
'for', 'while',
'switch', 'case', 'break', 'default',
'continue', 'func', 'return',
'delete' ,
'from', 'import' , 'as',
'try', 'catch', 'throw', 'finally',
'arrow', 'equal',
'iseq', 'siseq', 'neq', 'sneq', 'l', 'g', 'le', 'ge',
'colon', 'semicolon',
'increment', 'decrement',
'sumeq', 'subtreq', 'muleq', 'diveq',
'add', 'subtr', 'mul', 'div', 'mod',
'comma', 'dot', 'dotbetween',
'and', 'or', 'not', 'true', 'false',
'lb', 'rb', 'lsb', 'rsb', 'lcb', 'rcb',
'int', 'string', 'null', 'undefined', 'type', 'var']

# 2. List of grammar
grammars = {}

# Functions ----------------------------------------

# 1. Read CFG
def readCFG(cfg_path):

  with open(cfg_path) as cfg_file:
    line = cfg_file.readlines()
    grammarsRaw = []
    for i in range(len(line)):
      splitLine = line[i].replace("->", "").split()
      grammarsRaw.append(splitLine)
  
  return grammarsRaw

# 2. Add a grammar to list of grammars
def addGrammar(grammarRaw):
  
  global grammars

  if grammarRaw[0] not in grammars:
    grammars[grammarRaw[0]] = []
   
  grammars[grammarRaw[0]].append(grammarRaw[1:])

# 3. Convert CFG to CNF
def cfg2cnf(grammarsRaw):

  global grammars
  product, rules = [], []

  id = 0

  for grammar in grammarsRaw:
    newGrammar = []

    # Product with 1 terminal or non-terminal
    if len(grammar) == 2 and not grammar[1][0].islower():
      product.append(grammar)
      addGrammar(grammar)
      continue

    # Product with more than 3 non-terminal
    while len(grammar) > 3:
      newGrammar.append([f"{grammar[0]}{id}", grammar[1], grammar[2]])
      grammar = [grammar[0]] + [f"{grammar[0]}{id}"] + grammar[3:]
      id += 1
    
    if grammar:
      addGrammar(grammar)
      rules.append(grammar)
    
    if newGrammar:
      for i in range(len(newGrammar)):
        rules.append(newGrammar[i])

  # Product with 1 non-terminal
  while product:
    grammar = product.pop()

    if grammar[1] in grammars:
      for item in grammars[grammar[1]]:
        newGrammar = [grammar[0]] + item

        if len(newGrammar) > 2 or newGrammar[1][0].islower():
          rules.append(newGrammar)
        else:
          product.append(newGrammar)

        addGrammar(newGrammar)
    
  return rules

# Main Program -------------------------------------

cnf_file = open('cnf.txt', 'w')
cnfRules = cfg2cnf(readCFG("cfg.txt"))

for grammar in cnfRules:
  cnf_file.write(grammar[0])
  cnf_file.write(" -> ")
  for var in grammar[1:]:
    cnf_file.write(var)
    cnf_file.write(" ")
  cnf_file.write("\n")

cnf_file.close()