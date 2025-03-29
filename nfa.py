class NFA:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def move(self, states, symbol):
        next_states = set()
        for state in states:
            if (state, symbol) in self.transitions:
                next_states.update(self.transitions[(state, symbol)])
        return next_states

    def epsilon_closure(self, states):
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
        current_states = self.epsilon_closure({self.initial_state})

        for symbol in input_string:
            if symbol not in self.alphabet:
                return False

            next_states = self.move(current_states, symbol)
            current_states = self.epsilon_closure(next_states)

            if not current_states:
                return False

        return any(state in self.accepting_states for state in current_states)
