from urllib import request
import time
import os
import ctypes
import pygame
while True:
	try:
		r=request.urlopen("http://api.itmojun.com/pc/cmd/get?id=dengjun").read()
		#将byte类型数据转换为str类型
		msg=r.decode("gbk")
		#如果接受到一条消息，msg将不是空字符串，否则为空字符串
		if msg !="":
			print(msg)
			if "亚索" in msg:
				os.system("taskkill -f -in chrome.exe")
			elif '播放' in msg:
				pygame.mixer.music.load(r" D:\dj.mp3")
				pygame.mixer.music.play()
			elif '暂停' in msg:
				pygame.mixer.music.pause()
			elif '继续' in msg:
				pygame.mixer.music.unpause()
			elif '停止' in msg:
				pygame.mixer.music.stop()
			time.sleep(3)#休眠三秒，避免接受到重复的消息，因为微信端发送的每条消息都会在服务器上暂停3秒
		else:
			time.sleep(1)
	#except Exception as e:
		#print(e)
	except:#捕获处理TRY块代码产生的任何异常
		# pass  #空语句，啥也不干，为了满足python语法规则
		time.sleep(1)


