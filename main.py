from tkinter import *
from tkinter import ttk

import random

from Algorithms.bubble_sort import bubbleSort
from Algorithms.merge_sort import merge_sort

from colors import *

root=Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1000,700)
root.config(bg='#ffcce6')



algo_name=StringVar()

#Algo List
algo_list=['Bubble Sort','Merge Sort']

speed_name=StringVar()
#speed list for selecting sorting speed
speed_list=['Fast','Medium','Slow']


# array of the data
data=[]


# Drawing the  data
def  drawData(data,colorArray):
    canvas.delete('all')
    canvas_width=800
    canvas_height=400
    x_width=canvas_width/(len(data)+1)
    offset=4
    spacing=2
    normalized_data=[i/max(data) for i in data]

    for i,height in enumerate(normalized_data):
        x0=i*x_width+offset+spacing
        y0=canvas_height-height*390

        x1=(i+1)*x_width+offset
        y1=canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])

        root.update_idletasks()


#  function to generate random array/data
def generate():
    global data

    data=[]

    for i in range(0,int(nv.get())):
        random_val=random.randint(int(low_val.get()),int(high_val.get()))
        data.append(random_val)

    drawData(data,[BLUE for x in range(len(data))])




# function for sorting speed
def set_speed():
    if(speed_name.get()=='Slow'):
        return 2

    elif(speed_name.get()=='Medium'):
        return 1.5

    elif(speed_name.get()=='Fast'):
        return 1


def sort():
    global data
    timeTick=set_speed()

    if algo_name.get()=='Bubble Sort':
        bubbleSort(data, drawData, timeTick)

    elif algo_name.get()=='Merge Sort':
        merge_sort(data,0,len(data)-1,drawData,timeTick)

# Options Frane
options_frame=Frame(root,width=900,height=300,bg='#b3ffff')
options_frame.grid(row=0,column=0,padx=10,pady=5)

#Dropdown Menus
#Algo Menu
label1=Label(options_frame,text='Algorithm')
label1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
algo_menu=OptionMenu(options_frame, algo_name, *algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_name.set(algo_list[0])


#Sorting Speed Menu
label2=Label(options_frame,text='Sorting Speed')
label2.grid(row=1,column=0,padx=5,pady=5)
speed_menu=OptionMenu(options_frame,speed_name,*speed_list)
speed_menu.grid(row=1,column=1,padx=5,pady=5)
speed_name.set(speed_list[0])

n=Label(options_frame,text="Number of Values")
n.grid(row=2,column=0,padx=5,pady=5)

nv=Entry(options_frame)
nv.grid(row=2,column=1,padx=5,pady=5)


lower_bound=Label(options_frame,text="Lower Bound")
lower_bound.grid(row=3,column=0,padx=5,pady=5)

low_val=Entry(options_frame)
low_val.grid(row=3,column=1,padx=5,pady=5)


higher_bound=Label(options_frame,text="Higher Bound")
higher_bound.grid(row=4,column=0,padx=5,pady=5)

high_val=Entry(options_frame)
high_val.grid(row=4,column=1,padx=5,pady=5)


# Sort Button
sort_btn=Button(options_frame,text="Sort",command=sort)
sort_btn.grid(row=5,column=1)

#To generate Array
gen_arr=Button(options_frame,text="Generate Array",command=generate)
gen_arr.grid(row=5,column=0,padx=5,pady=5)


# Canvas to draw array
canvas=Canvas(root,width=800,height=400,bg='aqua')
canvas.grid(row=1,column=0,padx=5,pady=5)







root.mainloop()

