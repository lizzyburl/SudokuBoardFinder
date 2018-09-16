from PIL import Image
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def findSudokuBoardCorners(img):
  """Finds top-left and bottom-right corners of board in screenshot image (x1,y1, x2, y2)."""
  # Expects image to be grayscale. Convert to numpy array if not already.
  img = np.array(img)
  
  # Calculate X/Y sobel gradients with kernel size 5.
  sobelx = np.abs(cv.Sobel(img,cv.CV_64F,1,0,ksize=5))
  sobely = np.abs(cv.Sobel(img,cv.CV_64F,0,1,ksize=5))
  
  # Sum gradients along orthogonal axis, strong peaks indicate strong line.
  xpeaks = np.sum(sobelx, axis=0)
  ypeaks = np.sum(sobely, axis=1)
  
  # Naively look for strongest peak on left/right/top/bot to find board edges.
  # TODO (sam) : Use more robust edge detection (non-max 1D for example).
  halfx = int(len(xpeaks)/2)
  halfy = int(len(ypeaks)/2)
  x1 = np.argmax(xpeaks[:halfx])
  x2 = np.argmax(xpeaks[halfx:]) + halfx
  y1 = np.argmax(ypeaks[:halfy])
  y2 = np.argmax(ypeaks[halfy:]) + halfy
  
  return (x1, y1, x2, y2)

def main():
  # Load image as grayscale and convert to numpy array.
  img_orig = np.array(Image.open("screenshot.png").convert('L'))
  # Get corners of sudoku board.
  x1, y1, x2, y2 = findSudokuBoardCorners(img_orig)
  print("%d,%d - %d,%d" % (x1, y1, x2, y2))
  
  # Get cropped image using those corners.
  img_cropped = img_orig[y1:y2, x1:x2]
  
  # Display original image and cropped to board corners image.
  plt.subplot(1,2,1),plt.imshow(img_orig,cmap = 'gray')
  plt.title('Original'), plt.xticks([]), plt.yticks([])
  plt.subplot(1,2,2),plt.imshow(img_cropped,cmap = 'gray')
  plt.title('Cropped'), plt.xticks([]), plt.yticks([])
  plt.show()

if __name__ == '__main__':
  main()