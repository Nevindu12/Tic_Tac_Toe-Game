def ConstBoard(board):
    print("Current State of the Board: \n\n");
    for i in range(0, 9):
        if((i>0) and (i%3==0)):
            print("\n");
        if(board[i]==0):
            print("_", end=" ");
        if(board[i]==-1):
            print("X ", end=" ");
        if(board[i]==1):
            print("O ", end=" ");
    print("\n\n");

def User1Turn(board):
    pos = input("Enter X's position from [1,2,3,..., 9]");
    pos = int(pos);
    if(board[pos-1]!=0):
        print("Wrong Move");
        exit(0);
    board[pos-1]=-1;

def User2Turn(board):
    pos = input("Enter O's position from [1,2,3,..., 9]");
    pos = int(pos);
    if(board[pos-1]!=0):
        print("Wrong Move");
        exit(0);
    board[pos-1]=1;



def main():
    choice = input("Enter 1 for Single Player, Enter 2 for Multiplayer:");
    choice = int(choice);
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if(choice==1):
        print("Computer: O VS. You: X");
        player = input("Enter to play 1(st) or 2(nd): ");
        player = int(player);
        for i in range(0, 9):
            if(analayzeboard(board)!=0):    # check is there someone has won
                break;
            if((i+player)%2==0):       #to check who's turn(check whether it is AI turn).
                CompTurn(board);
            else:
                ConstBoard(board);
                User1Turn(board);
    else:
        for i in range(0, 9):
            if(analayzeboard(board)!=0):    # check is there some has won
                break;
            if(i%2==0):       #to check who's turn(check whether it is AI turn).
                ConstBoard(board);
                User1Turn(board);
            else:
                ConstBoard(board);
                User2Turn(board);
    
    x = analayzeboard(board);
    if(x==0):
        ConstBoard(board);
        print("Draw!");
    if(x==-1):
        ConstBoard(board);
        print("Player X WINS!!!! & O Looses!");
    if(x==1):
        ConstBoard(board);
        print("Player O WINS!!!! & X Looses!");