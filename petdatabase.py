from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
from tkinter import messagebox
from tkinter import ttk


root = Tk()
root.title('Happy Tails')
root.geometry("1400x780")
root.configure(bg="linen")

#Database
conn = sqlite3.connect('happy_tails.db')
c = conn.cursor()

lbl_title=Label(root,text='HAPPY TAILS',font=('times new roman',37,'bold'),fg='dark orange',bg='linen')
lbl_title.place(x=0,y=0,width=1400,height=50)

img_frame=Frame(root,bd=2,relief=RIDGE,bg='white')
img_frame.place(x=0,y=50,width=1400,height=165)

img=Image.open('/Users/santoshyss/Desktop/proj_imgs/petimg.png')
img=img.resize((540,160))
img_tk=ImageTk.PhotoImage(img)

img=Label(img_frame,image=img_tk)
img.place(x=420,y=0,width=540,height=160)

#Mainframe
Mainframe=Frame(root,bd=2,relief=RIDGE,bg='linen')
Mainframe.place(x=1,y=220,width=1397,height=555)

#upperFrame
upframe=LabelFrame(Mainframe,bd=2,relief=RIDGE,bg='linen',text='Add Pets',font=('times new roman',15,'bold'),fg='dark orange')
upframe.place(x=1,y=10,width=1390,height=110)

#down Frame
downframe=LabelFrame(Mainframe,bd=2,relief=RIDGE,bg='linen',text='Pets for Adoption',font=('times new roman',15,'bold'),fg='dark orange')
downframe.place(x=1,y=140,width=1390,height=400)

#table frame
tableframe=Frame(downframe,bd=3,relief=RIDGE,bg='linen')
tableframe.place(x=1,y=10,width=1380,height=340)

#scroll bar
scroll_x=Scrollbar(tableframe,orient=HORIZONTAL)
scroll_y=Scrollbar(tableframe,orient=VERTICAL)

