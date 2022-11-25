# TBFO - JavaScript (Node.js) Compiler
## Tubes TBFO
Tubes of Teori Bahasa Formal dan Otomata (IF2124). A simple compiler for javaScript (Node.js) codes built in python utilizing FA, CFG, CNF, and CYK Algorithm.
## Contributors (momen)
- 13521017 Varraz Hazzandra Abrar <br/>
- 13521019 Ditra Rizqa Amadia <br/>
- 13521020 Bagus Lathif Firmansyah <br/>
## Program Features
Syntax validator for:
- Import
- Assignment
- Arithmetic Operation
- Logical Operation
- If Conditional
- Switch Case Conditional
- Function
- Method
- For Loop
- While Loop
- Try Catch
- JSON
## Project Structure
```bash
.
├── doc ------------------------------------------ Folder containing project report
│   └── TBFO-momen.pdf
├── result --------------------------------------- Folder containing token from input file
│   └── tokenResult.txt
├── src ------------------------------------------ Folder containing source files
│   ├── grammar ---------------------------------- Folder containing grammar
│   │   ├── cfg_dev.txt
│   │   ├── cfg.txt
│   │   ├── cfg2cnf.py --------------------------- CFG to CNF converter
│   │   └── cnf.txt
|   ├── parser.py -------------------------------- CYK parser
│   └── tokenizer.py ----------------------------- Tokenizer
├── test ----------------------------------------- Folder containing test files
│   ├── 1-import.js
│   ├── 2-aritOp.js
│   ├── 3-logicOp.js
│   ├── 4-assignment.js
│   ├── 5-conditional.js
│   ├── 6-switch.js
│   ├── 7-function.js
│   ├── 8-comment.js
│   ├── 9-method.js
│   ├── 10-forLoop.js
│   ├── 11-whileLoop.js
│   ├── 12-tryCatch.js
│   ├── 13-json.js
│   ├── 14-emptyFile.js
│   ├── 15-illegalChar.js
│   ├── 16-illegalGram.js
│   ├── 17-illegalGram.js
│   ├── 18-wrongType.py
│   ├── inputAcc.js
│   └── inputReject.js  
├── Javascript Compiler.py
└── README.md
```
## Local Setup
1. Clone this repository
2. Run program by double clicking ```Javascript Compiler.py``` or
3. Run program by terminal ```python "Javascript Compiler.py"```
## Technology Used
- Python
- JavaScript
