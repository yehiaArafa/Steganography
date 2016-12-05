#!usr/bin/env python
from PIL import Image
from threading import Thread
import sys


def main():
	if len(sys.argv)<3:
		print("Missing arguments")
		sys.exit()
	elif len(sys.argv)>3:
		print("Too many arguments")
		sys.exit()
	
	originalIm=Image.open(sys.argv[1])

	temp1=originalIm.getdata() #####
	
	secretIm=Image.open(sys.argv[2]).convert('1')
	
	temp2=secretIm.getdata() #####
		
	numThread=4
	sectionY=originalIm.size[1]/numThread

	threadPool=[]

	for i in range(numThread):
		
		if i==0:
			startY=1
		else:
			startY=(sectionY*i)-2
		
		endY=(sectionY*i)+sectionY
		
		if i==(numThread-1) and endY!=originalIm.size[1]:
			endY=originalIm.size[1]	

		thread = Thread(target=hideMessage, args=(i,startY,endY,originalIm,secretIm))	
		thread.start()
		threadPool.append(thread)

	for t in threadPool:
		t.join()

	originalIm.save("message.png")	
 
	print("The message image is now ready")
	
		
def hideMessage(threadId,startY,endY,originalIm,secretIm):
	
	for x in range(1,originalIm.size[0]-1):
			for y in range(startY,endY-1):
				
				secretPix = secretIm.getpixel((x,y))
				originalPix = originalIm.getpixel((x,y))
				
				if secretPix==255: #white
					if (originalPix[0]%2 == 0): #must be odd
						originalIm.putpixel((x,y),(originalPix[0]+1,originalPix[1],originalPix[2]))
					else:
						originalIm.putpixel((x,y),(originalPix[0],originalPix[1],originalPix[2]))
				else: #black
					if (originalPix[0]%2!=0): #must be even
						originalIm.putpixel((x,y),(originalPix[0]-1,originalPix[1],originalPix[2]))
					else:
						originalIm.putpixel((x,y),(originalPix[0],originalPix[1],originalPix[2]))


if __name__=="__main__":
	main()	