from pyhop import *
import hanoi_domain
import sys
sys.setrecursionlimit(30000)

state = State('hanoi-state')
state.diskLocation = [1 for i in range(3)]

pyhop(state, [('move', 2, 1, 3, 2)], verbose=1)
