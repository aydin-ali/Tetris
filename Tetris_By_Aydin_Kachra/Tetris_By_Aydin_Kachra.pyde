def setup(): # declare any variables that shouldn't restart every new game
    global minim, intro, click
    global score, totalscores, highscores, First, Second, Third, Fourth, Fifth
    
    size(800, 800)
    background(0, 0, 0)
    
# Sound library
    add_library ('minim')
    minim = Minim(this)
    intro = minim.loadFile("TetrisTheme.mp3")
    click = minim.loadFile("click.mp3")    
# Score variables
    totalscores = [0, 0, 0, 0, 0]
    First = 0
    Second = 0
    Third = 0
    Fourth = 0
    Fifth = 0
    
    startup()

def startup():  # declares all the necessary start up variables
    global mode
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth
    global board_x, board_y, grid_values
    global column_dict, row_dict, column, row
    global block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9
    global block_locations, bottom_locations, left_locations, right_locations
    global piece, piece_cols, rotation_num, piece_shape
    global block_w, block_h
    global piece_x, piece_y, left_x, right_x, incr_y
    global column_vals
    global active_piece
    global arrowcontrols, pausekey, backarrow
    global blocks
    global startRectX, startRectY, rectXShow, rectYShow, rectHeight, rectWidth
    global startRectX2, startRectY2, rectXShow2, rectYShow2, rectHeight2, rectWidth2
    global score, score_append

    mode = 0
# Menu variables
    back = loadImage("tetrislogo.png")
    imageheight = 640
    imagewidth = 360
    imageCornerPointX = 80
    imageCornerPointY = 120
    font = createFont("Phosphate", 16, True)
    numSquares = 3
    startSquareX = 125
    startSquareY = 550
    squareHeight = 150
    squareWidth = 150
# Help screen images
    arrowcontrols = loadImage("arrowcontrols1.png")
    pausekey = loadImage("pausekey.png")
    backarrow = loadImage("backarrow.png")
#Game screen images
    blocks = loadImage("blocks.png")
# Board grid variables
    board_x = 125
    board_y = 20
    grid_values = [[0] * 10 for n in range(24)]
    column_dict = {125:0, 155:1, 185:2, 215:3, 245:4, 275:5, 305:6, 335:7, 365:8, 395:9}
    row_dict = {20:0, 50:1, 80:2, 110:3, 140:4, 170:5, 200:6, 230:7, 260:8, 290:9, 320:10, 350:11, 380:12, 410:13, 440:14, 470:15, 500:16, 530:17, 560:18, 590:19, 620:20, 650:21, 680:22, 710:23}
    column = 0
    row = 0
    block_1 = []
    block_2 = []
    block_3 = []
    block_4 = []
    block_5 = []
    block_6 = []
    block_7 = []
    block_8 = []
    block_9 = [] 
    block_locations = []
    bottom_locations = []
    left_locations = []
    right_locations = []
# Piece variables
    piece = 0
    piece_cols = 0
    rotation_num = 0
    piece_shape = 0
    piece_x = 10
    piece_y = 10
    left_x = -30
    right_x = 30
    incr_y = 0
    block_w = 30
    block_h = 30
    r = 0
    g = 0
    b = 0
    column_vals = [125, 155, 185, 215, 245, 275, 305, 335]
    active_piece = 0
# Paused menu variables
    font = createFont("Phosphate", 16, True)
    startRectX = 250
    startRectY = 225
    rectXShow = startRectX
    rectYShow = startRectY
    rectHeight = 100
    rectWidth = 300
# Game over menu variables
    font = createFont("Phosphate", 16, True)
    startRectX2 = 250
    startRectY2 = 325
    rectXShow2 = startRectX2
    rectYShow2 = startRectY2
    rectHeight2 = 100
    rectWidth2 = 300
# Current score variable
    score = 0
    score_append = 0

def grid(): #Draws the grid
    global board_x, board_y, grid_values

    board_x = 125
    board_y = 20

    fill(255, 255, 255)

    #Checks if there is a 0 or 1 in each grid to see if there is a piece at the location
    for row in grid_values:
        for col in row:
            #If there is a 1, that block should be filled in (meaning there is a piece there)
            if col == 1:
                fill(0, 0, 0)
            else:
            #Otherwise there is a 0, which means that block is empty and nothing is there
                fill(255,255,255)
            rect(board_x, board_y, block_w, block_h)
            board_x += block_w
        #draws each row of the grid
        board_y += block_w
        board_x = 125

