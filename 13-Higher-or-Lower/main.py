# import game logo
# use random
# import vs logo
# use random
# ask user to choose who has more followers a or b
# if a follower > b follower or b > a --> score++
# 'b' in the previous comparison will be 'a' in the next comparison
# if not --> end the game with the final score

import art
import game_data
import random
                          #first way to create this project#



print(art.logo)
ans = True
score = 0
A = random.choice(game_data.data)
print(f"compare A: {A["name"]} , {A["description"]} , {A["country"]}")
while ans:

    print(art.vs)

    B = random.choice(game_data.data)
    print(f"against B: {B["name"]} , {B["description"]} , {B["country"]}")

    user_ans = input("Who has more followers? Type 'A' or 'B': ")

    if A["follower_count"] > B["follower_count"] and user_ans == 'A':
        score +=1
    elif A["follower_count"] < B["follower_count"] and user_ans == 'B':
        score +=1
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"sorry you lose , final score:{score}")
        break

    print(f"the score is {score}")
    A = B
    print(f"compare A: {A["name"]} , {A["description"]} , {A["country"]}")




                         #second way to create this project#



















