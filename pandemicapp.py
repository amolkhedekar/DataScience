from tkinter import *
panwin = Tk()
panwin.title("Pandemic Analytics")

# size of window
panwin.geometry('500x280')

# corona Image
corphoto = PhotoImage(file="corona.png")
corphotoin = corphoto.subsample(20, 20)
icon = Button(panwin, image=corphotoin)
icon.place(x=50, y=35, anchor="center")

# Title of analyzer
titlepan = Label(panwin, text="Pandemic Analyzer")
titlepan.place(x=250, y=25, anchor="center")

state = Label(panwin, text="Select State")
state.place(x=125, y=85, anchor="center")
statelist = ['Andaman and Nicobar',
             'Andhra Pradesh',
             'Arunachal Pradesh',
             'Assam',
             'Bihar',
             'Chandigarh',
             'Chhattisgarh',
             'Dadra and Nagar Haveli',
             'Delhi',
             'Goa',
             'Gujarat',
             'Haryana',
             'Himachal Pradesh',
             'Jammu and Kashmir',
             'Jharkhand',
             'Karnataka',
             'Kerala',
             'Ladakh',
             'Lakshadweep',
             'Madhya Pradesh',
             'Maharashtra',
             'Manipur',
             'Meghalaya',
             'Mizoram',
             'Nagaland',
             'Odisha',
             'Puducherry',
             'Punjab',
             'Rajasthan',
             'Sikkim',
             'Tamil Nadu',
             'Telengana',
             'Tripura',
             'Uttar Pradesh',
             'Uttarakhand',
             'West Bengal']

variable = StringVar(panwin)
variable.set(statelist[0])
states = OptionMenu(panwin, variable, *statelist)
states.place(x=300, y=85, anchor="center")

panwin.mainloop()
