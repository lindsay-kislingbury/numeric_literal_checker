# Python Integer Literals NFA Checker
# ================================
#
# This program implements a Non-deterministic Finite Automaton (NFA) that recognizes
# all Python integer literals according to the Python language specification:
#   - Decimal literals (e.g., 0, 123, 100_000)
#   - Octal literals (e.g., 0o777, 0O123)
#   - Hexadecimal literals (e.g., 0xff, 0XAB)
#
# USAGE:
#   python main.py [input_file] [output_file]
#   or
#   python main.py [input_file]  (uses default out.txt)
#
# INPUT FILE FORMAT:
#   Each line should have a test case followed by "accept" or "reject", such as:
#   123 accept
#   0xff accept
#   0o777 accept
#   01 reject
#
#   The empty string can be tested with just "accept" or "reject" on a line.
#   Lines starting with # will be processed as test cases, not comments.
#   Empty lines are skipped.
#
# OUTPUT:
#   The program produces a formatted report showing:
#   - A summary of tests run, passed, and failed
#   - Detailed results for each test case
#
# EXAMPLES:
#   python main.py in_ans.txt results.txt
#   python main.py grader_tests.txt

import sys
from combined_nfa import create_combined_nfa
from test_framework import NFATester

# Main function
if __name__ == "__main__":
    # Ensure input file is provided
    if len(sys.argv) < 2:
        print("Usage: python main.py [input_file] [output_file]")
        print("If output_file is not provided, writes to out.txt")
        sys.exit(1)

    # Get input and output files
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "out.txt"

    # Create combined NFA
    nfa = create_combined_nfa()

    # Run tests
    tester = NFATester(nfa)
    tester.run_tests_from_file(input_file)
    tester.write_results_to_file(output_file)

    print(f"Test results written to {output_file}")
