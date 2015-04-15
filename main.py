""" POMDP Simulation for 2 rovers
"""

#Simulation Definition

class simParams(object):
    iter_limit = 5
    states = []
    reward = []
    start1 = ()
    start2 = ()
    goal = ()
    state1 = ()
    state2 = ()   
    def __init__(self):
        pass

class roverObject(object):
    belief = []
    world = []
    
    def __init__(self):
        pass
    
    def do_action(self,action):
        pass
    
    def observe(self):
        pass
    
    def announce(self):
        pass        
    
class worldObject(object):
    state = []
    agents = []
    
    def __init__(self, parameters):
        pass
    
    def step(self):
        """ Runs simulation step
        """
        pass
    
    def add_rover(self, rover):
        self.agents.append(rover)
        rover.world = self
        
    def step(self):
        print(len(self.agents))
        
def run():
    params = simParams()
    moon = worldObject(params)
    fred = roverObject()
    moon.add_rover(fred)
    unfinished = True
    i = 1
    while unfinished and i < params.iter_limit:
        moon.step()
        i+=1
    print('Done')

if __name__=="__main__":
    run()