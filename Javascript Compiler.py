# Import Modules -----------------------------------

import src.tokenizer as tokenizer
import src.grammar.cfg2cnf as cfg2cnf
import src.parser as parser

# Function -----------------------------------------

# 1. Display Splash Screen
def displaySplash():
    print("                                                        ")
    print("       _                   _____           _       _    ")
    print("      | |                 / ____|         (_)     | |   ")
    print("      | | __ ___   ____ _| (___   ___ _ __ _ _ __ | |_  ")
    print("  _   | |/ _` \ \ / / _` |\___ \ / __| '__| | '_ \| __| ")
    print(" | |__| | (_| |\ V / (_| |____) | (__| |  | | |_) | |_  ")
    print("  \____/ \__,_| \_/ \__,_|_____/_\___|_|  |_| .__/ \__| ")
    print("          _____                      _ _    | |         ")
    print("         / ____|                    (_) |   |_|         ")
    print("        | |     ___  _ __ ___  _ __  _| | __ __ __      ")
    print("        | |    / _ \| '_ ` _ \| '_ \| | |/ _ \ '__|     ")
    print("        | |___| (_) | | | | | | |_) | | |  __/ |        ")
    print("         \_____\___/|_| |_| |_| .__/|_|_|\___|_|        ")
    print("                              | |                       ")
    print("                              |_|                       ")
    print("                                                        ")

# 2. Display Result
def displayResult(isAccepted):
    
    if isAccepted:
        print()
        print("-----=========  ACCEPTED =========-----")
        print()
        print("Compilation successfull!")
        print()

    else:
        print()
        print("-----=========  SYNTAX ERROR =========-----")
        print()
        print("Maybe you forgot a comma?")
        print()

# Main Program -------------------------------------

# 1. Input
print("Enter the name of your code file: ", end="")
file_name = input()

while file_name.endswith(".js"):
    file_name = file_name[:-3]

file_path = f"test/{file_name}.js"

# 2. Display splash screen
displaySplash()
print(f"\nReading '{file_path}'")
print("Compiling your code...")

# 3. Validate character and Create token
tokens = tokenizer.createToken(file_path)
tokens = [token.lower() for token in tokens]

# 4. Validate grammar
cnf = cfg2cnf.mapCNF(cfg2cnf.cfg2cnf((cfg2cnf.readCFG("src/grammar/cfg.txt"))))
isAcc = parser.parse(tokens, cnf)

# 5. Display result
displayResult(isAcc)