def is_solved(board):
    l = []
    left_down_num = board[0][0] + board[1][1] + board[2][2]
    right_down_num = board[0][2] + board[1][1] + board[2][0]
    first_col_num = board[0][0] + board[1][0] + board[2][0]
    sec_col_num = board[0][1] + board[1][1] + board[2][1]
    third_col_num = board[0][2] + board[1][2] + board[2][2]
    first_row = board[0][0] + board[0][1] + board[0][2]
    second_row = board[1][0] + board[1][1] + board[1][2]
    third_row = board[2][0] + board[2][1] + board[2][2]
    
    if left_down_num 

    if left_down_num < 2 or 0 in board:
        return -1
    return l

is_solved([[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]])
#test.assert_equals(is_solved(board), -1)

# winning row
is_solved([[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]])
#test.assert_equals(is_solved(board), 1)

# winning column
is_solved([[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]])
#test.assert_equals(is_solved(board), 1)

# draw
is_solved([[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]])
#test.assert_equals(is_solved(board), 0)

'''
l = []
    left_down_num = board[0][0] + board[1][1] + board[2][2]
    right_down_num = board[0][2] + board[1][1] + board[2][0]
    first_col_num = board[0][0] + board[1][0] + board[2][0]
    sec_col_num = board[0][1] + board[1][1] + board[2][1]
    third_col_num = board[0][2] + board[1][2] + board[2][2]
    first_row = board[0][0] + board[0][1] + board[0][2]
    second_row = board[1][0] + board[1][1] + board[1][2]
    third_row = board[2][0] + board[2][1] + board[2][2]
    return l
'''
'''
    l = [
    [int(board[0][0] + board[1][1] + board[2][2])]
    [board[0][2] + board[1][1] + board[2][0]]
    [board[0][0] + board[1][0] + board[2][0]]
    [board[0][1] + board[1][1] + board[2][1]]
    [board[0][2] + board[1][2] + board[2][2]]
    [board[0][0] + board[0][1] + board[0][2]]
    [board[1][0] + board[1][1] + board[1][2]]
    [board[2][0] + board[2][1] + board[2][2]]
    ]
'''