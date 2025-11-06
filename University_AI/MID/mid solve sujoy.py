#Problem - 1:
'''
Problem 01: The Plant Growth Evaluator (7 marks) - CLO1- (Bloom’s TaxonomyCognitive/Apply)
Write a Python function named evaluate_growth that takes the heights of 4 plants (in cm) as
input and checks two conditions:
1. If the average height is more than 50 cm.
2. If the difference between tallest and shortest plant is less than 20 cm.
Based on the results, print:
● If both conditions are true → "Plants are healthy and consistent!"
● If only the first is true → "Plants are growing well but unevenly!"
● Otherwise → "Plants need better growth conditions."
Example:
Test-1:
Input: [52, 48, 55, 51]
Output: Plants are healthy and consistent!
Test-2:
Input: [70, 30, 60, 55]
Output: Plants are growing well but unevenly!
Test-3:
Input: [20, 30, 35, 40]
Output: Plants need better growth conditions.
'''
def evaluate_growth(T_H):
    h_avg = round((sum(T_H) / len(T_H)),2)
    h_diff = abs(max(T_H) - min(T_H))
    con1 = con2 = False
    if h_avg > 50:
        con1 = True
    if h_diff < 20:
        con2 = True
    if con1 and con2:
        print("Plants are healthy and consistent!\n")
    elif con1:
        print("Plants are growing well but unevenly!\n")
    else:
        print("Plants need better growth conditions.\n")
T_H = [int(x) for x in input("Enter the height: ").split()] #input = list comprehension        
#T_H = list(map(int, input("Enter the height = ").split()))
evaluate_growth(T_H)

#Problem - 2
'''
Problem 02: The Robot Task Scheduler (7 marks) - CLO1 - (Bloom’s TaxonomyCognitive/Apply)
A robot has to complete 3 tasks: cleaning, sorting, and charging.
Each task takes a certain amount of time (in minutes).
The robot’s battery limit is 100 minutes.2/3
Write a Python program that:
● Takes time inputs for the three tasks.
● Calculates the total required time.
● If total time ≤ 100, print "All tasks completed successfully!"
● If total time > 100, print how much extra time is needed and which task(s) could not be
completed based on the order.
Example:
Input: cleaning = 40, sorting = 30, charging = 50
Output:
● Total time = 120 minutes
● Tasks completed: cleaning, sorting
● Task not completed: charging
Extra time needed: 20 minutes
'''
cleaning = int(input("Enter the cleaning time = "))
sorting = int(input("Enter the sorting time = "))
charging = int(input("Enter the charging time = "))
TT = sum([cleaning, sorting, charging])
#print(TT)
if TT <= 100:
    print("All tasks completed successfully!\n")
else:
    Battery = 100
    c = [] #completed
    nc = [] #not_completed

    if Battery >= cleaning:
        c.append("cleaning")
        Battery -= cleaning
    else:
        nc.append("cleaning")

    if Battery >= sorting:
        c.append("sorting")
        Battery -= sorting
    else:
        nc.append("sorting")

    if Battery >= charging:
        c.append("charging")
        Battery -= charging
    else:
        nc.append("charging")
    print("Task Completed: ", ", ".join(c) + ".")
    print("Task not Completed: ", ", ".join(nc) + ".")
    print(f"Extra time needed: {TT - 100} minutes\n")
    
    
    #problem - 3
    '''
    Problem 3: Romania Map Traversal (4 Queens) (6 marks) - CLO2 - (Bloom’s TaxonomyCognitive/Apply)
You are given a map of Romania (next page) showing several cities connected by roads.
Your task is to find the optimal route from Arad to Bucharest.
You can use either A* or Greedy Best First Search based on the provided distances and
heuristics.
Find and print the final path from Start to Goal. Calculate the total cost of the path.
    '''
    #BFS
    from collections import deque
