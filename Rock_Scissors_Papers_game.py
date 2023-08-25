import random

rsp = ['Rock','Scissors','Paper']

draws = 0
wins = 0
loses = 0

while True:
    computer_pick = random.choice(rsp)
    print(computer_pick)

    player_pick = input('Rock Scissors Paper 중 하나를 선택하세요. ')

    if player_pick not in rsp:
        print('잘못 내셨습니다.')
        continue

    if computer_pick == player_pick :
        draws += 1
        print('비겼습니다.')
    elif (computer_pick == 'Scissors' and player_pick == 'Rock') or (computer_pick == 'Rock' and player_pick == 'Paper') or (computer_pick == 'Paper' and player_pick == 'Scissors'):
        wins += 1
        print('YOU WIN')
    else:
        loses += 1
        print('YOU LOSE')
    restart = input('한 판 더? (Y/N) ')
    if restart.upper() == 'Y':
        continue
    else:
        print(f"{wins}승 {draws}무 {loses}패")
        break
