## Write a program to solve a fractional Knapsack problem using a greedy method.

class ItemValue:

    def __init__(self, wt_, val_, ind_):
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        self.cost = val_ // wt_

    def __lt__(self, other):
        return self.cost < other.cost

def fractional_knapsack(wt, val, capacity):
    iVal = [ItemValue(wt[i], val[i], i) for i in range (len(wt))]

    #Sorting items by value
    iVal.sort(reverse=True)

    totalValue = 0
    for i in iVal:
        curwt = i.wt
        curVal = i.val
        if capacity - curwt >= 0:
            capacity -= curwt
            totalValue+= curVal
        else:
            fraction = capacity / curwt
            totalValue += curVal * fraction
            capacity = int(capacity - (curwt * fraction))
            break
    return totalValue

if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capactiy = 50


    maxValue = fractional_knapsack(wt, val, capactiy)
    print("Maximum value in knapsack = ", maxValue)
