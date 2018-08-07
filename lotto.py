#lotto
print ('請猜一個數字1~100之間')
import random

r = random.randint(1, 100)
r = int(r)
while True:
	y = input ('請猜一個數字：')
	y = int(y)
	if r == y:
		print ('答對了')
		break
	elif r > y:
		print ('猜太小了')
	elif r < y:
		print ('猜太大嚕')