#Heuristic value from each node to goal node
SuccList = {
    'O' : [['Z',374], ['S',253]],
    'Z' : [['O',380], ['A',366]],
    'A' : [['S',253], ['Z',374], ['T',329]],
    'T' : [['A',366], ['L',244]],
    'L' : [['T',329], ['M',241]],
    'M' : [['L',244], ['D',242]],
    'D' : [['M',241], ['C',160]],
    'C' : [['R',193], ['P',98]],
    'S' : [['R',193], ['F',178]],
    'F' : [['S',253], ['B',0]],
    'R' : [['S',253], ['P',98]],
    'P' : [['R',193], ['B',0]],
    'B' : [['F',178], ['P',98], ['G',77], ['U',80]],
    'G' : [['B',0]],
    'U' : [['B',0], ['V',199], ['H',151]],
    'N' : [['I',226]],
    'I' : [['N',234], ['V',199]],
    'V' : [['I',226], ['U',80]],
    'H' : [['U',80], ['E',161]],
    'E' : [['H',151]]
}
# path cost between two nodes
path_cost = {
    'O' : [['Z',71], ['S',151]],
    'Z' : [['O',71], ['A',75]],
    'A' : [['S',140], ['Z',75], ['T',118]],
    'T' : [['A',118], ['L',111]],
    'L' : [['T',111], ['M',70]],
    'M' : [['L',70], ['D',75]],
    'D' : [['M',75], ['C',120]],
    'C' : [['R',146], ['P',138]],
    'S' : [['R',80], ['F',99]],
    'F' : [['S',99], ['B',211]],
    'R' : [['S',80], ['P',97]],
    'P' : [['R',97], ['B',101]],
    'B' : [['F',211], ['P',101], ['G',90], ['U',85]],
    'G' : [['B',90]],
    'U' : [['B',85], ['V',142], ['H',98]],
    'N' : [['I',87]],
    'I' : [['N',87], ['V',92]],
    'V' : [['I',92], ['U',142]],
    'H' : [['U',98], ['E',86]],
    'E' : [['H',86]]
}
start = 'A'
goal = 'B'

