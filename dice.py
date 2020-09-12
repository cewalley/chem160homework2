from random import choices
player1wins=0
ntrials=15000
roll_dice=[1,2,3,4,5,6]

for i in range(ntrials):
    player2=[]
    player2=choices(roll_dice,weights=None,k=2)
    if player2[0]==player2[1]:
        continue
    player1=[]
    player1=choices(roll_dice,weights=None,k=3)
    player1.sort(reverse=True)
    if player1[0]+player1[1] > player2[0]+player2[1]:
        player1wins=player1wins+1

ratio=player1wins/ntrials
print(ratio)
