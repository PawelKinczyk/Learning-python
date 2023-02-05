import pyautogui, time

# Basics get screen size

wh = pyautogui.size() # Obtain the screen resolution.
wh
wh[0]
wh.width

# Simple mouse move

for i in range(5): # Move mouse in a square.
       pyautogui.moveTo(100, 100, duration=0.5)
       pyautogui.moveTo(200, 100, duration=0.25)
       pyautogui.moveTo(200, 200, duration=1)
       pyautogui.moveTo(100, 200, duration=0.25)

# Get mouse position

pyautogui.position() # Get current mouse position.
pyautogui.position() # Get current mouse position again.
p = pyautogui.position() # And again.
Point(x=1536, y=637)
p[0] # The x-coordinate is at index 0.
p.x # The x-coordinate is also in the x attribute.

# Mouse clicking

pyautogui.click(10,5) # mouse down & up left button
pyautogui.mouseDown() # left mouse button click
pyautogui.mouseUp() # oposit to previous 
pyautogui.rightClick() # right mouse button click
pyautogui.middleClick() # middle button
pyautogui.click('submit.png') # image click

# Drag and drop

time.sleep(5)
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)   # Move down.
pyautogui.click()    # Click to make the window active.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.

# Mouse scroll

pyautogui.scroll(200)

# Get mouse movement

pyautogui.mouseInfo()
pyautogui.pixel((0, 0)) # Pixel color
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))

# Get screeenshot

im = pyautogui.screenshot()

# Image recognition
## One image
b = pyautogui.locateOnScreen('Zrzut ekranu 2023-02-04 202702.png')
b
## Many images
list(pyautogui.locateAllOnScreen('Zrzut ekranu 2023-02-04 203319.png', confidence=0.9))

# Remember about try / exception

try:
    location = pyautogui.locateOnScreen('submit.png')
except:
    print('Image could not be found.')

# Get screen info

fw = pyautogui.getActiveWindow()
fw
str(fw)
fw.title
fw.size
fw.left, fw.top, fw.right, fw.bottom
fw.topleft
fw.area
pyautogui.click(fw.left + 10, fw.top + 20)

# More options for windows

pyautogui.getAllWindows() # return list of all windows
pyautogui.getWindowsAt(x, y) # return list of every visible windows in x,y
pyautogui.getWindowsWithTitle(title) # returns all visible windows with title
pyautogui.getActiveWindow() # return window with keyboard focus
pyautogui.getAllTitles() # return titles of all widows

# Manipulating window

fw = pyautogui.getActiveWindow()
fw.width # Gets the current width of the window.
fw.topleft # Gets the current position of the window.
fw.width = 1000 # Resizes the width.
fw.topleft = (800, 400) # Moves the window.

## Get info /change status

fw = pyautogui.getActiveWindow()
fw.isMaximized # Returns True if window is maximized.
fw.isMinimized # Returns True if window is minimized.
fw.isActive # Returns True if window is the active window.
fw.maximize() # Maximizes the window.
fw.isMaximized
fw.restore() # Undoes a minimize/maximize action.
fw.minimize() # Minimizes the window.
# Wait 5 seconds while you activate a different window:
time.sleep(5); fw.activate()
fw.close() # This will close the window you're typing in.

# Keyboard control

pyautogui.click(100, 200); pyautogui.write('Hello, world!')

## Key names use as string
pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

## Pressing and realeasing keyboard
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

## Hotkey combination
pyautogui.hotkey('ctrl', 'c')

# Prompt in 

pyautogui.alert('This is a message.', 'Important')
pyautogui.confirm('Do you want to continue?') # Click Cancel
pyautogui.prompt("What is your cat's name?")
pyautogui.password('What is the password?')
