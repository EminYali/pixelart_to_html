from PIL import Image
import os

try: os.remove("output.html")
except: pass
dosyaad=input("Dosya Adı : ")
gp=int(input("Pixel Art Gerçek Pixel Sayısı : "))
im = Image.open(dosyaad)
width, height = im.size
gp=width//gp
pix = im.load()
class Imagecheck():
    def __init__(self,resim):
        self.resim = resim
    def Check_XY(self):
        width, height = im.size
        return [self.resim[j,i] for i in range(height) for j in range(width) if i%gp==0 and j%gp==0]
    
ic=Imagecheck(pix)
width, height =width//gp, height//gp
if(width<=256 or height<=256):
    img_pixel=ic.Check_XY()
else: pass
f,a = open("output.txt", "a"),0
f.write(
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body
        {
            background-color:black;
        }
        td
        {
            width: 6.5px; height: 6px; box-shadow: black 0px 0px 3px;border-radius:1.4px;
        }
    </style>
</head>
<body>
    <table>"""
)
for i in range(height):
    f.write("\n<tr>")
    for j in range(width):
        f.write("""\n<td style="background-color: rgb%s;"></td>""" %(str(img_pixel[a])))
        a+=1
    f.write("<tr>\n")
f.write(
"""</table>
        <span style="font-family:Calibri;color:#747474;">%s x %s pixel</span>
    </div>
</body>
</html>""" %(str(width), str(height))
)
f.close()
os.replace("output.txt", "output.html")