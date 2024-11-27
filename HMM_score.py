class HMM_user:
    def __init__(self, name, win, loss):
        self.name = name
        self.win = win
        self.loss = loss

def score(winner, loser):
    with open('Score.txt', "a", encoding='utf-8') as file:
        file.write(winner + ";" + loser + "\n")

def scoreRead():
    with open('Score.txt', "r", encoding='utf-8') as file:
        for row in file:
            data = row.strip().split(';')
            return data

losses = 0
wins = 0

def HMM_scorecount(name):
    global losses
    global wins
    data = scoreRead()
    for i in range(len(data)):
        if i % 2 == 0 and data[i] == name:
            losses += 1
        elif i % 2 == 1 and data[i] == name:
            wins += 1
    u = HMM_user(name, wins, losses)
    return u