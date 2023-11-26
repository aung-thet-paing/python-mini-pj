import time
import pyautogui
import tkinter as tk
import os

def screenshot():
	root.withdraw()
	name = int(round(time.time()) * 1000)
	fileName = "screenshot/{}.png".format(name)
	time.sleep(3)
	img = pyautogui.screenshot(fileName)
	img.show()
	root.deiconify() 

def quit():
	root.quit()

os.makedirs("screenshot", exist_ok = True)

root = tk.Tk()
root.title("Screenshot Application")
frame = tk.Frame(root, bg="lightblue", padx = 10, pady =10)
frame.pack()

button = tk.Button(
		frame,
		text = "Take a screenshot",
		command = screenshot)
button.pack(side = tk.LEFT)

close = tk.Button(
		frame,
		text = "Quit",
		command = quit)
close.pack(side = tk.RIGHT)

root.mainloop()