def get_piece(): #Different rotations of shapes and randomization of piece dropping
    global piece, piece_cols, rotation_num, piece_shape
    global piece_x, piece_y, incr_y
    global column_vals

    #L piece shape + the different possible rotations 
    L = [[[0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 1]],
        [[0, 0, 0],
         [1, 1, 1],
         [1, 0, 0]],
        [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]]
    
    #J piece shape + the different possible rotations 
    J = [[[1, 0, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 1],
         [0, 1, 0],
         [0, 1, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 0, 1]],
        [[0, 1, 0],
         [0, 1, 0],
         [1, 1, 0]]]
    
    #T piece shape + the different possible rotations 
    T = [[[0, 1, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 0],
         [0, 1, 1],
         [0, 1, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 1, 0]],
        [[0, 1, 0],
         [1, 1, 0],
         [0, 1, 0]]]
    
    #Square shape + the different possible rotations (which are all the same)
    SQ = [[[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]]]
    
    #Z piece shape + the different possible rotations 
    Z = [[[0, 0, 1],
         [0, 1, 1],
         [0, 1, 0]],
        [[0, 0, 0],
         [1, 1, 0],
         [0, 1, 1]],
        [[0, 0, 1],
         [0, 1, 1],
         [0, 1, 0]],
        [[1, 1, 0],
         [0, 1, 1],
         [0, 0, 0]]]

    #S piece shape + the different possible rotations 
    S = [[[1, 0, 0],
         [1, 1, 0],
         [0, 1, 0]],
        [[0, 1, 1],
         [1, 1, 0],
         [0, 0, 0]],
        [[1, 0, 0],
         [1, 1, 0],
         [0, 1, 0]],
        [[0, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]]
    
    #I piece shape + the different possible rotations 
    I = [[[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 0, 0]]]
    
    #Initialize variables for the randomization of piece drops + colours
    piece = [L, J, T, SQ, Z, S, I]
    piece_cols = [[0, 255, 0], [255, 0, 0], [0, 255, 255], [255, 255, 0], [255, 165, 0], [0, 0, 255], [128, 0, 128]]
    
    #Randomizes the piece that is dropping each time after the previous one lands
    import random
    rotation_num = random.randint(0, 3)
    piece_shape = random.randint(0, 6)
    piece_x = random.choice(column_vals)
    if piece[piece_shape][rotation_num][0][0] == 1 or piece[piece_shape][rotation_num][0][1] == 1 or piece[piece_shape][rotation_num][0][2] == 1:
        piece_y = 20
    else:
        piece_y = -10
    incr_y = 2
    
def draw_piece(): #Draws the actual pieces onto the grid
    global active_piece
    global piece, piece_cols, rotation_num, piece_shape
    global piece_x, piece_y, incr_y
    global block_w, block_h
    
    #Resets if a piece lands so that the game knows to respawn another piece to fall
    if active_piece == 0:
        get_piece()
        active_piece = 1
    
    block_w = 30
    block_h = 30
    
    #Assigns set colours for specific pieces
    r = piece_cols[piece_shape][0]
    g = piece_cols[piece_shape][1]
    b = piece_cols[piece_shape][2]
                     
    fill(r, g, b)

    #Draws the piece based on which shape and rotation is selected
    for i in range (len(piece[piece_shape][rotation_num])):
        if piece[piece_shape][rotation_num][0][0] == 1:
            rect(piece_x, piece_y, block_w, block_h)
        if piece[piece_shape][rotation_num][0][1] == 1:
            rect(piece_x + 30, piece_y, block_w, block_h)
        if piece[piece_shape][rotation_num][0][2] == 1:
            rect(piece_x + 60, piece_y, block_w, block_h)
        if piece[piece_shape][rotation_num][1][0] == 1:
            rect(piece_x, piece_y + 30, block_w, block_h)
        if piece[piece_shape][rotation_num][1][1] == 1:
            rect(piece_x + 30, piece_y + 30, block_w, block_h)
        if piece[piece_shape][rotation_num][1][2] == 1:
            rect(piece_x + 60, piece_y + 30, block_w, block_h)
        if piece[piece_shape][rotation_num][2][0] == 1:
            rect(piece_x, piece_y + 60, block_w, block_h)
        if piece[piece_shape][rotation_num][2][1] == 1:
            rect(piece_x + 30, piece_y + 60, block_w, block_h)
        if piece[piece_shape][rotation_num][2][2] == 1:
            rect(piece_x + 60, piece_y + 60, block_w, block_h)
            
    
def piece_tracking(): #Tracks where the piece is located on the grid
    global grid_values
    global column_dict, row_dict, column, row
    global block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9
    global block_locations, bottom_locations, left_locations, right_locations
    global piece, piece_cols, rotation_num, piece_shape
    global block_w, block_h
    global piece_x, piece_y, left_x, right_x, incr_y
    global column_vals
    global active_piece
    
    #Empties the location lists so they start fresh each time draw runs
    block_1 = []
    block_2 = []
    block_3 = []
    block_4 = []
    block_5 = []
    block_6 = []
    block_7 = []
    block_8 = []
    block_9 = []
    block_locations = []
    bottom_locations = []
    left_locations = []
    right_locations = []
    
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists
    if piece[piece_shape][rotation_num][0][0] == 1:
        for x_val in column_dict:
            if x_val == piece_x:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y:
                row = row_dict[y_val]
        block_1.append(column)
        block_1.append(row)
        block_locations.append(block_1) 
        left_locations.append(block_1) #Doesn't work to full capacity
        if piece[piece_shape][rotation_num][0][1] == piece[piece_shape][rotation_num][0][2] == 0: #Doesn't work to full capacity
            right_locations.append(block_1) #Doesn't work to full capacity
        
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists
    if piece[piece_shape][rotation_num][0][1] == 1:
        for x_val in column_dict:
            if x_val == piece_x + 30:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y:
                row = row_dict[y_val]
        block_2.append(column)
        block_2.append(row)
        block_locations.append(block_2)
        if piece[piece_shape][rotation_num][0][0] == 0: #Doesn't work to full capacity
            left_locations.append(block_2) #Doesn't work to full capacity
        if piece[piece_shape][rotation_num][0][2] == 0: #Doesn't work to full capacity
            right_locations.append(block_2) #Doesn't work to full capacity
    
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists   
    if piece[piece_shape][rotation_num][0][2] == 1:
        for x_val in column_dict:
            if x_val == piece_x + 60:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y:
                row = row_dict[y_val]
        block_3.append(column)
        block_3.append(row)
        block_locations.append(block_3)
        if piece[piece_shape][rotation_num][0][0] == 0 and piece[piece_shape][rotation_num][0][1] == 0: #Doesn't work to full capacity 
            left_locations.append(block_3) #Doesn't work to full capacity
        right_locations.append(block_3) #Doesn't work to full capacity
    
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists
    if piece[piece_shape][rotation_num][1][0] == 1:
        for x_val in column_dict:
            if x_val == piece_x:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y + 30:
                row = row_dict[y_val]
        block_4.append(column)
        block_4.append(row)
        block_locations.append(block_4)
        left_locations.append(block_4) #Doesn't work to full capacity
        #Checks if a the bottom of the piece array is not occupied by a block, so the exact bottom location of the piece can be tracked
        if piece[piece_shape][rotation_num][2][0] == piece[piece_shape][rotation_num][2][1] == piece[piece_shape][rotation_num][2][2] == 0:
            bottom_locations.append(block_4)
        if piece[piece_shape][rotation_num][1][1] == piece[piece_shape][rotation_num][1][2] == 0: #Doesn't work to full capacity
            right_locations.append(block_4) #Doesn't work to full capacity
   
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists
    if piece[piece_shape][rotation_num][1][1] == 1:
        for x_val in column_dict:
            if x_val == piece_x + 30:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y + 30:
                row = row_dict[y_val]
        block_5.append(column)
        block_5.append(row)
        block_locations.append(block_5)
        #Checks if a the bottom of the piece array is not occupied by a block, so the exact bottom location of the piece can be tracked
        if piece[piece_shape][rotation_num][2][0] == piece[piece_shape][rotation_num][2][1] == piece[piece_shape][rotation_num][2][2] == 0:
            bottom_locations.append(block_5)
        if piece[piece_shape][rotation_num][1][0] == 0: #Doesn't work to full capacity
            left_locations.append(block_5) #Doesn't work to full capacity
        if piece[piece_shape][rotation_num][1][2] == 0: #Doesn't work to full capacity
            right_locations.append(block_5) #Doesn't work to full capacity
    
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists  
    if piece[piece_shape][rotation_num][1][2] == 1:
        for x_val in column_dict:
            if x_val == piece_x + 60:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y + 30:
                row = row_dict[y_val]
        block_6.append(column)
        block_6.append(row)
        block_locations.append(block_6)
        #Checks if a the bottom of the piece array is not occupied by a block, so the exact bottom location of the piece can be tracked
        if piece[piece_shape][rotation_num][2][0] == piece[piece_shape][rotation_num][2][1] == piece[piece_shape][rotation_num][2][2] == 0:
            bottom_locations.append(block_6)
        if piece[piece_shape][rotation_num][1][0] == piece[piece_shape][rotation_num][1][1] == 0: #Doesn't work to full capacity
            left_locations.append(block_6) #Doesn't work to full capacity
        right_locations.append(block_6) #Doesn't work to full capacity   
    
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists  
    if piece[piece_shape][rotation_num][2][0] == 1:
        for x_val in column_dict:
            if x_val == piece_x:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y + 60:
                row = row_dict[y_val]
        block_7.append(column)
        block_7.append(row)
        block_locations.append(block_7)
        left_locations.append(block_7) #Doesn't work to full capacity 
        #Checks if a the bottom of the piece array is occupied by a block, so the exact bottom location of the piece can be tracked
        if piece[piece_shape][rotation_num][2][0] == 1 or piece[piece_shape][rotation_num][2][1] == 1 or piece[piece_shape][rotation_num][2][2] == 1:
            bottom_locations.append(block_7)
        if piece[piece_shape][rotation_num][2][1] == piece[piece_shape][rotation_num][2][2] == 0: #Doesn't work to full capacity
                right_locations.append(block_7) #Doesn't work to full capacity  
    
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists
    if piece[piece_shape][rotation_num][2][1] == 1:
        for x_val in column_dict:
            if x_val == piece_x + 30:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y + 60:
                row = row_dict[y_val]
        block_8.append(column)
        block_8.append(row)
        block_locations.append(block_8)
        #Checks if a the bottom of the piece array is occupied by a block, so the exact bottom location of the piece can be tracked
        if piece[piece_shape][rotation_num][2][0] == 1 or piece[piece_shape][rotation_num][2][1] == 1 or piece[piece_shape][rotation_num][2][2] == 1:
            bottom_locations.append(block_8)
        if piece[piece_shape][rotation_num][2][0] == 0:
            left_locations.append(block_8)
        if piece[piece_shape][rotation_num][2][2] == 0:
            right_locations.append(block_8)
 
    #Checks if a block is at this location in the piece array, so the block's grid location can be appended to the appropriate lists  
    if piece[piece_shape][rotation_num][2][2] == 1:
        for x_val in column_dict:
            if x_val == piece_x + 60:
                column = column_dict[x_val]
        for y_val in row_dict:
            if y_val == piece_y + 60:
                row = row_dict[y_val]
        block_9.append(column)
        block_9.append(row)
        block_locations.append(block_9)
        #Checks if a the bottom of the piece array is occupied by a block, so the exact bottom location of the piece can be tracked
        if piece[piece_shape][rotation_num][2][0] == 1 or piece[piece_shape][rotation_num][2][1] == 1 or piece[piece_shape][rotation_num][2][2] == 1:
            bottom_locations.append(block_9)
        if piece[piece_shape][rotation_num][2][0] == piece[piece_shape][rotation_num][2][1] == 0:
            left_locations.append(block_9)
        right_locations.append(block_9) #Doesn't work to full capacity
            
def collision_checker(): #Checks for piece collision
    global grid_values
    global block_locations, bottom_locations, left_locations
    global piece, piece_cols, rotation_num, piece_shape
    global block_w, block_h
    global piece_x, piece_y, left_x, right_x, incr_y
    global r, g, b
    global column_vals
    global active_piece
    
    piece_tracking()
    
    #Detects if anything is below the piece (including bottom of grid or another piece)
    for i in range(len(bottom_locations)):
        if bottom_locations[i][1] != 23:
            if grid_values[bottom_locations[i][1] + 1][bottom_locations[i][0]] == 1:
                piece_y = piece_y
                incr_y = 0
                active_piece = 0
                for i in range(len(block_locations)):
                    grid_values[block_locations[i][1]][block_locations[i][0]] = 1
                
    #Checks if anything is on the bottom row of the shape array (if there is a 0 or not). If there is, the piece will adjust to fall further.
    if piece[piece_shape][rotation_num][2][0] == piece[piece_shape][rotation_num][2][1] == piece[piece_shape][rotation_num][2][2] == 0:
        if piece_y >= 680:
            piece_y = 710
            icr_y = 0
            active_piece = 0
            for i in range(len(block_locations)):
                grid_values[block_locations[i][1]][block_locations[i][0]] = 1
    
    #If the bottom row does have a 1, then the piece will collide per usual
    else:
        if piece_y >= 650:
            piece_y = 680
            icr_y = 0
            active_piece = 0
            for i in range(len(block_locations)):
                grid_values[block_locations[i][1]][block_locations[i][0]] = 1
  
def move_piece(): #Moves the piece down on the grid until collision occurs
    global block_locations, bottom_locations
    global piece, piece_cols, rotation_num, piece_shape
    global block_w, block_h
    global piece_x, piece_y, incr_y
    global r, g, b
    global column_vals
    global active_piece
    
    draw_piece()
            
    collision_checker()
    
    piece_y += incr_y
    
def clear_row(): #Clears row if entire row is filled with pieces
    
    global grid_values
    global block_locations, bottom_locations, left_locations
    global score
    
    #Checks if a row is entirely filled or not and then gets rid of it and moves the rows that are above down
    for i in range(24):
        if grid_values[i][0] == grid_values[i][1] == grid_values[i][2] == grid_values[i][3] == grid_values[i][4] == grid_values[i][5] == grid_values[i][6] == grid_values[i][7] == grid_values[i][8] == grid_values[i][9] == 1:
            for j in range(i, -1, -1):
                grid_values[j][0] = grid_values[j-1][0]
                grid_values[j][1] = grid_values[j-1][1]
                grid_values[j][2] = grid_values[j-1][2]
                grid_values[j][3] = grid_values[j-1][3]
                grid_values[j][4] = grid_values[j-1][4]
                grid_values[j][5] = grid_values[j-1][5]
                grid_values[j][6] = grid_values[j-1][6]
                grid_values[j][7] = grid_values[j-1][7]
                grid_values[j][8] = grid_values[j-1][8]
                grid_values[j][9] = grid_values[j-1][9]
            grid_values[0][0] = 0
            grid_values[0][1] = 0
            grid_values[0][2] = 0
            grid_values[0][3] = 0
            grid_values[0][4] = 0
            grid_values[0][5] = 0
            grid_values[0][6] = 0
            grid_values[0][7] = 0
            grid_values[0][8] = 0
            grid_values[0][9] = 0
            
            #Once the row clears, the player receives points
            score += 100
            
def endgame(): #Ends the game once pieces stack above the grid
    global mode
    global grid_values
    global score, totalscores, First, Second, Third, Fourth, Fifth
    global score_append
    
    #Brings up end gamescreen and resets the game once pieces stack above the grid
    for i in range(10):
        if grid_values[0][i] == 1:
            score_append = 1
            
    if score_append == 1:
        #Puts the current score into the leaderboard and sorts in descending order
        totalscores.append(score)
        totalscores.sort(reverse=True)
        First = totalscores[0]
        Second = totalscores[1]
        Third = totalscores[2]
        Fourth = totalscores[3]
        Fifth = totalscores[4]
        score_append = 0
        
        mode = 6

def menu(): #Menu screen
    global mode
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth

    background(0, 0, 0)
    
    #Plays tetris theme music
    ##intro.play()

    #Draws out all the different buttons on the menu screen
    image(back, imageCornerPointX, imageCornerPointY, imageheight, imagewidth)

    stroke(0, 0, 0)
    fill(0, 76, 153)
    rect(startSquareX, startSquareY, squareWidth, squareHeight)
    rect(startSquareX + squareWidth + 50,
         startSquareY, squareWidth, squareHeight)
    rect(startSquareX + squareWidth * 2 + 100,
         startSquareY, squareWidth, squareHeight)

    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 0, 0)
    text("START", 200, 640)
    text("HELP", 400, 640)
    text("HIGH", 600, 620)
    text("SCORE", 600, 660)

    #When mouse hovers over the button, the colour changes
    if mouseX >= 127 and mouseX <= 276:
        if mouseY >= 553 and mouseY <= 703:
            fill(178, 34, 34)
            rect(startSquareX, startSquareY, squareWidth, squareHeight)
            fill(0, 0, 0)
            text("START", 200, 640)
    if mouseX >= 327 and mouseX <= 476:
        if mouseY >= 553 and mouseY <= 703:
            fill(178, 34, 34)
            rect(startSquareX + squareWidth + 50,
                 startSquareY, squareWidth, squareHeight)
            fill(0, 0, 0)
            text("HELP", 400, 640)
    if mouseX >= 527 and mouseX <= 676:
        if mouseY >= 553 and mouseY <= 703:
            fill(178, 34, 34)
            rect(startSquareX + squareWidth * 2 + 100,
                 startSquareY, squareWidth, squareHeight)
            fill(0, 0, 0)
            text("HIGH", 600, 620)
            text("SCORE", 600, 660)

