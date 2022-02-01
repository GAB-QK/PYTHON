import tkinter as tk

fenenetre=tk.Tk()
fenetre2=tk.Tk()

canvas=tk.Canvas(fenenetre,width=400,height=300,background="blue")
canvas2=tk.Canvas(fenenetre,width=400,height=300,background="white")
canvas3=tk.Canvas(fenetre2,width=400,height=300,background="green")
canvas.grid()
canvas2.grid()
canvas3.grid()



#create_line (XA,YA,XB,YB)trace le segment AB
# attention les ordonnées vont en sens inverse des maths
#augmeente quand on dfescend
canvas.create_line(0,0,400,300,width=50,fill="white")
canvas.create_line(0,300,400,0,width=50,fill="white")
canvas2.create_line(200,0,200,300,width=40,fill="red")
canvas2.create_line(0,150,400,150,width=40,fill="red")
canvas3.create_polygon((20,150),(200,20),(380,150),(200,280),width=40,fill="yellow")
canvas3.create_oval(110,80,290,220,fill="blue")
canvas3.create_line(135,105,265,195,width=25,fill="white")
canvas3.create_text(200,150,text="j'adore l'eau",angle="325",fill="black")
tk.mainloop()

'''
Exo 
dessiner le drapeau de l'ecosse '''

'''
Exo 
dessiner le drapeau de l'anglette 
'''