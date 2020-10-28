import random
import json

class Policy:
    def __init__(self, c ='X'):
        self.char = c
        self.table = {} 

    #gibt die erfolgswahrscheinlichkeit(value) eines zuges aus der tabelle zurück. siege haben value =1, niederlagen value = 0 und remi auch value = 0
    #der rest hat am anfang value = 0.5
    def get_probability(self, state):
        #state ist ein string *XO_OX___X" steht für
        #X O _
        #O X _
        #_ _ X
        #bei table handelt es sich um ein dictionary
        prob = 0.5
        try:
            prob = self.table[state]
        except:
            result = winner(state)
            if result == self.char:
                self.table[state]= 1
                prob = 1
                #sieg zählt als 1
            elif result == '.':
                self.table[state] = 0.25
                prob = 0.25
                #unentschieden 0.25
            elif result == '_':
                self.table[state] = 0.5
                prob = 0.5
                #nicht terminale züge werden mit 0.5 angelegt
            else:
                self.table[state] = 0
                prob = 0
                #verlust 0
            
        return prob
    
    #basierend auf dem vom gegner gespielten zug wird der neue state bewertet und diese bewertung fliesst nun in den vorherigen state ein
    def update(self, state_0,state_1, alpha = 0.1):
        new_val = self.get_probability(state_1)
        old_val = self.get_probability(state_0)

        #Qlearning 
        val = old_val + alpha*(new_val - old_val)

        self.table[state_0] = val

    def load_table(self,filename):
        try:
            with open(filename, 'r+b') as f:
                self.table = json.load(f)
            print("load successful")
        except:
            print("unable to load")
        
    def save_table(self,filename):
        try:
            with open(filename, 'w') as f:
                json.dump(self.table, f)
            print("save successful")
        except:
            print("unable to save")    

    def print_table(self):
        JSON = json.dumps(self.table, indent = 2)
        print(JSON)

    #es wird der erfolgsversprechendste zug ausgewählt (greedy algrithmus)
    def choose_move(self, state):
        i = 0
        i_list = []
        for c in state:
            if c == '_':
                i_list.append(i)
            i += 1

        p_list = []
        #p_list wird momentan noch nicht genutzt
        max_p = 0
        index = 0
        for k in i_list:
            tmp = list(state)
            tmp[k] = self.char
            new_state = "".join(tmp)
            prob = self.get_probability(new_state)
            p_list.append(prob)
            if prob >= max_p:
                max_p = prob
                index = k
            #index ist die nummer des feldes welches die höchset gewinnwahrschlkt hat
        
        result = list(state)
        result[index] = self.char
        return "".join(result)


    def exploration_move(self,state):
        i = 0
        i_list = []
        for c in state:
            if c == '_':
                i_list.append(i)
            i += 1

        k = random.randint(0, len(i_list)- 1)
        result = list(state)
        result[i_list[k]] = self.char
        return "".join(result)

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