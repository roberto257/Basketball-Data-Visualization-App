#Basketball DataVis (Data Visualization)
#pylint:disable = W0614
#By Robert Smith

#Import 
import tkinter
import os
from tkinter import *

#Import the data file
NBAData = os.system("NBAdata.py")

#Create the main window
window = tkinter.Tk()
window.title("Basketball DataVis")
window.geometry("480x250")
window.configure(background = "grey")

#Data



#COLLEGE DATA

#Add a button to select a team
teamvar = StringVar(window)
teamvar.set("Select Team...")

#Team selection
if teamvar.get() == "Denver Nuggets": NBAData.DEN
if teamvar.get() == "Oklahoma City Thunder" : NBAData.OKC
if teamvar.get() == "Portland Trail Blazers" : NBAData.POR
if teamvar.get() == "Utah Jazz" : NBAData.UTA
if teamvar.get() == "Minnesota Timberwolves" : NBAData.MIN
if teamvar.get() == "Atlanta Hawks": NBAData.ATL
if teamvar.get() == "Boston Celtics" : NBAData.BOS
if teamvar.get() == "Brooklyn Nets" : NBAData.BKN
if teamvar.get() == "Charlotte Hornets" : NBAData.CHA
if teamvar.get() == "Chicago Bulls" : NBAData.CHI
if teamvar.get() == "Cleveland Cavaliers": NBAData.CLE
if teamvar.get() == "Dallas Mavericks" : NBAData.DAL
if teamvar.get() == "Detroit Pistons" : NBAData.DET
if teamvar.get() == "Golden State Warriors" : NBAData.GSW
if teamvar.get() == "Houston Rockets" : NBAData.HOU
if teamvar.get() == "Indiana Pacers": NBAData.IND
if teamvar.get() == "LA Clippers" : NBAData.LAC
if teamvar.get() == "LA Lakers" : NBAData.LAL
if teamvar.get() == "Memphis Grizzlies" : NBAData.MEM
if teamvar.get() == "Miami Heat" : NBAData.MIA
if teamvar.get() == "Milwaukee Bucks": NBAData.MIL
if teamvar.get() == "New Orleans Pelicans" : NBAData.NOP
if teamvar.get() == "New York Knicks" : NBAData.NYK
if teamvar.get() == "Philadelphia 76ers" : NBAData.PHI
if teamvar.get() == "Phoenix Suns" : NBAData.PHX
if teamvar.get() == "Sacramento Kings": NBAData.SAC
if teamvar.get() == "San Antonio Spurs" : NBAData.SAS
if teamvar.get() == "Toronto Raptors" : NBAData.TOR
if teamvar.get() == "Washington Wizards" : NBAData.WAS
if teamvar.get() == "Orlando Magics" : NBAData.ORL
    
#Start the first label for the window
labelone = Label(window, 
text="Welcome to Basketball DataVis!", 
font = ("Arial Bold", 31),
relief = RAISED)
labelone.configure(background = "grey")
labelone.grid(column = 0, 
row = 0, 
columnspan = 16, 
rowspan = 10, 
sticky = NW)

#Add the first image that goes with the first label
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'mj.gif')
mjgif = PhotoImage(file=image_path)
mjimg = Label(image = mjgif)
mjimg.image = mjgif
mjimg.grid(column = 1, row = 10, sticky = N)

datatype_label = Label(window, 
text="NBA Data", 
font = ("Arial", 28),
relief=GROOVE)
datatype_label.configure(background="grey")
datatype_label.grid(column=0, 
row=10, 
rowspan=2, 
sticky=NW)

#Add a button to exit the window
def quitwindow():
    window.destroy()

quitbutton = Button(window, 
text="Quit", 
command=quitwindow)
quitbutton.configure(background = "black")
quitbutton.grid(column=11, 
row=10, 
pady=180, 
sticky=E)

#Define a search variable
searchvar = "Player 1"

#Add a entry box to use to search
searchbox = Entry(window, textvariable=searchvar, relief=RAISED, width=18)
searchbox.configure(background="grey")
searchbox.grid(column=11,
row=10,
padx=5,
pady=75,
sticky=NW)

