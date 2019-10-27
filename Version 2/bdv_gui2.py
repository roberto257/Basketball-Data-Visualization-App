#Basketball DataVis (Data Visualization)
#pylint:disable = W0614
#By Robert Smith

#Import 
import tkinter
import os
from tkinter import *
import importlib 

#Import the data file
NBAdata = importlib.import_module("NBAdata")

#Create the main window
window = tkinter.Tk()
window.title("Basketball DataVis")
window.geometry("480x250")
window.configure(background = "grey")

#Add a button to select a team
teamvar = StringVar(window)
teamvar.set("Select Team...")

#Dictionary to get the dictionary from NBAData
#This dictionary replaces the old method of getting
#the teamvar 30 different times.

nbaTeams = {
        "Philadelphia 76ers" : NBAdata.PHI,
        "Toronto Raptors" : NBAdata.TOR,
        "Brooklyn Nets" : NBAdata.BKN,
        "New York Knicks" : NBAdata.NYK,
        "Milwaukee Bucks" : NBAdata.MIL,
        "Cleveland Cavaliers" : NBAdata.CLE,
        "Detroit Pistons" : NBAdata.DET,
        "Chicago Bulls" : NBAdata.CHI,
        "Indiana Pacers" : NBAdata.IND,
        "Atlanta Hawks" : NBAdata.ATL,
        "Miami Heat" : NBAdata.MIA,
        "Orlando Magic" : NBAdata.ORL,
        "Charlotte Hornets" : NBAdata.CHA,
        "Washington Wizards" : NBAdata.WAS,
        "Denver Nuggets" : NBAdata.DEN,
        "Minnesota Timberwolves" : NBAdata.MIN,
        "Utah Jazz" : NBAdata.UTA,
        "Portland Trailblazers" : NBAdata.POR,
        "Oklahoma City Thunder" : NBAdata.OKC,
        "Phoenix Suns" : NBAdata.PHX,
        "LA Clippers" : NBAdata.LAC,
        "Golden State Warriors" : NBAdata.GSW,
        "Sacramento Kings" : NBAdata.SAC,
        "Dallas Mavericks" : NBAdata.DAL,
        "San Antonio Spurs" : NBAdata.SAS,
        "Houston Rockets" : NBAdata.HOU,
        "Memphis Grizzlies" : NBAdata.MEM,
        "New Orleans Pelicans" : NBAdata.NOP
}
    
#Start the first label for the window
labelone = Label(window, 
text = "Welcome to Basketball DataVis!", 
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
mjgif = PhotoImage(file = image_path)
mjimg = Label(image = mjgif)
mjimg.image = mjgif
mjimg.grid(column = 1, row = 10, sticky = N)

datatype_label = Label(window, 
text = "NBA Data", 
font = ("Arial", 28),
relief = GROOVE)
datatype_label.configure(background = "grey")
datatype_label.grid(column = 0, 
row = 10, 
rowspan = 2, 
sticky = NW)

#Add a button to exit the window
def quitwindow():
    window.destroy()

quitbutton = Button(window, 
text = "Quit", 
command = quitwindow)
quitbutton.configure(background = "black")
quitbutton.grid(column = 11, 
row = 10, 
pady = 180, 
sticky = E)

#Define a search variable
searchvar = "Player 1"

#Add a entry box to use to search
searchbox = Entry(window, textvariable = searchvar, relief = RAISED, width = 18)
searchbox.configure(background = "grey")
searchbox.grid(column = 11,
row = 10,
padx  = 5,
pady = 75,
sticky = NW)

#Create the search function
def searchdata():
        #Take the team, and get their dictionary
        if teamvar.get() in nbaTeams:
                #Set a new variable for us to search
                thisDict = nbaTeams[(teamvar.get())]
                #If the player is in the dictionary of their team, output
                if searchbox.get() in thisDict:
                        searchresult = searchbox.get()
                        result = tkinter.Tk()
                        result.title(searchbox.get())
                        result.geometry("200x75")
                        searchres = Label(result, text = thisDict.get(searchresult))
                        searchres.pack()
                        mainloop()
                #If the player is not found
                else:
                        print("Player not found")
    
#Add a search button to start the search
gosearch = Button(window, 
text = "GO", 
command = searchdata)
gosearch.configure(background = "black")
gosearch.grid(column = 11, 
row = 10, 
pady = 75)

#All the teams we can choose from
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