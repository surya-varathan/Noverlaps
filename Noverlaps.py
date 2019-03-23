import tkinter as tk
from tkinter import *
from collections import defaultdict as dd

win1=tk.Tk()
win1.title("Welcome to Air Asia")
win1.geometry("285x300")
mess=tk.Label(text="Welcome to Flight Gate Allotment System",fg="blue",font=("Helvetica",16))
mess.grid(row=0,column=1)

noflights=tk.Label(text="Enter Number of flights : ")
noflights.grid(row=1,column=1)
num=StringVar()
nof=Entry(textvariable=num)
nof.pack()
nof.grid(row=2,column=1)
submit=tk.Button(text="Submit",command=win1.destroy)
submit.grid(row=4,column=1)

win1.mainloop()

flightscount=int(num.get())

Database=[]

for i in range(1,flightscount+1):
    window=tk.Tk()
    window.title("Flight Entry "+str(i))
    window.geometry("600x230")

    flightNo=tk.Label(text="Enter the flight number: ")
    flightNo.grid(row=2,column=0)
    v=StringVar()
    flightEntry=Entry(textvariable=v)
    flightEntry.pack()
    flightEntry.grid(row=2,column=1)

    arrTime=tk.Label(text='Time of Arrival:')
    arrTime.grid(row=3,column=0)
    ahour = StringVar()
    ahour.set("Hour") # default  value
    ah=OptionMenu(window,ahour,'0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23')
    ah.grid(row =3,column=1)
    amins1 = StringVar()
    amins1.set("Minute") # default  value
    am1=OptionMenu(window,amins1,'0','1','2','3','4','5')
    am1.grid(row =3,column=2)
    amins2 = StringVar()
    amins2.set("Minute") # default  value
    am2=OptionMenu(window,amins2,'0','1','2','3','4','5','6','7','8','9')
    am2.grid(row =3,column=3)

    depTime=tk.Label(text='Time of Departure:')
    depTime.grid(row=4,column=0)
    dhour = StringVar()
    dhour.set("Hour") # default  value
    dh=OptionMenu(window,dhour,'0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23')
    dh.grid(row =4,column=1)
    dmins1 = StringVar()
    dmins1.set("Minute") # default  value
    dm1=OptionMenu(window,dmins1,'0','1','2','3','4','5')
    dm1.grid(row =4,column=2)
    dmins2 = StringVar()
    dmins2.set("Minute") # default  value
    dm2=OptionMenu(window,dmins2,'0','1','2','3','4','5','6','7','8','9')
    dm2.grid(row =4,column=3)

    submitButton=tk.Button(text="Submit",command=window.destroy)
    submitButton.grid(row=10,column=1)

    window.mainloop()

    Data={"fno":0,"atime":0,"dtime":0}
    Data["atime"]=ahour.get()+amins1.get()+amins2.get()
    Data["dtime"]=dhour.get()+dmins1.get()+dmins2.get()
    Data["fno"]=v.get()

    Database.append(Data)

def vertex_colouring(G):                    #This is perfect. Vertex_Colouring is ready. 
    colours=[i for i in range(len(G))]
    c={}
    for i in G:
        color1=colours[:]
        for j in G[i]:
            if j in c:
                if c[j] in color1:
                    del color1[color1.index(c[j])]
        c[i]=color1[0]
    return c
graph=dd(list)
lis=[]
for i in Database:
    lis.append([int(i["fno"]),[int(i["atime"]),int(i["dtime"])]])
lis.sort(key=lambda i:i[1])
for i in range(len(lis)):
    for j in range(i,len(lis)):
        if lis[i]!=lis[j]:
            if (lis[i][1][0]<lis[j][1][0] and lis[j][1][0]<lis[i][1][1]) or (lis[i][1][0]<lis[j][1][1] and lis[j][1][1]<lis[i][1][1]):
                graph[lis[i][0]].append(lis[j][0])
                graph[lis[j][0]].append(lis[i][0])

ans=vertex_colouring(graph)
print(ans)
##final=tk.Tk()
##final.title("Welcome to Air Asia")
##final.geometry("285x300")
##disp=tk.Label(text="Welcome to Flight Gate\n Allotment System",fg="blue",font=("Helvetica",16))
