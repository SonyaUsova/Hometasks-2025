import random

def dice_game():

    cube = random.randint(1, 6)
    print(f"Выпало: {cube}")
    if cube in [5, 6]:
        print("Вы победили")
    elif cube in [1, 2]:
        print("Вы проиграли")
    else:
        dice_game()

if __name__ == "__main__":
    dice_game()
