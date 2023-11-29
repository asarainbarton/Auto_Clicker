from pynput.keyboard import Key, Listener
import pyautogui, csv

coords = []
filename = "locations.csv"

def write_data_to_csv(the_file):
    with open(the_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        for i in range(len(coords)):
            writer.writerow([coords[i][0], coords[i][1]])
    

def on_press(key):
    try:
        if key.shift:
            coords.append(pyautogui.position())
    except AttributeError: # Press q on keyboard anywhere on screen and program will properly exit
        write_data_to_csv(filename)
        exit(0)
        


def main():
    with Listener(on_press=on_press) as listener:
        listener.join()
  
main()