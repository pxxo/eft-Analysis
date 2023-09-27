import sys
import cv2
import pyocr
import numpy as np
from PIL import Image

image = "ss.png"
name = "test"

# original
img = cv2.imread(image)
# cv2.imwrite(f"1_{name}_original.png", img)

# gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imwrite(f"2_{name}_gray.png", img)

# threshold
th = 140
img = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)[1]
# cv2.imwrite(f"3_{name}_threshold_{th}.png", img)

# bitwise
img = cv2.bitwise_not(img)
# cv2.imwrite(f"4_{name}_bitwise.png", img)

cv2.imwrite("target.png", img)

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
res = tool.image_to_string(Image.open("target.png"), lang="eng")

res = res.replace(" ", "")
res = res.replace("\n", " ")
res = res.lower()
task_list = res.split()
print(task_list)
