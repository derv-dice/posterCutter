from PIL import Image
import sys

print("Enter full path to file name for example: ...\Folder\my image.png ")
name = input()
im = Image.open(name)
    
print("Image resolution: ", str(im.width), str(im.height))
print("Enter count of sheets: ")
n = int(input())
size_w = int(im.width/n)
size_h = int(size_w/1.4142857)
print("Size of single sheet : ",str(size_w), str(size_h))

i = round(im.width/size_w)
j = round(im.height/size_h)
print("Poster size in sheet: ",i, j)
            
a = 0
b = 0
c = size_w
d = size_h
counter = 0
for y in range(j):
    for x in range(i):
        counter += 1
        Current_im = im.crop((a,b,c,d))
        Current_im.save(str(counter)+'.png')
        a+=size_w
        c+=size_w
        print("Image № "+str(counter)+" saves as"+str(counter)+".png")
                
    a = 0
    c = size_w
    b+=size_h
    d+=size_h
    
print("Done!")


                
                
                
    
