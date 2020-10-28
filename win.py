def winner(state):
    #alle fälle des gewinnens werden einfach durchgeganen ^^
    if state[4] != '_':#mittleres feld
        if (state[3] == state[4]) & (state[4] == state[5]):
            return state[4]
        elif (state[2] == state[4]) & (state[4] == state[6]):
            return state[4]
        elif (state[1] == state[4]) & (state[4] == state[7]):
            return state[4]
        elif (state[0] == state[4]) & (state[4] == state[8]):
            return state[4]
    if state[0] != '_':#oberes linke feld
        if (state[0] == state[1]) & (state[1] == state[2]):
            return state[0]
        elif (state[0] == state[3]) & (state[3] == state[6]):
            return state[0]
    if state[8] != '_':#rechtes unteres feld
        if (state[6] == state[7]) & (state[7] == state[8]):
            return state[8]
        elif (state[2] == state[5]) & (state[5] == state[8]):
            return state[8]
    #ist das spiel fertig? 
    for c in state:
        if c == '_':
            return c
    #wenn untentschieden, return '.'
    return '.'