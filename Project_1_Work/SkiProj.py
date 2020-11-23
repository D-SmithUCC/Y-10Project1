import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import tkinter.font as font
from tkinter import filedialog
from PIL import ImageTk,Image
import webbrowser
from tkinter.ttk import *
import tkmacosx as tkm
from APIdata import*


#make a call to the API
for i in ResortIds:
  CreateData(i['id'])


RootOpen = False
StatsOpen = False
RankingsOpen = False



#Creates a list of windows
ListOfWindows=[]


# These functions will reopen widows that have already been opened during the current use session
def ReOpenRoot():
  root.deiconify()
def ReOpenStats():
  stats.deiconify()
def ReOpenRankings():
  Rankings.deiconify()


#initial opening of root, and will be followed by all the functions to initialize each window
def FirstOpenRoot():    
    #section of code that commands window structure when opening and closing windiws
    global RootOpen
    global root
    global picture
    global SearchBar
    global SnowLabel 
    global SearchLabel
    global SearchCan
    global f1, f2, f3, f4
    root= tk.Tk()
    RootOpen = True
    ListOfWindows.append(root)
    RootWidth=730
    RootHeight=400
       
    # secton of code with actual internals of creating the window and its elements
    root.title("It's Snow Time")
    root.geometry(str(RootWidth)+'x'+str(RootHeight))

    #images 
    icon = tk.PhotoImage(file= 'SkiGuy.png')
    root.iconphoto(False, icon)
    picture = tk.PhotoImage(file="Snowflake.png")

    #fonts
    f1 = font.Font(family="Lucida Grande", size=20)
    f2 = font.Font(family = "Lucida Grande", size = 50, weight='bold')
    f3 = font.Font(family= 'Lucida Grande', size= 15)
    f4 = font.Font(family= 'Lucida Grande', size= 17, weight= 'bold')

    #topframe
    topframe = tk.Frame(root, bg='#7126A2', height='75', pady= 10)
    topframe.pack(fill=tk.X)
    #main
    main = tk.Frame(root)
    main.pack(fill=tk.X)
    main.pack(fill=tk.Y)
    #canvases
    SearchCan = tk.Canvas(main, width= str(RootWidth), height = 200)
    SearchCan.grid(column=0, row=0)
    #labels
    SearchLabel= tk.Label(SearchCan, text='')
    SnowLabel= tk.Label(SearchCan, text= '')

    #spacing
    FluffLabel= tk.Label(topframe, text='                                     ', bg = '#7126A2').grid(column=2, row=0)   
    #buttons
    SearchButton= tkm.Button(SearchCan, text='Search', font= f3, command= SearchHome)
    Heading = tkm.Button(topframe, text ="Snow Time", font=f2, fg ='#FFFFFF', bg='#7126A2',activebackground='#7126A2',focuscolor='', borderless=True, command=CreateRoot ).grid(column=0, row=0)
    Logo= tkm.Button(topframe, image=picture, bg='#7126A2',activebackground='#7126A2',focuscolor='', borderless=True,command=CreateRoot).grid(column=1, row=0)
    Btn = tk.Button( main, text = "Click Here for a Deeper Dive on the Stats", command = CreateStats, font= f3).grid(column=0, row=1)
    StatsBtn= tk.Button(main, text='This Will Take You to The Rankings Page', font= f3, command= CreateRankings).grid(column=0, row=2)
    QuitBtn = tk.Button( topframe, text = 'Quit App', command = quit, font = f3).grid(column= 3, row= 0)
    #Entry
    SearchBar = tk.Entry (SearchCan)
    #SearchCan Creations
    SearchCan.create_window(120, 20, window=SearchBar)
    SearchCan.create_window(165, 50, window=SearchButton)

