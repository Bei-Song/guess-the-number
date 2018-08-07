#lotto
print ('請猜一個數字1~100之間')
import random
count = 0
r = random.randint(1, 100)
while True:
	y = input ('請猜一個數字：')
	y = int(y)
	count = count + 1
	if r == y:
		print ('答對了')
		print ('您總共猜了' ,count, '次')
		break
	elif r > y:
		print ('猜太小了')
	elif r < y:
		print ('猜太大嚕')
	print ('您總共猜了' ,count, '次')