# -----------BFS-----------
def BFS(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path #final path

        visited.add(node)

        for child, _ in SuccList.get(node, []):
            if child not in visited:
                new_path = list(path) #copy
                new_path.append(child)
                queue.append(new_path)

    return None

#----Cost Calculation---------
def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        current = path[i]
        nxt = path[i+1]

        #searching for neighbor nodes
        #for dest, c in path_cost.get(current):
        for dest, c in path_cost[current]:
            if dest == nxt:
                cost += c
                break

    return cost


final_path = BFS(start,goal)
if final_path:
    print("Final Path: "," -> ".join(final_path))
    total_cost = calculate_cost(final_path)
    print("Total Path Cost = ", total_cost)
else:
    print("Goal not found!!!")


#A*
# -------- Short-form Path Cost Graph --------
G = {
    'O' : [['Z',71], ['S',151]],
    'Z' : [['O',71], ['A',75]],
    'A' : [['S',140], ['Z',75], ['T',118]],
    'T' : [['A',118], ['L',111]],
    'L' : [['T',111], ['M',70]],
    'M' : [['L',70], ['D',75]],
    'D' : [['M',75], ['C',120]],
    'C' : [['R',146], ['P',138]],
    'S' : [['R',80], ['F',99]],
    'F' : [['S',99], ['B',211]],
    'R' : [['S',80], ['P',97]],
    'P' : [['R',97], ['B',101]],
    'B' : [['F',211], ['P',101], ['G',90], ['U',85]],
    'G' : [['B',90]],
    'U' : [['B',85], ['V',142], ['H',98]],
    'N' : [['I',87]],
    'I' : [['N',87], ['V',92]],
    'V' : [['I',92], ['U',142]],
    'H' : [['U',98], ['E',86]],
    'E' : [['H',86]]
}

# -------- Heuristic Values (Short Form) --------
H = {
    'A':366, 
    'Z':374, 
    'O':380, 
    'S':253, 
    'T':329, 
    'L':244, 
    'M':241,
    'D':242, 
    'C':160, 
    'R':193, 
    'P':98, 
    'F':178, 
    'B':0, 
    'G':77,
    'U':80, 
    'V':199, 
    'H':151, 
    'E':161, 
    'I':226, 
    'N':234
}

def A_star(start, goal):
    OPEN = [[start, 0, H[start], H[start], [start]]] # [node, g, h, f, path]
    CLOSED = []

    while OPEN:
        OPEN.sort(key = lambda x : x[3]) # sort by f
        node, g, h, f, path = OPEN.pop(0)
        CLOSED.append(node)

        if node == goal:
            return path, g

        for child, cost in G.get(node , []):
            if child in CLOSED:
                continue

            g2 = g + cost
            h2 = H[child]
            f2 = g2 + h2

            OPEN.append([child, g2, h2, f2, path + [child]])

    return None, None
    

#----- Run The ALgorithm ------------
path, total_cost = A_star('A', 'B')

print("Optimal Path = ", " -> ".join(path))
print("Path Cost = ",total_cost)

#Hill CLimbing
import random

class EightQueens:
    
    def __init__(self):
        #Initialize the board with 8 Queen in each row, placed them randomly in of the columns.
        self.board = [random.randint(0, 7) for _ in range(8)]
    '''
    
    def __init__(self, initial_board):
        """
        initial_board: Optional list of 8 integers (0-7) representing the column of queen in each row.
        If not provided, generate random board.
        """
        if initial_board:
            self.board = initial_board
        else:
            self.board = [random.randint(0, 7) for _ in range(8)]
    '''

    def print_board(self):
        for row in range(8):
            line = ""
            for col in range(8):
                if self.board[row] == col:
                    line += 'Q '
                else:
                    line += '. '
            print(line)
        print('\n')

    def calculate_conf(self, board):
        #calculating the number of conflicts (Queens Attacking each other) for a given board state.
        conflicts = 0
        for row1 in range(8):
            for row2 in range(row1+1, 8):
                # Check if same Column
                if board[row1] == board[row2]:
                    conflicts += 1
                # Check if same Diagonal
                if abs(board[row1] - board[row2]) == abs(row1 - row2):
                    conflicts += 1
        return conflicts

    def Hill_Climb(self):
        #Perform simple hill climbing until we reach a solution or local maxima

        current_conflicts = self.calculate_conf(self.board)

        while True:
            # Looking for better neighbour if we find....
            found_better = False

            #Try to moving each queen ( in each row) to a different column for better replacement
            for row in range(8):
                real_col = self.board[row]
                for col in range(8):
                    if col != real_col: #Moving different column
                        new_board = self.board[:] #Copying the current board
                        new_board[row] = col #Move the queen to the new column
                        new_conflicts = self.calculate_conf(new_board)

                        # If we find a better board
                        if new_conflicts < current_conflicts:
                            self.board = new_board
                            current_conflicts = new_conflicts
                            found_better = True
                            break # Move on without checking further neighbors

                    if found_better:
                        break # Move for the new iteration wih the new board

                if found_better == False:
                    break # If there any better neighbour exist
        
            return current_conflicts == 0    

#Examples Usage:
'''
manual_board = [3, 5, 7, 1, 6, 0, 2, 4]  # Q1-Q8 columns in row 0-7
solve = EightQueens(manual_board) #Create an 8 queens solver object
'''
solve = EightQueens()
print("Initial Board: ")
solve.print_board() #Print the initial random board

if solve.Hill_Climb(): #The Algorithm....
    print("Solution Found: ")
else:
    print("Local Maximum reached, no solution found: ")
solve.print_board() #Print the final board (solution or local maximum)
    


    
    
    
    
    
    