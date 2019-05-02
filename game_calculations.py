# Your name: Bansri Shah
# Your SBU ID: 110335850
# Your NetID: bpshah
#
# Game-Related Calculations (Homework 2-3) starter code
# CSE 101, Fall 2018


# Complete the functions that follow for this assignment
def updatePower(bowls, unitChange):
    temp = unitChange
    if unitChange < 0:
        temp = temp * -1

    while temp >= 1:
        if unitChange < 0 and bowls[2] >= 1:
            bowls[2] -= 1
            bowls[0] += 1
            temp -= 1
        elif unitChange > 0:
            if bowls[2] < 12:
                if bowls[0] >= 1:
                    bowls[0] -= 1
                    bowls[1] += 1
                    temp -= 1
                elif bowls[0] == 0 and bowls[1] >= 1:
                    bowls[1] -= 1
                    bowls[2] += 1
                    temp -= 1
            

def spellCost(words):
    # DO NOT DELETE THESE HELPER DICTIONARIES!
    power = {"Ya":1, "Lo":2, "Kath":3, "Ku":4, "Sar":5, "Ros":6}
    effect = {"Des":3, "Zo":4, "Oh":4, "Ven":5, "Ew":6, "Dain":7}
    element = {"Vi":4, "Ee":5, "Ra":6, "Mon":7, "Pal":7, "Neta":9}
    range1 = {"Um":2, "On":2, "Gor":3, "Ful":6, "Bro":6, "Ir":8}

    if len(words) < 2 or len(words) > 4:
        return None
    elif words[0] not in power:
        return None
    else:
        temp = []

        for i in range(1, len(words)):
            word = words[i]
            if word in effect:
                temp.append(1)
            elif word in element:
                temp.append(2)
            elif word in range1:
                temp.append(3)

        sort = sorted(temp)

        if temp != sort:
            return None
        else:
            power_value = power[words[0]]
            total_power = power_value
            cost = 0

            for j in range(1,len(words)):
                if temp[j-1] == 1:
                    cost = effect[words[j]]
                elif temp[j-1] == 2:
                    cost = element[words[j]]
                elif temp[j-1] == 3:
                    cost = range1[words[j]]
                total_power += (((power_value + 1) * cost)//2)
        return total_power


# DO NOT remove the code below! You can use it to test your work.

if __name__ == "__main__":
    print("Testing the updatePower() function:\n")
    bowls = [2, 3, 7]
    change = 4
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    bowls = [3, 4, 5]
    change = -3
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    bowls = [3, 3, 6]
    change = -2
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    bowls = [2, 6, 4]
    change = 7
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    bowls = [4, 6, 2]
    change = 11
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    bowls = [8, 1, 3]
    change = 2
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    bowls = [1, 1, 10]
    change = -5
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    bowls = [0, 1, 11]
    change = -10
    print("Testing updatePower(" + str(bowls) + ", " + str(change) + "):", end=' ')
    updatePower(bowls,change)
    print(bowls)
    print()

    print("Testing the spellCost() function:\n")
    print('Testing spellCost(["Sar","Ee"]):', spellCost(["Sar","Ee"]))
    print()

    print('Testing spellCost(["Ku", "Ven", "Um"]):', spellCost(["Ku", "Ven", "Um"]))
    print()

    print('Testing spellCost(["Gor"]):', spellCost(["Gor"]))
    print()

    print('Testing spellCost(["Ya", "Oh", "Ful"]):', spellCost(["Ya", "Oh", "Ful"]))
    print()

    print('Testing spellCost(["Kath", "Pal", "Des"]):', spellCost(["Kath", "Pal", "Des"]))
    print()

    print('Testing spellCost(["Lo", "Oh", "Mon", "On", "Um"]):', spellCost(["Lo", "Oh", "Mon", "On", "Um"]))
    print()

    print('Testing spellCost(["Kath", "Ven", "Pal", "Ir"]):', spellCost(["Kath", "Ven", "Pal", "Ir"]))
    print()

    print('Testing spellCost(["Zo", "Des", "Pal", "Bro"]):', spellCost(["Zo", "Des", "Pal", "Bro"]))
    print()

    print()
    
