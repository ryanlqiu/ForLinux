from PIL import Image
import argparse
CoefficientRED = 0.2126   #RGB系数值
CoefficientGREEN = 0.7152
CoefficientBLUE= 0.0722
#命令行参数获取

parser = argparse.ArgumentParser()

parser.add_argument("file")    #输入文件
parser.add_argument('-o','--output')  #输出文件
parser.add_argument('--width',type=int,default=100)  #输出字符宽度
parser.add_argument('--height',type=int,default=100) #输出字符长度


#定义参数
args=parser.parse_args()

IMG    = args.file
Out    = args.output
Width  = args.width
Height = args.height

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
##ascii_char = [chr(n) for n in range(128) if (n>=33 and n<=126)]

#RGB值转换成灰度值，映射到字符集
def get_char(r,g,b,alpha =256):
    if alpha==0:
        return ' '
    length = len(ascii_char)
    gray= int(CoefficientRED * r + CoefficientGREEN * g + CoefficientBLUE *b)

    unit =(256.0 + 1)/length
    return ascii_char[int(gray/unit)]

def Argu(x,y):
    lengthchar=len(x)
    for m in range(lengthchar):
        if x[m]!=y[m]:
            print('x= ',x[m],' y=  ',y[m],'m= ',m)
            return False
    return True
    

if __name__ =="__main__":
    im=Image.open(IMG)
    im=im.resize((Width,Height),Image.NEAREST)
    im=im.rotate(45)

    Txt_pic="          "

    for i in range(Height):
        for j in range(Width):
            Txt_pic+=get_char(*im.getpixel((j,i)))
        Txt_pic+="\n          "
##    print(len(im.getprojection()[0]))

    if Out:
        with open(Out,'w') as f:
            f.write(Txt_pic)
    else:
        with open('output.txt','w') as f:
            f.write(Txt_pic)




    

