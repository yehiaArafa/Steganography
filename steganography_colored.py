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
	
	secretIm=Image.open(sys.argv[2]).convert('P')
	
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

	originalIm.save("stego.png")	
 
	print("The stego image is now ready")
	
		
def hideMessage(threadId,startY,endY,originalIm,secretIm):
	
	for x in range(1,originalIm.size[0]-1):
			for y in range(startY,endY-1):
				
				originalPix = originalIm.getpixel((x,y))
				secretPix = secretIm.getpixel((x,y))

				secretPixBinary=list('{0:08b}'.format(secretPix))

				originalPixBinary_RED=list('{0:08b}'.format(originalPix[0]))
				originalPixBinary_Green=list('{0:08b}'.format(originalPix[1]))
				originalPixBinary_Blue=list('{0:08b}'.format(originalPix[2]))

				originalPixBinary_RED[7]  =secretPixBinary[0]
				originalPixBinary_Green[6]=secretPixBinary[1]
				originalPixBinary_Green[7]=secretPixBinary[2]
				originalPixBinary_Blue[5] =secretPixBinary[3]
				originalPixBinary_Blue[6] =secretPixBinary[4]
				originalPixBinary_Blue[7] =secretPixBinary[5]

				temp1=''.join(originalPixBinary_RED)
				RedPixels=int(temp1,2)
				
				temp2=''.join(originalPixBinary_Green)
				GreenPixels=int(temp2,2)
				
				temp3=''.join(originalPixBinary_Blue)
				BluePixels=int(temp3,2)

				originalIm.putpixel((x,y),(RedPixels,GreenPixels,BluePixels))
												

if __name__=="__main__":
	main()	