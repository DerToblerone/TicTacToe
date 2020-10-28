import random
import json
import win

class Policy:
    def __init__(self):
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
            if result == 'X':
                self.table[state]= 1
                prob = 1
                #sieg zählt als 1
            elif result == 'O':
                self.table[state] = 0
                prob = 0
                #verlust 0
            elif result == '.':
                self.table[state] = 0.25
                prob = 0.25
                #verlust 0
            else:
                self.table[state] = 0.5
                prob = 0.5
                #alle anderen züge inklusive unentschieden werden als 0.6 angelegt
            
        return prob
    
    #basierend auf dem vom gegner gespielten zug wird der neue state bewertet und diese bewertung fliesst nun in den vorherigen state ein
    def update(self, state_0,state_1, alpha = 0.1):
        new_val = self.get_probability(state_1)
        old_val = self.get_probability(state_0)

        #Qlearning 
        val = old_val + alpha*(new_val - old_val)

        self.table[state_0] = val

    def load_table(self):
        try:
            with open('./table.json', 'r+b') as f:
                self.table = json.load(f)
                JSON = json.dumps(self.table, indent = 2)
                print(JSON)
            print("load successful")
        except:
            print("unable to load table.json")
        
    def save_table(self):
        with open('./table.json', 'w') as f:
            JSON = json.dumps(self.table, indent = 2)
            print(JSON)
            json.dump(self.table, f)
            print("done writing")

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
            tmp[k] = 'X'
            new_state = "".join(tmp)
            prob = self.get_probability(new_state)
            p_list.append(prob)
            if prob >= max_p:
                max_p = prob
                index = k
            #index ist die nummer des feldes welches die höchset gewinnwahrschlkt hat
        
        result = list(state)
        result[index] = 'X'
        return "".join(result)


    def exploration_move(self,state):
        print("exploration move")
        i = 0
        i_list = []
        for c in state:
            if c == '_':
                i_list.append(i)
            i += 1

        k = random.randint(0, len(i_list)- 1)
        result = list(state)
        result[i_list[k]] = 'X'
        return "".join(result)
