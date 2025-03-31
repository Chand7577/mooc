# Write your solution here



def who_won(game_board:list):

    player1_pieces=0
    player2_pieces=0
    for row in game_board:
        for value in row:
            if value==1:
                player1_pieces+=1
            
            elif value==2:
                player2_pieces+=1
    

    if player1_pieces>player2_pieces:
        return 1
    
    elif player1_pieces<player2_pieces:
        return 2
    else:
        return 0






if __name__=="__main__":
    matrix=[
        [1,2,1],
        [0,0,1],
        [2,1,0]
    ]
    print(who_won(matrix))
