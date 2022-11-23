# Import modules -----------------------------------

import sys
import argparse

# Function -----------------------------------------

# 1. Display Splash Screen
def displaySplash():
    print("")
    print("       _                   _____           _       _   ")
    print("      | |                 / ____|         (_)     | |  ")
    print("      | | __ ___   ____ _| (___   ___ _ __ _ _ __ | |_ ")
    print("  _   | |/ _` \ \ / / _` |\___ \ / __| '__| | '_ \| __|")
    print(" | |__| | (_| |\ V / (_| |____) | (__| |  | | |_) | |_ ")
    print("  \____/ \__,_| \_/ \__,_|_____/_\___|_|  |_| .__/ \__|")
    print("         / ____|                    (_) |   | |        ")
    print("        | |     ___  _ __ ___  _ __  _| | __|_| __     ")
    print("        | |    / _ \| '_ ` _ \| '_ \| | |/ _ \ '__|    ")
    print("        | |___| (_) | | | | | | |_) | | |  __/ |       ")
    print("         \_____\___/|_| |_| |_| .__/|_|_|\___|_|       ")
    print("                              | |                      ")
    print("                              |_|                      ")
    print("")

# Main Program -------------------------------------

# 1. Argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type = argparse.FileType('r'))
args = parser.parse_args()

# 2. Display splash screen
displaySplash()
print(f"\nReading '{str(args.file.name)}'")
print("Compiling your code...")