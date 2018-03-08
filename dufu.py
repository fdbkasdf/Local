from PIL import Image
import pytesseract


img=Image.open("dufu.png")
text=pytesseract.image_to_string(img)
#print(text)
