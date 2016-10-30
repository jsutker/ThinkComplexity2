import random
class Spiteful():
    ''' Spiteful will do the opposite of its opponent's last move. '''
    def step(self, history, round):
        if round == 0:
            action = random.randint(0, 1)
        else:
            action = history[self.order^1][round - 1]^1
        return action

