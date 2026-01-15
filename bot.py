import numpy as np
bestMove = [0, -10]
board = np.array(["","","",
                  "","","",
                  "","",""])

def is_best_move(curMoveLocation, curMoveScore):
   global bestMove
   if curMoveScore > bestMove[1]:
      bestMove[1] = curMoveScore
      bestMove[0] = curMoveLocation

def your_turn():
    for j in range(3):
        print("| ", end="")
        for i in range(3):
            print(board[i+3*(j-1)] + " | ", end="")
        print("\n----------")
    num1 = int(input("Where do you want to put an X(1-9):"))
    if board[num1-1] == "":
       board[num1-1]="X"
    else:
       print("Alredy chosen.")


def bot_turn():
   global bestMove
   if not(board[4] == "" and board[3] == "" and board[5] == "" and board[1] == "" and board[7] == "" and board[0] == "" and board[2] == "" and board[6] == "" and board[8] == ""):
      for i in range(9):
         if board[i] == "":
            is_best_move(i, score(i, True))
      board[bestMove[0]] = "O"
      bestMove = [0, -10]

def win_check(checkBoard):
   if (checkBoard[0]==checkBoard[1]==checkBoard[2] and checkBoard[0]!="") or (checkBoard[3]==checkBoard[4]==checkBoard[5] and checkBoard[3]!="") or (checkBoard[6]==checkBoard[7]==checkBoard[8] and checkBoard[6]!="") or (checkBoard[0]==checkBoard[3]==checkBoard[6] and checkBoard[0]!="") or (checkBoard[1]==checkBoard[4]==checkBoard[7] and checkBoard[1]!="") or (checkBoard[2]==checkBoard[5]==checkBoard[8] and checkBoard[2]!="") or (checkBoard[0]==checkBoard[4]==checkBoard[8] and checkBoard[0]!="") or (checkBoard[2]==checkBoard[4]==checkBoard[6] and checkBoard[2]!=""):
      if checkBoard [0]=="X" or checkBoard [3]=="X" or checkBoard [6]=="X" or checkBoard [1]=="X" or checkBoard [4]=="X" or checkBoard [7]=="X" or checkBoard [2]=="X" or checkBoard [5]=="X" or checkBoard [8]=="X":
         print("You win!")
         return 1 #Player wins
      else:
         print("Bot wins!")
         return 2 #Bot wins
   else:
      return 0 #No win
   
def score(move, isMaximising):
   tempBoard = board.copy()
   if isMaximising == True and tempBoard[move] == "":
      tempBoard[move] = "O"
      if win_check(tempBoard) == 2:
         return 10
      else:
         return 0
   if isMaximising == False and tempBoard[move] == "":
      tempBoard[move] = "X"
      if win_check(tempBoard) == 1:
         return -10
      else:
         return 0
   else: 
      return 0

def main():
    for i in range(9):
        your_turn()
        if win_check(board) != 0:
            break
        bot_turn()
        if win_check(board) != 0:
            break
        


if __name__ == "__main__":
    main()  