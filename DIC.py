def hru_greedy(lattdesc, viewcost, k, topview, totalcost):
    s = {topview}
    currentcost = {w: viewcost[topview] for w in lattdesc.keys()}
    
    print(f"Starting state: {s}")

    for step in range(1, k + 1):
        maxbenefit = -1
        bestview = None

        for v in lattdesc.keys():
            if v in s:
                continue

            benefitv = 0
            costfromv = viewcost[v]

            for w in lattdesc[v]:
                if costfromv < currentcost[w]:
                    benefitv += (currentcost[w] - costfromv)

            if benefitv > maxbenefit:
                maxbenefit = benefitv
                bestview = v

        if maxbenefit <= 0 or bestview is None:
            break

        s.add(bestview)
        print(f"Step {step}: selected {bestview}, benefit = {maxbenefit}")
        totalcost += maxbenefit

        # Update current costs
        for w in lattdesc[bestview]:
            if viewcost[bestview] < currentcost[w]:
                currentcost[w] = viewcost[bestview]

    return s, totalcost


costs = {
    'a': 120, 'b': 70, 'c': 60, 'd': 65,
    'e': 40, 'f': 45, 'g': 35, 'h': 30,
    'i': 20, 'j': 15, 'k': 10
}

dependencies = {
    'a': ['a','b','c','d','e','f','g','h','i','j','k'],
    'b': ['b','e','f','i','j'],
    'c': ['c','f','g','i','j','k'],
    'd': ['d','g','h','j','k'],
    'e': ['e','i'],
    'f': ['f','i','j'],
    'g': ['g','j','k'],
    'h': ['h','k'],
    'i': ['i'],
    'j': ['j'],
    'k': ['k']
}

selected, totalcost = hru_greedy(dependencies, costs, 3, 'a', 0)

print("Selected views:", selected)
print("Total benefit:", totalcost)