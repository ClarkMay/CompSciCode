#library for creating the GUI
from tkinter import *
import tkinter as tk

#All The Arrays For Player Statistics
points = []
assists = []
rebounds = []
steals = []
blocks = []
fouls = []
fgShot = []
fgAttempt = []
threePointAttempt = []
threePointScored = []
freeThrowMade = []
freeThrowMissed = []
assistMade_Array = []
fgShot_Array = []
fgMade_Array = []
rebounds_Array = []
steal_Array = []
block_Array = []
foul_Array = []
threePointMade_Array = []
freeThrowMade_Array = []
freeThrowMissed_Array = []
fgAttempt_Array = []
threePointAttempt_Array = []
totalPoints = 0 #Total Points For Home Team
visitorScore = [] #Total Visitor Score
global visitorFoul
visitorFoul = 0 #Total Visitor Fouls
visitorScore_Array =[]

playerList = [] #Empty Player List

global buttonPress
buttonPress = False #The Add Player
global k
k = 1

#global playerCount

root = Tk()
newWindow = Tk()

root.title("Bearkats Stat Tracker")
root.geometry("1920x1080")
root.configure(background="gray30")

def gameWindow():
    statTracker()  # Draws The GUI
    root.deiconify()  # Makes Game Window Reappear
    newWindow.destroy()  # Destroys The First Window

def mainWindow():
    root.withdraw()  # This Hides The Game Window
    newWindow.title("Roster Import")  # Title For Window
    newWindow.geometry("480x270")  # Creates The Size For The Window
    newWindow.configure(background="gray30")  # Changes The Background Of The Window
    global k  # calling global int k

    if buttonPress == True:  # Insert Player Button
        k += 1  # Counts Up One (Tracks what number player it is)
        str(k)  # Changes K To A String so that it can be used in the Button and label "text"
        players = playerInput.get()
        playerList.append(players)  # adds player into the List
    playerInput.delete(0, 'end')  # clears Entry Box

    Button(newWindow, text='Insert Player ' + str(k), bg="black", command=buttonPressTrue, fg="white",
           highlightbackground="gray90",
           activebackground="deep sky blue").place(x=130, y=60, height=33, width=150) #GUI For The Insert Player Button
    Label(newWindow, text='Player ' + str(k) + " Name", bg="black", fg="white", highlightbackground="gray90")\
        .place(x=5, y=15, height=35, width=110) #GUI For Top Player Label

playerInput = Entry(newWindow)  # Input Box
playerInput.place(x=5, y=60, height=30, width=110)  # Placing the Input Box


# Makes buttonPress True so that Player is saved into playerList, and allows user to insert more players
def buttonPressTrue():
    global buttonPress
    buttonPress = True
    mainWindow()

Button(newWindow, text='Start Game', bg="black", command=gameWindow, fg="white", highlightbackground="gray90", activebackground="deep sky blue").place(x=130, y=120, height=33, width=150)  # GUI For The Start Game Button

def fieldGoalAttempt(j):
    get_fgAttempt = fgAttempt[j].get()
    add_fgAttempt = int(get_fgAttempt) + 1

    fgAttempt[j].delete(0, tk.END)
    fgAttempt[j].insert(0, add_fgAttempt)

def fieldGoalShot(j):
    get_fgShot = fgShot[j].get()
    add_fgShot = int(get_fgShot) + 1

    fgShot[j].delete(0, tk.END)
    fgShot[j].insert(0, add_fgShot)

def threePointerAttempted(j):
    get_threePointAttempt = threePointAttempt[j].get()
    add_threePointAttempt = int(get_threePointAttempt) + 1

    threePointAttempt[j].delete(0, tk.END)
    threePointAttempt[j].insert(0, add_threePointAttempt)

def threePointerScored(j):
    get_threePointScored = threePointScored[j].get()
    add_threePointScored = int(get_threePointScored) + 1

    threePointScored[j].delete(0, tk.END)
    threePointScored[j].insert(0, add_threePointScored)

def addAssists(j):
    get_assists = assists[j].get()
    add_assists = int(get_assists) + 1

    assists[j].delete(0, tk.END)
    assists[j].insert(0, add_assists)

def addRebounds(j):
    get_rebounds = rebounds[j].get()
    add_rebounds = int(get_rebounds) + 1

    rebounds[j].delete(0, tk.END)
    rebounds[j].insert(0, add_rebounds)