def gamescreen(): #Generates the entire game using the functions created in our code
    global mode
    global blocks
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth
    global board_x, board_y
    global score

    background(0, 76, 153)
    
    #Plays tetris theme music
    ##intro.play()
    
    image(blocks, 525, 175, 180, 500)
    
    fill(0, 0, 0)
    textFont(font, 50)
    text("SCORE: " + str(score), 600, 100)
    
    grid()
    move_piece()
    collision_checker()
    clear_row()
    endgame()
    
def helpscreen(): #Help screen for instructions for game
    global font, arrowcontrols, backarrow, pausekey
    
    background(0, 0, 0)
    
    #Plays Tetris music
    ##intro.play()


    font = createFont("Phosphate", 16, True)
    
    #Generates all the images and instruction labels
    fill(0, 76, 153)
    rect(35, 170, 730, 600)
    fill(255, 255, 255)
    textFont(font, 150)
    textAlign = (CENTER)
    fill(0, 76, 153)
    text("HELP", 400, 130)

    fill(0,0,0)
    textFont(font, 40)
    text("GAME CONTROLS", 400, 500)
    
    image(arrowcontrols, 100, 170, 600, 300)
    textFont(font, 20)
    text("LEFT + RIGHT MOVEMENT", 250, 200)
    text("ROTATE THE PIECE", 560 , 200)
    
    textFont(font, 40)
    image(pausekey, 325, 530, 150, 150)
    text("PRESS 'P' TO PAUSE", 400, 750)

    #Backarrow for if you want to go back to menu screen
    image(backarrow, 0, 0, 40, 40)
    
    #Arrow gets larger if you hover over it
    if mouseX >= 0 and mouseX <= 40:
        if mouseX >= 0 and mouseY <= 40:
            image(backarrow, 0, -5, 50, 50)
            
