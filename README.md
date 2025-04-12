# 🔢 Python Numeric Literal Checker

This project implements a Non-deterministic Finite Automaton (NFA) to recognize Python integer literals according to the official Python Language Specification. Our implementation demonstrates how formal language theory and automata can be applied to practical programming language parsing.

## Project Overview

This application:
- Uses NFAs to validate Python numeric literals without relying on regex or built-in parsing 
- Processes decimal, octal, hexadecimal, and floating point formats
- Combines individual NFAs into a single unified automaton
- Includes comprehensive test cases covering valid and invalid inputs
- Provides visual representations of all state machines

The project showcases both theoretical concepts from automata theory and practical implementation in Python, demonstrating how formal language recognition works in programming language design.

## Integer Literals

According to the [Python documentation](https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals), integer literals follow these lexical definitions:

```
integer      ::= decinteger | bininteger | octinteger | hexinteger
decinteger   ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
bininteger   ::= "0" ("b" | "B") (["_"] bindigit)+
octinteger   ::= "0" ("o" | "O") (["_"] octdigit)+
hexinteger   ::= "0" ("x" | "X") (["_"] hexdigit)+
nonzerodigit ::= "1"..."9"
digit        ::= "0"..."9"
bindigit     ::= "0" | "1"
octdigit     ::= "0"..."7"
hexdigit     ::= digit | "a"..."f" | "A"..."F"
``` 

Our NFA implementation supports decimal integers (e.g., `123`, `0`, `1_000`), octal integers (e.g., `0o777`, `0O123`), hexadecimal integers (e.g., `0xff`, `0XAB`), and floating point literals (e.g., `3.14`, `1e100`, `3.14e-10`)  with proper handling of underscore separators according to the specification.   


## Floating-point literals

According to the [Python documentation](https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals), Floating-point literals are described by the following lexical definitions:

floatnumber   ::= pointfloat | exponentfloat
pointfloat    ::= [digitpart] fraction | digitpart "."
exponentfloat ::= (digitpart | pointfloat) exponent
digitpart     ::= digit (["_"] digit)*
fraction      ::= "." digitpart
exponent      ::= ("e" | "E") ["+" | "-"] digitpart

Note that the integer and exponent parts are always interpreted using radix 10. For example, 077e010 is legal, and denotes the same number as 77e10. The allowed range of floating-point literals is implementation-dependent. As in integer literals, underscores are supported for digit grouping.

Some examples of floating-point literals:

3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93


---


## 👩‍💻 Team: Three Musketeers 

| Name | GitHub | Tasks |
|------|--------|-------|
<<<<<<< HEAD
| Roshan Karimi | [Roshaaw](https://github.com/Roshaaw) | Octal literal code implementation, Octal NFA diagram, Floating Point NFA diagram README documentation |
| Lindsay Kislingbury | [lindsay-kislingbury](https://github.com/lindsay-kislingbury) | Hexadecimal literal implementation, Floating Point NFA diagram, Hexadecimal NFA diagram, Combined NFA integration, Test framework development |
| Kaila Manaligod Manangan | [kailamanangan16](https://github.com/kailamanangan16) | Decimal literal code implementation, Decimal NFA diagram, Floating Point implementation Test case validation |
=======
| Roshan Karimi | [Roshaaw](https://github.com/Roshaaw) | Octal literal code implementation, Octal NFA diagram, Float NFA diagram, README documentation |
| Lindsay Kislingbury | [lindsay-kislingbury](https://github.com/lindsay-kislingbury) | Hexadecimal literal implementation, Hexadecimal NFA diagram, FLOAT NFA diagram, Combined NFA integration, Test framework development |
| Kaila Manaligod Manangan | [kailamanangan16](https://github.com/kailamanangan16) | Decimal literal code implementation, Decimal NFA diagram, Test case validation |
>>>>>>> e602e72b6065ade2bc4c0aad4c93fa52ccc99d6b

> All group members collaborated via voice calls to design **each individual NFA** and the **combined NFA**. We worked together on transitions, testing, and JFLAP design. Each member implemented code for one specific number type, but the logic and NFA design were collaborative.


## ⚙️ How to Run

`python main.py [input_file] [output_file]`

`[input_file]` is required and must be located in project root.   
`[output_file]` is not required. If not provided, the program will overwrite out.txt by default.

**Input File Format:**  
Each line should contain a test case followed by "accept" or "reject", such as:

```
123 accept
0xff accept
0o777 accept
01 reject
1e100 accept
``` 

- The empty string can be tested with just "accept" or "reject" on a line
- Empty lines are skipped
- Lines starting with # will be processed as test cases, not comments

**Output Format:**  
The program produces a formatted report showing:
- A summary of tests run, passed, and failed
- Detailed results for each test case


---

## 📁 NFA Diagrams

The `nfa` folder contains visual representations of our automata designs:

- **Decimal NFA**: State diagram showing the automaton that recognizes Python decimal literals
- **Octal NFA**: State diagram showing the automaton that recognizes Python octal literals
- **Hexadecimal NFA**: State diagram showing the automaton that recognizes Python hexadecimal literals 
- **Floating Point NFA**: State diagram showing the automaton that recognizes Python floating point literals
- **Combined NFA**: The unified automaton that integrates all three NFAs to recognize any valid Python integer literal

Each diagram is available in both JFLAP file format (`.jff`) for further exploration and as image files (`.jpg`) for quick reference. These diagrams were essential to our implementation process and directly correspond to the transition functions in our code.

--- 


## 📎 Notes
- Implementation follows strict automata theory principles without relying on any built-in parsing, regex, or third-party libraries
- All state transitions in code directly correspond to our NFA diagrams
- The project uses a modular design where each numeric type is handled by a dedicated NFA module



