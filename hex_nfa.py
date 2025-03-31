from nfa import NFA


def create_hex_nfa():
    """
    Create an NFA that recognizes Python hexadecimal integer literals
    """
    # Define states
    states = {"hex_q0", "hex_q1", "hex_q2", "hex_q3", "hex_q4"}

    # Define alphabet
    alphabet = set("0123456789abcdefABCDEFxX_")

    # Define transitions
    transitions = {}

    # Hex NFA transitions
    transitions[("hex_q0", "0")] = {"hex_q1"}
    transitions[("hex_q1", "x")] = {"hex_q2"}
    transitions[("hex_q1", "X")] = {"hex_q2"}

    # Hex digits from hex_q2 to hex_q3
    for digit in "0123456789abcdefABCDEF":
        transitions[("hex_q2", digit)] = {"hex_q3"}

    # Hex digits self-loop on hex_q3
    for digit in "0123456789abcdefABCDEF":
        transitions[("hex_q3", digit)] = {"hex_q3"}

    # Underscore and epsilon from hex_q3 to hex_q4
    transitions[("hex_q3", "_")] = {"hex_q4"}
    transitions[("hex_q3", None)] = {"hex_q4"}  # epsilon transition

    # Hex digits from hex_q4 back to hex_q3
    for digit in "0123456789abcdefABCDEF":
        transitions[("hex_q4", digit)] = {"hex_q3"}

    # Define accepting states
    accepting_states = {"hex_q3"}

    # Create and return the NFA
    return NFA(states, alphabet, transitions, "hex_q0", accepting_states)