def FirstOpenStats(): 
    #section of code that commands window structure when opening and closing windiws
    global stats
    global StatsOpen
    global SearchBar2
    global SnowLabel2 
    global SearchLabel2
    global SearchCan2
    global variable1,variable2, variable3
    global LeftLabel, MidLabel, RightLabel
    global LeftSelect, MidSelect, RightSelect

    stats = tk.Toplevel() 
    StatsOpen= True
    ListOfWindows.append(stats)

    # secton of code with actual internals of creating the window and its elements
    stats.title('stats') 
    stats.geometry("730x450")
    
    topframe2 = tk.Frame(stats, bg='#7126A2', height='75', pady= 10)
    topframe2.pack(fill=tk.X)
    
    #main
    main2 = tk.Frame(stats)
    main2.pack(fill=tk.X)
    main2.pack(fill=tk.Y)

    #spacing
    FluffLabel2= tk.Label(topframe2, text='                                     ', bg = '#7126A2').grid(column=2, row=0)   
   
    

    #canvases
    SearchCan2 = tk.Canvas(main2, width= str(730), height = 225)
    SearchCan2.grid(column=0, row=0)

    #Labels
    SearchLabel2= tk.Label(SearchCan2, text='')
    SnowLabel2= tk.Label(SearchCan2, text= '')
    LeftLabel= tk.Label(SearchCan2, text='')
    RightLabel= tk.Label(SearchCan2, text= '')
    MidLabel= tk.Label(SearchCan2, text= '')

    #buttons
    Heading2 = tkm.Button(topframe2, text ="Snow Time", font=f2, fg ='#FFFFFF', bg='#7126A2',activebackground='#7126A2',focuscolor='', borderless=True, command=CreateRoot ).grid(column=0, row=0)
    Logo2= tkm.Button(topframe2, image=picture, bg='#7126A2',activebackground='#7126A2',focuscolor='', borderless=True,command=CreateRoot).grid(column=1, row=0)
    Btn2 = tk.Button( main2, text = "This Will Open the Rankings Section", command = CreateRankings, font= f3).grid(column=0, row=1)
    QuitBtn2 = tk.Button( topframe2, text = 'Quit App', command = quit, font = f3).grid(column= 3, row= 0)
    SearchBar2 = tk.Entry (SearchCan2)
    SearchButton2= tkm.Button(SearchCan2, text='Search', font= f3, command= SearchStats)
    #option select 
    OptionList = ["freshsnow_in","temp_c",] 
    OptionList2 = ['upper', 'mid', 'base']

    variable1 = tk.StringVar(SearchCan2)
    variable1.set(OptionList[0])

    LeftSelect = tk.OptionMenu(SearchCan2, variable1, *OptionList)
    LeftSelect.config(width=10, font=('Helvetica', 12))



    variable2 = tk.StringVar(SearchCan2)
    variable2.set(OptionList[0])


    RightSelect = tk.OptionMenu(SearchCan2, variable2, *OptionList)
    RightSelect.config(width=10, font=('Helvetica', 12))

    variable3 = tk.StringVar(SearchCan2)
    variable3.set(OptionList2[0])


    MidSelect = tk.OptionMenu(SearchCan2, variable3, *OptionList2)
    MidSelect.config(width=10, font=('Helvetica', 12))





    #SearchCan Creations
    SearchCan2.create_window(350, 20, window=SearchBar2)
    SearchCan2.create_window(350, 50, window=SearchButton2)
    SearchCan2.create_window(125, 90, window=LeftSelect)
    SearchCan2.create_window(125, 140, window=LeftLabel)
    SearchCan2.create_window(575, 90, window=RightSelect)
    SearchCan2.create_window(575, 140, window=RightLabel)
    SearchCan2.create_window(350, 90, window= MidSelect)
    SearchCan2.create_window(350, 140, window= MidLabel)

    

