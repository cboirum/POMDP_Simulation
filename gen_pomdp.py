import sys

values = ['reward']
dim = 10
num_states = dim * dim + 1
l1x = 3
l1y = 3
obs = ['nothing', 'l1b', 'l1s', 'goal', 'l1b_r1_r2']
start = 8
goal = dim * (dim - 1) + 4
blur_threshold = 2
sharp_threshold = 1

def writeArray(f, arr):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            f.write(str(arr[x][y]))
            if y < len(arr[0]) - 1:
                f.write(' ')
        f.write('\n')
    f.write('\n')

def main():
    f = open('out.pomdp', 'w')

    # header
    f.write('discount: 0.9\n')
    f.write('values: ')
    for value in values:
        f.write(value)
    f.write('\n')
    f.write('states: %d\n' % num_states)
    f.write('actions: n s e w announce\n')
    f.write('observations: ')
    for observation in obs:
        f.write(observation + ' ')
    f.write('\n\n')

    # starting belief state
    f.write('start:\n')
    for state in range(num_states):
        if state == start:
            f.write('1.0 ')
        else:
            f.write('0.0 ')
        if state % dim == dim-1:
            f.write('\n')
    f.write('\n\n')

    # transitions
    transitions_n = [[0.0 for x in range(num_states)] for x in range(num_states)]
    transitions_s = [[0.0 for x in range(num_states)] for x in range(num_states)]
    transitions_e = [[0.0 for x in range(num_states)] for x in range(num_states)]
    transitions_w = [[0.0 for x in range(num_states)] for x in range(num_states)]

    drift = 0.1
    for x in range(dim):
        for y in range(dim):
            curr = x * dim + y

            # north
            if x == 0:
                transitions_n[curr][curr] = 1.0
            else:
                if y == 0:
                    transitions_n[curr][curr-dim] = 1-drift
                    transitions_n[curr][curr-dim+1] = drift
                elif y == dim-1:
                    transitions_n[curr][curr-dim] = 1-drift
                    transitions_n[curr][curr-dim-1] = drift
                else:
                    transitions_n[curr][curr-dim] = 1-2*drift
                    transitions_n[curr][curr-dim-1] = drift
                    transitions_n[curr][curr-dim+1] = drift

            # south
            if x == dim-1:
                transitions_s[curr][curr] = 1.0
            else:
                if y == 0:
                    transitions_s[curr][curr+dim] = 1-drift
                    transitions_s[curr][curr+dim+1] = drift
                elif y == dim-1:
                    transitions_s[curr][curr+dim] = 1-drift
                    transitions_s[curr][curr+dim-1] = drift
                else:
                    transitions_s[curr][curr+dim] = 1-2*drift
                    transitions_s[curr][curr+dim-1] = drift
                    transitions_s[curr][curr+dim+1] = drift

            # east
            if y == dim-1:
                transitions_e[curr][curr] = 1.0
            else:
                if x == 0:
                    transitions_e[curr][curr+1] = 1-drift
                    transitions_e[curr][curr+1+dim] = drift
                elif x == dim-1:
                    transitions_e[curr][curr+1] = 1-drift
                    transitions_e[curr][curr+1-dim] = drift
                else:
                    transitions_e[curr][curr+1] = 1-2*drift
                    transitions_e[curr][curr+1-dim] = drift
                    transitions_e[curr][curr+1+dim] = drift

            # west
            if y == 0:
                transitions_w[curr][curr] = 1.0
            else:
                if x == 0:
                    transitions_w[curr][curr-1] = 1-drift
                    transitions_w[curr][curr-1+dim] = drift
                elif x == dim-1:
                    transitions_w[curr][curr-1] = 1-drift
                    transitions_w[curr][curr-1-dim] = drift
                else:
                    transitions_w[curr][curr-1] = 1-2*drift
                    transitions_w[curr][curr-1-dim] = drift
                    transitions_w[curr][curr-1+dim] = drift

    transitions_n[dim*dim][dim*dim] = 1.0
    transitions_s[dim*dim][dim*dim] = 1.0
    transitions_e[dim*dim][dim*dim] = 1.0
    transitions_w[dim*dim][dim*dim] = 1.0

    f.write('T: n\n')
    writeArray(f, transitions_n)
    f.write('T: s\n')
    writeArray(f, transitions_s)
    f.write('T: e\n')
    writeArray(f, transitions_e)
    f.write('T: w\n')
    writeArray(f, transitions_w)

    f.write('T: announce : * : %d 1.0\n\n' % (dim*dim))

    # observation function
    f.write('O: *\n#')
    for observation in obs:
        f.write(observation + ' ')
    f.write('\n')

    observations = [[0.0 for x in range(len(obs))] for x in range(num_states)]
    for state in range(num_states):
        x = state / dim
        y = state % dim
        if x == l1x and y == l1y:
            observations[state][obs.index('l1s')] = 1.0
        elif abs(x-l1x) <= blur_threshold and abs(y-l1y) <= blur_threshold:
            observations[state][obs.index('l1b')] = 1.0-8.0/(dim*dim)
            observations[state][obs.index('l1b_r1_r2')] = 8.0/(dim*dim)
        elif state == goal:
            observations[state][obs.index('goal')] = 1.0
        else:
            observations[state][obs.index('nothing')] = 1.0

    writeArray(f, observations)

    # reward function
    f.write('# R: <action> : <start-state> : <end-state> : <observation> %f\n')
    f.write('R: * : * : * : l1b 5\n')
    f.write('R: * : * : * : l1s 10\n')
    f.write('R: * : * : * : l1b_r1_r2 7\n')
    f.write('R: announce : * : * : * -2000\n')
    f.write('R: announce : %d : * : * 200\n' % goal)
    f.write('R: n : * : * : * -1\n')
    f.write('R: e : * : * : * -1\n')
    f.write('R: s : * : * : * -1\n')
    f.write('R: w : * : * : * -1\n')


if __name__ == "__main__":
    main()
