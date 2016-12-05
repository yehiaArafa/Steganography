#!usr/bin/env python
import numpy as np
from PIL import Image
from threading import Thread
import sys


def main():
	if len(sys.argv)<2:
		print("Missing arguments")
		sys.exit()
	elif len(sys.argv)>2:
		print("Too many arguments")
		sys.exit()
	
	messageIm=Image.open(sys.argv[1])
	secretMessageIm=Image.new('RGB',messageIm.size)

	temp1=messageIm.getdata() #####
			
	numThread=4
	sectionY=messageIm.size[1]/numThread

	threadPool=[]

	for i in range(numThread):
		
		if i==0:
			startY=1
		else:
			startY=(sectionY*i)-2
		
		endY=(sectionY*i)+sectionY
		
		if i==(numThread-1) and endY!=messageIm.size[1]:
			endY=messageIm.size[1]	

		thread = Thread(target=findMessage, args=(i,startY,endY,messageIm,secretMessageIm))	
		thread.start()
		threadPool.append(thread)

	for t in threadPool:
		t.join()

	secretMessageIm.save("secretMessage.png")	
 
	print("The secret message image is now ready")
	
		
def findMessage(threadId,startY,endY,messageIm,secretMessageIm):
	
	for x in range(1,messageIm.size[0]-1):
			for y in range(startY,endY-1):
				
				originalMessagePix = messageIm.getpixel((x,y))
				
				if (originalMessagePix[0]%2==0): #black
					secretMessageIm.putpixel((x,y),(0,0,0))
					
				else: #white
					secretMessageIm.putpixel((x,y),(255,255,255))
					
if __name__=="__main__":
	main()	