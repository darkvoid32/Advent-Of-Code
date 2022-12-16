import math

items = {
    0: [56, 52, 58, 96, 70, 75, 72],
    1: [75, 58, 86, 80, 55, 81],
    2: [73, 68, 73, 90],
    3: [72, 89, 55, 51, 59],
    4: [76, 76, 91],
    5: [88],
    6: [64, 63, 56, 50, 77, 55, 55, 86],
    7: [79, 58],
}

inspections = [0] * 8
div = [11, 3, 5, 7, 19, 2, 13, 17]

global M 
M = math.prod(div)

def check_condition(item, items, cond, t, f):
    if (item % cond == 0):
        items[t].append(item % M)
    else:
        items[f].append(item % M)
    return items

def do_round(items, inspections):
    
    for key in items:
        if key == 0:
            for item in items[key]:
                inspections[key] += 1
                new_item = item * 17
                items = check_condition(new_item, items, div[key], 2, 3)
            items[key] = []
        elif key == 1:
            for item in items[key]:
                inspections[key] += 1
                new_item = item + 7
                items = check_condition(new_item, items, div[key], 6, 5)
            items[key] = []
        elif key == 2:
            for item in items[key]:
                inspections[key] += 1
                new_item = item ** 2
                items = check_condition(new_item, items, div[key], 1, 7)
            items[key] = []
        elif key == 3:
            for item in items[key]:
                inspections[key] += 1
                new_item = item + 1
                items = check_condition(new_item, items, div[key], 2, 7)
            items[key] = []
        elif key == 4:
            for item in items[key]:
                inspections[key] += 1
                new_item = item * 3
                items = check_condition(new_item, items, div[key], 0, 3)
            items[key] = []
        elif key == 5:
            for item in items[key]:
                inspections[key] += 1
                new_item = item + 4
                items = check_condition(new_item, items, div[key], 6, 4)
            items[key] = []
        elif key == 6:
            for item in items[key]:
                inspections[key] += 1
                new_item = item + 8
                items = check_condition(new_item, items, div[key], 4, 0)
            items[key] = []
        elif key == 7:
            for item in items[key]:
                inspections[key] += 1
                new_item = item + 6
                items = check_condition(new_item, items, div[key], 1, 5)
            items[key] = []
        else:
            print("Unknown key")
        
    return items, inspections
        
for i in range(10000):
    items, inspections = do_round(items, inspections)

print(items)
inspections.sort()
print(inspections)
print(inspections[-1] * inspections[-2])