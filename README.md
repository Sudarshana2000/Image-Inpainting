# Image-Inpainting

Image inpainting is a form of image conservation and image restoration, that allows us to:

- restore old, degraded photos
- repair photos with missing areas due to damage and aging
- mask out and remove particular objects from an image


Using OpenCV in python, we can apply all the above options, giving athestically pleasing images. The OpenCV library ships with two inpainting algorithms:

1. cv2.INPAINT_TELEA
2. cv2.INPAINT_NS


## Pre-requisite

The OpenCV requires two inputs:
1. input image to be restored
2. mask of the image regions we wish to restore - zero pixel depicts normal while non-zero pixel demands restoration

The second task is supported by providing an option to create the mask of input image manually using '''image_masking.py''' script.


## Results

Restoring and repairing old photographs

<div style="float:left"><img width="30%" src="https://github.com/Sudarshana2000/Image-Inpainting/blob/master/images/input3.jpg" />
<img width="30%" src="https://github.com/Sudarshana2000/Image-Inpainting/blob/master/images/mask3.jpg" />
<img width="30%" src="https://github.com/Sudarshana2000/Image-Inpainting/blob/master/images/output3.jpg" />
</div>
<br /><br />


Removing objects from image 
(Check out the lady near right end corner)
<div style="float:left"><img width="30%" src="https://github.com/Sudarshana2000/Image-Inpainting/blob/master/images/input4.jpg" />
<img width="30%" src="https://github.com/Sudarshana2000/Image-Inpainting/blob/master/images/mask4.jpg" />
<img width="30%" src="https://github.com/Sudarshana2000/Image-Inpainting/blob/master/images/output4.jpg" />
</div>
<br /><br />