Ptable=ttk.Treeview(tableframe,column=('id','brd','age','gend','prc'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
Ptable.pack()
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=Ptable.xview)
scroll_y.config(command=Ptable.yview)

style = ttk.Style(root)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
style.configure("Treeview", background="bisque",fieldbackground="bisque", foreground="DarkOrange3")

Ptable.heading('id',text='Pet ID')
Ptable.heading('brd',text='Breed')
Ptable.heading('age',text='Age')
Ptable.heading('gend',text='Gender')
Ptable.heading('prc',text='Price')

Ptable.pack(fill=BOTH,expand=1)

c.execute("SELECT * FROM Pets")
rows = c.fetchall()
for row in rows:
    Ptable.insert("", "end", values=row)

def success():
	messagebox.showinfo("Adoption Confirmation", "Pet adopted")

def adopt():
	ad = Tk()
	ad.title('Adopt Pet')
	ad.geometry("400x200")
	ad.configure(bg="linen")

	comm_l=Label(ad,text='Enter Pet ID of pet to be adopted',fg='dark orange',bg='linen')
	comm_l.grid(row=0,column=0,padx=85,pady=20)
	comm=Entry(ad,width=20,highlightbackground="linen",fg='black',bg='white')
	comm.grid(row=1,column=0,padx=10,pady=5)

	comm_btn=Button(ad, text='Adopt Pet', fg='DarkOrange3',highlightbackground='linen', width=15,command=success)
	comm_btn.grid(row=2,column=0)

#Login Labels
username_label=Label(upframe,text='Username',fg='dark orange',bg='linen')
username_label.grid(row=0,column=0)
password_label=Label(upframe,text='Password',fg='dark orange',bg='linen')
password_label.grid(row=1,column=0)

username=Entry(upframe,width=20,highlightbackground="linen",fg='black',bg='white')
username.grid(row=0,column=1)

password=Entry(upframe,width=20,highlightbackground="linen",fg='black',bg='white')
password.grid(row=1,column=1)

#login function
def login():
	conn = sqlite3.connect('happy_tails.db')
	c = conn.cursor()

	u = 'admin'
	p = 'hello'
	if username.get()==u and password.get()==p:
		new = Toplevel(root)
		new.title('Add Pets')
		new.geometry('400x500')
		new.configure(bg='linen')

		Petid=Entry(new,width=30,highlightbackground="linen",fg='black',bg='white')
		Petid.grid(row=0,column=2,padx=20,pady=20)

		Breed=Entry(new,width=30,highlightbackground="linen",fg='black',bg='white')
		Breed.grid(row=1,column=2)

		Age=Entry(new,width=30,highlightbackground="linen",fg='black',bg='white')
		Age.grid(row=2,column=2)

		Gender=Entry(new,width=30,highlightbackground="linen",fg='black',bg='white')
		Gender.grid(row=3,column=2)

		Price=Entry(new,width=30,highlightbackground="linen",fg='black',bg='white')
		Price.grid(row=4,column=2)

		delete_box=Entry(new,width=30,highlightbackground="linen",fg='black',bg='white')
		delete_box.grid(row=7,column=2)

		#Creating labels
		Petid_l=Label(new,text='Pet ID',fg='dark orange',bg='linen')
		Petid_l.grid(row=0,column=1,padx=10)

		Breed_l=Label(new,text='Breed',fg='dark orange',bg='linen')
		Breed_l.grid(row=1,column=1)

		Age_l=Label(new,text='Age',fg='dark orange',bg='linen')
		Age_l.grid(row=2,column=1)

		Gender_l=Label(new,text='Gender',fg='dark orange',bg='linen')
		Gender_l.grid(row=3,column=1)

		Price_l=Label(new,text='Price',fg='dark orange',bg='linen')
		Price_l.grid(row=4,column=1)

		delete_box_label=Label(new,text="Select ID",fg='dark orange',bg='linen')
		delete_box_label.grid(row=7,column=1,padx=10)

		def update():
			conn = sqlite3.connect('happy_tails.db')
			c = conn.cursor()

			record_id = delete_box.get()

			c.execute("""UPDATE Pets SET
				Pet_id = :id,
				Breed = :breed,
				Age = :age,
				Gender = :gender,
				Price = :price

				WHERE oid = :oid""",
		        {
		        'id': Petid_editor.get(),
		        'breed': Breed_editor.get(),
		        'age': Age_editor.get(),
		        'gender': Gender_editor.get(),
		        'price': Price_editor.get(),
		        'oid': record_id
		        })

			conn.commit()
			conn.close()

			editor.destroy()

		#update records
		def edit():
			global editor
			editor = Tk()
			editor.title('Update A Record')
			editor.geometry("400x300")
			editor.configure(bg="linen")

			conn = sqlite3.connect('happy_tails.db')
			c = conn.cursor()

			record_id=delete_box.get()
			c.execute("SELECT * FROM Pets WHERE oid = " + record_id)
			records=c.fetchall()

			global Petid_editor
			global Breed_editor
			global Age_editor
			global Gender_editor
			global Price_editor

			Petid_editor=Entry(editor,width=30,highlightbackground="linen",fg='black',bg='white')
			Petid_editor.grid(row=0,column=1,padx=20,pady=(10,0))

			Breed_editor=Entry(editor,width=30,highlightbackground="linen",fg='black',bg='white')
			Breed_editor.grid(row=1,column=1)

			Age_editor=Entry(editor,width=30,highlightbackground="linen",fg='black',bg='white')
			Age_editor.grid(row=2,column=1)

			Gender_editor=Entry(editor,width=30,highlightbackground="linen",fg='black',bg='white')
			Gender_editor.grid(row=3,column=1)

			Price_editor=Entry(editor,width=30,highlightbackground="linen",fg='black',bg='white')
			Price_editor.grid(row=4,column=1)

			#Creating labels
			Petid_l=Label(editor,text='Pet ID',fg='dark orange',bg='linen')
			Petid_l.grid(row=0,column=0,pady=(10,0))

			Breed_l=Label(editor,text='Breed',fg='dark orange',bg='linen')
			Breed_l.grid(row=1,column=0)

			Age_l=Label(editor,text='Age',fg='dark orange',bg='linen')
			Age_l.grid(row=2,column=0)

			Gender_l=Label(editor,text='Gender',fg='dark orange',bg='linen')
			Gender_l.grid(row=3,column=0)

			Price_l=Label(editor,text='Price',fg='dark orange',bg='linen')
			Price_l.grid(row=4,column=0)

			for record in records:
				Petid_editor.insert(0,record[0])
				Breed_editor.insert(0,record[1])
				Age_editor.insert(0,record[2])
				Gender_editor.insert(0,record[3])
				Price_editor.insert(0,record[4])

			#Save Button
			edit_btn = Button(editor,text='Save Record',highlightbackground='linen',command=update)
			edit_btn.grid(row=5,column=1,pady=7,padx=2,ipadx=30)

			conn.commit()
			conn.close()

		#delete records
		def delete():
			conn = sqlite3.connect('happy_tails.db')
			c = conn.cursor()

			c.execute("DELETE FROM Pets WHERE oid= " + delete_box.get())

			conn.commit()
			conn.close()

		#submit function
		def submit():
			conn = sqlite3.connect('happy_tails.db')
			c = conn.cursor()

			c.execute("INSERT INTO Pets VALUES (:Pet_id,:Breed,:Age,:Gender,:Price)",
				{
					'Pet_id':Petid.get(),
					'Breed':Breed.get(),
					'Age':Age.get(),
					'Gender':Gender.get(),
					'Price':Price.get()
				})

			conn.commit()
			conn.close()

			Petid.delete(0,END)
			Breed.delete(0,END)
			Age.delete(0,END)
			Gender.delete(0,END)
			Price.delete(0,END)

		#query function
		def query():
			conn = sqlite3.connect('happy_tails.db')
			c = conn.cursor()

			c.execute("SELECT *,oid FROM Pets")
			records=c.fetchall()

			print_records=''
			for record in records:
				print_records+=str(record[0])+' '+str(record[1])+"\n"

			query_label=Label(new,text=print_records,fg='dark orange',bg='linen')
			query_label.grid(row=10,column=2,columnspan=2)



			conn.commit()
			conn.close()


		#creating submit button
		submit_btn=Button(new,text='Add Pet',highlightbackground='linen',command=submit)
		submit_btn.grid(row=5,column=2,pady=7,padx=2,ipadx=50)

		#Query Button
		query_btn = Button(new,text='Show Records',highlightbackground='linen',command=query)
		query_btn.grid(row=6,column=2,pady=7,padx=2,ipadx=30)

		#Delete Button
		delete_btn = Button(new,text='Delete Record',highlightbackground='linen',command=delete)
		delete_btn.grid(row=8,column=2,pady=7,padx=2,ipadx=30)

		edit_btn = Button(new,text='Edit Record',highlightbackground='linen',command=edit)
		edit_btn.grid(row=9,column=2,pady=7,padx=2,ipadx=30)


	else:
		messagebox.showerror(title='Error',message='Invalid login')

	

	username.delete(0,END)
	password.delete(0,END)

	conn.commit()
	conn.close()

#login button
login_btn=Button(upframe,text='Login',highlightbackground='linen',command=login)
login_btn.grid(row=2,column=1)

#Adopt Button
adopt_button = Button(downframe, text='Adopt Pet', fg='DarkOrange3',highlightbackground='linen', width=15,command=adopt)
# Calculate the position of the button based on the size of tableframe
button_x = 1 + (1380 - 750)  
button_y = 340 + 10  
adopt_button.place(x=button_x, y=button_y)


'''
c.execute("""CREATE TABLE Pets(
	Pet_id integer,
	Breed text,
	Age integer,
	Gender text,
	Price integer
	)""")

c.execute("""CREATE TABLE LOG(
	user text,
	pas text
	)""")
'''

conn.commit()
conn.close()

root.mainloop()