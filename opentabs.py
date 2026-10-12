import time
import webbrowser


url = input("Website URL: ").strip()
count = int(input("How many tabs should be opened? "))
delay = float(input("Delay between tabs in seconds: "))

for _ in range(count):
	webbrowser.open_new_tab(url)
	time.sleep(delay)

