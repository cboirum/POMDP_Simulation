""" POMDP Simulation for 2 rovers
"""
import random

#Simulation Definition
simParams = {'iter_limit':10, #Limit on number of simulation steps or iterations
              'height': 9, #Size of simulation world (Height, Width)
              'width' : 9,
              'landmarks' : [('Hill 1', 3,4),
                             ('Boulder', 4,1)],
              'states' : [],
              'reward' : [],
              'start1' : (0,4,1), #Initial pose (X, Y, orientation) oreintation = 0,1,2,3=N,E,S,W
              'start2' : (),
              'goal' : (),
              'state1' : (),
              'state2' : (),
              'action_que1' : ['F','F','F','F','F','F','F','F','F'], #Forced initial actions
              'ordinals' : {'0':'N',
                            '1':'E',
                            '2':'S',
                            '3':'W'},
              'moves': {'0': (0,1),
                        '1': (1,0),
                        '2': (0,-1),
                        '3': (-1,0)}, #definition of directional effects to forward movement
              'transProb': {'F': 0.5, #encoding of transition probabilities on [0-1]
                            'deviateL': 0.5, #probability of deviating left instead of right, if deviation occurs
                            }
              }

def probChoice(op1,op2,prob1):
    """ Chooses "op1" or "op2" based on probability (0-1) of "op1" """
    if prob1 == 1:
        return op1
    elif prob1 == 0:
        return op2
    else:
        num = random.random()
        if num <= prob1:
            return op1
        else: 
            return op2

def probTest(op1,op2,prob1,numTimes):
    """ Test random probability function """
    numOpt1 = 0
    numOpt2 = 0
    for i in range(numTimes):
        if probChoice(op1,op2,prob1) == op1:
            numOpt1+=1
        else:
            numOpt2+=1
    print("Probability: %f"%prob1)
    print("Opt1: %d/%d"%(numOpt1,numTimes))
    print("Opt2: %d/%d"%(numOpt2,numTimes))

class POMDP():
    """ Data structures for Partially Observable Markhov Descision Process """
    world = ''
    
    def __init__(self):
        pass
    
    def transitionFnct(self,s,b,a):
        """ Transitions from state "s" to state "s2" using action "a".
        This function will also perform belief propagation if a belief matrix is supplied
        
        Args:
            s        True state of agent
            b        Belief matrix of agent
            a        action agent has taken
            
        Returns:
            s2         new actual state as result of a
            b_local    list of locations that have just had their beliefs changed by this action (X,Y,prob)
            """
            
        X1,Y1,Or1 = s
        Or2 = Or1
        b_local = []
        if a == 'F':
            #Find Proposed new location
            dx,dy = self.world.moves[str(Or1)]
            X2,Y2 = [X1+dx,Y1+dy]
            new_b = (X1,Y1,0)
            b_local.append(new_b)
            if a in self.world.transProb.keys():
                prob = self.world.transProb[a]
            else:
                prob = 1
            result = probChoice('forward','deviate',prob)
            if result == 'forward':
                X3,Y3 = X2,Y2
            elif result == 'deviate':
                prob2 = self.world.transProb['deviateL']
                drift = probChoice('left','right',prob2)
                ddy = 0
                ddx = 0
                if dx < 0: #W
                    if drift == 'left':
                        ddy = -1
                    else:
                        ddy = 1
                elif dx > 0: #E
                    if drift == 'left':
                        ddy = 1
                    else:
                        ddy = -1
                elif dy > 0: #N
                    if drift == 'left':
                        ddx = -1
                    else:
                        ddx = 1
                elif dy < 0: #S
                    if drift == 'left':
                        ddx = 1
                    else:
                        ddx = -1
                X3,Y3 = [X2+ddx, Y2+ddy]
            s2 = (X3,Y3,Or1)
        elif a == 'L':
            Or2 = Or1 - 1
            if Or2<0:
                Or2 = 3
            elif Or2>3:
                Or2 = 0
            s2 = (X1,Y1,Or2)
        elif a == 'R':
            Or2 = Or1 + 1
            if Or2<0:
                Or2 = 3
            elif Or2>3:
                Or2 = 0
            s2 = (X1,Y1,Or2)
        elif a == 'O': #Observation
            pass
        elif a == 'A': #Announce at goal
            pass
        Xn,Yn,Orn = s2
        if Xn > self.world.width-1:
            Xn = self.world.width-1
        if Xn < 0:
            Xn = 0
        if Yn > self.world.height-1:
            Yn = self.world.height-1
        if Yn < 0:
            Yn = 0
        if not self.world.map[Xn][Yn]==0: #If there is an obsticle in the way
            #TO DO - differentiate between obsticle/landmark/other rover and goal
            Xn,Yn = X1,Y1
        s2 = (Xn, Yn, Orn)
        
        return s2
    
    def beliefProp(self,b,a):
        """ Propagates belief after action "a" """
        #Find all locations where belief is nonzero
        
    
    def observe(self,s):
        """ Returns observation "E" from system in state "s" """
        pass
    
    def announce(self,):
        """ Announce agent is at the goal """
        pass

