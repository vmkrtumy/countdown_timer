import time

def countdown(t):
	while t:
		mins, sec = divmod(t, 60)
		hours, mins = divmod(mins, 60)
		timer = "{:02d}:{:02d}:{:02d}".format(hours, mins, sec)
		print(timer)
		time.sleep(1)
		t -= 1
try:
	t1 = input("Insert time to countdown (h:m:s): ").split(':')
	if len(t1) != 3:
		raise ValueError("Invalid input format. Please use h:m:s format.")
	t = (int(t1[0])*3600) + (int(t1[1]))*60 + int(t1[2])
	countdown(t)
except ValueError as e:
	print(e)
