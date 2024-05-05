'''
A simple program which pretends to play tic-tac-toe with the user.
Computer will always begins at the centerof the board as it was requested.
'''
def draw_board (spots):
    # Row line character
    row_l = "-"
    # Column line character 
    col_l = " "
    # A f string for each row in the square 
    row_sqr = f"+{row_l*7}+{row_l*7}+{row_l*7}+"
    # A f string for each column in the square
    col_sqr = f"|{col_l*7}|{col_l*7}|{col_l*7}|"
    # A f string for each column in that poses a value (spot in spots)
    col_sqr_spt_r1 = f"|{col_l*3}{spots [1]}{col_l*3}|{col_l*3}{spots [2]}{col_l*3}|{col_l*3}{spots [3]}{col_l*3}|"
    col_sqr_spt_r2 = f"|{col_l*3}{spots [4]}{col_l*3}|{col_l*3}{spots [5]}{col_l*3}|{col_l*3}{spots [6]}{col_l*3}|"
    col_sqr_spt_r3 = f"|{col_l*3}{spots [7]}{col_l*3}|{col_l*3}{spots [8]}{col_l*3}|{col_l*3}{spots [9]}{col_l*3}|"
    #Each row of the 3X3 square including values from the dict spots
    board = [row_sqr, col_sqr, col_sqr_spt_r1, col_sqr, row_sqr, col_sqr, col_sqr_spt_r2, col_sqr, row_sqr, col_sqr, col_sqr_spt_r3, col_sqr, row_sqr]

    return board

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for e in board:
        print (e)

def enter_move(input_list):
    # The function accepts the board's current status, asks the user about their move, 
    
    # checks the input, and updates the board according to the user's decision.
    check_e_m = True
    while check_e_m:
        try:
            value = input ("Enter a value in the board to make your move: ") 
            value = int (value) 
            #Conditions for the selection of a spot inside the board
            if value > 0 and value < 10 and value not in input_list:
                input_list.append (value)
                spots [value] = "O"
                return False
            else:
                print ("Enter a non selected number equal to a place in the board")
        except ValueError:
            print ("Enter a real value equal to a place in the board")
        except:
            print ("Something is wrong try with a number inside the board once more")

def draw_move(input_list):
# The function draws the computer's move and updates the board.
    check_d_m = True
    while check_d_m:

        for num in range (10):
            value = num
            if value > 0 and value < 10 and value not in input_list:
                input_list.append (value)
                spots [value] = "X"
                return False

def victory_for(input_dict):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    #Horizontal Win
    if (spots [1] == spots [2] == spots [3])\
        or (spots [4] == spots [5] == spots [6])\
        or (spots [7] == spots [8] == spots [9]):
        return False
    elif (spots [1] == spots [4] == spots [7])\
        or (spots [2] == spots [5] == spots [8])\
        or (spots [3] == spots [6] == spots [9]):
        return False
    elif (spots [1] == spots [5] == spots [9])\
        or (spots [3] == spots [5] == spots [7]):
        return False
    else:
        return True
            
def main ():
    global playing
    playing = True
    #spots dict and values list must be global in order to store values that change during the game and be funtional to other fuctions
    global spots 
    spots = {1:"1", 2:"2", 3:"3", 4:"4", 5:"X", 6:"6", 7:"7", 8:"8", 9:"9"}
    global values
    values = [5]
    # While playingis True, the loop will execute
    while playing:
        board = draw_board (spots)
        print (display_board(board))
        print (enter_move(values))
        draw_move(values)
        if victory_for(spots) == False:
            print (display_board(board))
            print ("There is a winner")
            playing = False
        elif len (values) > 10:
            print (display_board(board))
            print ("No winner, play again and good luck")
            break

   
if __name__ == "__main__":
    main ()