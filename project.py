from tkinter import *
from tkinter import messagebox

class patient:
    specialization=0
    stat=0
    name=""
    def __init__(self,name,stat,specialization):
        self.name=name
        self.stat=stat
        self.specialization=specialization

class hospital:
    normal=[]
    urgent=[]
    superUrgent=[]
    specialization_now={}
    def add(self,name,specialization,stat):
        x=patient(name,stat,specialization)
        if specialization in self.specialization_now:
            if self.specialization_now[specialization]>1:
                messagebox.showerror("full capacity",f'there is no more rooms for patients with spesialization: {specialization}!')
                return
            else:
                self.specialization_now[specialization]+=1
        elif not specialization in self.specialization_now:
            self.specialization_now.update({specialization:1})
        if stat == 'super urgent':
            self.superUrgent.append(x)
        if stat == 'urgent':
            self.urgent.append(x)
        if stat == 'normal':
            self.normal.append(x)
    def next_patient(self,specialization):
        found=0
        for i in self.superUrgent:
            if i.specialization==specialization:
                messagebox.showinfo("next patient",f"next patient is {i.name}, stat: {i.stat}")
                self.superUrgent.remove(i)
                found=1
                break
        for i in self.urgent:
            if found ==1:
                break
            elif i.specialization==specialization:
                messagebox.showinfo("next patient",f"next patient is {i.name}, stat: {i.stat}")
                self.urgent.remove(i)
                found=1
                break
        for i in self.normal:
            if found ==1:
                break
            if i.specialization==specialization:
                messagebox.showinfo("next patient",f"next patient is {i.name}, stat: {i.stat}")
                self.normal.remove(i)
                found=1
                break
        if found == 0:
            messagebox.showerror("not found",f"there is no patient with specialization {specialization}")
        else:
            self.specialization_now[specialization]-=1
            if self.specialization_now[specialization] == 0:
                self.specialization_now.pop(specialization)
            
    def remove_patient(self,specialization,name):
        found=0
        for i in self.superUrgent:
            if i.specialization==specialization and i.name==name:
                messagebox.showinfo("removed",f"patient {i.name}, stat: {i.stat}\nhas been removed!")
                self.superUrgent.remove(i)
                found=1
                break
        for i in self.urgent:
            if found ==1:
                break
            elif i.specialization==specialization and i.name==name:
                messagebox.showinfo("removed",f"patient {i.name}, stat: {i.stat}\nhas been removed!")
                self.urgent.remove(i)
                found=1
                break
        for i in self.normal:
            if found ==1:
                break
            if i.specialization==specialization and i.name==name:
                messagebox.showinfo("removed",f"patient {i.name}, stat: {i.stat}\nhas been removed!")
                self.normal.remove(i)
                found=1
                break
        if found == 0:
            messagebox.showerror("not found",f"there is no patient with name {name} and specialization {specialization}")
        else:
            self.specialization_now[specialization]-=1
            if self.specialization_now[specialization] == 0:
                self.specialization_now.pop(specialization)

sys=hospital()
root=Tk()
root.geometry('400x500')

def exit():
    r=messagebox.askyesno("end?",'are you sure you want to end the program?')
    if r == 1:
        root.destroy()
    elif r == 0:
        pass

    
def add_window_button():
    def add_des(n,spec,st):
        if n=='' or spec=='' or st=='':
            messagebox.showerror("information needed!",'each patient needs a name,specialization and stat!')
            return
        else:
            sys.add(n,spec,st)
            add_window.destroy()
    add_window=Toplevel()
    add_window.title("add patient")
    Label(add_window,text='Name',font=('times new roman',20)).grid(row=0,column=0,pady=10)
    name_e=Entry(add_window,width=30,font=('times new roman',15))
    name_e.grid(row=0,column=1,columnspan=5,padx=10,pady=10)
    Label(add_window,text='Specialization',font=('times new roman',20)).grid(row=1,column=0,pady=10)
    specialization_e=Entry(add_window,width=30,font=('times new roman',15))
    specialization_e.grid(row=1,column=1,columnspan=5,padx=10,pady=10)
    stat=StringVar()
    Label(add_window,text='Stat',font=('times new roman',20)).grid(row=3,column=0,pady=10)
    Radiobutton(add_window,text='normal',value='normal',variable=stat,font=('times new roman',15)).grid(row=3,column=1)
    Radiobutton(add_window,text='urgent',value='urgent',variable=stat,font=('times new roman',15)).grid(row=3,column=2)
    Radiobutton(add_window,text='super urgent',value='super urgent',variable=stat,font=('times new roman',15)).grid(row=3,column=3)
    Button(add_window,text='add',font=('times new roman',20),command= lambda: add_des(name_e.get(),specialization_e.get(),stat.get())).grid(row=6,column=5,pady=10)
