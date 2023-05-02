import sys

sys.stdin = open("input.txt", "rt")
def findParent(name):
    if network[name][0] == name:
        return name
    return findParent(network[name][0])    
T = int(sys.stdin.readline())
for _ in range(T):
    network = {}
    N = int(sys.stdin.readline())
    for i in range(N):
        name1, name2 = sys.stdin.readline().split()
        if network.get(name1, False) and network.get(name2, False):
            parent1 = findParent(name1)
            parent2 = findParent(name2)
            if parent1 == parent2:
                print(network[parent1][1])
            else:
                if network[parent1][1] < network[parent2][1]:
                    network[parent1][0] = parent2
                    network[parent2][1] += network[parent1][1]
                    print(network[parent2][1])
                else: 
                    network[parent2][0] = parent1
                    network[parent1][1] += network[parent2][1]
                    print(network[parent1][1])
        elif network.get(name1, False):
            parent = findParent(name1)
            network[name2] = [parent, 1]
            network[parent][1] += 1
            print(network[parent][1])
        elif network.get(name2, False):
            parent = findParent(name2)
            network[name1] = [parent, 1]
            network[parent][1] += 1
            print(network[parent][1]) 
        else:
            network[name1] = [name1, 2]
            network[name2] = [name1, 1]
            print(2)
        
                


