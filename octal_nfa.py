from nfa import NFA


def create_octal_nfa():
    """
    Create an NFA that recognizes Python octal integer literals
    """
    # Define states
    states = {}

    # Define alphabet
    alphabet = set()

    # Define transitions
    transitions = {}

    # Define accepting states
    accepting_states = set()

    # Create and return the NFA
    return NFA(states, alphabet, transitions, "octal_q0", accepting_states)
