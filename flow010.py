# Created by rashed at 3/4/20
# URL: https://www.codechef.com/problems/FLOW010

for test_case in range(int(input())):
    ship = input()

    if ship.lower() == "b":
        print("BattleShip")
    elif ship.lower() == "c":
        print("Cruiser")
    elif ship.lower() == "d":
        print("Destroyer")
    elif ship.lower() == "f":
        print("Frigate")

