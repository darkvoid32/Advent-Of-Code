puzzle = """
noop
noop
addx 5
addx 3
addx -2
noop
addx 5
addx 4
noop
addx 3
noop
addx 2
addx -17
addx 18
addx 3
addx 1
noop
addx 5
noop
addx 1
addx 2
addx 5
addx -40
noop
addx 5
addx 2
addx 3
noop
addx 2
addx 3
addx -2
addx 2
addx 2
noop
addx 3
addx 5
addx 2
addx 3
addx -2
addx 2
addx -24
addx 31
addx 2
addx -33
addx -6
addx 5
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx -1
addx 6
noop
noop
addx 1
addx 4
noop
noop
addx -15
addx 20
noop
addx -23
addx 27
noop
addx -35
addx 1
noop
noop
addx 5
addx 11
addx -10
addx 4
addx 1
noop
addx 2
addx 2
noop
addx 3
noop
addx 3
addx 2
noop
addx 3
addx 2
addx 11
addx -4
addx 2
addx -38
addx -1
addx 2
noop
addx 3
addx 5
addx 2
addx -7
addx 8
addx 2
addx 2
noop
addx 3
addx 5
addx 2
addx -25
addx 26
addx 2
addx 8
addx -1
addx 2
addx -2
addx -37
addx 5
addx 3
addx -1
addx 5
noop
addx 22
addx -21
addx 2
addx 5
addx 2
addx 13
addx -12
addx 4
noop
noop
addx 5
addx 1
noop
noop
addx 2
noop
addx 3
noop
noop
""".strip().split("\n")

total = 0
cycle = 1
register = 1
drawing = []
currDrawing = ""
def add_cycle(cycle, register, currDrawing, drawing):
    if register - 1 <= cycle <=  register + 1:
        currDrawing += "#"
    else:
        currDrawing += "."
        
    cycle += 1
    
    if len(currDrawing) == 40:
        drawing.append(currDrawing)
        currDrawing = ""
        cycle = 0

    return cycle, currDrawing, drawing
        
for line in puzzle:
    if line.split(" ")[0] == "noop":
        cycle, currDrawing, drawing = add_cycle(cycle, register, currDrawing, drawing)
    else:
        cycle, currDrawing, drawing = add_cycle(cycle, register, currDrawing, drawing)
        cycle, currDrawing, drawing = add_cycle(cycle, register, currDrawing, drawing)
        register += int(line.split(" ")[1])

for line in drawing:
    print(line)
