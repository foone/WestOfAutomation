import pyautogui,time,itertools

# Go to Equipment Fabrication inside Curious Abandoned Well
# Stand in front of the machine
# This will convert unsellable El Vibrato Scrap into Broaches.

def pressFor(key, duration):
	pyautogui.keyDown(key)
	time.sleep(duration)
	pyautogui.keyUp(key)


time.sleep(2)
for runi in itertools.count(1):
	print 'Run {}'.format(runi)
	pressFor('down', 0.1)
	pressFor('up', 0.15)
	pyautogui.press('2', interval=0.01)
	pyautogui.press('space', interval=0.01)
