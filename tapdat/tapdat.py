#!/usr/bin/env python
import json

state = (
    "11101110" "00010000" "11100110" "01110000" "01111100"
    "11011010" "00010000" "01111000" "00111100" "01111110"
    "01111100" "01110000" "10111100" "00010000" "11011010"
    "11101100" "01100000" "11100010" "11110000" "00010000"
    "11101110" "01111010" "11101110" "01100000" "01101111"
)

def xnor(v1, v2):
    if v1 == v2:
        return "1"
    else:
        return "0"

def chunks(state):
        return ["".join(a) for a in zip(*[iter(state)]*8)]

def cycle():
    global state
    g1 = xnor(state[-1] , state[-3])
    g2 = xnor(state[-4], state[-6])
    g = xnor(g1, g2)
    state = g + state[:-1]


states = []
for i in range(100000000):
    c = chunks(state)
    states.append(c)
    cycle()

with open("f.out", "w") as f:
    f.write( json.dumps(states) )
