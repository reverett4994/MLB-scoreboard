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
    #print(game.__dict__)
    hometeam=game.home_team
    homescore=game.home_team_runs
    awayteam=game.away_team
    awayscore=game.away_team_runs
    idd=game.game_id


box = mlbgame.game.box_score(idd)
overview = mlbgame.game.overview(idd)
print(box)
homescore = overview['home_team_runs']
awayscore = overview['away_team_runs']
status = overview['status']
#TEAM LOGOS
scoreboard_logo_home = ImageTk.PhotoImage(Image.open(hometeam+'-full-logo.png'))
scoreboard_logo_away = ImageTk.PhotoImage(Image.open(awayteam+'-full-logo.png'))
panel_logo_home = Label(root, image = scoreboard_logo_home, borderwidth=0, relief="groove")
panel_logo_away = Label(root, image = scoreboard_logo_away, borderwidth=0, relief="groove")
panel_logo_away.place(relx=0.25,rely=0.125,anchor=CENTER)
panel_logo_home.place(relx=0.25,rely=0.375,anchor=CENTER)
#TEAM SCORES
panel_home_score = Label(root,height=0,width=2,text=homescore, font=("century gothic bold", 175),bg='black',fg="white")
panel_away_score = Label(root,height=0,width=2,text=awayscore, font=("century gothic bold", 175),bg='black',fg="white")
panel_away_score.place(relx=0.445,rely=0.115,anchor=CENTER)
panel_home_score.place(relx=0.442,rely=0.368,anchor=CENTER)

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

#BASES
first_base=True
second_base=True
third_base=True
base_icon = ImageTk.PhotoImage(Image.open('onbase.png'))
if first_base==True:
   panel_first_base = Label(root, image = base_icon, borderwidth=0, relief="groove",bg='grey15')
   panel_first_base.place(relx=.85,rely=0.25,anchor=CENTER)
if second_base==True:
   panel_second_base = Label(root, image = base_icon, borderwidth=0, relief="groove",bg='grey15')
   panel_second_base.place(relx=.7775,rely=0.12,anchor=CENTER)
if third_base==True:
  panel_third_base = Label(root, image = base_icon, borderwidth=0, relief="groove",bg='grey15')
  panel_third_base.place(relx=.705,rely=0.25,anchor=CENTER)


#COUNT
count="3-2"
panel_count = Label(root,text=count, font=("century gothic bold", 100),bg='grey15',fg="white")
panel_count.place(relx=0.625,rely=0.4,anchor=CENTER)

#PITCH COUNT
pitch_count="42"
panel_count = Label(root,text="P:"+pitch_count, font=("century gothic bold", 75),bg='grey15',fg="white")
panel_count.place(relx=0.78,rely=0.41,anchor=CENTER)


