from combined_nfa import create_combined_nfa


def process_test_file(input_file, output_file):
    """
    Process a test file and write results to output file
    """
    nfa = create_combined_nfa()

    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = line.split()
            if len(parts) >= 2:
                test_input = parts[0]
                expected = parts[1].lower() == "accept"

                result = nfa.accepts(test_input)

                status = "Pass" if result == expected else "Fail"
                fout.write(
                    f"Input: {test_input}, Expected: {'Accept' if expected else 'Reject'}, "
                    f"Got: {'Accept' if result else 'Reject'}, Status: {status}\n"
                )
