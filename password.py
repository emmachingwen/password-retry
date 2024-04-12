support = input('今天有沒有人去支援?')

if support =='沒有':
	print('太讚啦!')

elif support =='有':
	number = input('去幾位?')
	number = int(number)
	if number >= 2:
		print('今日人力緊缺')
	elif number == 1:
		print('還撐得下去')
	elif number == 0:
		print('太讚啦!')
else:
	print('只能輸入有/沒有')

