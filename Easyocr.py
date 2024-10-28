import easyocr

reader = easyocr.Reader(['ko'])
result = reader.readtext(r"C:\Users\chae\Desktop\giyeok.png")

print(result)