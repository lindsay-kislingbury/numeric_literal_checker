from nfa import NFA


def create_decimal_nfa():
    """
    Create an NFA that recognizes Python decimal integer literals
    """
    # Define states
    states = {"dec_q0","dec_q1","dec_q2","dec_q3","dec_q4"}

    # Define alphabet
    alphabet = set("0123456789_")

    # Define transitions
    transitions = {}

    # starts with 0
    transitions[("dec_q0","0")] = {"dec_q1"} # if it starts with 0 
    transitions[("dec_q1","0")] = {"dec_q1"} # if more 0s!
    transitions[("dec_q1","_")] = {"dec_q2"} # if an _ is put in between
    transitions[("dec_q2","0")] = {"dec_q1"} # if 0, brings it back to accepting

    # does not start with 0
    for i in "123456789": # if it starts with a digit other than 0
        transitions[("dec_q0", i)] = {"dec_q3"}
    
    transitions[("dec_q3","_")] = {"dec_q4"} # if _

    for i in "0123456789": # if a digit is placed after _
        transitions[("dec_q3", i)] = {"dec_q3"}
        transitions[("dec_q4", i)] = {"dec_q3"}


    # Define accepting states
    accepting_states = {"dec_q1", "dec_q3"}

    # Create and return the NFA
    return NFA(states, alphabet, transitions, "dec_q0", accepting_states)
