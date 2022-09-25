import cv2
import numpy as np


class maskImage():    
    val=2
    thickness=2
    drawing=False
    img=np.zeros((0))
    mask=np.zeros((0))
    values = [
    	("Definite Background", cv2.GC_BGD,(0,0,0)),
    	("Probable Background", cv2.GC_PR_BGD,(0,0,255)),
    	("Definite Foreground", cv2.GC_FGD,(255,255,255)),
    	("Probable Foreground", cv2.GC_PR_FGD,(255,0,0))
	]
    
    def onmouse(self, event,x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDOWN:
            self.drawing=True
        elif event==cv2.EVENT_LBUTTONUP:
            self.drawing=False
        elif event==cv2.EVENT_MOUSEMOVE and self.drawing:
            res=cv2.circle(self.img,(x,y),self.thickness,self.values[self.val+1][2],-1)
            res=cv2.circle(self.mask,(x,y),self.thickness,self.values[self.val][2],-1)
            
    def process(self, inPath,outPath,thickness=2):
        image=cv2.imread(inPath)
        self.img=image.copy()
        self.mask=np.zeros(image.shape[:2],dtype="uint8")
        self.thickness=thickness
        cv2.namedWindow("Image")
        cv2.namedWindow("Mask")
        cv2.setMouseCallback("Image",self.onmouse)
        print("Press 2 to include in mask")
        print("Press 0 to exclude from mask")
        print("Press n to check results")
        print("Press s to save the mask")
        print("Press q to quit")
        while True:
            cv2.imshow("Image",self.img)
            cv2.imshow("Mask",self.mask)
            key=cv2.waitKey(1) & 0xFF
            if key==ord('q'):
                break
            elif key==ord("0") or key==ord("1"):
                # exclude
                self.val=0
            elif key==ord("2") or key==ord("3"):
                # include
                self.val=2
            elif key==ord("r"):
                # reset
                self.img=image.copy()
                self.mask=np.zeros(image.shape[:2],dtype="uint8")
                self.drawing=False
                self.val=2
            elif key==ord("n"):
                # result
                inv_mask=cv2.bitwise_not(self.mask)
                self.img=cv2.bitwise_and(image,image,mask=inv_mask)
            elif key==ord("s"):
                cv2.imwrite(outPath, self.mask)
        cv2.destroyAllWindows()