def FirstOpenRankings():
    #section of code that commands window structure when opening and closing windiws
    global Rankings
    global RankingsOpen
    global Title1, Title2, Title3
    global Answer1, Answer2, Answer3
    global InCase
    global RankingsCan
    Rankings = tk.Toplevel()
    RankingsOpen= True 
    ListOfWindows.append(Rankings)
    # secton of code with actual internals of creating the window and its elements
    Rankings.title('This will return you home') 
    Rankings.geometry("800x450")
    
    topframe3 = tk.Frame(Rankings, bg='#7126A2', height='75', pady= 10)
    topframe3.pack(fill=tk.X)
    
    #canvases
    RankingsCan= tk.Canvas(Rankings, width= 800, height = 225)
    RankingsCan.pack()

    #main
    main3 = tk.Frame(Rankings)
    main3.pack()
    main3.pack(fill=tk.X)
    main3.pack(fill=tk.Y)

    #spacing
    FluffLabel3= tk.Label(topframe3, text='                                     ', bg = '#7126A2').grid(column=2, row=0)   
   
  
    #Labels
    Title1 = tk.Label(RankingsCan, text= 'The Number 1 Resort \n for Inches of Fresh Snow Is:', font=f4)
    Title2 = tk.Label(RankingsCan, text= 'The Number 2 Resort \n for Inches of Fresh Snow Is:', font=f4)
    Title3 = tk.Label(RankingsCan, text= 'The Number 3 Resort \n for Inches of Fresh Snow Is:', font=f4)
    Answer1= tk.Label(RankingsCan, text= '')
    Answer2= tk.Label(RankingsCan, text= '')
    Answer3= tk.Label(RankingsCan, text= '')
    InCase=  tk.Label(RankingsCan, text= ' Sorry, it appears that none of the ski resorts in our data base have \n snow right now.')

    #buttons
    StatsBtn= tk.Button(main3, text='This will Return You to the Stats Page', font= f3, command= CreateStats).grid(column=0, row=0)
    Heading3 = tkm.Button(topframe3, text ="Snow Time", font=f2, fg ='#FFFFFF', bg='#7126A2',activebackground='#7126A2',focuscolor='', borderless=True, command=CreateRoot ).grid(column=0, row=0)
    Logo3= tkm.Button(topframe3, image=picture, bg='#7126A2',activebackground='#7126A2',focuscolor='', borderless=True,command=CreateRoot).grid(column=1, row=0)
    QuitBtn3 = tk.Button( topframe3, text = 'Quit App', command = quit, font = f3).grid(column= 3, row= 0)

    #canvas creations:
    RankingsCan.create_window(130, 40, window=Title1)
    RankingsCan.create_window(130, 120, window=Answer1)
    RankingsCan.create_window(400, 40, window=Title2)
    RankingsCan.create_window(400, 120, window=Answer2)
    RankingsCan.create_window(650, 40, window=Title3)
    RankingsCan.create_window(650, 120, window=Answer3)
    
    FindRankings()


#Rankings Function
def FindRankings():
  templist= data
  NoSnow= False
  GreatestVal= 0
  NameOfGreatest=''
  IndexOfGreatest=0
  NameOfSecond=''
  IndexOfSecond=0
  NameOfThird=''
  IndexOfThird=0
  SecondVal= 0
  ThirdVal= 0
  #find the GreatestVal value in my copy of the data
  for i in range(len(templist)):
    if templist[i]['forecast'][0]['snow_in'] >= GreatestVal:
      GreatestVal= templist[i]['forecast'][0]['snow_in']
      NameOfGreatest= templist[i]['name']
      NameOfGreatest= templist[i]['name']
      IndexOfGreatest= i
  
  #get rid of index where previous greates value was
  temp=len(templist)
  for i in range(len(templist)):
    if temp >= 3:
      if i == IndexOfGreatest:
        del templist[i]
      
  
  NameOfSecond=''
  for i in range(len(templist)):
    if templist[i]['forecast'][0]['snow_in'] >= SecondVal:
      SecondVal= templist[i]['forecast'][0]['snow_in']
      NameOfSecond= templist[i]['name']
      IndexOfSecond= i
  temp=len(templist)
  for i in range(len(templist)):
    if temp >= 3:
      if i == IndexOfGreatest:
        del templist[i]


  NameOfThird=''
  for i in range(len(templist)):
    if templist[i]['forecast'][0]['snow_in'] >= ThirdVal:
      ThirdVal= templist[i]['forecast'][0]['snow_in']
      NameOfThird= templist[i]['name']
      IndexOfThird= i
  temp=len(templist)
  for i in range(len(templist)):
    if temp >= 3:
      if i == IndexOfGreatest:
        del templist[i]

  Answer1.config(text=' '+str(NameOfGreatest) + '\n with an overall snowfall \nfor the day of ' + str(GreatestVal))
  Answer2.config(text=' '+str(NameOfSecond) + '\n with an overall snowfall \nfor the day of ' + str(SecondVal))
  Answer3.config(text=' '+str(NameOfThird) + '\n with an overall snowfall \nfor the day of ' + str(ThirdVal))

  if GreatestVal == 0:
    NoSnow=True
    Answer1.config(text='')
    Answer2.config(text='')
    Answer3.config(text='')
    RankingsCan.create_window(360, 200, window= InCase)
