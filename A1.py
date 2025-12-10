import random

def pick_ball_experiment():
    #defining our balls as lists
    balls = ['Blue', 'Red', 'Green']

    # flipping coins randomly
    result = random.choice(balls)

    # finding the probability
    pro = balls.count('Red')/len(balls)
    print("Probability of picking the Red Ball is: ", pro)

    # checking if the red ball was picked 
    if result == 'Red':
        return 'Red Ball was Picked'
    else:
        return 'Better luck Next Time'
    
res = pick_ball_experiment()
print(res)