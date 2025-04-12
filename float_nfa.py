from nfa import NFA


def create_float_nfa():
    """
    Create an NFA that recognizes Python float literals
    """
    # Define states
    states = {
        "float_q0",
        "float_q1",
        "float_q2a",
        "float_q2b",
        "float_q3",
        "float_q4",
        "float_q5",
        "float_q6",
        "float_q7",
        "float_q8",
        "float_q9",
    }

    # Define alphabet
    alphabet = set("0123456789_.+-e")

    # Define transitions
    transitions = {}

    transitions[("float_q0", ".")] = {"float_q2b"}  # q0 -> q2b

    for i in "0123456789":  # for any transitions with 0-9
        transitions[("float_q0", i)] = {"float_q1"}  # q0 -> q1
        transitions[("float_q1", i)] = {"float_q1"}  # q1 -> q1
        transitions[("float_q2a", i)] = {"float_q3"}  # q2a -> q3
        transitions[("float_q2b", i)] = {"float_q3"}  # q2a -> q3
        transitions[("float_q3", i)] = {"float_q3"}  # q3 -> q23
        transitions[("float_q4", i)] = {"float_q6"}  # q4 -> q5
        transitions[("float_q5", i)] = {"float_q6"}  # q5 -> q6
        transitions[("float_q6", i)] = {"float_q6"}  # q6 -> q6
        transitions[("float_q7", i)] = {"float_q1"}  # q7 -> q1
        transitions[("float_q8", i)] = {"float_q3"}  # q8 -> q3
        transitions[("float_q9", i)] = {"float_q6"}  # q9 -> q6

    transitions[("float_q1", "_")] = {"float_q7"}  # q1 -> q7
    transitions[("float_q1", "e")] = {"float_q4"}  # q1 -> q4
    transitions[("float_q1", "E")] = {"float_q4"}  # q1 -> q4
    transitions[("float_q1", ".")] = {"float_q2a"}  # q1 -> q2a

    transitions[("float_q2a", "e")] = {"float_q4"}  # q1 -> q2a
    transitions[("float_q2a", "E")] = {"float_q4"}  # q1 -> q2a
    transitions[("float_q3", "e")] = {"float_q4"}  # q3 -> q4
    transitions[("float_q3", "E")] = {"float_q4"}  # q3 -> q4

    transitions[("float_q3", "_")] = {"float_q8"}  # q3 -> q8

    transitions[("float_q4", "+")] = {"float_q5"}  # q4 -> q5
    transitions[("float_q4", "-")] = {"float_q5"}  # q4 -> q5

    transitions[("float_q6", "_")] = {"float_q9"}  # q6 -> q9

    # Define accepting states
    accepting_states = {"float_q2a", "float_q3", "float_q6"}

    # Create and return the NFA
    return NFA(states, alphabet, transitions, "float_q0", accepting_states)
