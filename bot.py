import numpy as np
x = np.array(["","","","","","","","",""])

def best_move(curMoveLocation,curMoveScore):
   curMove = np.array([curMoveLocation,curMoveScore])
   for i in range(9):
      bestMove = np.array([0,-10])
      if curMove[2] > bestMove[2]:
            bestMove = curMove
            curMove = np.array([0,-10])
    

def your_turn():
    for j in range(3):
        print("| ", end="")
        for i in range(3):
            print(x[i+3*(j-1)] + " | ", end="")
        print("\n--------------")
    num1 = int(input("Where do you want to put an X(1-9):"))
    if x[num1] == "":
       x[num1]="X"
    else:
       print("Alredy chosen.")


def bot_turn():
   pass

your_turn()