class NFA:
    """A class representing a Non-deterministic Finite Automaton (NFA).

    An NFA contains states, an alphabet, transitions between states,
    an initial state, and accepting states. It can determine whether
    a given input string is accepted by the NFA.

    Attributes:
        states (set): Set of all states in the NFA.
        alphabet (set): Set of all symbols in the NFA's alphabet.
        transitions (dict): Dictionary mapping (state, symbol) pairs to sets of next states.
        initial_state: The starting state of the NFA.
        accepting_states (set): Set of all accepting states.
    """

    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        """Initialize an NFA with the specified components.

        Args:
            states (set): Set of all states in the NFA.
            alphabet (set): Set of all symbols in the NFA's alphabet.
            transitions (dict): Dictionary mapping (state, symbol) pairs to sets of next states.
            initial_state: The starting state of the NFA.
            accepting_states (set): Set of all accepting states.
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def move(self, states, symbol):
        """Compute the set of states reachable from the given states on the given symbol.

        Args:
            states (set): A set of states to move from.
            symbol: The symbol to move on.

        Returns:
            set: The set of states reachable from the given states on the given symbol.
        """
        next_states = set()
        for state in states:
            if (state, symbol) in self.transitions:
                next_states.update(self.transitions[(state, symbol)])
        return next_states

    def epsilon_closure(self, states):
        """Compute the epsilon closure of the given set of states.

        The epsilon closure of a set of states is the set of states reachable
        from the given states by following epsilon transitions (represented by None).

        Args:
            states (set): A set of states to compute the epsilon closure for.

        Returns:
            set: The epsilon closure of the given states.
        """
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            if (state, None) in self.transitions:
                for next_state in self.transitions[(state, None)]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)

        return closure

    def accepts(self, input_string):
        """Determine whether the given input string is accepted by this NFA.

        Args:
            input_string (str): The input string to check for acceptance.

        Returns:
            bool: True if the input string is accepted, False otherwise.
        """
        current_states = self.epsilon_closure({self.initial_state})

        for symbol in input_string:
            if symbol not in self.alphabet:
                return False

            next_states = self.move(current_states, symbol)
            current_states = self.epsilon_closure(next_states)

            if not current_states:
                return False

        return any(state in self.accepting_states for state in current_states)
