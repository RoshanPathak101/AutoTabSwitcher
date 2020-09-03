import webbrowser
import keyboard
import random
import time

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

chrome = webbrowser.get('chrome')

links = input("enter links ex: google.com,jio.com,fb.com\n").split(",")
interval = int(input("Enter interval of switching tabs in (Seconds)\n"))
print(links)
for i in links:
	chrome.open(i,new=1)
while True:
	x = random.randrange(1,len(links)+1)
	for i in range(0,x):
		keyboard.press_and_release('ctrl + tab')
	time.sleep(interval) 


