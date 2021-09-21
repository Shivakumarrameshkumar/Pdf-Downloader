from tkinter import *
import webbrowser
Shivakumar=Tk()
Shivakumar.title("Python Documentation")
Shivakumar.config(bg="light blue")
Shivakumar.geometry('900x500')
Shivakumar.resizable(0,0)
class Shivakumars:
    def __init__(self):
        self.open_tamil="https://drive.google.com/open?id=1yeuT9Ks6r49DHlk_78A635VdUWltudhq"
        self.name=Label(Shivakumar,text="PDF DOWNLOAD",font=("Roboto",20),fg="red",bg="#1e2121",width=50).place(x=-5,y=0)
        self.box=Label(Shivakumar,text="General Subjects",font=("Roboto",15),bg='#2a78ad',fg='white',width=40).place(x=0,y=80)
        self.box_support=Label(Shivakumar,text="Download Link",font=('Roboto',15),bg='#2a78ad',fg='white',width=20).place(x=600,y=80)
        self.white=Label(Shivakumar,text="",bg='white',pady=6).place(x=600,y=79)
        self.english=Label(Shivakumar,text="English",font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=115)
        self.tamil=Label(Shivakumar,text="Tamil",font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=150)
        self.chemistry=Label(Shivakumar,text="Chemistry",font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=185)
        self.computer=Label(Shivakumar,text="Computer Science",font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=220)
        self.maths=Label(Shivakumar,text='Maths',font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=255)
        self.Physcis=Label(Shivakumar,text='Physcis',font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=290)
        self.Phy2=Label(Shivakumar,text='Physcis-2',font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=325)
        self.Chemistry2=Label(Shivakumar,text='Chemistry-2',font=("Roboto",15),bg='white',fg='black',width=40).place(x=0,y=361)
        self.maths2=Label(Shivakumar,text='Maths-2',font=("Roboto",15),bg='white',fg='black',width=40,height=1).place(x=0,y=398)
        
        self.english_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.englishs).place(x=605,y=115)
        self.tamil_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.tamils).place(x=605,y=149)
        self.chemistry_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.chemis).place(x=605,y=185)
        self.computer_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.comany).place(x=605,y=220)
        self.maths_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.maths).place(x=605,y=255)
        self.physcis1_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.physcis1).place(x=605,y=290)
        self.physcis2_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.physcis2).place(x=605,y=328)    
        self.chemistry2_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.chemistry2).place(x=605,y=360)
        self.maths2_download=Button(Shivakumar,text="Download",font=('impact',10),bg='light green',fg='blue',width=40,command=self.maths1).place(x=605,y=398)
    def englishs(self):
        path='https://drive.google.com/open?id=1Tuk7ENEQ7vay8hW97S__bncgBBBywoh9'
        webbrowser.open_new(path)
       
    def tamils(self):
        path='https://drive.google.com/open?id=1yeuT9Ks6r49DHlk_78A635VdUWltudhq'
        webbrowser.open_new(path)#using this webbrowser to use pdf and open it easily
        
    def chemis(self):
        path='https://drive.google.com/file/d/172ycbPz04r90GIfGMdbjPRFjA1yDayRc/view?usp=sharing'
        webbrowser.open_new(path)
    def comany(self):
        path='https://drive.google.com/file/d/1A4SUA4H-uOF7htenPVA2z24dwc4vljQd/view?usp=sharing'
        webbrowser.open_new(path)
    
    def maths(self):
        path='https://drive.google.com/file/d/17G2nYAoPuKSrTPV5gZJmIMXVF-8KhRw4/view?usp=sharing'
        webbrowser.open_new(path)
    def maths1(self):
        path='https://drive.google.com/file/d/1AGU4Lxdj0hmhHdVpC715CCb1oN9i1tvl/view?usp=sharing'
        webbrowser.open_new(path)
    def physcis1(self):
        path='https://drive.google.com/file/d/1AZ3ylll5a11Bg70Sv8IT2TivUbgW4dwF/view?usp=sharing'
        webbrowser.open_new(path)
    def physcis2(self):
        path='https://drive.google.com/file/d/1J6GOALmk5nvPGVOaNLMTFR16k8Vw_t1T/view?usp=sharing'
        webbrowser.open_new(path)
    def chemistry2(self):
        path='https://drive.google.com/file/d/1738pqhgmZWPDFy9ZRobgEEWm-LS8WksV/view?usp=sharing'
        webbrowser.open_new(path)


Man=Shivakumars()
Shivakumar.mainloop()