def leaderboard(): #Screen that shows highscores in descending order
    global minim, intro
    global backarrow
    global score, totalscore, First, Second, Third, Fourth, Fifth
    
    #Plays Tetris music
    #intro.play()
    
    background(0, 0, 0)

    #Generates the first - fifth place labels and their values based on the scores players got
    textFont(font, 110)
    fill(0, 76, 153)
    textAlign = (CENTER)
    text("HIGHSCORES", 400, 100)

    stroke(0, 0, 0)
    rect(80, 150, 650, 600)

    textFont(font, 50)
    fill(0, 0, 0)
    text("POINTS", 400, 200)
    text("1.", 110, 260)
    text(First, 400, 260)
    
    text("2.", 110, 340)
    text(Second, 400, 340)
    
    text("3.", 110, 420)
    text(Third, 400, 420)
    
    text("4.", 110, 500)
    text(Fourth, 400, 500)
    
    text("5.", 110, 580)
    text(Fifth, 400, 580)
    
    #Backarrow for if you want to go back to menu screen
    image(backarrow, 0, 0, 40, 40)

    #Arrow gets larger if you hover over it
    if mouseX >= 0 and mouseX <= 40:
        if mouseX >= 0 and mouseY <= 40:
            image(backarrow, 0, -5, 50, 50)
    
