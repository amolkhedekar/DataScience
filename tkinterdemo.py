from tkinter import *  # tkinter module is imported
import csv  # csv module is imported
import tkinter.font as tkFont  # font is imported for using font family
# statelist for state option menu
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

# IMR function to calculate imr value


def IMR():
    valinp.delete(first=0, last=100)
    inf = infinp.get()
    inf = int(inf)
    decr = decinp.get()
    decr = int(decr)
    state1 = variable.get()
    res = ((decr/inf)*1000)
    mystr = "IMR value of  "+state1+" is "+str(res)
    valinp.insert(0, mystr)
    infinp.delete(first=1, last=100)
    decinp.delete(first=1, last=100)

# CMR function to calculate CMR value


def CMR():
    valinp.delete(first=1, last=100)
    reck = recinp.get()
    reck = int(reck)
    decr = decinp.get()
    decr = int(decr)
    state1 = variable.get()
    res = ((decr/(reck+decr))*100)
    mystr = "CMR value of "+state1+" is "+str(res)
    valinp.insert(0, mystr)
    recinp.delete(first=1, last=100)
    decinp.delete(first=1, last=100)


def read_from_file(state):
    f = open('covidfile.csv')
    csv_f = csv.reader(f)
    result = {}
    for row in csv_f:
        if state in row[0]:
            result['State'] = state
            result['Infected'] = row[1]
            result['Recovered'] = row[3]
            result['Deceased'] = row[4]
    return result


def OptionMenu_SelectionEvent(event):
    selected_state = variable.get()
    record = read_from_file(selected_state)
    infinp.insert(0, record['Infected'])
    recinp.insert(0, record['Recovered'])
    decinp.insert(0, record['Deceased'])

    # tkinter window is initialized
panwin = Tk()

# title for window
panwin.title("Pandemic Analytics")

# size of window
panwin.geometry('700x480')
panwin.configure(bg="white")

# font declearation
fontStyle = tkFont.Font(family="Times", size=40)
fontStyle1 = tkFont.Font(family="Times", size=20)
fontStyle2 = tkFont.Font(family="Times", size=20)

# corona Image
corphoto = PhotoImage(file="corona.png")
corphotoin = corphoto.subsample(20, 20)
icon = Button(panwin, image=corphotoin)
icon.place(x=50, y=35, anchor="center")

# Title of analyzer
titlepan = Label(panwin, text="Pandemic Analyzer", font=fontStyle)
titlepan.place(x=250, y=25, anchor="center")

# state list
state = Label(panwin, text="Select State", font=fontStyle1)
state.place(x=125, y=85, anchor="center")
variable = StringVar(panwin)
variable.set(statelist[0])
states = OptionMenu(panwin, variable, *statelist,
                    command=OptionMenu_SelectionEvent)
states.place(x=300, y=85, anchor="center")

# infected number label & entry
infected = Label(panwin, text="Infected", font=fontStyle1, fg="yellow4")
infected.place(x=125, y=120, anchor="center")
infinp = Entry(panwin, bd=1, bg="yellow")
infinp.place(x=300, y=120, anchor="center")

# recovered number label & entry
recovered = Label(panwin, text="Recovered", font=fontStyle1, fg="green")
recovered.place(x=125, y=155, anchor="center")
recinp = Entry(panwin, bd=1, bg="green")
recinp.place(x=300, y=155, anchor="center")

# decreased number label & entry
decreased = Label(panwin, text="Decreased", font=fontStyle1, fg="red")
decreased.place(x=125, y=190, anchor="center")
decinp = Entry(panwin, bd=1, bg="red")
decinp.place(x=300, y=190, anchor="center",)

# IMR & CMR Buttons
imrbtn = Button(panwin, text="IMR", width=5, height=1, command=IMR)
imrbtn.place(x=200, y=220, anchor="center")
cmrbtn = Button(panwin, text="CMR", width=5, height=1, command=CMR)
cmrbtn.place(x=300, y=220, anchor="center")

# To Show result
value = Label(panwin, text="Value", font=fontStyle1)
value.place(x=125, y=250, anchor="center")
valinp = Entry(panwin, bd=1, width=25)
valinp.place(x=300, y=250, anchor="center")
panwin.mainloop()
