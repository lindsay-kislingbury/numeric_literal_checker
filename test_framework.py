class NFATester:
    def __init__(self, nfa):
        """Initialize with an NFA instance"""
        self.nfa = nfa
        self.results = []

    def run_tests_from_file(self, input_file):
        """Run tests from a file and collect results"""
        test_cases = self._load_test_cases(input_file)
        for test_case in test_cases:
            self._run_test(test_case)
        return self.results

    def _load_test_cases(self, input_file):
        """Load test cases from a file"""
        test_cases = []
        with open(input_file, "r") as fin:
            for line in fin:
                line = line.rstrip(
                    "\n"
                )  # Keep any leading/trailing spaces but remove newline

                if not line:  # Skip empty lines
                    continue

                test_case = self._parse_test_case(line)
                if test_case:
                    test_cases.append(test_case)

        return test_cases

    def _parse_test_case(self, line):
        """Parse a test case from a line"""
        # Check for "accept" or "reject" at the end
        if line.endswith(" accept"):
            test_input = line[:-7]  # Remove " accept"
            expected = True
        elif line.endswith(" reject"):
            test_input = line[:-7]  # Remove " reject"
            expected = False
        # Check for just "accept" or "reject" (for empty string test)
        elif line == "accept":
            test_input = ""
            expected = True
        elif line == "reject":
            test_input = ""
            expected = False
        # For all other formats, try standard parsing
        elif " " in line:
            # Split from right to find accept/reject
            parts = line.rsplit(" ", 1)
            if len(parts) == 2 and parts[1].lower() in ["accept", "reject"]:
                test_input = parts[0]
                expected = parts[1].lower() == "accept"
            else:
                return None  # Skip lines without clear accept/reject
        else:
            return None  # Skip lines without clear accept/reject

        return {"input": test_input, "expected": expected}

    def _run_test(self, test_case):
        """Run a single test case"""
        test_input = test_case["input"]
        expected = test_case["expected"]

        # Run the NFA on the input
        result = self.nfa.accepts(test_input)

        # Create result entry
        self.results.append(
            {
                "input": test_input,
                "actual": result,
                "expected": expected,
                "pass": (result == expected),
            }
        )

    def write_results_to_file(self, output_file):
        """Write results to a file with improved formatting"""
        with open(output_file, "w") as fout:
            # Calculate summary statistics
            total = len(self.results)
            passed = sum(1 for r in self.results if r.get("pass"))
            failed = total - passed

            # Write summary header
            if total > 0:
                fout.write(f"TEST SUMMARY\n")
                fout.write(f"============\n")
                fout.write(f"Total tests: {total}\n")
                fout.write(f"Tests passed: {passed}\n")
                if failed > 0:
                    fout.write(f"Tests failed: {failed}\n")
                fout.write("\n")

            # Write detailed results
            fout.write(f"DETAILED RESULTS\n")
            fout.write(f"================\n\n")

            for i, result in enumerate(self.results):
                # Handle empty string display
                display_input = (
                    "'" + result["input"] + "'" if result["input"] != "" else "''"
                )

                fout.write(f"Test #{i+1}: {display_input}\n")
                fout.write(
                    f"  Expected: {'Accept' if result['expected'] else 'Reject'}\n"
                )
                fout.write(f"  Got: {'Accept' if result['actual'] else 'Reject'}\n")
                fout.write(f"  Status: {'PASS' if result['pass'] else 'FAIL'}\n")
                fout.write("\n")
