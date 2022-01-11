from time import time

"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""

def twoCitySchedCost(costs) -> int:
    ## difference of price of sending people to A and not to B
    diffs = [(i, cost[0] - cost[1]) for i, cost in enumerate(costs)]
    diffs.sort(key=lambda x : x[1])
    indices, _ = zip(*diffs)
    a_indices = set(indices[:len(costs) // 2])

    tot_cost = 0
    for i, cost in enumerate(costs):
        if(i in a_indices):
            tot_cost += cost[0]
        else :
            tot_cost += cost[1]
    return tot_cost


## Approximately 10 times faster
def other_implementation(costs) -> int:

    ## cost of sending every one to B
    tot_cost = sum(list(zip(*costs))[1])
    
    ## get the best difference we can have by sending someone to A rather than to B
    diffs = [cost[0] - cost[1] for i, cost in enumerate(costs)]
    diffs.sort()

    gain = sum(diffs[:len(costs) //2])

    return tot_cost + gain







if __name__ == "__main__":
    ## few tests :

    for i, func in enumerate([twoCitySchedCost, other_implementation]):
        print("Implemation ", i + 1)
        start = time()
        print("1) ", end="\t")
        print(func([[10,20],[30,200],[400,50],[30,20]]))
        print("Expected : 110")
        print("2) ", end="\t")
        print(func([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
        print("Expected : 1859")
        print("3) ", end="\t")
        print(func([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
        print("Expected : 3086")

        print(round(time() - start, 6))



