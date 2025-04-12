from nfa import NFA
from decimal_nfa import create_decimal_nfa
from octal_nfa import create_octal_nfa
from hex_nfa import create_hex_nfa
from float_nfa import create_float_nfa


def create_combined_nfa():
    """
    Create a combined NFA that recognizes all Python integer literals
    """
    # Get individual NFAs
    dec_nfa = create_decimal_nfa()
    oct_nfa = create_octal_nfa()
    hex_nfa = create_hex_nfa()
    float_nfa = create_float_nfa()

    # Create new combined NFA
    states = (
        {"start"}
        .union(dec_nfa.states)
        .union(oct_nfa.states)
        .union(hex_nfa.states)
        .union(float_nfa.states)
    )

    # Combined alphabet
    alphabet = (
        dec_nfa.alphabet.union(oct_nfa.alphabet)
        .union(hex_nfa.alphabet)
        .union(float_nfa.alphabet)
    )

    # Combined transitions
    transitions = {}

    # Add epsilon transitions from new start state to each NFA's start state
    transitions[("start", None)] = {
        dec_nfa.initial_state,
        oct_nfa.initial_state,
        hex_nfa.initial_state,
        float_nfa.initial_state,
    }

    # Add all transitions from individual NFAs
    for (state, symbol), next_states in dec_nfa.transitions.items():
        transitions[(state, symbol)] = next_states

    for (state, symbol), next_states in oct_nfa.transitions.items():
        transitions[(state, symbol)] = next_states

    for (state, symbol), next_states in hex_nfa.transitions.items():
        transitions[(state, symbol)] = next_states

    for (state, symbol), next_states in float_nfa.transitions.items():
        transitions[(state, symbol)] = next_states

    # Combined accepting states
    accepting_states = (
        dec_nfa.accepting_states.union(oct_nfa.accepting_states)
        .union(hex_nfa.accepting_states)
        .union(float_nfa.accepting_states)
    )

    # Create and return the combined NFA
    return NFA(states, alphabet, transitions, "start", accepting_states)
