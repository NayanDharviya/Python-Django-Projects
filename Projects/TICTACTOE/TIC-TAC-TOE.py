from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('TicTacToe')
#root.geometry('300x400')

click=True

def check_button(button):
    count=0
    global click  #globally use
    if button['text']=="" and click == True: #check button is empty and click means first user one have to press button 
        button['text']= "X"  #when user one press the button it will consider as 'X'
        button.config(bg='red')
        click=False
        
    if button['text']=="" and click == False:
        button['text']="O" #when user second press the button it will consider as 'O'
        button.config(bg='blue')
        click=True

    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X')==True:
        count+=1
        button1.config(bg='grey')
        button2.config(bg='grey')
        button3.config(bg='grey')
        messagebox.showinfo('Winner X','You Have Won The Game')
        clear()
    if (button4['text']=='X' and button5['text']=='X' and button6['text']=='X')==True:
            count+=1
            button4.config(bg='grey')
            button5.config(bg='grey')
            button6.config(bg='grey')
            messagebox.showinfo('Winner X','You Have Won The Game')
            clear()
    if(button7['text']=='X' and button8['text']=='X' and button9['text']=='X')==True:
            count+=1
            button7.config(bg='grey')
            button8.config(bg='grey')
            button9.config(bg='grey')
            messagebox.showinfo('Winner X','You Have Won The Game')
            clear()
    if( button1['text']=='X' and button4['text']=='X' and button7['text']=='X')==True:
            count+=1
            button1.config(bg='grey')
            button4.config(bg='grey')
            button7.config(bg='grey')
            messagebox.showinfo('Winner X','You Have Won The Game')
            clear()
    if( button2['text']=='X' and button5['text']=='X' and button8['text']=='X')==True:
            count+=1
            button2.config(bg='grey')
            button5.config(bg='grey')
            button8.config(bg='grey')
            messagebox.showinfo('Winner X','You Have Won The Game')
            clear()
    if(button3['text']=='X' and button6['text']=='X' and button9['text']=='X')==True:
            count+=1
            button3.config(bg='grey')
            button6.config(bg='grey')
            button9.config(bg='grey')
            messagebox.showinfo('Winner X','You Have Won The Game')
            clear()
    if(button1['text']=='X' and button5['text']=='X' and button9['text']=='X')==True:
            count+=1
            button1.config(bg='grey')
            button5.config(bg='grey')
            button9.config(bg='grey')
            messagebox.showinfo('Winner X','You Have Won The Game')
            clear()
    if(button3['text']=='X' and button5['text']=='X' and button7['text']=='X')==True:
            count+=1
            button3.config(bg='grey')
            button5.config(bg='grey')
            button7.config(bg='grey')
            messagebox.showinfo('Winner X','You Have Won The Game')
            clear()


    if(button1['text']=='O' and button2['text']=='O' and button3['text']=='O')==True:
        count+=1
        button1.config(bg='grey')
        button2.config(bg='grey')
        button3.config(bg='grey')
        messagebox.showinfo('Winner O','You Have Won The Game')
        clear()
        
    if(button4['text']=='O' and button5['text']=='O' and button6['text']=='O'):
            count+=1 
            button4.config(bg='grey')
            button5.config(bg='grey')
            button6.config(bg='grey')
            messagebox.showinfo('Winner O','You Have Won The Game')
            clear()
        
         
    if(button7['text']=='O' and button8['text']=='O' and button9['text']=='O'):
        count+=1     
        button7.config(bg='grey')
        button8.config(bg='grey')
        button9.config(bg='grey')
        messagebox.showinfo('Winner O','You Have Won The Game')
        clear()
        
        
    if(button1['text']=='O' and button4['text']=='O' and button7['text']=='O'):
        count+=1     
        button1.config(bg='grey')
        button4.config(bg='grey')
        button7.config(bg='grey')
        messagebox.showinfo('Winner O','You Have Won The Game')
        clear()
        
         
    if(button2['text']=='O' and button5['text']=='O' and button8['text']=='O'):
             
        button2.config(bg='grey')
        button5.config(bg='grey')
        button8.config(bg='grey')
        messagebox.showinfo('Winner O','You Have Won The Game')
        clear()
        
         
    if(button3['text']=='O' and button6['text']=='O' and button9['text']=='O'):
        count+=1    
        button3.config(bg='grey')
        button6.config(bg='grey')
        button9.config(bg='grey')
        messagebox.showinfo('Winner O','You Have Won The Game')
        clear()
        
         
    if(button1['text']=='O' and button5['text']=='O' and button9['text']=='O'):
        count+=1   
        button1.config(bg='grey')
        button5.config(bg='grey')
        button9.config(bg='grey')
        messagebox.showinfo('Winner O','You Have Won The Game')
        clear()
        
        
    if(button3['text']=='O' and button5['text']=='O' and button7['text']=='O') :
        count+=1     
        button3.config(bg='grey')
        button5.config(bg='grey')
        button7.config(bg='grey')
        messagebox.showinfo('Winner O','You Have Won The Game')
        clear()
        
         
    if(button1['text']!='' and button2['text']!='' and button3['text']!='' and button4['text']!=''
       and button5['text']!='' and button6['text']!='' and button7['text']!='' and button8['text']!='' and button9['text']!='' and count<=0):
        messagebox.showinfo('Game Over','No Player is Won')
        clear()
    
def clear():
        button1["text"]=''
        button1.config(bg='white')
        button2["text"]=''
        button2.config(bg='white')
        button3["text"]=''
        button3.config(bg='white')
        button4["text"]=''
        button4.config(bg='white')
        button5["text"]=''
        button5.config(bg='white')
        button6["text"]=''
        button6.config(bg='white')
        button7["text"]=''
        button7.config(bg='white')
        button8["text"]=''
        button8.config(bg='white')
        button9["text"]=''
        button9.config(bg='white')
        

    
##buttons=StringVar()
button1=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button1))
#it uses lambda function because lambda is a anonymous function which is use when function has no name and it execute single line expression
button1.grid(row=1,column=0)
button2=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button2))
button2.grid(row=1,column=1)
button3=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button3))
button3.grid(row=1,column=2)
button4=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button4))
button4.grid(row=2,column=0)
button5=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button5))
button5.grid(row=2,column=1)
button6=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button6))
button6.grid(row=2,column=2)
button7=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button7))
button7.grid(row=3,column=0)
button8=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button8))
button8.grid(row=3,column=1)
button9=Button(root,text="",font=('Times 26 bold'),bg='white',height=4,width=8,command=lambda:check_button(button9))
button9.grid(row=3,column=2)
b=Button(root,text="Replay",command=clear)
b.grid(row=4,column=1)

root.mainloop()