def addSteals(j):
    get_steals = steals[j].get()
    add_steals = int(get_steals) + 1

    steals[j].delete(0, tk.END)
    steals[j].insert(0, add_steals)

def addBlocks(j):
    get_blocks = blocks[j].get()
    add_blocks = int(get_blocks) + 1

    blocks[j].delete(0, tk.END)
    blocks[j].insert(0, add_blocks)

def freeThrowMiss(j):
    get_ftMissed = freeThrowMissed[j].get()
    add_ftMissed = int(get_ftMissed) + 1

    freeThrowMissed[j].delete(0, tk.END)
    freeThrowMissed[j].insert(0, add_ftMissed)

def visitorScores(j):
    get_visitorScore = visitorScore[j].get()
    add_visitorScore = int(get_visitorScore) + 1

    visitorScore[j].delete(0, tk.END)
    visitorScore[j].insert(0, add_visitorScore)

def statTracker():
    global playerCount
    playerCount = len(playerList) #Finds The Number Of Players In The List So The Appropriate Amount Of Stat GUIs are Created
    pointCounter = 0
    xCoordinate = 0 #Instantiating xCoordinate
    yCoordinate = 120 #Instantiating yCoordinate
    for j in range(0, playerCount): #for-loop that creates a Stat GUI for Each Player in playerList
        if j == 9 :#Moves Every Stat GUI after 9 Down in the Window So That 18 Stat GUIs can fit as opposed to just 9
            yCoordinate = 600
        if j == 9:
            xCoordinate = 0
        xCoordinate += 175  # Seperates each Stat GUI

        playerLabel = Label(root, text=playerList[j], bg="white", fg="black", highlightbackground="gray90", borderwidth=1,
                            relief="raised").place(x=5 + xCoordinate, y=5 + yCoordinate, height=30, width=150) #Player Name & Number Label

        #GUI For points
        pointLabel = Label(root, text="Points ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1,
                           relief="raised").place(x=5 + xCoordinate, y = 40 + yCoordinate, height=30, width=55)
        boxname = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        points.append(boxname)
        points[j].insert(0, 0)
        boxname.place(x=60 + xCoordinate, y=40 + yCoordinate, height=30, width=95)

        #GUI For assists Label & Box
        assistLabel = Label(root, text="Assists ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y = 70 + yCoordinate, height=30, width=55)
        assistBox = Entry(root,bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        assists.append(assistBox)
        assists[j].insert(0, 0)
        assistBox.place(x=60 + xCoordinate, y=70 + yCoordinate, height=30, width=95)

        #GUI For the Plus button that adds an assist to the respective player
        assistAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addAssists(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        assistMade_Array.append(assistAddition)
        assistAddition.place(x = 120 + xCoordinate, y = 76 + yCoordinate, height=20, width=20)

        #GUI For Rebounds Label & Box
        reboundLabel = Label(root, text="Rebounds ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y = 100 + yCoordinate, height=30, width=55)
        reboundBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        rebounds.append(reboundBox)
        rebounds[j].insert(0, 0)
        reboundBox.place(x=60 + xCoordinate, y = 100 + yCoordinate, height=30, width=95)

        #GUI & functionality For the Plus button that adds a rebound to the respective player
        reboundAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addRebounds(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        rebounds_Array.append(reboundAddition)
        reboundAddition.place(x = 120 + xCoordinate, y = 106 + yCoordinate, height=20, width=20)

        #GUI For Steals Label & Box
        stealLabel = Label(root, text="Steals ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=130 + yCoordinate, height=30, width=55)
        stealBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        steals.append(stealBox)
        steals[j].insert(0, 0)
        stealBox.place(x=60 + xCoordinate, y = 130 + yCoordinate, height=30, width=95)

        #GUI & functionality For the Plus button that adds a steal to the respective player
        stealAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addSteals(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        steal_Array.append(stealAddition)
        stealAddition.place(x = 120 + xCoordinate, y = 136 + yCoordinate, height=20, width=20)

        #GUI For Blocks Label & Box
        blockLabel = Label(root, text="Blocks ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=160 + yCoordinate, height=30, width=55)
        blockBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        blocks.append(blockBox)
        blocks[j].insert(0, 0)
        blockBox.place(x=60 + xCoordinate, y = 160 + yCoordinate, height=30, width=95)

        #GUI & functionality For the Plus button that adds a block to the respective player
        blockAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addBlocks(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        block_Array.append(blockAddition)
        blockAddition.place(x = 120 + xCoordinate, y = 166 + yCoordinate, height=20, width=20)

        #GUI For Fouls Label & Box
        foulsLabel = Label(root, text="Fouls ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=190 + yCoordinate, height=30, width=55)
        foulsBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        fouls.append(foulsBox)
        fouls[j].insert(0, 0)
        foulsBox.place(x=60 + xCoordinate, y = 190 + yCoordinate, height=30, width=95)

        #GUI & functionality For the Plus button that adds a foul to the respective player
        foulsAddition = Button(root, text='+', command = lambda pointCounter=pointCounter: addFouls(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        foul_Array.append(foulsAddition)
        foulsAddition.place(x = 120 + xCoordinate, y = 195 + yCoordinate, height=20, width=20)

        #GUI & functionality For the FG Made button that adds a FG attempt, & FG Made to the respective player
        fgMade = Button(root, text='FG Made',
                        command=lambda pointCounter=pointCounter: [fieldGoalShot(pointCounter), fieldGoalAttempt(pointCounter),fgMade_Fun(pointCounter)],bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",
                        activebackground="deep sky blue")
        fgMade_Array.append(fgMade)
        fgMade.place(x=5 + xCoordinate, y=310 + yCoordinate, height=50, width=75)

        #GUI & functionality For the FG Missed button that adds a FG attempt to the respective player
        fgMissed = Button(root, text='FG Missed',
                                  command=lambda pointCounter=pointCounter: fieldGoalAttempt(pointCounter)
                                  , bg="white", fg="black", highlightbackground="gray90", borderwidth=2,
                                  relief="raised", activebackground="deep sky blue")
        fgAttempt_Array.append(fgMissed)
        fgMissed.place(x=80 + xCoordinate, y=310 + yCoordinate, height=50, width=75)

        #GUI & functionality For the 3PT Made button that adds a FG attempt, FG Made, 3PT attempt & 3PT Made to the respective player
        threePointFGMadeButton = Button(root, text='3PT Made',
                                  command=lambda pointCounter=pointCounter:[fieldGoalShot(pointCounter),fieldGoalAttempt(pointCounter), threePointerMade(pointCounter),
                                      threePointerScored(pointCounter), threePointerAttempted(pointCounter)]
                                  , bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",activebackground="deep sky blue")
        threePointMade_Array.append(threePointFGMadeButton)
        threePointFGMadeButton.place(x=5 + xCoordinate, y=360 + yCoordinate, height=50, width=75)

        #GUI & functionality For the 3PT Missed button that adds a FG attempt & 3PT attempt to the respective player
        threePointMissed = Button(root, text='3PT Missed', command=lambda pointCounter=pointCounter:[threePointerAttempted(pointCounter),fieldGoalAttempt(pointCounter)], bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",activebackground="deep sky blue")
        threePointAttempt_Array.append(threePointMissed)
        threePointMissed.place(x=80 + xCoordinate, y=360 + yCoordinate, height=50, width=75)

        #GUI & functionality For the FT Percentage Label
        freeThrowLabel = Label(root, text="FT %: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1,
                           relief="raised").place(x=5 + xCoordinate, y=280 + yCoordinate, height=30, width=55)
        freeThrowFGMade = Button(root, text='FT Made', command=lambda pointCounter=pointCounter: [freeThrowMake(pointCounter), freeThrowMiss(pointCounter)], bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",activebackground="deep sky blue")
        freeThrowMade_Array.append(freeThrowFGMade)
        freeThrowFGMade.place(x=5 + xCoordinate, y=410 + yCoordinate, height=50, width=75)

        #GUI & functionality For the freeThrowMade to the respective player
        ftMadeBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        freeThrowMade.append(ftMadeBox)
        freeThrowMade[j].insert(0, 0)
        ftMadeBox.place(x=60 + xCoordinate, y=280 + yCoordinate, height=30, width=47)

        #free throw missed
        ftBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        freeThrowMissed.append(ftBox)
        freeThrowMissed[j].insert(0, 0)
        ftBox.place(x=107.5 + xCoordinate, y=280 + yCoordinate, height=30, width=47)

        #GUI & functionality For the FT Missed button that adds a FT attempt to the respective player
        freeThrowFGMissed = Button(root, text='FT Missed',
                                 command=lambda pointCounter=pointCounter: freeThrowMiss(pointCounter), bg="white",
                                 fg="black", highlightbackground="gray90", borderwidth=2, relief="raised",
                                 activebackground="deep sky blue")
        freeThrowMissed_Array.append(freeThrowFGMissed)
        freeThrowFGMissed.place(x=80 + xCoordinate, y=410 + yCoordinate, height=50, width=75)

        #GUI & functionality For the FG Percentage Label
        fgLabel = Label(root, text="FG %: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=220 + yCoordinate, height=30, width=55)
        fgBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        fgShot.append(fgBox)
        fgShot[j].insert(0, 0)
        fgBox.place(x=60 + xCoordinate, y=220 + yCoordinate, height=30, width=47.5)

        fgAttemptBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        fgAttempt.append(fgAttemptBox)
        fgAttempt[j].insert(0, 0)
        fgAttemptBox.place(x=107.5 + xCoordinate, y=220 + yCoordinate, height=30, width=47)

        #GUI & functionality For the 3PT Percentage Label
        threePointPercentage = Label(root, text="3PT %: ", bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="raised").place(x=5 + xCoordinate, y=250 + yCoordinate, height=30, width=55)
        threePointAttemptBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        threePointAttempt.append(threePointAttemptBox)
        threePointAttempt[j].insert(0, 0)
        threePointAttemptBox.place(x=107.5 + xCoordinate, y=250 + yCoordinate, height=30, width=47)

        threePointMadeBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        threePointScored.append(threePointMadeBox)
        threePointScored[j].insert(0, 0)
        threePointMadeBox.place(x=60 + xCoordinate, y=250 + yCoordinate, height=30, width=47)

        #bearkats box
        Label(root, text="Bearkats", bg="white", fg="black", borderwidth=1, relief="raised").place(x=730, y=15, height=30, width=150)
        Label(root, text="Visitor", bg="white", fg="black", borderwidth=1, relief="raised").place(x=730, y=45, height=30, width=150)

        global bearkatBox
        bearkatBox = Entry(root,bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="solid")
        bearkatBox.place(x=880, y=15, height=30, width=150)
        #bearkat Fouls
        Label(root, text="Fouls: ", bg="white", fg="black", borderwidth=1, relief="solid").place(x=1030, y=15, height=30, width=50)

        global bearkatFouls
        bearkatFouls = Entry(root,bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="solid")
        bearkatFouls.place(x=1080, y=15, height=30, width=50)

        #visitor box
        visitorBox = Entry(root, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised")
        visitorScore.append(visitorBox)
        visitorScore[j].insert(0, 0)
        visitorBox.place(x=880, y = 45, height=30, width=150)

        #visitor fouls
        global visitorFoulsBox
        Label(root, text="Fouls: ", bg="white", fg="black", borderwidth=1, relief="solid").place(x=1030, y=45, height=30, width=50)
        visitorFoulsBox = Entry(root,bg="white", fg="black", highlightbackground="gray90", borderwidth=1, relief="solid")
        visitorFoulAddition = Button(root, text='Foul Committed', command = lambda pointCounter=pointCounter: visitorFouls(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        visitorFoulAddition.place(x=1130, y=45, height=30, width=100)
        visitorFoulsBox.place(x=1080, y=45, height=30, width=50)

        #visitor score
        visitorAddition = Button(root, text='Add Points', command = lambda pointCounter=pointCounter: visitorScores(pointCounter),bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue")
        visitorScore_Array.append(visitorAddition)
        visitorAddition.place(x = 655, y = 45, height=30, width=75)

        pointCounter += 1

def visitorFouls(j):
    global visitorFoul
    visitorFoul += 1

    visitorFoulsBox.delete(0, tk.END)
    visitorFoulsBox.insert(0, visitorFoul)

    if visitorFoul == 5:
        bonusMessage = tk.Tk()
        bonusMessage.title("BONUS MESSAGE")
        tk.Label(bonusMessage, text="Bearkats Are In The Bonus").place(x=50, y=10, height=100,width=150)
        tk.Button(bonusMessage, text="Understood", command=bonusMessage.destroy).place(x=50, y=90, height=100,
                                                                                         width=100)
def addFouls(j):
    totalFouls = 1
    get_fouls = fouls[j].get()
    add_fouls = int(get_fouls) + 1

    for i in range(playerCount):
        totalGetFouls = fouls[i].get()
        intTotalGetFouls = int(totalGetFouls)
        totalFouls = totalFouls + intTotalGetFouls

    bearkatFouls.delete(0, tk.END)
    bearkatFouls.insert(0, totalFouls)

    fouls[j].delete(0, tk.END)
    fouls[j].insert(0, add_fouls)

    if totalFouls == 5:
        bonusMessage = tk.Tk()
        bonusMessage.title("BONUS MESSAGE")
        tk.Label(bonusMessage, text="Visitors Are Now In The Bonus").place(x=50, y=10, height=100,width=150)
        tk.Button(bonusMessage, text="Understood", command=bonusMessage.destroy).place(x=50, y=90, height=100,
                                                                                         width=100)
def fgMade_Fun(j):
    totalPoints = 0
    get_points = points[j].get()
    add_points = int(get_points) + 2

    points[j].delete(0, tk.END)
    points[j].insert(0, add_points)

    for i in range(playerCount):
        totalGetPoints = points[i].get()
        intTotalGetPoints = int(totalGetPoints)
        totalPoints = totalPoints + intTotalGetPoints

    bearkatBox.delete(0, totalPoints)
    bearkatBox.insert(0, totalPoints)

def threePointerMade(j):
    totalPoints = 0
    get_points = points[j].get()
    add_points = int(get_points) + 3

    points[j].delete(0, tk.END)
    points[j].insert(0, add_points)

    for i in range(playerCount):
        totalGetPoints = points[i].get()
        intTotalGetPoints = int(totalGetPoints)
        totalPoints = totalPoints + intTotalGetPoints

    bearkatBox.delete(0, totalPoints)
    bearkatBox.insert(0, totalPoints)

def freeThrowMake(j):
    totalPoints = 0
    get_points = points[j].get()
    add_points = int(get_points) + 1

    points[j].delete(0, tk.END)
    points[j].insert(0, add_points)

    for i in range(playerCount):
        totalGetPoints = points[i].get()
        intTotalGetPoints = int(totalGetPoints)
        totalPoints = totalPoints + intTotalGetPoints

    get_ftMade = freeThrowMade[j].get()
    add_ftMade = int(get_ftMade) + 1

    freeThrowMade[j].delete(0, tk.END)
    freeThrowMade[j].insert(0, add_ftMade)

    bearkatBox.delete(0, totalPoints)
    bearkatBox.insert(0, totalPoints)

def saveToFile():
    fileToSaveTo = open('Game.csv', "w")
    for i in range(playerCount):
        tempPoints = points[i].get()  #Lines from 443-454 are getting the statistics for each player using .get()
        tempAssist = assists[i].get()
        tempRebound = rebounds[i].get()
        tempSteal = steals[i].get()
        tempBlock = blocks[i].get()
        tempFouls = fouls[i].get()
        tempFgMade = fgShot[i].get()
        tempFgMissed = fgAttempt[i].get()
        tempThreePointMade = threePointScored[i].get()
        tempThreePointMissed = threePointAttempt[i].get()
        tempFreeThrowMade = freeThrowMade[i].get()
        tempFreeThrowMissed = freeThrowMissed[i].get()
        # Lines 456-470 are turning the variables into Strings and laying them out for the CSV
        str_tempPoints = str(tempPoints) + " Points, "
        str_tempAssist = str(tempAssist) + " Assists, "
        str_tempRebound = str(tempRebound) + " Rebounds, "
        str_tempSteal = str(tempSteal) + " Steals, "
        str_tempBlock = str(tempBlock) + " Blocks, "
        str_tempFgMade = "FGs: " + str(tempFgMade) + "/"
        str_tempFgMissed = str(tempFgMissed) + ", "
        str_tempThreePointMade = "3PTs: " + str(tempThreePointMade) + "/"
        str_tempThreePointMissed = str(tempThreePointMissed) + ", "
        str_tempFreeThrowMade = "FTs: " + str(tempFreeThrowMade) + "/"
        str_tempFreeThrowMissed = str(tempFreeThrowMissed) + ", "
        str_tempFouls = str(tempFouls) + " Fouls \n"
        #Lays out all of the variables for the csv at the end of the game
        playerStats = playerList[i] + ": " + str_tempPoints + str_tempAssist + str_tempRebound + str_tempSteal \
                      + str_tempBlock + str_tempFgMade + str_tempFgMissed + str_tempThreePointMade \
                      + str_tempThreePointMissed + str_tempFreeThrowMade + str_tempFreeThrowMissed + str_tempFouls
        fileToSaveTo.writelines(playerStats) #writes to the file

    fileToSaveTo.close()

saveData = Button(text="Export", bg="white", fg="black", command=saveToFile, highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x=10, y=10, height=30, width=150)


mainWindow()

mainloop()