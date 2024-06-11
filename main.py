"""
Made to stop roblox from marking you as AFK and disconnecting you.
This work is subject to the GNU General Public License v3.0
Source: github.com/Gulmul/fightingRobloxAFKchecks
"""
from random import randint
from time import sleep
from keyboard import press, release


def robloxInactivityStop(interval, inputs):
    for i in range(10):
        print(f"Starting in {10-i} ")
        sleep(1)
    print("Starting macro ")
    while True:
        toPress = inputs[randint(0, (len(inputs) - 1))]
        print(f"toPress= \'{toPress}\',  ", end="")
        press(toPress)
        print(f"pressing \'{toPress}\',  ", end="")
        sleep(randint(1, 4))
        release(toPress)
        print(f"released \'{toPress}\n")
        for i in range(interval):
            sleep(60)
            print(f"{(interval - (i+1))} minutes left. ")
        # sleep((float(interval) * 60))


def main():
    robloxInactivityStop(interval=int(input("Interval between each keypress (minutes): ")), inputs=["w", "a", "s", "d"])
# You can change the possible keys by changing the "inputs" list.


if __name__ == "__main__":
    main()
