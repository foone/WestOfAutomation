import win32gui,pyautogui,time,itertools

# Go to the lost dutch oven mine
# position yourself between the button to spawn drones
# and the drones platform

# Find the window and get its position, so we can move the mouse relative to it
hwnd = win32gui.FindWindowEx(0,0,None,'West of Loathing')
wx,wy,_,_ = win32gui.GetWindowRect(hwnd)

# A push a button for a given number of a seconds, then release it
def pressFor(key, duration):
	pyautogui.keyDown(key)
	time.sleep(duration)
	pyautogui.keyUp(key)

# A helper function to move the mouse relative to the window
def winCursor(x,y):
	pyautogui.moveTo(wx+x,wy+y)

## Give the user time to click on the West of Loathing window after running this
time.sleep(5)

for runi in itertools.count(1):
	print 'Run {}'.format(runi)

	pressFor('left', 1.1)
	pyautogui.press(['3']) # push 3 to fight 5 enemies
	pressFor('right', 1.0)
	pyautogui.press('e') # push e to say you want to fight 'em'

	time.sleep(1.7) # wait for the battle to load
	winCursor(817,624) # move the mouse over the Rain of Teeth spell
	pyautogui.click() # Click it

	# Keep whacking Space to attack and have Gary attack, until we have definitely won
	for i in range(10): 
		if i>0: # After the first time, wait a half-second between presses
			time.sleep(0.5)
		pyautogui.press('space')
	
	time.sleep(0.1) # wait for the battle to end
	pyautogui.press('1') # press 1 to end the loot screen

