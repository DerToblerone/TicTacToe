import os
import sys
import random
sys.path.append('.')
from pol import Policy
from oppo import Human, RandomPolicy
from win import winner

def display_state(state):
    
    os.system('cls||clear')
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])


#play against any opponent without learning
def play(generations, agent, opponent, prnt = False):
    for g in range(generations):
        state = "_________" #empty field
        new_state = state
        while(True):
            if prnt: display_state(new_state)
            if winner(new_state) != '_':
                input()
                break
            new_state = agent.choose_move(new_state)
            if prnt: display_state(new_state)
            if winner(new_state) != '_':
                input()
                break
            state = new_state
            new_state = opponent.choose_move(state)
            

#play against any opponent with learning
def play_train(generations, agent, opponent, prnt = False, xplre = 0.05):
    for g in range(generations):
        state = "_________" #empty field
        new_state = state
        while(True):
            if random.random() < xplre:
                new_state = agent.exploration_move(new_state)
            else:
                new_state = agent.choose_move(new_state)
                agent.update(state, new_state)
            if prnt: display_state(new_state)
            if winner(new_state) != '_':
                break
            state = new_state
            new_state = opponent.choose_move(state)
            if prnt: display_state(new_state)
            if winner(new_state) != '_':
                agent.update(state,new_state)
                break

#play against self
def play_self(generations, agent, opponent, prnt = False, xplre = 0.05, init_xpl = 1, learn_factor = 0.1, l_scale = True, xpl_scale = True):
    l_rate = learn_factor
    gen_factor = 1

    for g in range(generations):
        state = "_________" #empty field
        new_state = state#aktueller zug
        opp_state = "notastate"#letzter zug des gegners


        if xpl_scale:
            gen_factor = ((generations - g)*1.0/generations)#wahrschl. für random züge nimmt ab mit der zeit

        xpl = init_xpl*gen_factor #erster zug hat eine höhere wahrschl. ein erkundungszug zu sein


        if l_scale:
            l_rate = learn_factor*gen_factor#die lernrate kann auch mit der zeit reuduziert werden
        while(True):
            if random.random() < xpl:#erkundungszug
                new_state = agent.exploration_move(new_state)
            else:#lernzug bzw zug mit höchster bewertung
                new_state = agent.choose_move(new_state)
                agent.update(state, new_state, alpha = l_rate)
            if prnt: display_state(new_state)
            if winner(new_state) != '_':#bei sieg des agenten lernt der gegner auch dazu
                opponent.update(opp_state, new_state, alpha = l_rate)
                break
            state = new_state
            if random.random() < xplre:
                new_state = opponent.exploration_move(state)
            else:
                new_state = opponent.choose_move(state)
                opponent.update(opp_state, new_state, alpha = l_rate)
                opp_state = new_state
            if prnt: display_state(new_state)
            if winner(new_state) != '_':
                agent.update(state,new_state, alpha = l_rate)
                break
            if xpl != xplre:
                xpl = xplre*gen_factor
        print("game {0}/{1}".format(g+1, generations), end ="\r")
            



ag = Policy()
op = Policy(c = 'O')
rng = RandomPolicy()
pl = Human()

gen = 10000
ag.load_table("./table_X.json")
op.load_table("./table_O.json")

if int(input("train? 0/1")) == 1:
    gen = int(input("how many games?"))
    play_self(gen, ag, op, xplre=0.3, l_scale=False, learn_factor=0.05)
    ag.save_table("./table_X.json")
    op.save_table("./table_O.json")
    input()

if int(input("print value vector of empty field? 0/1")) == 1:
    state = "_________"
    p_list = []
    for k in range(len(state)):
        tmp = list(state)
        tmp[k] = 'X'
        new_state = "".join(tmp)
        prob = ag.get_probability(new_state)
        p_list.append(prob)
    print(p_list)
    input()

print("\n")
while(True):
    if int(input("play? 0/1")) == 1:
        pl.char = 'O'
        play(1, ag, pl, prnt = True)
        pl.char = 'X'
        play(1, pl, op, prnt = True)
    else:
        break
if int(input("print? 0/1")) == 1:
    ag.print_table()
    op.print_table()
    input()