def paused(): #Pause screen if you want to pause the game
    global startRectX, startRectY, rectXShow, rectYShow, rectHeight, rectWidth
    global font

    background(0, 0, 0)
    
    #Plays tetris theme music
    #intro.play()

    font = createFont("Phosphate", 16, True)
    textFont(font, 100)
    textAlign(CENTER)
    fill(0, 76, 153)
    text("PAUSED", 400, 100)

    #Generates all the different buttons 
    stroke(0, 0, 0)
    fill(0, 76, 153)
    rect(rectXShow, rectYShow, rectWidth, rectHeight)
    rect(rectXShow, rectYShow + rectHeight + 100, rectWidth, rectHeight)
    rect(rectXShow, rectYShow + rectHeight * 2 + 200, rectWidth, rectHeight)

    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 0, 0)
    text("RESUME", 400, 290)
    text("HELP", 400, 490)
    text("MAIN", 400, 670)
    text("MENU", 400, 710)
    
    #Changes colour of the button if you hover over it with mouse
    if mouseY >= 225 and mouseY <= 325:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow, rectYShow, rectWidth, rectHeight)
            fill(0, 0, 0)
            text("RESUME", 400, 290)
    if mouseY >= 425 and mouseY <= 525:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow, rectYShow + rectHeight + 100,
                 rectWidth, rectHeight)
            fill(0, 0, 0)
            text("HELP", 400, 490)
    if mouseY >= 625 and mouseY <= 725:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow, rectYShow + rectHeight *
                 2 + 200, rectWidth, rectHeight)
            fill(0, 0, 0)
            text("MAIN", 400, 670)
            text("MENU", 400, 710)
            
