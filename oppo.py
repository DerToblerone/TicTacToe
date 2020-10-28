import random
class Human:
    def __init__(self, c = 'O'):
        self.char = c
        pass
    def choose_move(self, state):
        while(True):
            try:
                x = int(input("x:"))
                y = int(input("y:"))
                k = x + y*3
                if state[k] == "_":
                    result = list(state)
                    result[k] = self.char
                    return "".join(result)
            except:
                pass

import random  
class RandomPolicy:
    def __init__(self, c = 'O'):
        self.char = c
        pass
    def choose_move(self,state):
        k = 0
        empty_spaces =[]
        #welche felder sind leer
        for c in state:
            if c == '_':
                empty_spaces.append(k)
            k += 1
        result = list(state)
        #wähle ein zufälliges feld
        result[random.choice(empty_spaces)] = self.char
        return "".join(result) #ausgabe als string nicht liste