""" POMDP Simulation for 2 rovers
"""

#Simulation Definition
simParams = {'iter_limit':5, #Limit on number of simulation steps or iterations
              'height': 10, #Size of simulation world (Height, Width)
              'width' : 10,
              'landmarks' : [('Hill 1', 3,4),
                             ('Boulder', 4,1)],
              'states' : [],
              'reward' : [],
              'start1' : (0,3),
              'start2' : (),
              'goal' : (),
              'state1' : (),
              'state2' : ()   }

class roverObject(object):
    belief = []
    world = []
    orientation = 1
    
    def __init__(self,name):
        self.name = name
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
    
    def __init__(self, params):
        for name in params.keys():
            setattr(self,name,params[name])
        self.map = [[0 for x in range(self.width)] for x in range(self.height)]

        pass
    
    def add_rover(self, rover, position):
        """ Adds a rover to the X,Y location in the world """
        self.agents.append(rover)
        rover.world = self
        self.move(rover,position)
        rover.belief = a = [[0 for x in range(self.width)] for x in range(self.height)]
        rover.belief[position[0]][position[1]] = 1
        #rover.belief[][]
        
    def step(self):
        """ Runs simulation step
        """
        print(len(self.agents)) #debug print
        
    def move(self,thing,pos):
        """ Utility function for updating all maps to object's new position """
        if thing.name in self.map:
            self.map.remove(thing.name)
        self.map[pos[0]][pos[1]] = thing.name
        #print self.map
            
        
    def show_object_map(self):
        """ Cheap printout of world object locations"""
        #print(self.map)
        for row in self.map:
            print row
            
    def show_belief_map(self):
        """ Cheap printout of belief states for first rover"""
        for row in self.agents[0].belief:
            print row
def run():
    moon = worldObject(simParams)
    fred = roverObject('R1')
    moon.add_rover(fred, moon.start1)
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