def helpscreen2(): #Help screen for when you click it in the pause menu
    global font, arrowcontrols, backarrow, pausekey
    
    #Plays Tetris music
    background(0, 0, 0)
    
    #intro.play()


    font = createFont("Phosphate", 16, True)

    #Generates all the images and instruction labels
    fill(0, 76, 153)
    rect(35, 170, 730, 600)
    fill(255, 255, 255)
    textFont(font, 150)
    textAlign = (CENTER)
    fill(0, 76, 153)
    text("HELP", 400, 130)

    fill(0,0,0)
    textFont(font, 40)
    text("GAME CONTROLS", 400, 500)
    
    image(arrowcontrols, 100, 170, 600, 300)
    textFont(font, 20)
    text("LEFT + RIGHT MOVEMENT", 250, 200)
    text("ROTATE THE PIECE", 560 , 200)
    
    textFont(font, 40)
    image(pausekey, 310, 530, 150, 150)
    text("PRESS 'P' TO PAUSE", 400, 750)

    #Backarrow for if you want to go back to menu screen
    image(backarrow, 0, 0, 40, 40)
    
    #Arrow gets larger if you hover over it
    if mouseX >= 0 and mouseX <= 40:
        if mouseX >= 0 and mouseY <= 40:
            image(backarrow, 0, -5, 50, 50)

