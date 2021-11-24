border(30)
if(len(lineErr)!= 0):
    print(red_color,"Terdapat error di line")
    for i in range(len(lineErr)):
        print(red_color,lineErr[i],normalizer)
else:
    print(green_color,"Tidak terdapat kesalahan pada file python.",normalizer)