# My Project

Substitutes manually using a computer mouse with predetermined auto-clicking. Perfect for performing repetitive mundane tasks, enrolling in courses as quickly as possible, or whatever else you could possibly think of.

## Installation

Built to run on macOS. May or may not work on other operating systems. 
Just make sure you have the following installed:

**pip install pyautogui**
**pip install pynput**

Also make sure that your system's privacy/security settings allow for automated clicks. Otherwise, this program will not work. 
To do so on macOS, go to *System Settings -> Privacy & Security -> Accessibility* and then check off whatever application you plan to run this on.

## Usage

**Initial Mapping:**

Start by figuring out the pixel coordinate locations of each of the clicks you plan to make on your computer. Do this by running *python3 mouse_location.py* to perform an initial walkthrough. Whenever you're about to click, hover your mouse over that location and press **Shift** to store those coordinates. Keep doing this until you have gone through all of your pre-planned clicks. Then tap 'q' on your keyboard anywhere you want to quit the process. This location data will automatically get stored in *locations.csv*. Note that if you run this file again, the previous csv data will get overwritten.

***

**Execution:**

Start by making sure that you are where you need to be on your computer before proceeding. Run *python3 clicker.py* to begin execution.
Next, go back to the interface where you will perform your clicks. Make sure there are no obstructions from other windows. Now just hit **shift** every time you want to advance to the next click! This process will end on its own once you've gone through all your clicks.

## Author

Asa Barton
