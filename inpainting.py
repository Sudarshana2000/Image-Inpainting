import argparse
import cv2
from image_masking import *


def inpaint(imagePath, maskPath, method="telea", radius=3):
    flags=cv2.INPAINT_TELEA
    if method=="ns":
        flags=cv2.INPAINT_NS
    image=cv2.imread(imagePath)
    mask=cv2.imread(maskPath)
    if mask is None or mask.shape != image.shape:
        print("The given mask is not applicable. Please create a new mask.")
        maskImage().process(imagePath, maskPath)
        mask=cv2.imread(maskPath)
    mask=cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    output=cv2.inpaint(image, mask, radius, flags=flags)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputPath', help='Input original image')
    parser.add_argument('maskPath', help='Mask image')
    parser.add_argument('outputPath', help='Restored image')
    parser.add_argument('method', choices=["telea", "ns"], default="telea", help="Inpainting algorithm to use")
    args = parser.parse_args()
    output = inpaint(args.inputPath, args.maskPath, args.method)
    cv2.imwrite(args.outputPath, output)