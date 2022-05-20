import argparse
import random
import pyautogui as gui

gui.PAUSE = 2.5
gui.FAILSAFE = True

parser = argparse.ArgumentParser()
parser.add_argument("--time_wait", help="The amount of time to wait between clicks in seconds", type=int, nargs="?", const=20)
parser.add_argument("--num_clicks", help="The number of positions the program will click", type=int, nargs="?", const=3)

args = parser.parse_args()

def main(args):
  print("Hello World!")
    

if __name__ == "__main__":
    main(args)