import random
import os

def game():
    print("You are playing the game...")
    score = random.randint(10,62)
    print(f"Your Score is {score}")

    if not os.path.exists("./09 Practice Set./score.txt"):
        with open("./09 Practice Set./score.txt", "w") as f:
            f.write("0")

    with open("./09 Practice Set./score.txt", 'r+') as f:
        p_score = f.read().strip()
        p_score = int(p_score) if p_score else 0
 
        if (p_score < score):
            f.seek(0)
            f.write(str(score))
            print(f"🎉 New High Score: {score}")
        else:
            print(f"💡 Current High Score remains: {p_score}")

    return score

game()