#functions for searchbar

def SearchStats():
  SearchFound= False
  for i in data:
    if i['name']== SearchBar2.get():
      SearchFound=True
      SearchCan2.create_window(475, 65, window=SnowLabel2)
      MidLabel.config(text='')
      LeftLabel.config(text='The ' + str(variable1.get()) + ' of ' + str(SearchBar2.get())+ ' \nat the mountain level of ' + str(variable3.get()) +' is '+ str(i['forecast'][0][str(variable3.get())][str(variable1.get())]))
      RightLabel.config(text='The ' + str(variable2.get()) + ' of ' + str(SearchBar2.get())+ ' \nat the mountain level of ' + str(variable3.get()) +' is '+ str(i['forecast'][0][str(variable3.get())][str(variable2.get())]))
  if SearchFound==False:
    RightLabel.config(text='')
    LeftLabel.config(text='')
    SnowLabel2.config(text='')
    MidLabel.config(text='Sorry, Either you made a mistake typing, \nor the resort you are looking for is not in our data base')


def SearchHome():
    for i in ResortIds:
      if i['name']== SearchBar.get():
        SearchCan.create_window(475, 65, window=SnowLabel)
        SearchLabel.config(text='')
        ShowSearchData(SnowLabel,SearchBar.get())
      else:
        SnowLabel.config(text='')
        SearchCan.create_window(500, 40, window=SearchLabel)
        SearchLabel.configure(text= 'Sorry, Either you made a mistake typing, \nor the resort you are looking for is not in our data base')

def ShowSearchData(a,b):
  for i in range(len(data)):
    if data[i]['name'] == b:
      a.config(text= ' \n\nAlpine:\n inches of fresh snow: '+ str(data[i]['forecast'][0]['upper']['freshsnow_in']) + '\ntemperature (cel): '+ str(data[i]['forecast'][0]['upper']['temp_c']) + '\n MidMountain:\n ' + 'inches of fresh snow: ' + str(data[i]['forecast'][0]['mid']['freshsnow_in']) +  '\nTemperature (cel): '+ str(data[i]['forecast'][0]['mid']['temp_c'])+ '\n' + 'Base: \n' + 'inches of fresh snow: ' + str(data[i]['forecast'][0]['base']['freshsnow_in']) + '\n temperature(cels): '+ str(data[i]['forecast'][0]['base']['temp_c']))



# these functions will decide whether to init the windows or to re-open them
def CreateRoot():
  if RootOpen == False:
    FirstOpenRoot()
  else:
    ReOpenRoot()
  #closes windows other than the one being opened
  for i in ListOfWindows:
    if i != root:
      i.withdraw()

def CreateStats():
  if StatsOpen == False:
    FirstOpenStats()
  else:
    ReOpenStats()
   #closes windows other than the one being opened
  for i in ListOfWindows:
    if i != stats:
      i.withdraw()


def CreateRankings():
  if RankingsOpen == False:
    FirstOpenRankings()
  else:
    ReOpenRankings()
  #closes windows other than the one being opened
  for i in ListOfWindows:
    if i != Rankings:
      i.withdraw()



FirstOpenRoot()




tk.mainloop() 

 