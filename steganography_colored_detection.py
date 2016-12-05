#!usr/bin/env python
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
	
	stegoIm=Image.open(sys.argv[1])
	secretMessageIm=Image.new('RGB',stegoIm.size)

	temp1=stegoIm.getdata() #####
		
	numThread=4
	sectionY=stegoIm.size[1]/numThread

	threadPool=[]

	for i in range(numThread):
		
		if i==0:
			startY=1
		else:
			startY=(sectionY*i)-2
		
		endY=(sectionY*i)+sectionY
		
		if i==(numThread-1) and endY!=stegoIm.size[1]:
			endY=stegoIm.size[1]	

		thread = Thread(target=findMessage, args=(i,startY,endY,stegoIm,secretMessageIm))	
		thread.start()
		threadPool.append(thread)

	for t in threadPool:
		t.join()

	secretMessageIm.save("coloredSecretMessage.png")	
 
	print("The colored secret image is now ready")
	
		
def findMessage(threadId,startY,endY,stegoIm,secretMessageIm):
	
	for x in range(1,stegoIm.size[0]-1):
			for y in range(startY,endY-1):
				
				stegoPix = stegoIm.getpixel((x,y))
				secretPixBinary=list('{0:08b}'.format(0))

				stegoPixBinary_RED=list('{0:08b}'.format(stegoPix[0]))
				stegoPixBinary_Green=list('{0:08b}'.format(stegoPix[1]))
				stegoPixBinary_Blue=list('{0:08b}'.format(stegoPix[2]))

				secretPixBinary[0] = stegoPixBinary_RED[7]  
				secretPixBinary[1] = stegoPixBinary_Green[6]
				secretPixBinary[2] = stegoPixBinary_Green[7]
				secretPixBinary[3] = stegoPixBinary_Blue[5] 
				secretPixBinary[4] = stegoPixBinary_Blue[6] 
				secretPixBinary[5] = stegoPixBinary_Blue[7]
				secretPixBinary[6] = '0'
				secretPixBinary[7] = '0'

				temp1=''.join(secretPixBinary)
				secretPixels=int(temp1,2)
				
				secretMessageIm.putpixel((x,y),(secretPixels))
												

if __name__=="__main__":
	main()	
