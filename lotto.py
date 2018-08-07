#lotto
start = input('請決定一個開始數值')
end = input('請決定一個結束數值')
start = int(start)
end = int(end)
import random
count = 0
r = random.randint(start, end)
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
