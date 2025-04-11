from nfa import NFA


def create_float_nfa():
    """
    Create an NFA that recognizes Python float literals
    """
    # Define states
    states = {"dec_q0","dec_q1","dec_q2a","dec_q2b","dec_q3","dec_q4","dec_q5","dec_q6","dec_q7","dec_q8","dec_q9"}

    # Define alphabet
    alphabet = set("0123456789_.+-e")

    # Define transitions
    transitions = {}

    transitions[("dec_q0", ".")] = {"dec_q2b"}              #q0 -> q2b

    for i in "0123456789":                                  # for any transitions with 0-9
        transitions[("dec_q0", i)] = {"dec_q1"}             #q0 -> q1
        transitions[("dec_q1", i)] = {"dec_q1"}             #q1 -> q1
        transitions[("dec_q2a", i)] = {"dec_q3"}            #q2a -> q3
        transitions[("dec_q2b", i)] = {"dec_q3"}            #q2a -> q3
        transitions[("dec_q3", i)] = {"dec_q3"}             #q3 -> q23
        transitions[("dec_q4", i)] = {"dec_q6"}             #q4 -> q5
        transitions[("dec_q5", i)] = {"dec_q6"}             #q5 -> q6
        transitions[("dec_q6", i)] = {"dec_q6"}             #q6 -> q6
        transitions[("dec_q7", i)] = {"dec_q1"}             #q7 -> q1
        transitions[("dec_q8", i)] = {"dec_q3"}             #q8 -> q3
        transitions[("dec_q9", i)] = {"dec_q6"}             #q9 -> q6

    transitions[("dec_q1", "_")] = {"dec_q7"}               #q1 -> q7
    transitions[("dec_q1", "e")] = {"dec_q4"}               #q1 -> q4
    transitions[("dec_q1", "E")] = {"dec_q4"}               #q1 -> q4
    transitions[("dec_q1", ".")] = {"dec_q2a"}              #q1 -> q2a

    transitions[("dec_q2a", "e")] = {"dec_q4"}              #q1 -> q2a
    transitions[("dec_q2a", "E")] = {"dec_q4"}              #q1 -> q2a

    transitions[("dec_q3", "_")] = {"dec_q8"}               #q3 -> q8

    transitions[("dec_q4", "+")] = {"dec_q5"}               #q4 -> q5
    transitions[("dec_q4", "-")] = {"dec_q5"}               #q4 -> q5

    transitions[("dec_q6", "_")] = {"dec_q9"}               #q6 -> q9

    # Define accepting states
    accepting_states = {"dec_q2a", "dec_q3", "dec_q6"}

    # Create and return the NFA
    return NFA(states, alphabet, transitions, "dec_q0", accepting_states)