def gameover(): #Game over screen
    global startRectX2, startRectY2, rectXShow2, rectYShow2, rectHeight2, rectWidth2
    global font

    background(0, 0, 0)
    
    #Plays Tetris theme music
    #intro.play()

    #Generates the words on the game over screen
    font = createFont("Phosphate", 16, True)
    textFont(font, 100)
    textAlign(CENTER)
    fill(0, 76, 153)
    text("YOU LOST!", 400, 100)
    
    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 76, 153)
    text("YOU SCORED: " + str(score),  400, 200)

    #Generates the buttons for 'RESTART' and 'MAIN MENU'
    stroke(0, 0, 0)
    fill(0, 76, 153)
    rect(rectXShow2, rectYShow2, rectWidth2, rectHeight2)
    rect(rectXShow2, rectYShow2 + rectHeight2 + 100, rectWidth2, rectHeight2)

    textFont(font, 50)
    textAlign(CENTER)
    fill(0, 0, 0)
    text("RESTART", 400, 390)
    text("MAIN", 400, 570)
    text("MENU", 400, 610)

    #Changes colour of button if you hover over it with mouse
    if mouseY >= 325 and mouseY <= 425:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow2, rectYShow2, rectWidth2, rectHeight2)
            fill(0, 0, 0)
            text("RESTART", 400, 390)
    if mouseY >= 525 and mouseY <= 625:
        if mouseX >= 250 and mouseX <= 550:
            fill(178, 34, 34)
            rect(rectXShow2, rectYShow2 + rectHeight2 + 100, rectWidth2, rectHeight2)
            fill(0, 0, 0)
            text("MAIN", 400, 570)
            text("MENU", 400, 610)

def mousePressed(): #All mouse operations within the game
    global mode

    #GAMESCREEN
    if mode == 0:
        #If you click 'START' the game screen will start up
        if mouseX >= 127 and mouseX <= 276:
            if mouseY >= 553 and mouseY <= 703:
                background(0, 0, 0)
                startup()
                mode = 1
        #If you click 'HELP' the help screen will appear
        if mouseX >= 327 and mouseX <= 476:
            if mouseY >= 553 and mouseY <= 703:
                background(0, 0, 0)
                mode = 2
        #If you click 'HIGHSCORES' the leaderboard will appear
        if mouseX >= 527 and mouseX <= 676:
            if mouseY >= 553 and mouseY <= 703:
                background(0, 0, 0)
                mode = 3
    
    #HELPSCREEN
    if mode == 2:
        #If you click the backarrow it brings you back to the main menu
        if mouseX >= 0 and mouseX <= 40:
            if mouseY >= 0 and mouseY <= 40:
                background(0, 0, 0)
                mode = 0
    
    #HIGHSCORES
    if mode == 3:
        #If you click the backarrow it brings you back to the main menu
        if mouseX >= 0 and mouseX <= 40:
            if mouseY >= 0 and mouseY <= 40:
                background(0, 0, 0)
                mode = 0
    
    #PAUSESCREEN
    if mode == 4:
        #If you click 'RESUME' the gamescreen will reappear and you can continue playing
        if mouseX >= 250 and mouseX <= 550:
            if mouseY >= 225 and mouseY <= 325:
                background(0, 0, 0)
                mode = 1
        #If you click 'HELP' the in-game helpscreen will appear
        if mouseX >= 250 and mouseX <= 550:
            if mouseY >= 425 and mouseY <= 525:
                background(0, 0, 0)
                mode = 5
        #If you click 'MAIN MENU' the game will reset and you'll be brought to the main menu screen
        if mouseX >= 250 and mouseX <= 550:
            if mouseY >= 625 and mouseY <= 725:
                background(0, 0, 0)
                mode = 0
                
    #IN-GAME PAUSED HELPSCREEN
    if mode == 5:
        #If you click the backarrow it brings you back to the pause screen
        if mouseX >= 0 and mouseX <= 40:
            if mouseY >= 0 and mouseY <= 40:
                background(0, 0, 0)
                mode = 4
    
    #GAMEOVER SCREEN
    if mode == 6:
        #If you click 'RESTART' the game resets and you'll be playing a new game
        if mouseY >= 325 and mouseY <= 425:
            if mouseX >= 250 and mouseX <= 550:
                background(0, 0, 0)
                startup()
                mode = 1
        #If you click 'MAIN MENU' the game will reset you'll be brought to the main menu screen
        if mouseY >= 525 and mouseY <= 625:
            if mouseX >= 250 and mouseX <= 550:
                background(0, 0, 0)
                mode = 0
                
