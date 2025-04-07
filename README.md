# 🔢 Python Numerical Literals NFA Recognition

This project implements a Non-deterministic Finite Automaton (NFA), and equivalent code, to recognize Python numerical literals based on the Python Language Specification. It supports decimal, octal, and hexadecimal integer literals. Extra credit for floating point literals was **not** implemented.

---

## 👨‍👩‍👧 Group Members

| Full Name                  | GitHub Username         | Tasks Completed                      |
|---------------------------|--------------------------|--------------------------------------|
| Roshan Karimi             | `Roshaaw`                | Octal literal code implementation    |
| Lindsay Kislingbury       | `lindsay-kislingbury`    | Hexadecimal literal implementation   |
| Kaila Manaligod Manangan  | `kailamanangan16`        | Decimal literal code implementation  |

> All group members collaborated via voice calls to design **each individual NFA** and the **combined NFA**. We worked together on transitions, testing, and JFLAP design. Each member implemented code for one specific number type, but the logic and NFA design were collaborative.

---

## 📁 Project Structure


---

## ⚙️ How to Run

python main.py <mode> <input_file> [output_file]

---

## Modes:
1 – Hexadecimal mode

2 – Decimal mode

3 – Octal mode

The <input_file> is required, and if [output_file] is not provided, the program will overwrite out.txt by default.

---

## 🏷️ Git Tags
Tag Name	Description
- v1.0	Initial version with decimal only
- v1.1	Added octal and hex support
- final	Final merged version of all features

Branches were merged to main before submission. All members made commits throughout development.

---

## 📎 Notes
No built-in parsing, regex, or third-party libraries were used.

All transitions and logic mirror our NFA designs.

Extra credit for floating point literals was not completed.
