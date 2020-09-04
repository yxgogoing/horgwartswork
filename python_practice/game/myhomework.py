""""
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""


# def game():
#     my_hp = 1000
#     my_power = 200
#     your_hp = 1000
#     your_power = 199
def fight():
    my_hp = 1000
    my_power = 3000
    your_hp = 2000
    your_power = 100
    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        print(my_hp)
        print(your_hp)
        if my_hp <= 0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break


fight()