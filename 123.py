from tkinter import *
from operator import itemgetter
#import tkFileDialog
import tkinter.filedialog as tkFileDialog
from PIL import Image, ImageDraw, ImageFilter, ImageTk

import numpy as np



class xc(Frame):
    def __init__(self):

        self.image1=0
        self.image2=0
        self.photo=0
        self.photo2=0
        self.im2=0
        self.sss=[]
        self.var=IntVar()
        self.rbutton1=0
        self.rbutton2=0
        self.rbutton3=0



    def LoadFile(self):
        fn=tkFileDialog.Open(root,filetypes = [('*.jpg files','.jpg')]).show()
        if fn=='':
            return
        textbox.insert(1.0,fn)

        self.image1 = Image.open(fn)
        self.photo = ImageTk.PhotoImage(self.image1)
        self.image2 = Image.open(fn)
        photo2 = ImageTk.PhotoImage(self.image2)



        label3 = Label(root, image=self.photo).place(x=50, y=200, width=600, height=400)
        root.update_idletasks(label3)
        #root.update_idletasks()

        label4 = Label(root, image=photo2).place(x=750, y=200, width=600, height=400)
        root.update_idletasks(label4)
        #root.update_idletasks()

    def Clear(self):
        self.image2=self.image1
        photo2 = ImageTk.PhotoImage(self.image2)
        label4 = Label(root, image=photo2).place(x=750, y=200, width=600, height=400)
        root.update_idletasks(label4)
        #root.update_idletasks()

    def filt1(self):
        out2 = self.image2.filter(ImageFilter.UnsharpMask)   #DETAIL  SHARPEN  .UnsharpMask
        # out3 = out2.filter(ImageFilter.UnsharpMask)
        # out33 = out3.filter(ImageFilter.UnsharpMask)
        # out333 = out33.filter(ImageFilter.UnsharpMask)
        self.image2=out2


        photo2 = ImageTk.PhotoImage(self.image2)

        label4 = Label(root, image=photo2).place(x=750, y=200, width=600, height=400)
        root.update_idletasks(label4)
        #root.update_idletasks()


        # photo2 = ImageTk.PhotoImage(out333)
        # label4 = Label(root, image=photo2).place(x=750, y=100, width=600, height=400)
        # root.update_idletasks(label4)


    def filt2(self):
        out = self.image2.filter(ImageFilter.FIND_EDGES)
        self.image2=out


        photo = ImageTk.PhotoImage(self.image1)
        photo2 = ImageTk.PhotoImage(self.image2)


        label4 = Label(root, image=photo2).place(x=750, y=200, width=600, height=400)
        root.update_idletasks(label4)
        #root.update_idletasks()

        # photo2 = ImageTk.PhotoImage(out)
        # label4 = Label(root, image=photo2).place(x=750, y=100, width=600, height=400)
        # root.update_idletasks(label4)

    def filt3(self):
        im=self.image2.convert("P")
        self.im2=Image.new("P",im.size,255)
        im.convert("P")
        temp={}
        his = im.histogram()

        values = {}

        for i in range(256):
            values[i] = his[i]

        for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
             print(j,k)


        for x in range(im.size[1]):
            for y in range(im.size[0]):
                pix = im.getpixel((y,x))
                temp[pix] = pix
                if pix == 225 : # !!!!!!!225 255
                    self.im2.putpixel((y,x),0)# 128 192
        photo2 = ImageTk.PhotoImage(self.im2)
        label4 = Label(root, image=photo2).place(x=750, y=200, width=600, height=400)
        root.update_idletasks(label4)
        #root.update_idletasks()

    def SaveFile(self):
        fn = tkFileDialog.SaveAs(root, filetypes = [('*.gif files', '.gif')]).show()
        if fn == '':
            return
        if not fn.endswith(".gif"):
            fn+=".gif"

        self.im2.save(fn)

    def LoadBD(self):

        fn=tkFileDialog.Open(root,filetypes = [('*.txt files','.txt')]).show()
        if fn=='':
            return

        f=open(fn,"r")
        s=f.read()
        f.close()

        ss=s.split("\n")
        print(ss.__len__())

        for i in range(ss.__len__()):
            self.sss.append(ss[i].split("\t"))


        print(ss)
        print(self.sss)
        textbox2.insert(1.0,self.sss)
        self.var.set(1)

        self.rbutton1=Radiobutton(panelFrame,text=self.sss[0][0],variable=self.var,value=self.sss[0][1])
        self.rbutton2=Radiobutton(panelFrame,text=self.sss[1][0],variable=self.var,value=self.sss[1][1])
        self.rbutton3=Radiobutton(panelFrame,text=self.sss[2][0],variable=self.var,value=self.sss[2][1])
        self.rbutton4=Radiobutton(panelFrame,text=self.sss[3][0],variable=self.var,value=self.sss[3][1])
        self.rbutton5=Radiobutton(panelFrame,text=self.sss[4][0],variable=self.var,value=self.sss[4][1])
        self.rbutton6=Radiobutton(panelFrame,text=self.sss[5][0],variable=self.var,value=self.sss[5][1])
        self.rbutton1.place(x=1000,y=0,width=60,height=30)
        self.rbutton2.place(x=1000,y=30,width=60,height=30)
        self.rbutton3.place(x=1000,y=60,width=60,height=30)
        self.rbutton4.place(x=1050,y=0,width=60,height=30)
        self.rbutton5.place(x=1050,y=30,width=60,height=30)
        self.rbutton6.place(x=1050,y=60,width=60,height=30)
        self.rbutton1.pack("right")
        self.rbutton2.pack("right")
        self.rbutton3.pack("right")
        self.rbutton4.pack("right")
        self.rbutton5.pack("right")
        self.rbutton6.pack("right")



    def Shaib(self):
        width, height = self.image2.size
        work = self.image2
        x1, x2 = 0, width
        gray = work.convert('L')
        bw = np.asarray(gray).copy()
        bw[bw < 128] = 0
        bw[bw >= 128] = 255

        print(bw)

        for i in range(width // 2):
            for j in range(height):
                if bw[j, i] != 255:
                    x1 = i
                    break
            else:
                continue
            break
        for i in range(width - 1, width // 2, -1):
            for j in range(height):
                if bw[j, i] != 255:
                    x2 = i
                    break
            else:
                continue
            break

        diamPx = x2 - x1
        diamMM = diamPx / 15


        print(diamMM)
        v = self.var.get()

        diamMM2= str(diamMM)

        if v-3 <= diamMM and v+3 >= diamMM:
            textbox.insert(1.0,"OK!!!!\n")
            textbox.insert(1.0,"Diam - " + diamMM2+"\n")
        else:
            textbox.insert(1.0,"Error!!!!\n")
            textbox.insert(1.0,"Diam - " + diamMM2+"\n")

    def Spravk(self):
        root2=Tk()
        root2.title('Reference')
        root2.geometry('200x150+300+225')
        l2=Label(root2,
		 text="Reference",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()
        panelFrame3 = Frame(root2, height = 200, bg = 'gray')
        panelFrame3.pack(side = 'top', fill = 'x')
        textbox3=Text(panelFrame3, width=100,heigh=50)
        textbox3.insert(1.0,'Load - zagruzka foto\nfilt1 - filtr rezkosti \nfilt2 - filtr obescvechivaniya \nfilt3 - filtr podavleniya shumov \nSave - sohranit rezultat \nLoad BD - zagruzka bd \nsize - razmer obrabotanoy photografii \nClear - ochistit photo ot filtrov ')


        textbox3.pack()


    def Spravk2(self):
        root2=Tk()
        root2.title('Matmodel')
        root2.geometry('200x150+300+225')
        l2=Label(root2,
		 text="Reference",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()
        panelFrame3 = Frame(root2, height = 200, bg = 'gray')
        panelFrame3.pack(side = 'top', fill = 'x')
        textbox3=Text(panelFrame3, width=100,heigh=50)
        textbox3.insert(1.0,'Dlya polucheniya razmera shaidy, mi uznaem razmer kartinki, a imenno dlinnu i visoty. Prohodim v cikle po kazhdoy stroke pixeley c levoy storony v poiskah chernogo pixelya, i nayda pixel zapominayem koordinaty. tozhe samoe prodelyvaem s pravoy storony. Dalee vychitaem 2 koordinaty i polychaem diametr nashey shaiby.   ')
        textbox3.pack()

root=Tk()
cc=xc()
root.title('myWindow')
root.geometry('200x150+300+225')




l=Label(root,
		 text="SSPR",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

panelFrame = Frame(root, height = 60, bg = 'gray')
panelFrame.pack(side = 'top', fill = 'x')
panelFrame2 = Frame(root, height = 1, bg = 'orange')
panelFrame2.pack(side = 'top', fill = 'x')

but=Button(panelFrame,text = 'Load',command=cc.LoadFile)
but.place(x=10,y=10,width=60,height=30)

but2=Button(panelFrame,text = 'filt1',command=cc.filt1)
but2.place(x=70,y=10,width=60,height=30)

but3=Button(panelFrame,text = 'filt2',command=cc.filt2)
but3.place(x=130,y=10,width=60,height=30)

but4=Button(panelFrame,text = 'filt3',command=cc.filt3)
but4.place(x=190,y=10,width=60,height=30)

but5=Button(panelFrame,text = 'Save',command=cc.SaveFile)
but5.place(x=250,y=10,width=60,height=30)

but6=Button(panelFrame,text = 'Load BD',command=cc.LoadBD)
but6.place(x=310,y=10,width=60,height=30)

but7=Button(panelFrame,text = 'size',command=cc.Shaib)
but7.place(x=370,y=10,width=60,height=30)

but8=Button(panelFrame,text = 'Clear',command=cc.Clear)
but8.place(x=430,y=10,width=60,height=30)

but9=Button(panelFrame,text = 'Reference',command=cc.Spravk)
but9.place(x=10,y=40,width=60,height=30)

but10=Button(panelFrame,text = 'Reference 2',command=cc.Spravk2)
but10.place(x=70,y=40,width=60,height=30)

textbox=Text(panelFrame,width=50,heigh=3)
textbox.pack()

textbox2=Text(panelFrame,width=50,heigh=3)
textbox2.pack()



root.mainloop()