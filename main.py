"""
Python Integer Literals NFA Checker

This program implements a Non-deterministic Finite Automaton (NFA) that recognizes
Python integer literals (decimal, octal, and hexadecimal formats).

USAGE:
  python main.py [input_file] [output_file]

See README.md for detailed usage instructions and file formats.
"""

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