class roverObject(object):
    belief = []
    world = []
    orientation = 1
    s_p = [] #State estimate
    s = [] #True State
    b = [] #belief matrix
    action_que = []
    
    
    def __init__(self,name):
        self.name = name
        pass
    
    def do_action(self,action):
        self.s = self.world.POMDP.transitionFnct(self.s,self.b,action)
        pass
    
    def observe(self):
        pass
    
    def announce(self):
        pass     
    
    def update(self):
        """ Runs 1 iteration of POMDP action on rover """
        if len(self.action_que):
            action = self.action_que.pop()
            self.do_action(action)
        
    
class worldObject(object):
    state = []
    agents = []
    iter = 0
    
    def __init__(self, sim, params):
        self.POMDP = sim
        sim.world = self
        for name in params.keys():
            setattr(self,name,params[name])
        self.map = [[0 for x in range(self.width)] for x in range(self.height)]

        pass
    
    def add_rover(self, rover, state):
        """ Set rover's state and add it to the world """
        self.agents.append(rover)
        rover.world = self
        rover.s = state
        self.move_in_world(rover)
        rover.belief = a = [[0 for x in range(self.width)] for x in range(self.height)]
        rover.belief[state[0]][state[1]] = 1
        #rover.belief[][]
        
    def step(self):
        """ Runs simulation step
        """
        self.iter +=1
        for agent in self.agents:
            agent.update()
            self.move_in_world(agent)
        
        print(len(self.agents)) #debug print
        
    def move_in_world(self,thing):
        """ Utility function for updating all maps to object's new position """
        pose = thing.s[:2]
#        if thing.name in self.map:
#            self.map.remove(thing.name)
        ordinal = self.ordinals[str(thing.s[2])]
        tag = thing.name +'%s_%d'%(ordinal, self.iter)
        self.map[pose[0]][pose[1]] = tag
        
    """ Non data altering methods after this point.
        May include: visualization and debug
    """
            
    def show_object_map(self):
        """ Cheap printout of world object locations"""
        #print(self.map)
        for row in self.map:
            print row
        for agent in self.agents:
            print agent.s
            
    def show_belief_map(self):
        """ Cheap printout of belief states for first rover"""
        for row in self.agents[0].belief:
            print row
            
def printTmatrix():
    
    pass

            
def run():
    sim = POMDP()
    moon = worldObject(sim,simParams)
    fred = roverObject('R1')
    moon.add_rover(fred, simParams['start1'])
    fred.action_que = simParams['action_que1']
    unfinished = True
    i = 1
    while unfinished and i < simParams['iter_limit']:
        moon.step()
        i+=1
    print('Done')
    moon.show_object_map()
    print
    moon.show_belief_map()
    

if __name__=="__main__":
    run()
    #probTest(1,2,0.25,1000)