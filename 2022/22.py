puzzle = """
Monkey 0:
  Starting items: 56, 52, 58, 96, 70, 75, 72
  Operation: new = old * 17
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 75, 58, 86, 80, 55, 81
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 6
    If false: throw to monkey 5

Monkey 2:
  Starting items: 73, 68, 73, 90
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 3:
  Starting items: 72, 89, 55, 51, 59
  Operation: new = old + 1
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 4:
  Starting items: 76, 76, 91
  Operation: new = old * 3
  Test: divisible by 19
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 88
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 6:
  Starting items: 64, 63, 56, 50, 77, 55, 55, 86
  Operation: new = old + 8
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 7:
  Starting items: 79, 58
  Operation: new = old + 6
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 5
""".strip().split("\n")

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

inspections = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0
}

def check_condition(item, items, cond, t, f):
    if (item % cond == 0):
        items[t].append(item)
    else:
        items[f].append(item)
    return items

def do_round(items, inspections):
    for key in items:
        if key == 0:
            for item in items[key]:
                inspections[key] += 1
                new_item = (item * 17) // 3
                items = check_condition(new_item, items, 11, 2, 3)
            items[key] = []
        elif key == 1:
            for item in items[key]:
                inspections[key] += 1
                new_item = (item + 7) // 3
                items = check_condition(new_item, items, 3, 6, 5)
            items[key] = []
        elif key == 2:
            for item in items[key]:
                inspections[key] += 1
                new_item = (item ** 2) // 3
                items = check_condition(new_item, items, 5, 1, 7)
            items[key] = []
        elif key == 3:
            for item in items[key]:
                inspections[key] += 1
                new_item = (item + 1) // 3
                items = check_condition(new_item, items, 7, 2, 7)
            items[key] = []
        elif key == 4:
            for item in items[key]:
                inspections[key] += 1
                new_item = (item * 3) // 3
                items = check_condition(new_item, items, 19, 0, 3)
            items[key] = []
        elif key == 5:
            for item in items[key]:
                inspections[key] += 1
                new_item = (item + 4) // 3
                items = check_condition(new_item, items, 2, 6, 4)
            items[key] = []
        elif key == 6:
            for item in items[key]:
                inspections[key] += 1
                new_item = int((item + 8) / 3)
                items = check_condition(new_item, items, 13, 4, 0)
            items[key] = []
        elif key == 7:
            for item in items[key]:
                inspections[key] += 1
                new_item = int((item + 6) / 3)
                items = check_condition(new_item, items, 17, 1, 5)
            items[key] = []
        else:
            print("Unknown key")
        
    return items, inspections
        
for i in range(20):
    #print("="*20)
    items, inspections = do_round(items, inspections)

print(items)
print(inspections)

# maximum value
max = max(inspections.values())
 
# iterate through the dictionary
max2 = 0
for v in inspections.values():
     if(v>max2 and v<max):
            max2 = v
 
# print the second largest value
print(max)
print(max2)
print(max * max2)