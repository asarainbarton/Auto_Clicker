import pyautogui as pag
from collections import deque
from pynput.keyboard import Listener
import csv

def getCoordinates(coord_file):
   with open(coord_file, 'r') as file:
      reader = csv.reader(file, delimiter=',')
      coordinates = deque([tuple(map(int, row)) for row in reader])

   return coordinates


coordinates = getCoordinates("locations.csv")


def on_press(key):
   if key.shift and coordinates:
      pag.moveTo(coordinates.popleft())
      pag.click()

      if not coordinates:
         exit(0)


def main():
   with Listener(on_press=on_press) as listener:
      listener.join()


main()
   


