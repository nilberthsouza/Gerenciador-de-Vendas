from tkinter import *
from db import Database
from tkinter import messagebox
db = Database('store.db')

def select_item(event):
    print('select'


def populate_list():
    #certifica que não há nada no listbox antes de mostrar o resultado do db
    parts_list.delete(0,END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    if part_text.get() == '' or customer_text() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Field', 'Please include all field')
        return 
    db.insert(part_text.get(),customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get()))
    populate_list()

def remove_item():
    print('remove')
def update_item():
    print('Update')

def clear_text():
    print('clear')

app = Tk()

#part
part_text = StringVar()
part_label = Label(app, text='Part Name',font=('bold',14), pady=20)
part_label.grid(row=0, column=0,stick='w')

part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)
#customer
customer_text = StringVar()
customer_label = Label(app, text='Customer ', font=('bold',14))
customer_label.grid(row=0, column=2,stick='w')

customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0,column=3)
#Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer',font=('bold',14) )
retailer_label.grid(row=1, column=0,stick='w')

customer_entry = Entry(app, textvariable=retailer_text)
customer_entry.grid(row=1,column=1)
#price
price_text = StringVar()
price_label = Label(app, text='Price',font=('bold',14))
price_label.grid(row=1, column=2,stick='w')

price_entry = Entry(app, textvariable= price_text)
price_entry.grid(row=1,column=3)

#Parts List(ListBox)
parts_list = Listbox(app, height=8, width=50,border=0)
parts_list.grid(row=3, column=0, columnspan=3,rowspan=6, pady=20, padx=20)
#create scroll
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

parts_list.bind('<<ListboxSelect>>',select_item)


#buttons
add_btn = Button(app, text='Add Part',width=12,command=add_item)
add_btn.grid(row=2, column=0,pady=20)

remove_btn = Button(app, text='Remove',width=12,command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update',width=12,command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input',width=12,command=clear_text)
clear_btn.grid(row=2, column=3)



app.title('Part Manager')
app.geometry('700x350')

populate_list()

app.mainloop()
