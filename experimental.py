from __future__ import print_function
from tkinter import *
from tkinter import Tk, font
import PIL
from PIL import ImageTk, Image
import datetime
import mlbgame
root= Tk()
#root.attributes("-fullscreen", True)
root.title("Scoreboard")
root.geometry('2560x1080')
#SCOREBOARD
scoreboard_path ='scoreboard.png'
scoreboard_background = ImageTk.PhotoImage(Image.open('scoreboard V1.1.png'))
panel = Label(root, image = scoreboard_background)
panel.place(relx=0.5,rely=0.0,anchor='n')


now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day


month = mlbgame.games(2018, 3,4, home='Yankees',away='Yankees')
games = mlbgame.combine_games(month)
for game in games:
    print(game.__dict__)
    hometeam=game.home_team
    homescore=game.home_team_runs
    awayteam=game.away_team
    awayscore=game.away_team_runs
    game=Label(root,text=game)


#TEAM LOGOS
scoreboard_logo_home = ImageTk.PhotoImage(Image.open(hometeam+'-full-logo.png'))
scoreboard_logo_away = ImageTk.PhotoImage(Image.open(awayteam+'-full-logo.png'))
panel_logo_home = Label(root, image = scoreboard_logo_home, borderwidth=0, relief="groove")
panel_logo_away = Label(root, image = scoreboard_logo_away, borderwidth=0, relief="groove")
panel_logo_home.place(relx=0.25,rely=0.125,anchor=CENTER)
panel_logo_away.place(relx=0.25,rely=0.375,anchor=CENTER)
#TEAM SCORES
panel_home_score = Label(root,height=0,width=2,text=homescore, font=("century gothic bold", 175),bg='black',fg="white")
panel_away_score = Label(root,height=0,width=2,text=awayscore, font=("century gothic bold", 175),bg='black',fg="white")
panel_home_score.place(relx=0.445,rely=0.115,anchor=CENTER)
panel_away_score.place(relx=0.445,rely=0.368,anchor=CENTER)

#INNING
top_inning=False
bottom_inning=True
inning="7"
if top_inning==True:
   toparrow = ImageTk.PhotoImage(Image.open('top_arrow.png'))
   panel_toparrow = Label(root, image = toparrow, borderwidth=0, relief="groove",bg='grey15')
   panel_toparrow.place(relx=0.533,rely=0.084,anchor=CENTER)
elif bottom_inning==True:
   bottomarrow = ImageTk.PhotoImage(Image.open('bottom_arrow.png'))
   panel_bottomarrow = Label(root, image = bottomarrow, borderwidth=0, relief="groove",bg='grey15')
   panel_bottomarrow.place(relx=0.533,rely=0.42,anchor=CENTER)
else:
    nothing="nothing?"

panel_inning = Label(root, text = inning, borderwidth=0, relief="groove", font=("century gothic bold", 125),bg='grey15',fg="white")
panel_inning.place(relx=0.533,rely=0.25,anchor=CENTER)

#OUTS
one_out=True
two_out=False
out_icon = ImageTk.PhotoImage(Image.open('out.png'))
if one_out==True:
   panel_out_icon = Label(root, image = out_icon, borderwidth=0, relief="groove",bg='grey15')
   panel_out_icon.place(relx=.916,rely=0.4,anchor=CENTER)
elif two_out==True:
   panel_out_icon = Label(root, image = out_icon, borderwidth=0, relief="groove",bg='grey15')
   panel_out_icon_two = Label(root, image = out_icon, borderwidth=0, relief="groove",bg='grey15')
   panel_out_icon.place(relx=.916,rely=0.4,anchor=CENTER)
   panel_out_icon_two.place(relx=.9669,rely=0.4,anchor=CENTER)
else:
    nothing="nothing?"

#COUNT
count="3-2"
panel_count = Label(root,text=count, font=("century gothic bold", 100),bg='grey15',fg="white")
panel_count.place(relx=0.625,rely=0.4,anchor=CENTER)

#PITCH COUNT
pitch_count="42"
panel_count = Label(root,text="P:"+pitch_count, font=("century gothic bold", 75),bg='grey15',fg="white")
panel_count.place(relx=0.78,rely=0.41,anchor=CENTER)

root.mainloop()