def keyPressed(): #All keyboard operations within the game
    global mode
    global grid_values
    global block_locations, bottom_locations, left_locations, right_locations
    global piece, piece_cols, rotation_num, piece_shape
    global block_w, block_h
    global piece_x, piece_y, left_x, right_x, incr_y
    global r, g, b
    global column_vals
    global active_piece
    
    #Activates the different rotations of the current falling piece
    if mode == 1:
        # Rotation of pieces
        if keyCode == UP:
            rotation_num = 0
        elif keyCode == DOWN:
            rotation_num = 2
        elif keyCode == RIGHT:
            rotation_num = 1
        elif keyCode == LEFT:
            rotation_num = 3
        
        #Checks if where in the arrary the piece is located, and adjusts the left bound accordingly; if the piece is at the left bound then it can no longer move left
        if piece[piece_shape][rotation_num][0][0] == piece[piece_shape][rotation_num][1][0] == piece[piece_shape][rotation_num][2][0] == 0:
            if piece_x + left_x <= 95:
                piece_x = 95
                left_x = 0
            else:
                left_x = -30
        else:
            if piece_x + left_x <= 125:
                piece_x = 125
                left_x = 0
            else:
                left_x = -30
        
        #Checks if where in the arrary the piece is located, and adjusts the right bound accordingly; if the piece is at the right bound then it can no longer move right          
        if piece[piece_shape][rotation_num][0][2] == piece[piece_shape][rotation_num][1][2] == piece[piece_shape][rotation_num][2][2] == 0:
            if piece_x + right_x >= 365:
                piece_x = 365
                right_x = 0
            else:
                right_x = 30
        else:
            if piece_x + right_x >= 335:
                piece_x = 335
                right_x = 0
            else:
                right_x = 30
        
        #Detects if anything is to the left of the piece, if there is then the piece can't move further left
        for i in range(len(left_locations)):
            if left_locations[i][0] > 0:
                if grid_values[left_locations[i][1]][left_locations[i][0] - 1] == 1:
                    left_x = 0
                    for x_val in column_dict:
                        if column_dict[x_val] == left_locations[i][0]:
                            piece_x = x_val
        
        #Detects if anything is to the right of the piece, if there is then the piece can't move further right
        for i in range(len(right_locations)):
            if right_locations[i][0] < 9:
                if grid_values[right_locations[i][1]][right_locations[i][0] + 1] == 1:
                    right_x = 0
                    for x_val in column_dict:
                        if column_dict[x_val] == right_locations[i][0]:
                            piece_x = x_val - 60
                    
        #Left movement of piece
        if (key == "A" or key == "a"):
            piece_x += left_x
        #Right movement of piece
        elif (key == "D" or key == "d"):
            piece_x += right_x
    
        #Activates pause screen
        if (key == 'P' or key == 'p'):
            background(0, 0, 0)
            mode = 4
    
def draw(): #Activates the screens depending upon the mode
    global mode
    global imageheight, imagewidth, imageCornerPointX, imageCornerPointY
    global canvasX, canvasY, back, font
    global numSquares, startSquareX, startSquareY, squareHeight, squareWidth

    if mode == 0:
        menu()
        
    elif mode == 1:
        gamescreen()
        
    elif mode == 2:
        helpscreen()

    elif mode == 3:
        leaderboard()

    elif mode == 4:
        paused()
    
    elif mode == 5:
        helpscreen2()
        
    elif mode == 6:
        gameover()
