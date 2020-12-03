import tkinter
import winsound
import time
import math



def countdown(count):
    label['text'] ="Hours: "+ str(count//3600)+ " Minutes:  " +str(count//60)+ " Seconds: " +str(count)
    if  count >= 0:
        top.after(1000, countdown,count-1)
    else:
        for x in range(6):
         winsound.Beep(1200,1200)

        label['text']="Done !!!"


def updateButton():
    hour,minute,sec=hoursInput.get(),minuteInput.get(),secondInput.get()
    time=int(hour or 0)*3600+int(minute or 0)*60+int(sec or 0)
    countdown(time)

top = tkinter.Tk()
top.geometry("250x150")

hoursLabel=tkinter.Label(top, text="Hours:" , bg="#222831" , foreground="white")
# hoursLabel.configure()
hoursInput=tkinter.Entry(top)

minuteLabel=tkinter.Label(top, text="Minutes:", bg="#222831" , foreground="white")
minuteInput=tkinter.Entry(top)

secondLabel=tkinter.Label(top, text="Seconds:", bg="#222831" , foreground="white")
secondInput=tkinter.Entry(top)

hoursLabel.grid(row=1,column=1)
hoursInput.grid(row=1,column=3)

minuteLabel.grid(row=2,column=1)
minuteInput.grid(row=2,column=3,padx=(20,20))

secondLabel.grid(row=3,column=1)
secondInput.grid(row=3,column=3)

label = tkinter.Label(top,bg='#222831')
label.grid(row=7,column=3)

button=tkinter.Button(top,text="Start Timer",command=updateButton, pady=5 , bg="#ff4d4d")
button.grid(row=9,column=3 , pady=(20,20))

top.configure(bg='#222831')
top.mainloop()