#Create the search function
def searchdata():
        if teamvar.get() == "Denver Nuggets":
                if searchbox.get() in NBAData.DEN:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.DEN.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Oklahoma City Thunder":
                if searchbox.get() in NBAData.OKC:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.OKC.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Portland Trail Blazers":
                if searchbox.get() in NBAData.POR:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.POR.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Utah Jazz":
                if searchbox.get() in NBAData.UTA:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.UTA.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Minnesota Timberwolves":
                if searchbox.get() in NBAData.MIN:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.MIN.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Atlanta Hawks":
                if searchbox.get() in NBAData.ATL:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.ATL.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Milwaukee Bucks":
                if searchbox.get() in NBAData.MIL:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.MIL.get(searchresult))
                        searchres.pack()
                        mainloop()  
        if teamvar.get() == "New Orleans Pelicans":
                if searchbox.get() in NBAData.NOP:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.NOP.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "New York Knicks":
                if searchbox.get() in NBAData.NYK:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.NYK.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Orlando Magic":
                if searchbox.get() in NBAData.ORL:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.ORL.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Philadelphia 76ers":
                if searchbox.get() in NBAData.PHI:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.PHI.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Phoenix Suns":
                if searchbox.get() in NBAData.PHX:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.PHX.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Sacramento Kings":
                if searchbox.get() in NBAData.SAC:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.SAC.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "San Antonio Spurs":
                if searchbox.get() in NBAData.SAS:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.SAS.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Toronto Raptors":
                if searchbox.get() in NBAData.TOR:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.TOR.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Washington Wizards":
                if searchbox.get() in NBAData.WAS:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.WAS.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Boston Celtics":
                if searchbox.get() in NBAData.BOS:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.BOS.get(searchresult))
                        searchres.pack()
                        mainloop()  
        if teamvar.get() == "Brooklyn Nets":
                if searchbox.get() in NBAData.BKN:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.BKN.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Charlotte Hornets":
                if searchbox.get() in NBAData.CHA:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.CHA.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Chicago Bulls":
                if searchbox.get() in NBAData.CHI:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.CHI.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Cleveland Cavaliers":
                if searchbox.get() in NBAData.CLE:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.CLE.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Dallas Mavericks":
                if searchbox.get() in NBAData.DAL:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.DAL.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Detroit Pistons":
                if searchbox.get() in NBAData.DET:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.DET.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Golden State Warriors":
                if searchbox.get() in NBAData.GSW:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.GSW.get(searchresult))
                        searchres.pack()
                        mainloop() 
        if teamvar.get() == "Houston Rockets":
                if searchbox.get() in NBAData.HOU:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.HOU.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Indiana Pacers":
                if searchbox.get() in NBAData.IND:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.IND.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "LA Clippers":
                if searchbox.get() in NBAData.LAC:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.LAC.get(searchresult))
                        searchres.pack()
                        mainloop()  
        if teamvar.get() == "LA Lakers":
                if searchbox.get() in NBAData.LAL:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.LAL.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Memphis Grizzlies":
                if searchbox.get() in NBAData.MEM:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.MEM.get(searchresult))
                        searchres.pack()
                        mainloop()
        if teamvar.get() == "Miami Heat":
                if searchbox.get() in NBAData.MIA:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = NBAData.MIA.get(searchresult))
                        searchres.pack()
                        mainloop()
    
#Add a search button to start the search
gosearch = Button(window, 
text = "GO", 
command = searchdata)
gosearch.configure(background = "black")
gosearch.grid(column = 11, 
row = 10, 
pady = 75)

teamselect = OptionMenu(window, 
teamvar,
"Atlanta Hawks",
"Boston Celtics",
"Brooklyn Nets",
"Charlotte Hornets",
"Chicago Bulls",
"Cleveland Cavaliers",
"Dallas Mavericks",
"Denver Nuggets",
"Detroit Pistons",
"Golden State Warriors",
"Houston Rockets",
"Indiana Pacers",
"LA Clippers",
"LA Lakers",
"Memphis Grizzlies",
"Miami Heat",
"Milwaukee Bucks",
"Minnesota Timberwolves",
"New Orleans Pelicans",
"New York Knicks",
"Oklahoma City Thunder",
"Orlando Magic",
"Philadelphia 76ers",
"Phoenix Suns",
"Portland Trail Blazers",
"Sacramento Kings",
"San Antonio Spurs",
"Toronto Raptors",
"Utah Jazz",
"Washington Wizards")
teamselect.configure(background = "black")
teamselect.grid(column=11, 
row=10, 
pady = 30,
sticky=NW)

#End the main loop
window.mainloop()