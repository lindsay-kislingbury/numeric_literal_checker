# Simple NFA Tester
# Usage:
#   FILE MODE
#   python nfa.py [type] [input_file] [output_file]
#   or
#   MANUAL MODE
#   python nfa.py [type]
#
#   if you use an input file, it'll run in file mode
#   if you use an input file but no output file, it'll overwrite out.txt (totally fine!)
#   if you don't use an input file, it'll run in manual mode (enter inputs manually)
#
# Where:
#   [type] - NFA type: 1=hex, 2=dec, 3=oct
#   [input_file] - JFLAP format test file ex: 23_4 accept
#   [output_file] - Output results file ( will be created if it doesn't exist )
#
# Examples:
#   python octal_nfa.py 1 octal_tests.txt octal_output.txt  // octal nfa file mode test
#   python decimal_nfa.py 2 // decimal nfa manual mode test

import sys

# Import NFA modules
try:
    from hex_nfa import create_hex_nfa

except ImportError:
    create_hex_nfa = None

try:
    from decimal_nfa import create_decimal_nfa
except ImportError:
    create_dec_nfa = None

try:
    from octal_nfa import create_octal_nfa
except ImportError:
    create_oct_nfa = None


# Create NFA based on type
def get_nfa(nfa_type):
    if nfa_type == 1 and create_hex_nfa:
        return create_hex_nfa()
    elif nfa_type == 2 and create_dec_nfa:
        return create_dec_nfa()
    elif nfa_type == 3 and create_oct_nfa:
        return create_oct_nfa()
    return None


# Main function
if __name__ == "__main__":
    # Parse arguments
    if len(sys.argv) < 2:
        sys.exit(1)

    # Get NFA type (1=hex, 2=dec, 3=oct)
    nfa_type = int(sys.argv[1])
    nfa = get_nfa(nfa_type)
    if not nfa:
        sys.exit(1)

    # File testing mode
    if len(sys.argv) == 4:
        input_file = sys.argv[2]
        output_file = sys.argv[3]

        with open(input_file, "r") as fin, open(output_file, "w") as fout:
            for line in fin:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                parts = line.split()
                if len(parts) >= 2:
                    test_input = parts[0]
                    expected = "accept" in " ".join(parts[1:]).lower()

                    result = nfa.accepts(test_input)
                    status = "Pass" if result == expected else "Fail"

                    fout.write(
                        f"Input: {test_input}, Expected: {'Accept' if expected else 'Reject'}, "
                        f"Got: {'Accept' if result else 'Reject'}, Status: {status}\n"
                    )

    # Interactive mode
    else:
        try:
            while True:
                user_input = input("> ")
                result = nfa.accepts(user_input)
                print(f"{'Accept' if result else 'Reject'}")
        except KeyboardInterrupt:
            pass
