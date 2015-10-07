# implementation of card game - Memory

import simplegui
import random



#global variables
num_cards = 16
l1 = range(num_cards//2)
l2 = range(num_cards//2)
full_list = l1 + l2



# helper function to initialize globals
def new_game():
    global exposed, state, index_exposed_card1, index_exposed_card2, turn_counter
    random.shuffle(full_list)      
    exposed = [False for x in full_list] 
    index_exposed_card1 = -1
    index_exposed_card2 = -1
    state = 0
    turn_counter = 0
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,index_exposed_card1,turn_counter, label,index_exposed_card2
    
    int_x_pos = pos[0]//50
                 
    if not exposed[int_x_pos]:       
        exposed[int_x_pos] = True
        if state == 0:          
            state = 1
            turn_counter += 1  
        elif state == 1:              
            state = 2
        else:
            if full_list[index_exposed_card1] != full_list[index_exposed_card2]:
                exposed[index_exposed_card1] = False
                exposed[index_exposed_card2] = False
            state = 1
            turn_counter += 1

        index_exposed_card1 = index_exposed_card2
        index_exposed_card2 = int_x_pos

        
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global index_exposed_card1 , index_exposed_card2, turn_counter
    card_counter = 0
    for card in full_list:
        if exposed[card_counter]:
            canvas.draw_text(str(card),[card_counter * 50,100],100,"White")
        else:
            canvas.draw_polygon([[card_counter * 50,0],[(card_counter + 1) * 50,0], [(card_counter + 1) * 50, 100], [card_counter * 50, 100]],2,"Black","Green")
        card_counter += 1
        
    label.set_text("Turns = " + str(turn_counter))   

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
