import math
import matplotlib.pyplot as plt
import numpy as np
# initialize the conditions

nodes = True

support_list=[]
load_dict = {}

#total_length = int(input("Enter total length of beam: "))
total_length = 10

while nodes:
    ch = input("Do you want to add a node?: (Y/N)")
    if ch.casefold() == 'n':
        nodes = False
        continue
    else:
        node_type = input("What time of Node do you want to add? (Support/Load) ")

        if node_type.casefold() == 'support':
            x = int(input("Enter distance from origin: "))
            support_list.append([x,0])
            

        elif node_type.casefold() == 'load':
            x = int(input("Enter distance from origin: "))
            f = int(input("Enter force with direction: "))

            load_dict[x] = f

"""
dummy values to test
load_dict ={5:-100}
support_list =[[0,0],[10,0]]
"""
def reaction_support():
    load_moment = 0
    for load_distance in load_dict:
        load_moment += (load_distance - support_list[1][0])*load_dict.get(load_distance)

    support_list[0][1] =  -load_moment/(support_list[0][0]-support_list[1][0])

    support_list[1][1] = -sum(load_dict.values())-support_list[0][1]
    return None


reaction_support()
#print(support_list)
nodes = [support for support in support_list]
nodes += list(load_dict.items())
nodes.sort(key = lambda x: x[0])
print(nodes)
  

l = np.linspace(0,total_length+1,10)
sheers = []
bending_moment =[]


def sheer_calculations(nodes):
    n = int(total_length/0.01)#0.1
    sheers = [0 for _ in range(0,n)]
    for dist,force in nodes:
        #print(f'{dist}:{force}')
        x = int(dist/0.01)#0.1
        if x==0:
            sheers[0] = force
        else:
            sheers[x-1] = force
    #print(sheers)
    final_sheer = [0 for _ in range(len(sheers))]
    for i in range(0,len(sheers)):
        final_sheer[i] = sum(sheers[0:i+1])
    #print(final_sheer)
    return final_sheer

y_axis = sheer_calculations(nodes)
x_axis = [i*0.01 for i in range(1000)]
    

plt.plot(x_axis,y_axis)
plt.plot(x_axis,[0 for _ in range(len(x_axis))])
plt.show()
