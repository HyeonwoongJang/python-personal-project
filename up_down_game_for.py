import random

def up_down_game():

    records = []
    
    for search_num in range(1,10000):
            print('---------------------------------------')
            print('Up & Down 게임을 시작합니다.')
            print('1~100 사이의 숫자를 입력하세요.')
            rn = random.randint(1, 100)
            tries = 0
            for search_num in range(1,10000):
                try :
                    print('---------------------------------------')
                    input_num = int(input('숫자를 입력하세요 : '))
                    tries += 1
                    records.append(tries)
                    max_record = max(records)
                    if (0 > input_num or 100 < input_num):
                        print('1~100 사이의 숫자를 입력하세요')
                    elif (search_num <= input_num < rn):
                        print('UP')
                    elif (input_num > rn >= search_num or search_num >= input_num > rn):
                        print('DOWN')
                    elif (input_num == rn <= search_num or input_num == rn >= search_num):
                        print(tries, '번째 시도에 맞혔습니다.')
                        records.append(tries)
                        break 
                except ValueError:
                    print('정수로 입력해주세요.')
            restart = str(input('한 판 더? (Y/N) '))
            if restart.upper() == 'Y' :
                continue
            else :
                print('---------------------------------------')
                print(f'최고 시도 횟수 : {max_record}번')
                print('Up & Down 게임을 종료합니다.')
                break

up_down_game()