#BOX SCORE
away_ab = overview['away_name_abbrev']
panel_away_ab = Label(root, text = away_ab, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_ab.place(relx=0.06,rely=0.671,anchor=CENTER)
home_ab = overview['home_name_abbrev']
panel_home_ab = Label(root, text = home_ab, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_ab.place(relx=0.06,rely=0.7785,anchor=CENTER)
    #RUNS HITS & ERROS
panel_home_runs = Label(root, text = overview['home_team_runs'], borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_runs = Label(root, text = overview['away_team_runs'], borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_runs.place(relx=0.84,rely=0.671,anchor=CENTER)
panel_home_runs.place(relx=0.84,rely=0.7785,anchor=CENTER)

panel_home_hits = Label(root, text = overview['home_team_hits'], borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_hits = Label(root, text = overview['away_team_hits'], borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_hits.place(relx=0.91,rely=0.671,anchor=CENTER)
panel_home_hits.place(relx=0.91,rely=0.7785,anchor=CENTER)

panel_home_errors = Label(root, text = overview['home_team_errors'], borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_errors = Label(root, text = overview['away_team_errors'], borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_errors.place(relx=0.964,rely=0.671,anchor=CENTER)
panel_home_errors.place(relx=0.964,rely=0.7785,anchor=CENTER)

    # PER INNING
home_1=""
away_1=""
if status == 'Final':
    home_1 = box[1]['home']
    away_1 = box[1]['away']
    home_2 = box[2]['home']
    away_2 = box[2]['away']
    home_3 = box[3]['home']
    away_3 = box[3]['away']
    home_4 = box[4]['home']
    away_4 = box[4]['away']
    home_5 = box[5]['home']
    away_5 = box[5]['away']
    home_6 = box[6]['home']
    away_6 = box[6]['away']
    home_7 = box[7]['home']
    away_7 = box[7]['away']
    home_8 = box[8]['home']
    away_8 = box[8]['away']
    home_9 = box[9]['home']
    away_9 = box[9]['away']
    pass
panel_home_1 = Label(root, text = home_1, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_1 = Label(root, text = away_1, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_2 = Label(root, text = home_2, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_2 = Label(root, text = away_2, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_3 = Label(root, text = home_3, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_3 = Label(root, text = away_3, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_4 = Label(root, text = home_4, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_4 = Label(root, text = away_4, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_5 = Label(root, text = home_5, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_5 = Label(root, text = away_5, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_6 = Label(root, text = home_6, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_6 = Label(root, text = away_6, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_7 = Label(root, text = home_7, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_7 = Label(root, text = away_7, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_8 = Label(root, text = home_8, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_8 = Label(root, text = away_8, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_home_9 = Label(root, text = home_9, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
panel_away_9 = Label(root, text = away_9, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")

panel_away_1.place(relx=0.15,rely=0.671,anchor=CENTER)
panel_home_1.place(relx=0.15,rely=0.7785,anchor=CENTER)
panel_away_2.place(relx=0.22,rely=0.671,anchor=CENTER)
panel_home_2.place(relx=0.22,rely=0.7785,anchor=CENTER)
panel_away_3.place(relx=0.29,rely=0.671,anchor=CENTER)
panel_home_3.place(relx=0.29,rely=0.7785,anchor=CENTER)
panel_away_4.place(relx=0.36,rely=0.671,anchor=CENTER)
panel_home_4.place(relx=0.36,rely=0.7785,anchor=CENTER)
panel_away_5.place(relx=0.425,rely=0.671,anchor=CENTER)
panel_home_5.place(relx=0.425,rely=0.7785,anchor=CENTER)
panel_away_6.place(relx=0.496,rely=0.671,anchor=CENTER)
panel_home_6.place(relx=0.496,rely=0.7785,anchor=CENTER)
panel_away_7.place(relx=0.565,rely=0.671,anchor=CENTER)
panel_home_7.place(relx=0.565,rely=0.7785,anchor=CENTER)
panel_away_8.place(relx=0.634,rely=0.671,anchor=CENTER)
panel_home_8.place(relx=0.634,rely=0.7785,anchor=CENTER)
panel_away_9.place(relx=0.704,rely=0.671,anchor=CENTER)
panel_home_9.place(relx=0.704,rely=0.7785,anchor=CENTER)


#IF FINISHED WINDOW
if status == 'Final':
    if int(overview['home_team_runs']) > int(overview['away_team_runs']) and overview['home_name_abbrev'] == 'NYY' :
        message="Yankees ("+overview['home_win']+"-"+overview['home_loss'] +") Win"
    elif int(overview['away_team_runs']) > int(overview['home_team_runs']) and overview['away_name_abbrev'] == 'NYY' :
        message="Yankees ("+overview['away_win']+"-"+overview['away_loss'] +") Win"
    else:
        if overview['home_name_abbrev'] == 'NYY':
            message="Yankees ("+overview['home_win']+"-"+overview['home_loss'] +") Lose"
        else:
            message="Yankees ("+overview['away_win']+"-"+overview['away_loss'] +") Lose"
            pass

        pass
    panel_message= Label(root, text = message, borderwidth=0, relief="groove", font=("century gothic bold", 60),bg='grey15',fg="white")
    panel_message.place(relx=0.75,rely=0.1,anchor=CENTER)

    pass

#RUN WINDOW
root.mainloop()