def list_patients():
    if len(list(sys.specialization_now))==0:
        messagebox.showinfo('empty','there is no patients at the moment')
        return
    list_patients_window=Toplevel()
    list_patients_window.title("patient's list")
    
    for i in list(sys.specialization_now.keys()):
        l_f=LabelFrame(list_patients_window,text=i,font=('times new roman',15))
        l_f.pack(padx=100,pady=5)
        for j in sys.superUrgent:
            if j.specialization == i:
                Label(l_f,text=f'patient: {j.name}, stat: {j.stat}',font=('times new roman',15)).pack(padx=100,pady=5)
        for j in sys.urgent:
            if j.specialization == i:
                Label(l_f,text=f'patient: {j.name}, stat: {j.stat}',font=('times new roman',15)).pack(padx=100,pady=5)
        for j in sys.normal:
            if j.specialization == i:
                Label(l_f,text=f'patient: {j.name}, stat: {j.stat}',font=('times new roman',15)).pack(padx=100,pady=5)

def next_patient_button():
    def find_next(spec):
        if spec =='':
            messagebox.showerror("Error",'you did not chose a specialization!')
            return
        else:
            sys.next_patient(spec)
            next_patient_window.destroy()
    if len(list(sys.specialization_now))==0:
        messagebox.showinfo("empty!",'there is no patients at the moment')
    else:
        next_patient_window=Toplevel()
        next_patient_window.title("specialization ?")
        l_f=LabelFrame(next_patient_window,text='specializations',padx=50)
        l_f.grid(row=0,column=0,columnspan=5,padx=10)
        spec= StringVar()
        for i in sys.specialization_now:
            Radiobutton(l_f,text=i,value=i,variable=spec,font=('times new roman',15)).pack()
        Button(next_patient_window,text='next',font=('times new roman',20),command= lambda: find_next(spec.get()),padx=50,pady=5).grid(row=1,column=4,padx=50,pady=5)

def remove_patient_button():
    def find_remove(spec,name):
        if spec =='':
            messagebox.showerror("Error",'you did not chose a specialization!')
            return
        elif name=='':
            messagebox.showerror("Error",'you did not type a name!')
            return
        else:
            sys.remove_patient(spec,name)
            remove_patient_window.destroy()
    if len(list(sys.specialization_now))==0:
        messagebox.showinfo("empty!",'there is no patients at the moment')
    else:
        remove_patient_window=Toplevel()
        remove_patient_window.title("name, specializatio ?")
        Label(remove_patient_window,text='name:',font=('times new roman',15)).grid(row=0,column=0)
        name_e=Entry(remove_patient_window,width=50,font=('times new roman',15))
        name_e.grid(row=0,column=1)
        l_f=LabelFrame(remove_patient_window,text='specializations',padx=50)
        l_f.grid(row=1,column=0,columnspan=5,padx=10)
        spec= StringVar()
        for i in sys.specialization_now:
            Radiobutton(l_f,text=i,value=i,variable=spec,font=('times new roman',15)).pack()
        Button(remove_patient_window,text='remove',font=('times new roman',20),command= lambda: find_remove(spec.get(),name_e.get()),padx=50,pady=5).grid(row=2,column=2,padx=50,pady=5)


Button(root,text='add patient',padx=40,pady=10,font=('times new roman',20),command= add_window_button).pack(padx=50,pady=10)
Button(root,text='list patients',padx=40,pady=10,font=('times new roman',20),command=list_patients).pack(padx=50,pady=10)
Button(root,text='next patient',padx=40,pady=10,font=('times new roman',20),command=next_patient_button).pack(padx=50,pady=10)
Button(root,text='remove patient',padx=28,pady=10,font=('times new roman',20),command=remove_patient_button).pack(padx=50,pady=10)
Button(root,text='end program',padx=40,pady=10,font=('times new roman',20),command=exit).pack(padx=50,pady=10)



root.mainloop()