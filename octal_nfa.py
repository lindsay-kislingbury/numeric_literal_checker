from nfa import NFA


def create_octal_nfa():
    """
    Create an NFA that recognizes Python octal integer literals
    """
    # Define states
    states = {"octal_q0", "octal_q1", "octal_q2", "octal_q3", "octal_q4"}

    # Define alphabet
    alphabet = set("01234567oO_")

    # Define transitions
    transitions = {}
    
    # Start with '0'
    transitions[("octal_q0", "0")] = {"octal_q1"}

    # 'o' or 'O' transitions from q1 to q2
    transitions[("octal_q1", "o")] = {"octal_q2"}
    transitions[("octal_q1", "O")] = {"octal_q2"}

    # Octal digits (0-7) from q2 to q3
    for digit in "01234567":
        transitions[("octal_q2", digit)] = {"octal_q3"}

    # Octal digits (0-7) Self-loop on q3 
    for digit in "01234567":
        transitions[("octal_q3", digit)] = {"octal_q3"}

    # Underscore and epsilon (lambda) transition from q3 to q4
    transitions[("octal_q3", "_")] = {"octal_q4"}
    transitions[("octal_q3", None)] = {"octal_q4"}  # epsilon transition

    # Octal digits from q4 back to q3
    for digit in "01234567":
        transitions[("octal_q4", digit)] = {"octal_q3"}

    # Define accepting states
    accepting_states = set("octal_q3")

    # Create and return the NFA
    return NFA(states, alphabet, transitions, "octal_q0", accepting_states)
