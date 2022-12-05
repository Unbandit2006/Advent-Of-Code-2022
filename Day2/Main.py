# def choosen_card(hand, player:bool=True):
#     card_value = 0

#     if player == True:
#         if hand.lower() == "x": #Rock
#             card_value = 1
        
#         elif hand.lower() == "y": #Paper
#             card_value = 2
        
#         elif hand.lower() == "z": #Scissors
#             card_value = 3
        
#     else:
#         if hand.lower() == "a":
#             card_value = 1
        
#         elif hand.lower() == "b":
#             card_value = 2
        
#         elif hand.lower() == "c":
#             card_value = 3        
    
    # return card_value

def win_or_lose(result, hand2):
    result_val = 0

    result = result.lower()
    hand2 = hand2.lower()

    match result:
        case "x": # Lose
            if hand2 == "a": # Rock
                result_val = 3 + 0
            
            elif hand2 == "b": # Paper
                result_val = 1 + 0
            
            elif hand2 == "c": # Scissors
                result_val = 2 + 0
        
        case "y": # Draw
            if hand2 == "a": # Rock
                result_val = 1 + 3
            
            elif hand2 == "b": # Paper
                result_val = 2 + 3
            
            elif hand2 == "c": # Scissors
                result_val = 3 + 3        

        case "z": # Win
            if hand2 == "a": # Rock
                result_val = 2 + 6
            
            elif hand2 == "b": # Paper
                result_val = 3 + 6
            
            elif hand2 == "c": # Scissors
                result_val = 1 + 6
    
    return result_val

score = 0
with open("Day2.txt") as f:
    for line in f.readlines():
        round_score = 0

        opponent_hand = line.split(" ")[0]
        your_hand = line.split(" ")[1].strip()

        # round_score += choosen_card(your_hand)
        round_score += win_or_lose(your_hand, opponent_hand)
    
        score += round_score
    
print(score)

