# Import Modules -----------------------------------

import src.tokenizer as tokenizer

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
def displayResult():
    print()
    print("-----=========  ACCEPTED =========-----")
    print()
    print("Compilation successfull")
    print()

# Main Program -------------------------------------

# 1. Argparse
print("Enter the name of your code file: ", end="")
file_name = input()
file_path = f"test/{file_name}.js"

# 2. Display splash screen
displaySplash()
print(f"\nReading '{file_path}'")
print("Compiling your code...")

# 3. Validate character and Create token
tokens = tokenizer.createToken(file_path)

# 4. Validate grammar

# 5. Display result
displayResult()
