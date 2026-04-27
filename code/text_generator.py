import os
from PIL import Image
from colorama import init, Fore

# Initialize Colorama
init(convert=True)


try: 
    script_dir = os.path.dirname(__file__)
    image_path = os.path.join(script_dir, '../images/hp1.3.jpg')


    text="HARRYPOTTER"


    #pixel info list    0->Black 15->white
    im = Image.open(image_path)
    width, height = im.size
    pixel_values = list(im.getdata())
    #print(pixel_values)
    l=pixel_values
    c=-1
    for i in l:
        c=c+1
        if i==0:continue
        elif i==15:continue
        elif i <(151,151,151):l[c]=0
        elif i >=(151,151,151):l[c]=15
    #print(l)
    li=l
    c=-1
    count=-width
    for i in range(height):
        count+=width
        #print(count)
        for i in range(count,count+width):
            c+=1
            if li[i]==0:
                print(Fore.BLACK+text[c%len(text)],end='')
            else:
                print(Fore.WHITE+text[c%len(text)],end='') 
        print('')


except FileNotFoundError:
    print("Error: Please place image inside the 'images' folder.")