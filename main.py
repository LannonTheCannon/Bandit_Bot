# Hello

from tkinter import *
# from tkcalendar import *
#import pymysql
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr
from PIL import ImageTk, Image, ImageSequence
import csv
from tkinter import font
from tkinter import filedialog
#import emoji

class studentRecords():

    def __init__(self, root):

        self.root = root
        self.root.title('Student Records System')
        self.root.geometry('1273x798+0+0')

        notebook = ttk.Notebook(self.root)
        TabControl1 = ttk.Frame(notebook)
        TabControl2 = ttk.Frame(notebook)

        notebook.add(TabControl1, text='Student Managment')
        notebook.add(TabControl2, text='Student Details')

        notebook.grid()
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

        self.eyes_close_col = 'grey30'
        self.student1 = 'Lord Tater-Tot'
        self.student2 = 'Lil Moo'
        self.student3 = 'Kimchi'
        self.student4 = 'Shenanigans'
        self.student5 = 'Hot Dog Tragedy'
        self.student6 = 'Tangerine'
        self.student7 = 'YUH'
        self.student8 = 'HOOGUS'
        self.student9 = 'MAT-BOT'
        self.student10 = 'i-BOT'
        self.student11 = 'Bad-luck'
        self.student12 = 'Roblox-User'
        self.student13 = '[Enter Name]'
        self.student14 = '[Enter Name]'
        self.student15 = '[Enter Name]'
        self.student16 = '[Enter name]'

        self.frame_col = '#2f4c77'

        self.level1ProgBar, self.level2ProgBar, self.level2ProgBar, self.level4ProgBar = 0, 0, 0, 0
        self.level5ProgBar, self.level6ProgBar, self.level7ProgBar, self.level8ProgBar = 0, 0, 0, 0
        self.level9ProgBar, self.level10ProgBar, self.level11ProgBar, self.level12ProgBar = 0, 0, 0, 0
        self.level13ProgBar, self.level14ProgBar, self.level15ProgBar, self.level16ProgBar = 0, 0, 0, 0

        self.countOne, self.countTwo, self.countThree, self.countFour = 0, 0, 0, 0
        self.countFive, self.countSix, self.countSeven, self.countEight = 0, 0, 0, 0
        self.countNine, self.countTen, self.countEleven, self.countTwelve = 0, 0, 0, 0
        self.countThirteen, self.countFourteen, self.countFifteen, self.countSixteen = 0, 0, 0, 0

        self.seq_fire1 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/water11.gif'))]

        self.seq_fire2 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/poison_green.gif'))]

        self.seq_fire3 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/poison_green.gif'))]

        self.seq_fire4 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/poison_green.gif'))]

        self.seq_fire5 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/poison_green.gif'))]

        self.seq_fire6 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/fire5.gif'))]

        self.seq_fire7 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/water13.gif'))]

        self.seq_fire8 = [ImageTk.PhotoImage(img)
                          for img in ImageSequence.Iterator(
                Image.open('images/water11.gif'))]

        self.seq_water9 = [ImageTk.PhotoImage(img)
                           for img in ImageSequence.Iterator(
                Image.open('images/water13.gif'))]

        self.seq_water10 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/fire5.gif'))]

        self.seq_water11 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/water11.gif'))]

        self.seq_water12 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/water13.gif'))]

        self.seq_water13 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/ice_spell.gif'))]

        self.seq_water14 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/phantom.gif'))]

        self.seq_water15 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/pulsar.gif'))]

        self.seq_water16 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/poison_blue.gif'))]

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # LEVEL 1 | FULL ROBOT SEQUENCE   X
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.sequence_dead = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_dead.gif'))]
        self.sequence_idle = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_idle.gif'))]
        self.sequence_go = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_go.gif'))]
        self.sequence_prev1 = [ImageTk.PhotoImage(img)
                               for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo1.gif'))]
        self.sequence_prev2 = [ImageTk.PhotoImage(img)
                               for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo2.gif'))]

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # LEVEL 10 | FULL ROBOT SEQUENCE   X
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.sequence_dead10 = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_dead_level10.gif'))]
        self.sequence_idle10 = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_idle_level10.gif'))]
        self.sequence_go10 = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_go_level10.gif'))]
        self.sequence_prev1_10 = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo1_level10.gif'))]
        self.sequence_prev2_10 = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo2_level10.gif'))]

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # Copper | FULL ROBOT SEQUENCE   X
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.sequence_dead_copper = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_dead_copper.gif'))]
        self.sequence_idle_copper = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_idle_copper.gif'))]
        self.sequence_go_copper = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_go_copper.gif'))]
        self.sequence_prev1_copper = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo1_copper.gif'))]
        self.sequence_prev2_copper = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo2_copper.gif'))]

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # Copper | FULL ROBOT SEQUENCE   X
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.sequence_dead_grape = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_dead_grape.gif'))]
        self.sequence_idle_grape = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_idle_grape.gif'))]
        self.sequence_go_grape = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_go_grape.gif'))]
        self.sequence_prev1_grape = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo1_grape.gif'))]
        self.sequence_prev2_grape = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo2_grape.gif'))]

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # Copper | FULL ROBOT DAVID SEQUENCE   X
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.sequence_dead_david = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_dead_david.gif'))]
        self.sequence_idle_david = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_idle_david.gif'))]
        self.sequence_go_david = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo_go_david.gif'))]
        self.sequence_prev1_grape = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo1_grape.gif'))]
        self.sequence_prev2_grape = [ImageTk.PhotoImage(img)
                                  for img in ImageSequence.Iterator(
                Image.open(
                    'images/robo2_grape.gif'))]

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        self.MAINFRAME = Frame(TabControl1, bd=12, relief=RAISED,
                               bg=self.frame_col, width=1110, height=300)
        self.MAINFRAME.pack(fill='both', expand=1)

        notebook.add(TabControl1, text='BANDIT-BOT')

        self.HEADLINE_FRAME = tkinter.Frame(self.MAINFRAME, bd=12,
                                            bg=self.frame_col,
                                            relief=RAISED, width=1110,
                                            height=55)
        self.HEADLINE_FRAME.pack(side=TOP, padx=1, pady=0,
                                 expand=True, fill=BOTH)

        # Second Level Frames
        self.TOPFRAME_OUTER = tkinter.Frame(self.MAINFRAME, bd=10, width=1055,
                                            height=300, padx=0, relief=SUNKEN,
                                            bg='grey')
        self.TOPFRAME_OUTER.pack(side=TOP, expand=True, fill=BOTH)

        self.TOPFRAME_1 = tkinter.Frame(self.TOPFRAME_OUTER, bd=10, width=200,
                                        height=300, padx=0, relief=SUNKEN,
                                        bg='black')
        self.TOPFRAME_1.pack(side=LEFT, expand=True, fill=BOTH)

        self.TOPFRAME_2 = tkinter.Frame(self.TOPFRAME_OUTER, bd=15, width=200,
                                        height=300, padx=0, pady=10,
                                        relief=SUNKEN, bg='black')
        self.TOPFRAME_2.pack(side=LEFT, anchor=N)

        self.TOPFRAME_3 = tkinter.Frame(self.TOPFRAME_OUTER, bd=15, height=300,
                                        padx=0, width=200, relief=SUNKEN,
                                        bg='black')
        self.TOPFRAME_3.pack(side=LEFT, expand=True, fill=BOTH)

        self.TOPFRAME_4 = tkinter.Frame(self.TOPFRAME_OUTER, bd=15, width=200,
                                        height=300, padx=0, relief=SUNKEN,
                                        bg='black')
        self.TOPFRAME_4.pack(side=LEFT, expand=True, fill=BOTH)

        self.TOPFRAME_5 = tkinter.Frame(self.TOPFRAME_OUTER, bd=15, width=200,
                                        height=300, padx=0, relief=SUNKEN,
                                        bg='black',
                                        pady=10)
        self.TOPFRAME_5.pack(side=LEFT, anchor=N)

        self.TOPFRAME_6 = tkinter.Frame(self.TOPFRAME_OUTER, bd=10, width=200,
                                        height=300, padx=0, relief=SUNKEN,
                                        bg='black')
        self.TOPFRAME_6.pack(side=LEFT, expand=True, fill=BOTH)

        # Third Level Frames

        self.LEFT_FRAME_1 = Frame(self.MAINFRAME, bd=0, width=200,
                                  height=150, relief=SUNKEN)
        self.LEFT_FRAME_1.pack(side=TOP, anchor=NW, expand=True, fill=BOTH)

        self.LEFT_FRAME_2 = Frame(self.LEFT_FRAME_1, bd=14, width=280,
                                  height=150, relief=SUNKEN, bg='grey15')
        self.LEFT_FRAME_2.pack(side=LEFT, anchor=W, expand=True, fill=BOTH)

        self.CHATBOT_FRAME_A = Frame(self.LEFT_FRAME_2, bd=4, width=210,
                                     height=90, relief=SUNKEN, bg='black')
        self.CHATBOT_FRAME_A.pack(side=TOP, expand=True, fill=BOTH)

        self.CHATBOT_FRAME_B = Frame(self.LEFT_FRAME_2, bd=8, width=210,
                                     relief=SUNKEN, bg='grey')
        self.CHATBOT_FRAME_B.pack(side=TOP)

        self.MID_FRAME_OUTER = Frame(self.LEFT_FRAME_1, bd=14, width=780,
                                     height=230, relief=RIDGE,
                                     bg='grey10')
        self.MID_FRAME_OUTER.pack(side=RIGHT, fill=BOTH, expand=True)
        self.MIDDLE_FRAME = Frame(self.MID_FRAME_OUTER, bd=0, width=780,
                                  height=230, relief=RIDGE,
                                  bg='grey')
        self.MIDDLE_FRAME.pack(side=RIGHT, expand=True, fill=BOTH)

        self.btnMenu = Button(self.HEADLINE_FRAME, padx=16, pady=1, bd=8,
                              fg='cornsilk', font=('terminal', 19, 'bold'),
                              width=6, height=2, bg=self.frame_col,
                              text='MENU', command=self.saveTotal)
        self.btnMenu.grid(row=0, column=0)

        self.btnCreateNew = Button(self.HEADLINE_FRAME, padx=16, pady=1, bd=8,
                                   bg=self.frame_col, fg='cornsilk',
                                   font=('terminal', 19, 'bold'), width=6,
                                   height=2, text='NEW', command=self.saveTotal)
        self.btnCreateNew.grid(row=0, column=1)

        self.btnSave = Button(self.HEADLINE_FRAME, padx=16, pady=1, bd=8,
                              fg='cornsilk', font=('terminal', 19, 'bold'),
                              width=29, height=2, bg=self.frame_col,
                              text='VIRUS CONTAINMENT LAB', command=self.saveTotal)
        self.btnSave.grid(row=0, column=2)

        self.btnLoad = Button(self.HEADLINE_FRAME, padx=16, pady=1, bd=8,
                              fg='cornsilk', font=('terminal', 19, 'bold'),
                              width=6, height=2, bg=self.frame_col, text='LOAD',
                              command=self.loadAll)
        self.btnLoad.grid(row=0, column=3)

        self.btnExit = Button(self.HEADLINE_FRAME, padx=16, pady=1, bd=8,
                              fg='cornsilk', font=('terminal', 19, 'bold'),
                              width=6, height=2, bg=self.frame_col,
                              text='EXIT', command=self.saveTotal)
        self.btnExit.grid(row=0, column=4)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        # Level 2 Widgets

        self.lblStudentName1 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                text=self.student1, padx=5, pady=5,
                                width=19, bg='black', fg='grey50')
        self.lblStudentName1.pack(side=TOP)
        self.lblStudentName2 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                text=self.student2, padx=5, pady=5,
                                width=19, bg='black', fg='grey50')
        self.lblStudentName2.pack(side=TOP)
        self.lblStudentName3 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                width=19, text=self.student3, padx=5,
                                pady=5, bg='black', fg='grey50')
        self.lblStudentName3.pack(side=TOP)
        self.lblStudentName4 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                width=19, text=self.student4, padx=5,
                                pady=5, bg='black', fg='grey50')
        self.lblStudentName4.pack(side=TOP)
        self.lblStudentName5 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                width=19, text=self.student5, padx=5,
                                pady=5, bg='black', fg='grey50')
        self.lblStudentName5.pack(side=TOP)
        self.lblStudentName6 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                width=19, text=self.student6, padx=5,
                                pady=5, bg='black', fg='grey50')
        self.lblStudentName6.pack(side=TOP)
        self.lblStudentName7 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                width=19, text=self.student7, padx=5,
                                pady=5, bg='black', fg='grey50')
        self.lblStudentName7.pack(side=TOP)
        self.lblStudentName8 = Label(self.TOPFRAME_3, font=('consolas', 12, 'bold'),
                                width=19, text=self.student8, padx=5,
                                pady=5, bg='black', fg='grey50')
        self.lblStudentName8.pack(side=TOP)

        self.lblStudentName9 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                text=self.student9, padx=5, pady=5,
                                width=19, bg='black', fg='grey50')
        self.lblStudentName9.pack(side=TOP)
        self.lblStudentName10 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                 text=self.student10, padx=5, pady=5,
                                 width=19, bg='black', fg='grey50')
        self.lblStudentName10.pack(side=TOP)
        self.lblStudentName11 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                 width=19, text=self.student11, padx=5, pady=5,
                                 bg='black', fg='grey50')
        self.lblStudentName11.pack(side=TOP)
        self.lblStudentName12 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                 width=19, text=self.student12, padx=5, pady=5,
                                 bg='black', fg='grey50')
        self.lblStudentName12.pack(side=TOP)
        self.lblStudentName13 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                 width=19, text=self.student13, padx=5, pady=5,
                                 bg='black', fg='grey50')
        self.lblStudentName13.pack(side=TOP)
        self.lblStudentName14 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                 width=19, text=self.student14, padx=5, pady=5,
                                 bg='black', fg='grey50')
        self.lblStudentName14.pack(side=TOP)
        self.lblStudentName15 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                 width=19, text=self.student15, padx=5, pady=5,
                                 bg='black', fg='grey50')
        self.lblStudentName15.pack(side=TOP)
        self.lblStudentName16 = Label(self.TOPFRAME_4, font=('consolas', 12, 'bold'),
                                 width=19, text=self.student16, padx=5, pady=5,
                                 bg='black', fg='grey50')
        self.lblStudentName16.pack(side=TOP)

        # Level 2 Widgets (TOPFRAME 2 and 5)

        eye_col_1 = 'ghost white'
        eye_col_2 = 'grey7'

        length_bar = 175

        self.OnebtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12),
                                     text='1', padx=0, width=4, bd=0, relief=FLAT,
                                     height=1, bg=eye_col_1, command=self.Student1PointOne)
        self.OnebtnPointOne.grid(row=0, column=1)
        self.OnebtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                      text='5', padx=0, width=4, bd=0, relief=FLAT,
                                      height=1, bg=eye_col_1, command=self.Student1PointFive)
        self.OnebtnPointFive.grid(row=0, column=2)
        self.OnebtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                     text='10', padx=0, width=4, bd=0, relief=FLAT,
                                     height=1, bg=eye_col_1, command=self.Student1PointTen)
        self.OnebtnPointTen.grid(row=0, column=3)
        self.OnebtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                        text='20', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_1, command=self.Student1PointTwe)
        self.OnebtnPointTwenty.grid(row=0, column=4)

        self.TwobtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12), text='1',
                                     padx=0, width=4, bd=0, relief=FLAT, height=1,
                                     bg=eye_col_1, command=self.Student2PointOne)
        self.TwobtnPointOne.grid(row=1, column=1)
        self.TwobtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                      text='5', padx=0, width=4, bd=0, relief=FLAT,
                                      height=1, bg=eye_col_1, command=self.Student2PointFive)
        self.TwobtnPointFive.grid(row=1, column=2)
        self.TwobtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                     text='10', padx=0, width=4, bd=0, relief=FLAT,
                                     height=1, bg=eye_col_1, command=self.Student2PointTen)
        self.TwobtnPointTen.grid(row=1, column=3)
        self.TwobtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                        text='20', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_1, command=self.Student2PointTwe)
        self.TwobtnPointTwenty.grid(row=1, column=4)

        self.ThreebtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12), text='1',
                                       padx=0, width=4, bd=0, relief=FLAT, height=1,
                                       bg=eye_col_1, command=self.Student3PointOne)
        self.ThreebtnPointOne.grid(row=2, column=1)
        self.ThreebtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                        text='5', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_1, command=self.Student3PointFive)
        self.ThreebtnPointFive.grid(row=2, column=2)
        self.ThreebtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                       text='10', padx=0, width=4, bd=0, relief=FLAT,
                                       height=1, bg=eye_col_1, command=self.Student3PointTen)
        self.ThreebtnPointTen.grid(row=2, column=3)
        self.ThreebtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                          text='20', padx=0, width=4, bd=0, relief=FLAT,
                                          height=1, bg=eye_col_1, command=self.Student3PointTwe)
        self.ThreebtnPointTwenty.grid(row=2, column=4)

        self.FourbtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12), text='1',
                                      padx=0, width=4, bd=0, relief=FLAT, height=1,
                                      bg=eye_col_1, command=self.Student4PointOne)
        self.FourbtnPointOne.grid(row=3, column=1)
        self.FourbtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                       text='5', padx=0, width=4, bd=0, relief=FLAT,
                                       height=1, bg=eye_col_1, command=self.Student4PointFive)
        self.FourbtnPointFive.grid(row=3, column=2)
        self.FourbtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                      text='10', padx=0, width=4, bd=0, relief=FLAT,
                                      height=1, bg=eye_col_1, command=self.Student4PointTen)
        self.FourbtnPointTen.grid(row=3, column=3)
        self.FourbtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                         text='20', padx=0, width=4, bd=0, relief=FLAT,
                                         height=1, bg=eye_col_1, command=self.Student4PointTwe)
        self.FourbtnPointTwenty.grid(row=3, column=4)

        self.FivebtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12), text='1',
                                      padx=0, width=4, bd=0, relief=FLAT, height=1,
                                      bg=eye_col_1, command=self.Student5PointOne)
        self.FivebtnPointOne.grid(row=4, column=1)
        self.FivebtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                       text='5', padx=0, width=4, bd=0, relief=FLAT,
                                       height=1, bg=eye_col_1, command=self.Student5PointFive)
        self.FivebtnPointFive.grid(row=4, column=2)
        self.FivebtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                      text='10', padx=0, width=4, bd=0, relief=FLAT,
                                      height=1, bg=eye_col_1, command=self.Student5PointTen)
        self.FivebtnPointTen.grid(row=4, column=3)
        self.FivebtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                         text='20', padx=0, width=4, bd=0, relief=FLAT,
                                         height=1, bg=eye_col_1, command=self.Student5PointTwe)
        self.FivebtnPointTwenty.grid(row=4, column=4)

        self.SixbtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12), text='1',
                                     padx=0, width=4, bd=0, relief=FLAT, height=1,
                                     bg=eye_col_1, command=self.Student6PointOne)
        self.SixbtnPointOne.grid(row=5, column=1)
        self.SixbtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                      text='5', padx=0, width=4, bd=0, relief=FLAT,
                                      height=1, bg=eye_col_2, command=self.Student6PointFive)
        self.SixbtnPointFive.grid(row=5, column=2)
        self.SixbtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                     text='10', padx=0, width=4, bd=0, relief=FLAT,
                                     height=1, bg=eye_col_2, command=self.Student6PointTen)
        self.SixbtnPointTen.grid(row=5, column=3)
        self.SixbtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                        text='20', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_2, command=self.Student6PointTwe)
        self.SixbtnPointTwenty.grid(row=5, column=4)

        self.SevenbtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12), text='1',
                                       padx=0, width=4, bd=0, relief=FLAT, height=1,
                                       bg=eye_col_1, command=self.Student7PointOne)
        self.SevenbtnPointOne.grid(row=6, column=1)
        self.SevenbtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                        text='5', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_2, command=self.Student7PointFive)
        self.SevenbtnPointFive.grid(row=6, column=2)
        self.SevenbtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                       text='10', padx=0, width=4, bd=0, relief=FLAT,
                                       height=1, bg=eye_col_2, command=self.Student7PointTen)
        self.SevenbtnPointTen.grid(row=6, column=3)
        self.SevenbtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                          text='20', padx=0, width=4, bd=0, relief=FLAT,
                                          height=1, bg=eye_col_2, command=self.Student7PointTwe)
        self.SevenbtnPointTwenty.grid(row=6, column=4)

        self.EightbtnPointOne = Button(self.TOPFRAME_2, font=('consolas', 12), text='1',
                                       padx=0, width=4, bd=0, relief=FLAT, height=1,
                                       bg=eye_col_1, command=self.Student8PointOne)
        self.EightbtnPointOne.grid(row=7, column=1)
        self.EightbtnPointFive = Button(self.TOPFRAME_2, font=('consolas', 12),
                                        text='5', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_2, command=self.Student8PointFive)
        self.EightbtnPointFive.grid(row=7, column=2)
        self.EightbtnPointTen = Button(self.TOPFRAME_2, font=('consolas', 12),
                                       text='10', padx=0, width=4, bd=0, relief=FLAT,
                                       height=1, bg=eye_col_2, command=self.Student8PointTen)
        self.EightbtnPointTen.grid(row=7, column=3)
        self.EightbtnPointTwenty = Button(self.TOPFRAME_2, font=('consolas', 12),
                                          text='20', padx=0, width=4, bd=0, relief=FLAT,
                                          height=1, bg=eye_col_2, command=self.Student8PointTwe)
        self.EightbtnPointTwenty.grid(row=7, column=4)

        self.NinebtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                      padx=0, width=4, bd=0, relief=FLAT, height=1,
                                      bg=eye_col_1, command=self.Student9PointOne)
        self.NinebtnPointOne.grid(row=0, column=1)
        self.NinebtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                       text='5', padx=0, width=4, bd=0, relief=FLAT,
                                       height=1, bg=eye_col_1, command=self.Student9PointFive)
        self.NinebtnPointFive.grid(row=0, column=2)
        self.NinebtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                      text='10', padx=0, width=4, bd=0, relief=FLAT,
                                      height=1, bg=eye_col_1, command=self.Student9PointTen)
        self.NinebtnPointTen.grid(row=0, column=3)
        self.NinebtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                         text='20', padx=0, width=4, bd=0, relief=FLAT,
                                         height=1, bg=eye_col_1, command=self.Student9PointTwe)
        self.NinebtnPointTwenty.grid(row=0, column=4)

        self.TenbtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                     padx=0, width=4, bd=0, relief=FLAT, height=1,
                                     bg=eye_col_1, command=self.Student10PointOne)
        self.TenbtnPointOne.grid(row=1, column=1)
        self.TenbtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                      text='5', padx=0, width=4, bd=0, relief=FLAT,
                                      height=1, bg=eye_col_1, command=self.Student10PointFive)
        self.TenbtnPointFive.grid(row=1, column=2)
        self.TenbtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                     text='10', padx=0, width=4, bd=0, relief=FLAT,
                                     height=1, bg=eye_col_1, command=self.Student10PointTen)
        self.TenbtnPointTen.grid(row=1, column=3)
        self.TenbtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                        text='20', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_1, command=self.Student10PointTwe)
        self.TenbtnPointTwenty.grid(row=1, column=4)

        self.ElevenbtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                        padx=0, width=4, bd=0, relief=FLAT, height=1,
                                        bg=eye_col_1, command=self.Student11PointOne)
        self.ElevenbtnPointOne.grid(row=2, column=1)
        self.ElevenbtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                         text='5', padx=0, width=4, bd=0, relief=FLAT,
                                         height=1, bg=eye_col_1, command=self.Student11PointFive)
        self.ElevenbtnPointFive.grid(row=2, column=2)
        self.ElevenbtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                        text='10', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_1, command=self.Student11PointTen)
        self.ElevenbtnPointTen.grid(row=2, column=3)
        self.ElevenbtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                           text='20', padx=0, width=4, bd=0, relief=FLAT,
                                           height=1, bg=eye_col_1, command=self.Student11PointTwe)
        self.ElevenbtnPointTwenty.grid(row=2, column=4)

        self.TwelvebtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                        padx=0, width=4, bd=0, relief=FLAT, height=1,
                                        bg=eye_col_1, command=self.Student12PointOne)
        self.TwelvebtnPointOne.grid(row=3, column=1)
        self.TwelvebtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                         text='5', padx=0, width=4, bd=0, relief=FLAT,
                                         height=1, bg=eye_col_1, command=self.Student12PointFive)
        self.TwelvebtnPointFive.grid(row=3, column=2)
        self.TwelvebtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                        text='10', padx=0, width=4, bd=0, relief=FLAT,
                                        height=1, bg=eye_col_1, command=self.Student12PointTen)
        self.TwelvebtnPointTen.grid(row=3, column=3)
        self.TwelvebtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                           text='20', padx=0, width=4, bd=0, relief=FLAT,
                                           height=1, bg=eye_col_1, command=self.Student12PointTwe)
        self.TwelvebtnPointTwenty.grid(row=3, column=4)

        self.ThirteenbtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                          padx=0, width=4, bd=0, relief=FLAT, height=1,
                                          bg=eye_col_1, command=self.Student13PointOne)
        self.ThirteenbtnPointOne.grid(row=4, column=1)
        self.ThirteenbtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                           text='5', padx=0, width=4, bd=0, relief=FLAT,
                                           height=1, bg=eye_col_1, command=self.Student13PointFive)
        self.ThirteenbtnPointFive.grid(row=4, column=2)
        self.ThirteenbtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                          text='10', padx=0, width=4, bd=0, relief=FLAT,
                                          height=1, bg=eye_col_1, command=self.Student13PointTen)
        self.ThirteenbtnPointTen.grid(row=4, column=3)
        self.ThirteenbtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                             text='20', padx=0, width=4, bd=0, relief=FLAT,
                                             height=1, bg=eye_col_1, command=self.Student13PointTwe)
        self.ThirteenbtnPointTwenty.grid(row=4, column=4)

        self.FourteenbtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                          padx=0, width=4, bd=0, relief=FLAT, height=1,
                                          bg=eye_col_2, command=self.Student14PointOne)
        self.FourteenbtnPointOne.grid(row=5, column=1)
        self.FourteenbtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                           text='5', padx=0, width=4, bd=0, relief=FLAT,
                                           height=1, bg=eye_col_2, command=self.Student14PointFive)
        self.FourteenbtnPointFive.grid(row=5, column=2)
        self.FourteenbtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                          text='10', padx=0, width=4, bd=0, relief=FLAT,
                                          height=1, bg=eye_col_2, command=self.Student14PointTen)
        self.FourteenbtnPointTen.grid(row=5, column=3)
        self.FourteenbtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                             text='20', padx=0, width=4, bd=0, relief=FLAT,
                                             height=1, bg=eye_col_1, command=self.Student14PointTwe)
        self.FourteenbtnPointTwenty.grid(row=5, column=4)

        self.FifteenbtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                         padx=0, width=4, bd=0, relief=FLAT, height=1,
                                         bg=eye_col_2, command=self.Student15PointOne)
        self.FifteenbtnPointOne.grid(row=6, column=1)
        self.FifteenbtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                          text='5', padx=0, width=4, bd=0, relief=FLAT,
                                          height=1, bg=eye_col_2, command=self.Student15PointFive)
        self.FifteenbtnPointFive.grid(row=6, column=2)
        self.FifteenbtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                         text='10', padx=0, width=4, bd=0, relief=FLAT,
                                         height=1, bg=eye_col_2, command=self.Student15PointTen)
        self.FifteenbtnPointTen.grid(row=6, column=3)
        self.FifteenbtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                            text='20', padx=0, width=4, bd=0, relief=FLAT,
                                            height=1, bg=eye_col_1, command=self.Student15PointTwe)
        self.FifteenbtnPointTwenty.grid(row=6, column=4)

        self.SixteenbtnPointOne = Button(self.TOPFRAME_5, font=('consolas', 12), text='1',
                                         padx=0, width=4, bd=0, relief=FLAT, height=1,
                                         bg=eye_col_2, command=self.Student16PointOne)
        self.SixteenbtnPointOne.grid(row=7, column=1)
        self.SixteenbtnPointFive = Button(self.TOPFRAME_5, font=('consolas', 12),
                                          text='5', padx=0, width=4, bd=0, relief=FLAT,
                                          height=1, bg=eye_col_2, command=self.Student16PointFive)
        self.SixteenbtnPointFive.grid(row=7, column=2)
        self.SixteenbtnPointTen = Button(self.TOPFRAME_5, font=('consolas', 12),
                                         text='10', padx=0, width=4, bd=0, relief=FLAT,
                                         height=1, bg=eye_col_2, command=self.Student16PointTen)
        self.SixteenbtnPointTen.grid(row=7, column=3)
        self.SixteenbtnPointTwenty = Button(self.TOPFRAME_5, font=('consolas', 12),
                                            text='20', padx=0, width=4, bd=0, relief=FLAT,
                                            height=1, bg=eye_col_1, command=self.Student16PointTwe)
        self.SixteenbtnPointTwenty.grid(row=7, column=4)

        ## Frames 1 & 6 Loading Bars

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('red.Horizontal.TProgressbar', background='cornsilk',
                    troughcolor='black', bordercolor='black',
                    darkcolor='black')

        self.myLevelOne = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                          length=length_bar, mode='determinate',
                                          style='red.Horizontal.TProgressbar')
        self.myLevelOne.pack(side=TOP, pady=7.5)

        self.myLevelTwo = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                          length=length_bar, mode='determinate',
                                          style='red.Horizontal.TProgressbar')
        self.myLevelTwo.pack(side=TOP, pady=7.5)

        self.myLevelThree = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                            length=length_bar, mode='determinate',
                                            style='red.Horizontal.TProgressbar')
        self.myLevelThree.pack(side=TOP, pady=7.5)

        self.myLevelFour = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                           length=length_bar, mode='determinate',
                                           style='red.Horizontal.TProgressbar')
        self.myLevelFour.pack(side=TOP, pady=7.5)

        self.myLevelFive = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                           length=length_bar, mode='determinate',
                                           style='red.Horizontal.TProgressbar')
        self.myLevelFive.pack(side=TOP, pady=7.5)

        self.myLevelSix = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                          length=length_bar, mode='determinate',
                                          style='red.Horizontal.TProgressbar')
        self.myLevelSix.pack(side=TOP, pady=7.5)

        self.myLevelSeven = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                            length=length_bar, mode='determinate',
                                            style='red.Horizontal.TProgressbar')
        self.myLevelSeven.pack(side=TOP, pady=7.5)

        self.myLevelEight = ttk.Progressbar(self.TOPFRAME_1, orient=HORIZONTAL,
                                            length=length_bar, mode='determinate',
                                            style='red.Horizontal.TProgressbar')
        self.myLevelEight.pack(side=TOP, pady=7.5)

        self.myLevelNine = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                           length=length_bar, mode='determinate',
                                           style='red.Horizontal.TProgressbar')
        self.myLevelNine.pack(side=TOP, pady=7.5)

        self.myLevelTen = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                          length=length_bar, mode='determinate',
                                          style='red.Horizontal.TProgressbar')
        self.myLevelTen.pack(side=TOP, pady=7.5)

        self.myLevelEleven = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                             length=length_bar, mode='determinate',
                                             style='red.Horizontal.TProgressbar')
        self.myLevelEleven.pack(side=TOP, pady=7.5)

        self.myLevelTwelve = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                             length=length_bar, mode='determinate',
                                             style='red.Horizontal.TProgressbar')
        self.myLevelTwelve.pack(side=TOP, pady=7.5)

        self.myLevelThirteen = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                               length=length_bar, mode='determinate',
                                               style='red.Horizontal.TProgressbar')
        self.myLevelThirteen.pack(side=TOP, pady=7.5)

        self.myLevelFourteen = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                               length=length_bar, mode='determinate',
                                               style='red.Horizontal.TProgressbar')
        self.myLevelFourteen.pack(side=TOP, pady=7.5)

        self.myLevelFifteen = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                              length=length_bar, mode='determinate',
                                              style='red.Horizontal.TProgressbar')
        self.myLevelFifteen.pack(side=TOP, pady=7.5)

        self.myLevelSixteen = ttk.Progressbar(self.TOPFRAME_6, orient=HORIZONTAL,
                                              length=length_bar, mode='determinate',
                                              style='red.Horizontal.TProgressbar')
        self.myLevelSixteen.pack(side=TOP, pady=7.5)

        ##########################################################################

        # Level 3 Widgets (Chatbot Frame stuff)

        self.Query = StringVar()

        self.lbl_input = Entry(self.CHATBOT_FRAME_B, font='consolas 12 bold',
                               fg='black', width=24, bg='white',
                               textvariable =self.Query)
        self.lbl_input.pack(side=LEFT, padx=5)

        self.btn_send = Button(self.CHATBOT_FRAME_B, text='SEND', relief=RAISED,
                               width=6, height=1, font='consolas 10 bold',
                               padx=0, pady=0, bg='grey',
                               bd=7, fg='black', command = self.send_box)
        self.btn_send.pack(side=RIGHT)

        # self.sequence_door = [ImageTk.PhotoImage(img)
        #                     for img in ImageSequence.Iterator(
        #                         Image.open('better gate2.gif'))]

        self.sequence_X = [ImageTk.PhotoImage(img)
                           for img in ImageSequence.Iterator(
                Image.open('images/mech.gif'))]

        self.sequence_hurt = [ImageTk.PhotoImage(img)
                              for img in ImageSequence.Iterator(
                Image.open('images/mech_hurt2.gif'))]

        self.sequence_X2 = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                Image.open('images/worm2.gif'))]

        self.myLevelX = ttk.Progressbar(self.CHATBOT_FRAME_A, orient=HORIZONTAL,
                                        length=length_bar, mode='determinate',
                                        style='red.Horizontal.TProgressbar')

        self.sequence_Y = [ImageTk.PhotoImage(img)
                           for img in ImageSequence.Iterator(
                Image.open('images/wormA.gif'))]

        self.sequence_Z = [ImageTk.PhotoImage(img)
                           for img in ImageSequence.Iterator(
                Image.open('images/wormB.gif'))]

        self.myLevelX['value'] = 100

        self.myLevelX.pack(side=TOP)

        self.canvasX = Canvas(self.CHATBOT_FRAME_A,
                              width=300, height=180, bg='black', highlightbackground='black',
                              highlightthickness=0)
        self.canvasX.pack(side=TOP, fill=BOTH, expand=True)

        self.lblhealth_left = Label(self.canvasX, width=17, height=1,
                                    bg='black', text='Protector-Bot', fg='cornsilk', font='consolas 12 bold')
        self.lblhealth_left.pack(side=LEFT, anchor=NE)

        self.health_num = '        HP ' + str(self.myLevelX['value'])

        self.lblhealth_right = Label(self.canvasX, width=14, height=1,
                                     bg='black', text=self.health_num, fg='cornsilk', font='consolas 12 bold')
        self.lblhealth_right.pack(side=RIGHT, anchor=NW)

        self.imageX = self.canvasX.create_image(155, 125, image=self.sequence_X[0])

        # self.imageY = self.canvasX.create_image(75,160, image = self.sequence_Y[0])

        # self.imageZ = self.canvasX.create_image(265,160, image = self.sequence_Z[0])

        # self.imageDoor = self.canvasX.create_image(135, 115, image = self.sequence_door[0])

        ##########################################################################

        # Level 3 Widgets (Nano-Bots)
        canvas_width = 90
        canvas_height = 93
        btn_col = 'red'

        can_bg = 'white'

        self.canvas1 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas1.grid(row=1, column=0)

        # self.btn_stud1 = Button(self.canvas1, width = 3, height = 1, relief = RAISED)
        # self.canvas1.create_window(20,20, window = self.btn_stud1)

        self.canvas2 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas2.grid(row=1, column=1)
        self.canvas3 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas3.grid(row=1, column=2)
        self.canvas4 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas4.grid(row=1, column=3)
        self.canvas5 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas5.grid(row=1, column=4)
        self.canvas6 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas6.grid(row=1, column=5)
        self.canvas7 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas7.grid(row=1, column=6)
        self.canvas8 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas8.grid(row=1, column=7)
        self.canvas9 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                              height=canvas_height, bg=can_bg, bd=9,
                              relief=RAISED, highlightbackground='black',
                              highlightthickness=1)
        self.canvas9.grid(row=2, column=0)
        self.canvas10 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                               height=canvas_height, bg=can_bg, bd=9,
                               relief=RAISED, highlightbackground='black',
                               highlightthickness=1)
        self.canvas10.grid(row=2, column=1)
        self.canvas11 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                               height=canvas_height, bg=can_bg, bd=9,
                               relief=RAISED, highlightbackground='black',
                               highlightthickness=1)
        self.canvas11.grid(row=2, column=2)
        self.canvas12 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                               height=canvas_height, bg=can_bg, bd=9,
                               relief=RAISED, highlightbackground='black',
                               highlightthickness=1)
        self.canvas12.grid(row=2, column=3)
        self.canvas13 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                               height=canvas_height, bg=can_bg, bd=9,
                               relief=RAISED, highlightbackground='black',
                               highlightthickness=1)
        self.canvas13.grid(row=2, column=4)
        self.canvas14 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                               height=canvas_height, bg=can_bg, bd=9,
                               relief=RAISED, highlightbackground='black',
                               highlightthickness=1)
        self.canvas14.grid(row=2, column=5)

        self.canvas15 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                               height=canvas_height, bg=can_bg, bd=9,
                               relief=RAISED, highlightbackground='black',
                               highlightthickness=1)
        self.canvas15.grid(row=2, column=6)
        self.canvas16 = Canvas(self.MIDDLE_FRAME, width=canvas_width,
                               height=canvas_height, bg=can_bg, bd=9,
                               relief=RAISED, highlightbackground='black',
                               highlightthickness=1)
        self.canvas16.grid(row=2, column=7)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

        self.lblart1 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='1',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire1_go, state=DISABLED)

        self.lblart1.grid(row=0, column=0, sticky=W)
        self.lblart2 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='2',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire2_go, state=DISABLED)

        self.lblart2.grid(row=0, column=1, sticky=W)
        self.lblart3 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='3',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire3_go, state=DISABLED)

        self.lblart3.grid(row=0, column=2, sticky=W)
        self.lblart4 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='4',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire4_go, state=DISABLED)
        self.lblart4.grid(row=0, column=3, sticky=W)
        self.lblart5 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='5',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire5_go, state=DISABLED)
        self.lblart5.grid(row=0, column=4, sticky=W)
        self.lblart6 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='6',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire6_go, state=DISABLED)
        self.lblart6.grid(row=0, column=5, sticky=W)
        self.lblart7 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='7',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire7_go, state=DISABLED)
        self.lblart7.grid(row=0, column=6, sticky=W)
        self.lblart8 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='8',
                              bg='black', fg=btn_col, relief=RAISED, width=4, height=1,
                              command=self.fire8_go, state=DISABLED)
        self.lblart8.grid(row=0, column=7, sticky=W)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

        self.lblart9 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='9',
                              bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                              command=self.water9_go, state=DISABLED)
        self.lblart9.grid(row=3, column=0, sticky=SW)
        self.lblart10 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='10',
                               bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                               command=self.water10_go, state=DISABLED)
        self.lblart10.grid(row=3, column=1, sticky=SW)
        self.lblart11 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='11',
                               bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                               command=self.water11_go, state=DISABLED)
        self.lblart11.grid(row=3, column=2, sticky=SW)
        self.lblart12 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='12',
                               bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                               command=self.water12_go, state=DISABLED)
        self.lblart12.grid(row=3, column=3, sticky=SW)
        self.lblart13 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='13',
                               bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                               state=DISABLED, command=self.water13_go)
        self.lblart13.grid(row=3, column=4, sticky=SW)
        self.lblart14 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='14',
                               bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                               state=DISABLED, command=self.water14_go)
        self.lblart14.grid(row=3, column=5, sticky=SW)
        self.lblart15 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='15',
                               bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                               state=DISABLED, command=self.water15_go)
        self.lblart15.grid(row=3, column=6, sticky=SW)
        self.lblart16 = Button(self.MIDDLE_FRAME, font=('Consolas', 12, 'bold'), text='16',
                               bg='black', fg=btn_col, relief=SUNKEN, width=4, height=1,
                               state=DISABLED, command=self.water16_go)
        self.lblart16.grid(row=3, column=7, sticky=SW)

        self.lbl1Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countOne, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl1Level.grid(row=0, column=0, sticky=E)
        self.lbl2Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countTwo, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl2Level.grid(row=0, column=1, sticky=E)
        self.lbl3Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countThree, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl3Level.grid(row=0, column=2, sticky=E)
        self.lbl4Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countFour, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl4Level.grid(row=0, column=3, sticky=E)
        self.lbl5Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countFive, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl5Level.grid(row=0, column=4, sticky=E)
        self.lbl6Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countEight, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl6Level.grid(row=0, column=5, sticky=E)
        self.lbl7Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countSeven, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl7Level.grid(row=0, column=6, sticky=E)
        self.lbl8Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countEight, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl8Level.grid(row=0, column=7, sticky=E)

        self.lbl9Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                               text=self.countNine, bg='cornsilk', relief=SUNKEN,
                               width=9, height=2)
        self.lbl9Level.grid(row=3, column=0, sticky=SE)
        self.lbl10Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                                text=self.countTen, bg='cornsilk', relief=SUNKEN,
                                width=9, height=2)
        self.lbl10Level.grid(row=3, column=1, sticky=SE)
        self.lbl11Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                                text=self.countEleven, bg='cornsilk', relief=SUNKEN,
                                width=9, height=2)
        self.lbl11Level.grid(row=3, column=2, sticky=SE)
        self.lbl12Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                                text=self.countTwelve, bg='cornsilk', relief=SUNKEN,
                                width=9, height=2)
        self.lbl12Level.grid(row=3, column=3, sticky=SE)
        self.lbl13Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                                text=self.countThirteen, bg='cornsilk', relief=SUNKEN,
                                width=9, height=2)
        self.lbl13Level.grid(row=3, column=4, sticky=SE)
        self.lbl14Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                                text=self.countFourteen, bg='cornsilk', relief=SUNKEN,
                                width=9, height=2)
        self.lbl14Level.grid(row=3, column=5, sticky=SE)
        self.lbl15Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                                text=self.countFifteen, bg='cornsilk', relief=SUNKEN,
                                width=9, height=2)
        self.lbl15Level.grid(row=3, column=6, sticky=SE)
        self.lbl16Level = Label(self.MIDDLE_FRAME, font=('consolas', 10, 'bold'),
                                text=self.countSixteen, bg='cornsilk', relief=SUNKEN,
                                width=9, height=2)
        self.lbl16Level.grid(row=3, column=7, sticky=SE)

        x1 = 57
        y1 = 46
        x2 = 55
        y2 = 46

        self.image1 = self.canvas1.create_image(x1, y1)  # , image = self.sequence_prev1[0])
        self.image2 = self.canvas2.create_image(x1, y1)  # , image = self.sequence_go[0])
        self.image3 = self.canvas3.create_image(x1, y1)  # , image = self.sequence_dead[0])
        self.image4 = self.canvas4.create_image(x1, y1)  # , image = self.sequence_go[0])
        self.image5 = self.canvas5.create_image(x1, y1)  # , image = self.sequence_prev1[0])
        self.image6 = self.canvas6.create_image(x1, y1)  # , image = self.sequence_dead[0])
        self.image7 = self.canvas7.create_image(x1, y1)  # , image = self.sequence_go[0])
        self.image8 = self.canvas8.create_image(x1, y1)  # , image = self.sequence_go[0])
        self.image9 = self.canvas9.create_image(55, y2)  # , image = self.sequence_prev1[0])
        self.image10 = self.canvas10.create_image(x2, y2)  # , image = self.sequence_prev1[0])
        self.image11 = self.canvas11.create_image(x2, y2)  # , image = self.sequence_prev1[0])
        self.image12 = self.canvas12.create_image(x2, y2)  # , image = self.sequence_prev1[0])
        self.image13 = self.canvas13.create_image(x2, y2)  # , image = self.sequence_prev1[0])
        self.image14 = self.canvas14.create_image(x2, y2)  # , image = self.sequence_prev1[0])
        self.image15 = self.canvas15.create_image(x2, y2)  # , image = self.sequence_prev1[0])
        self.image16 = self.canvas16.create_image(x2, y2)  # , image = self.sequence_prev1[0])

        self.animate1(0)
        self.animate2(0)
        self.animate3(0)
        self.animate4(0)
        self.animate5(0)
        self.animate6(0)
        self.animate7(0)
        self.animate8(0)
        self.animate9(0)
        self.animate10(0)
        self.animate11(0)
        self.animate12(0)
        self.animate13(0)
        self.animate14(0)
        self.animate15(0)
        self.animate16(0)

        while True:
            self.blinking()
            self.waithere(5000)
            self.blinking()
            self.waitRand()
            self.blinking()
            self.Look_Straight()
            self.waitRand()

    # self.animateDoor(0)

    #############################################################################################
    #############################################################################################
    #############################################################################################
    #############################################################################################
    #############################################################################################
    #############################################################################################
    #############################################################################################



        # if self.bot_input == 'Magikid C1 has defeated the guard':
        #     self.countSeven = int(self.countSeven)
        #     self.countSeven += 75
        #     self.lbl7Level.config(text=str(self.countSeven))
        #     self.countEight = int(self.countEight)
        #     self.countEight += 75
        #     self.lbl8Level.config(text=str(self.countEight))
        #     self.countNine = int(self.countNine)
        #     self.countNine += 75
        #     self.lbl9Level.config(text=str(self.countNine))
        #     self.countTen = int(self.countTen)
        #     self.countTen += 75
        #     self.lbl10Level.config(text=str(self.countTen))
        #
        # if self.bot_input == 'Magikid C2 has defeated the guard':
        #     self.countEleven = int(self.countEleven)
        #     self.countEleven += 75
        #     self.lbl11Level.config(text=str(self.countEleven))
        #     self.countTwelve = int(self.countTwelve)
        #     self.countTwelve += 75
        #     self.lbl12Level.config(text=str(self.countTwelve))

    def createNew(self):
        file = open('Point System 2.csv', 'w')
        file.close()

    def saveTotal(self):
        file = open('Point System 2.csv', 'w')

        new_record = str(self.student1) + ',' + str(self.countOne) + '\n' + \
                     str(self.student2) + ',' + str(self.countTwo) + '\n' + \
                     str(self.student3) + ',' + str(self.countThree) + '\n' + \
                     str(self.student4) + ',' + str(self.countFour) + '\n' + \
                     str(self.student5) + ',' + str(self.countFive) + '\n' + \
                     str(self.student6) + ',' + str(self.countSix) + '\n' + \
                     str(self.student7) + ',' + str(self.countSeven) + '\n' + \
                     str(self.student8) + ',' + str(self.countEight) + '\n' + \
                     str(self.student9) + ',' + str(self.countNine) + '\n' + \
                     str(self.student10) + ',' + str(self.countTen) + '\n' + \
                     str(self.student11) + ',' + str(self.countEleven) + '\n' + \
                     str(self.student12) + ',' + str(self.countTwelve) + '\n' + \
                     str(self.student13) + ',' + str(self.countThirteen) + '\n' + \
                     str(self.student14) + ',' + str(self.countFourteen) + '\n' + \
                     str(self.student15) + ',' + str(self.countFifteen) + '\n' + \
                     str(self.student16) + ',' + str(self.countSixteen) + '\n'

        file.write(new_record)
        file.close()

    def loadAll(self):

        file = csv.reader(open('point system 2.csv'))

        tmp = []
        for row in file:
            tmp.append(row)

        x = 0
        for i in tmp:
            data = tmp[x]
            x += 1

        print(f'tmp: {tmp}')
        print(f'data: {data}')

        self.lbl1Level['text'] = tmp[0][1]
        self.countOne = tmp[0][1]
        self.lbl2Level['text'] = tmp[1][1]
        self.countTwo = tmp[1][1]
        self.lbl3Level['text'] = tmp[2][1]
        self.countThree = tmp[2][1]
        self.lbl4Level['text'] = tmp[3][1]
        self.countFour = tmp[3][1]
        self.lbl5Level['text'] = tmp[4][1]
        self.countFive = tmp[4][1]
        self.lbl6Level['text'] = tmp[5][1]
        self.countSix = tmp[5][1]
        self.lbl7Level['text'] = tmp[6][1]
        self.countSeven = tmp[6][1]
        self.lbl8Level['text'] = tmp[7][1]
        self.countEight = tmp[7][1]

        self.lbl9Level['text'] = tmp[8][1]
        self.countNine = tmp[8][1]
        self.lbl10Level['text'] = tmp[9][1]
        self.countTen = tmp[9][1]
        self.lbl11Level['text'] = tmp[10][1]
        self.countEleven = tmp[10][1]
        self.lbl12Level['text'] = tmp[11][1]
        self.countTwelve = tmp[11][1]
        self.lbl13Level['text'] = tmp[12][1]
        self.countThirteen = tmp[12][1]
        self.lbl14Level['text'] = tmp[13][1]
        self.countFourteen = tmp[13][1]
        self.lbl15Level['text'] = tmp[14][1]
        self.countFifteen = tmp[14][1]
        self.lbl16Level['text'] = tmp[15][1]
        self.countSixteen = tmp[15][1]

        self.animateX(0)
        self.animateY(0)
        self.animateZ(0)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno('The Great Python Adventure', 'Confirm if you want to quit.')
        if iExit > 0:
            root.destroy()

    # def animateDoor(self, counter):
    #     self.canvasX.itemconfig(self.imageDoor, image = self.sequence_door[counter])
    #     self.root.after(75, lambda: self.animateDoor((counter + 1) % len(self.sequence_door)))

    def animateX(self, counter):
        self.canvasX.itemconfig(self.imageX, image=self.sequence_X[counter])
        self.root.after(80, lambda: self.animateX((counter + 1) % len(self.sequence_X)))

    def animateX2(self, counter):
        self.canvasX.itemconfig(self.imageX, image=self.sequence_X2[counter])
        self.root.after(80, lambda: self.animateX2((counter + 1) % len(self.sequence_X2)))

    def animateY(self, counter):
        self.canvasX.itemconfig(self.imageY, image=self.sequence_Y[counter])
        self.root.after(80, lambda: self.animateY((counter + 1) % len(self.sequence_Y)))

    def animateZ(self, counter):
        self.canvasX.itemconfig(self.imageZ, image=self.sequence_Z[counter])
        self.root.after(50, lambda: self.animateZ((counter + 1) % len(self.sequence_Z)))

    def Hurt1(self, counter):
        # I always want the counter to only loop through once
        self.canvasX.itemconfig(self.imageX, image=self.sequence_hurt[counter])

        if (counter < len(self.sequence_hurt) - 1):
            self.root.after(50, lambda: self.Hurt1((counter + 1) % len(self.sequence_hurt)))

    def print_general(self, message, duration, size, wraplen, font_n, col, loc):
        string_output = ''
        for char in message:
            string_output += char
            loc.config(text=string_output, font=f'{font_n} {size}',
                       wraplength=wraplen, justify=LEFT, fg=col, pady=2)
            self.waithere(duration)

    def waithere(self, duration):
        var = IntVar()
        root.after(duration, var.set, 1)
        root.wait_variable(var)

    def send_box(self):

        self.bot_input = self.Query.get()

        list_char = self.bot_input.split(' ')
        self.frame_col2 = 'indianred'
        self.frame_col3 = 'purple'
        self.frame_col4 = '#E3655B'
        self.frame_col5 = '#847996'

        self.lblStudentName1.configure(fg='grey50')
        self.lblStudentName2.configure(fg='grey50')
        self.lblStudentName3.configure(fg='grey50')
        self.lblStudentName4.configure(fg='grey50')
        self.lblStudentName5.configure(fg='grey50')
        self.lblStudentName6.configure(fg='grey50')
        self.lblStudentName7.configure(fg='grey50')
        self.lblStudentName8.configure(fg='grey50')
        self.lblStudentName9.configure(fg='grey50')
        self.lblStudentName10.configure(fg='grey50')
        self.lblStudentName11.configure(fg='grey50')
        self.lblStudentName12.configure(fg='grey50')
        self.lblStudentName13.configure(fg='grey50')
        self.lblStudentName14.configure(fg='grey50')
        self.lblStudentName15.configure(fg='grey50')
        self.lblStudentName16.configure(fg='grey50')

        if list_char[0] == 'Magikid':
            if list_char[1] == 'C1':
                self.MAINFRAME.configure(bg = self.frame_col2)
                self.HEADLINE_FRAME.configure(bg = self.frame_col2)
                self.btnMenu.configure(bg = self.frame_col2)
                self.btnCreateNew.configure(bg = self.frame_col2)
                self.btnSave.configure(bg = self.frame_col2)
                self.btnLoad.configure(bg=self.frame_col2)
                self.btnExit.configure(bg=self.frame_col2)

                self.lblStudentName7.configure(fg='green2')
                self.lblStudentName8.configure(fg='green2')
                self.lblStudentName9.configure(fg='green2')
                self.lblStudentName10.configure(fg='green2')
            if list_char[1] == 'C2':
                self.MAINFRAME.configure(bg = self.frame_col3)
                self.HEADLINE_FRAME.configure(bg = self.frame_col3)
                self.btnMenu.configure(bg = self.frame_col3)
                self.btnCreateNew.configure(bg = self.frame_col3)
                self.btnSave.configure(bg = self.frame_col3)
                self.btnLoad.configure(bg=self.frame_col3)
                self.btnExit.configure(bg=self.frame_col3)

                self.lblStudentName11.configure(fg='green2')
                self.lblStudentName12.configure(fg='green2')

            #########################################

        elif list_char[0] == 'Premier':
            self.MAINFRAME.configure(bg = self.frame_col3)
            self.HEADLINE_FRAME.configure(bg = self.frame_col3)
            self.btnMenu.configure(bg = self.frame_col3)
            self.btnCreateNew.configure(bg = self.frame_col3)
            self.btnSave.configure(bg = self.frame_col3)
            self.btnLoad.configure(bg=self.frame_col3)
            self.btnExit.configure(bg=self.frame_col3)

            #########################################
        elif list_char[0] == 'Creative':
            self.MAINFRAME.configure(bg = self.frame_col4)
            self.HEADLINE_FRAME.configure(bg = self.frame_col4)
            self.btnMenu.configure(bg = self.frame_col4)
            self.btnCreateNew.configure(bg = self.frame_col4)
            self.btnSave.configure(bg = self.frame_col4)
            self.btnLoad.configure(bg=self.frame_col4)
            self.btnExit.configure(bg=self.frame_col4)

        elif list_char[0] == 'Tangerine':
            self.MAINFRAME.configure(bg = self.frame_col5)
            self.HEADLINE_FRAME.configure(bg = self.frame_col5)
            self.btnMenu.configure(bg = self.frame_col5)
            self.btnCreateNew.configure(bg = self.frame_col5)
            self.btnSave.configure(bg = self.frame_col5)
            self.btnLoad.configure(bg=self.frame_col5)
            self.btnExit.configure(bg=self.frame_col5)
            self.lblStudentName6.configure(fg='green2')

        if list_char[0] == 'subtract':
            if list_char[3] == 'Tangerine':
                pass

        print(list_char[0])
        self.lbl_input.delete(0, END)


    def next_boss(self):

        if self.bot_input == 'Magikid C1 has joined the battle':
            self.countSeven = int(self.countSeven)
            self.countSeven += 75
            self.lbl7Level.config(text=str(self.countSeven))
            self.countEight = int(self.countEight)
            self.countEight += 75
            self.lbl8Level.config(text=str(self.countEight))
            self.countNine = int(self.countNine)
            self.countNine += 75
            self.lbl9Level.config(text=str(self.countNine))
            self.countTen = int(self.countTen)
            self.countTen += 75
            self.lbl10Level.config(text=str(self.countTen))

        if self.bot_input == 'Magikid C2 has joined the battle':
            self.countEleven = int(self.countEleven)
            self.countEleven += 75
            self.lbl11Level.config(text=str(self.countEleven))
            self.countTwelve = int(self.countTwelve)
            self.countTwelve += 75
            self.lbl12Level.config(text=str(self.countTwelve))


        self.canvasX.delete('all')
        self.lblhealth_left.destroy()
        self.lblhealth_right.destroy()

        # if self.bot_input == 'class 1':
        #     pass
        # elif self.bot_input == 'class 2':
        #     pass
        # elif self.bot_input == 'class 3':
        #     pass

        monster_list = ['bacterio2.gif', 'bacterio3.gif', 'bacterio4.gif',
                        'bacterio5.gif']
        new_monster = random.choice(monster_list)

        power_up_type = 'Mineral'
        power_up = 'Full ultimate for the robot that defeated the monster.'
        name_monster = 'Protector Bot'

        if new_monster == 'bacterio2.gif':
            name_monster = 'Diamond Mechatron'
            monster_health = 190
            power_up = 'Virus Nano-bots 1,5,12 automatically begin with ultimate ready weapons.'
            power_up_type = 'diamond'
            self.myLevelOne['value'] = 100
            self.myLevelFive['value'] = 100
            self.myLevelTwelve['value'] = 100

            # how to give points to specific robots

        elif new_monster == 'bacterio3.gif':
            name_monster = 'Ruby Mechatron'
            monster_health = 165
            power_up = 'Virus Nano-bots 2,8,16 automatically begin with ultimate ready weapons.'
            power_up_type = 'emerald'
            self.myLevelTwo['value'] = 100
            self.myLevelEight['value'] = 100
            self.myLevelSixteen['value'] = 100

        elif new_monster == 'bacterio4.gif':
            name_monster = 'Emerald Mechatron'
            monster_health = 250
            power_up = 'Virus Nano-bots 3,13, and 15 automatically begin with ultimate ready weapons.'
            power_up_type = 'Jade'
            self.myLevelThree['value'] = 100
            self.myLevelThirteen['value'] = 100
            self.myLevelFifteen['value'] = 100

        elif new_monster == 'bacterio5.gif':
            name_monster = 'Opal Mechatron'
            monster_health = 225
            power_up = 'Virus Nano-bots 1,11 automatically begin with ultimate ready weapons.'
            power_up_type = 'Quartz'
            self.myLevelOne['value'] = 100
            self.myLevelEleven['value'] = 100

#         elif new_monster == 'bluerob_2.gif':
#             name_monster = 'TANKER Mecha'
#             monster_health = 300
#             power_up = 'The virus bot that defeated the last monster chooses three virus nano-bots to\
# automatically begin with ultimate ready weapons.'
#             power_up_type = 'Ruby'
#
#         elif new_monster == 'bluerob_2.gif':
#             name_monster = 'Ancient Unknown'
#             monster_health = 240
#             power_up = 'the virus nano bot that defeated the last monster chooses two virus nano-bots to\
# automatically begin with ultimate ready weapons.'
#
#         elif new_monster == 'bluerob_2.gif':
#             name_monster = 'ROBO-CAT'
#             monster_health = 240
#             power_up = 'All virus nano-bots begin with 50% ultimate ready weapon systems.'
#             power_up_type = 'Magnetic'
#             self.myLevelOne['value'] += 50
#             self.myLevelTwo['value'] += 50
#             self.myLevelThree['value'] += 50
#             self.myLevelFour['value'] += 50
#             self.myLevelFive['value'] += 50
#             self.myLevelSix['value'] += 50
#             self.myLevelSeven['value'] += 50
#             self.myLevelEight['value'] += 50
#             self.myLevelNine['value'] += 50
#             self.myLevelTen['value'] += 50
#             self.myLevelEleven['value'] += 50
#             self.myLevelTwelve['value'] += 50
#             self.myLevelThirteen['value'] += 50
#             self.myLevelFourteen['value'] += 50
#             self.myLevelFifteen['value'] += 50
#             self.myLevelSixteen['value'] += 50
#         else:
#             power_up_type = 'Mineral'
#             power_up = 'Full ultimate for the robot that defeated the monster.'
#             name_monster = 'Protector Bot'

        self.lblChatText = Label(self.canvasX, width = 23, height = 13, font='System 12 bold',
                               text='', fg='green2', bg='black')
        self.lblChatText.pack_propagate(0)
        self.lblChatText.pack()

        self.print_general(f'You have defeated the enemy bot! power_up: {power_up_type}.\
This power up allows: {power_up}. Now get ready... {name_monster} appears.', 50, 12, 285,
                           'terminal', 'green2', self.lblChatText)

        self.waithere(5000)
        self.lblChatText.destroy()

        self.lblhealth_left = Label(self.canvasX, width=17, height=1,
                                        bg='black', text = name_monster,
                                    fg='cornsilk', font='consolas 12 bold')
        self.lblhealth_left.pack(side=LEFT, anchor=NE)

        self.myLevelX['value'] = monster_health

        self.health_num = '        HP ' + str(self.myLevelX['value'])

        self.lblhealth_right = Label(self.canvasX, width=14, height=1,
                                         bg='black', text=self.health_num, fg='cornsilk', font='consolas 12 bold')
        self.lblhealth_right.pack(side=RIGHT, anchor=NW)

        self.imageX = self.canvasX.create_image(155, 135, image=self.sequence_X[0])
        self.sequence_X = [ImageTk.PhotoImage(img)
                           for img in ImageSequence.Iterator(
                Image.open(f'images/{new_monster}'))]

#         if self.myLevelX['value'] <= 0:
#
#             self.canvasX.delete('all')
#             self.lblhealth_left.destroy()
#             self.lblhealth_right.destroy()
#
#             self.lblChatText = Label(self.canvasX, width=22, height=8, font='System 12 bold',
#                                      text='', fg='green2', bg='black')
#             self.lblChatText.pack_propagate(0)
#             self.lblChatText.pack()
#
#             self.print_general(f'You have defeated the {name_monster}! You have just\
# received {power_up_type} powerup. This powerup allows: {power_up}.', 50, 12, 300,
#                                'terminal', 'green2', self.lblChatText)
#
#             self.waithere(5000)
#             self.lblChatText.destroy()

    def anim_fire1(self, counter):
        if (len(self.seq_fire1)) == len(self.seq_fire1):
            self.myLevelX['value'] -=  1.725
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire1, image=self.seq_fire1[counter])
        if (counter < len(self.seq_fire1) - 1):
            self.root.after(60, lambda: self.anim_fire1((counter + 1) % len(self.seq_fire1)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()


    def anim_fire2(self, counter):
        if len(self.seq_fire2) == len(self.seq_fire2):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire2, image=self.seq_fire2[counter])
        if (counter < len(self.seq_fire2) - 1):
            self.root.after(50, lambda: self.anim_fire2((counter + 1) % len(self.seq_fire2)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_fire3(self, counter):
        if len(self.seq_fire3) == len(self.seq_fire3):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire3, image=self.seq_fire3[counter])
        if (counter < len(self.seq_fire3) - 1):
            self.root.after(60, lambda: self.anim_fire3((counter + 1) % len(self.seq_fire3)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_fire4(self, counter):
        if len(self.seq_fire4) == len(self.seq_fire4):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire4, image=self.seq_fire4[counter])
        if (counter < len(self.seq_fire4) - 1):
            self.root.after(60, lambda: self.anim_fire4((counter + 1) % len(self.seq_fire4)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_fire5(self, counter):
        if len(self.seq_fire5) == len(self.seq_fire5):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire5, image=self.seq_fire5[counter])
        if (counter < len(self.seq_fire5) - 1):
            self.root.after(60, lambda: self.anim_fire5((counter + 1) % len(self.seq_fire5)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_fire6(self, counter):
        if len(self.seq_fire6) == len(self.seq_fire6):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire6, image=self.seq_fire6[counter])
        if (counter < len(self.seq_fire6) - 1):
            self.root.after(60, lambda: self.anim_fire6((counter + 1) % len(self.seq_fire6)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_fire7(self, counter):
        if len(self.seq_fire7) == len(self.seq_fire7):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire7, image=self.seq_fire7[counter])
        if (counter < len(self.seq_fire7) - 1):
            self.root.after(60, lambda: self.anim_fire7((counter + 1) % len(self.seq_fire7)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_fire8(self, counter):

        if len(self.seq_fire8) == len(self.seq_fire8):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.fire8, image=self.seq_fire8[counter])
        if (counter < len(self.seq_fire8) - 1):
            self.root.after(60, lambda: self.anim_fire8((counter + 1) % len(self.seq_fire8)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water9(self, counter):
        if len(self.seq_water9) == len(self.seq_water9):
            self.myLevelX['value'] -= 1.525
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water9, image=self.seq_water9[counter])
        if (counter < len(self.seq_water9) - 1):
            self.root.after(60, lambda: self.anim_water9((counter + 1) % len(self.seq_water9)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water10(self, counter):
        if len(self.seq_water10) == len(self.seq_water10):
            self.myLevelX['value'] -= 0.765
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water10, image=self.seq_water10[counter])
        if (counter < len(self.seq_water10) - 1):
            self.root.after(60, lambda: self.anim_water10((counter + 1) % len(self.seq_water10)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water11(self, counter):
        if len(self.seq_water11) == len(self.seq_water11):
            self.myLevelX['value'] -= 0.765
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water11, image=self.seq_water11[counter])
        if (counter < len(self.seq_water11) - 1):
            self.root.after(50, lambda: self.anim_water11((counter + 1) % len(self.seq_water11)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water12(self, counter):
        if len(self.seq_water12) == len(self.seq_water12):
            self.myLevelX['value'] -= 0.765
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water12, image=self.seq_water12[counter])
        if (counter < len(self.seq_water12) - 1):
            self.root.after(50, lambda: self.anim_water12((counter + 1) % len(self.seq_water12)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water13(self, counter):
        if len(self.seq_water13) == len(self.seq_water13):
            self.myLevelX['value'] -= 0.765
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water13, image=self.seq_water13[counter])
        if (counter < len(self.seq_water13) - 1):
            self.root.after(60, lambda: self.anim_water13((counter + 1) % len(self.seq_water13)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water14(self, counter):
        if len(self.seq_water14) == len(self.seq_water14):
            self.myLevelX['value'] -= 0.765
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water14, image=self.seq_water14[counter])
        if (counter < len(self.seq_water14) - 1):
            self.root.after(45, lambda: self.anim_water14((counter + 1) % len(self.seq_water14)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water15(self, counter):
        if len(self.seq_water15) == len(self.seq_water15):
            self.myLevelX['value'] -= 0.765
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water15, image=self.seq_water15[counter])
        if (counter < len(self.seq_water15) - 1):
            self.root.after(55, lambda: self.anim_water15((counter + 1) % len(self.seq_water15)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    def anim_water16(self, counter):
        if len(self.seq_water16) == len(self.seq_water16):
            self.myLevelX['value'] -= 1.40
            self.lblhealth_right.configure(text=('HP ' + str(round(self.myLevelX['value'], 5))))
            print(self.myLevelX['value'])

        self.canvasX.itemconfig(self.water16, image=self.seq_water16[counter])
        if (counter < len(self.seq_water16) - 1):
            self.root.after(60, lambda: self.anim_water16((counter + 1) % len(self.seq_water16)))

        if self.myLevelX['value'] <= 0:
            self.next_boss()

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

    def fire1_go(self):
        try:
            if (not (self.is_fire1_animating and self.is_hurt1)):
                self.is_fire1_animating = True
                # How to make it animate just one time
                self.fire1 = self.canvasX.create_image(165, 135, image=self.seq_fire1[0])
                self.anim_fire1(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.fire1)  # I'm not sure why the program restarts at a new
                # position rather than 0. also, if you click on it
                # too fast, you'll find that the picture imprints
                # itself.
                self.lblart1.configure(state=DISABLED)
                self.myLevelOne['value'] = 10
                self.animate1(0)

        # if (not self.is_hurt1):
        # 	self.is_hurt1 = True
        # 	self.Hurt1()
        # 	self.waithere(500)
        #     #self.waithere(500)

        # here we can flash the image and then show the worm getting hurt
        # Using Sequence_hurt to show attack
        # Create a def for sequence hurt
        # if (not self.is_hurt1):
        # 	self.is_hurt1 = True
        # 	self.Hurt1(0)
        # 	self.waithere(500)

        # self.animateX2(0)
        except TypeError:
            pass

    def fire2_go(self):
        try:
            if (not (self.is_fire2_animating and self.is_hurt1)):
                self.is_fire2_animating = True
                self.fire2 = self.canvasX.create_image(150, 135, image=self.seq_fire2[0])
                # How to make it animate just one time ?
                self.anim_fire2(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.fire2)
                self.lblart2.configure(state=DISABLED)
                self.myLevelTwo['value'] = 10
                self.animate2(0)
        except TypeError:
            pass

    def fire3_go(self):
        try:
            if (not (self.is_fire3_animating and self.is_hurt1)):
                self.is_fire3_animating = True
                self.fire3 = self.canvasX.create_image(165, 135, image=self.seq_fire3[0])
                self.anim_fire3(0)
                self.Hurt1(0)
                self.waithere(2000)

                self.canvasX.delete(self.fire3)
                self.lblart3.configure(state=DISABLED)
                self.myLevelThree['value'] = 10
                self.animate3(0)
        except TypeError:
            pass

    def fire4_go(self):

        try:
            if (not (self.is_fire4_animating and self.is_hurt1)):
                self.is_fire4_animating = True
                self.fire4 = self.canvasX.create_image(165, 135, image=self.seq_fire4[0])
                self.anim_fire4(0)
                self.waithere(2000)
                self.Hurt1(0)
                self.canvasX.delete(self.fire4)
                self.lblart4.configure(state=DISABLED)
                self.myLevelFour['value'] = 10
                self.animate4(0)

        except TypeError:
            pass

    def fire5_go(self):

        try:
            # How to make it animate just one time ?
            if (not (self.is_fire5_animating and self.is_hurt1)):
                self.fire5 = self.canvasX.create_image(165, 135, image=self.seq_fire5[0])
                self.anim_fire5(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.fire5)
                self.lblart5.configure(state=DISABLED)
                self.myLevelFive['value'] = 10
                self.animate5(0)
        except TypeError:
            pass

    def fire6_go(self):
        try:
            if (not (self.is_fire6_animating and self.is_hurt1)):
                self.fire6 = self.canvasX.create_image(165, 150, image=self.seq_fire6[0])

                self.anim_fire6(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.fire6)
                self.lblart6.configure(state=DISABLED)
                self.myLevelSix['value'] = 10
                self.animate6(0)
        except TypeError:
            pass

    def fire7_go(self):

        try:
            if (not (self.is_fire7_animating and self.is_hurt1)):
                self.fire7 = self.canvasX.create_image(155, 125, image=self.seq_fire7[0])
                # How to make it animate just one time ?
                self.anim_fire7(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.fire7)
                self.lblart7.configure(state=DISABLED)
                self.myLevelSeven['value'] = 10
                self.animate7(0)
        except TypeError:
            pass

    def fire8_go(self):

        try:
            if (not (self.is_fire8_animating and self.is_hurt1)):
                self.fire8 = self.canvasX.create_image(150, 135, image=self.seq_fire8[0])
                # How to make it animate just one time ?
                self.anim_fire8(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.fire8)
                self.lblart8.configure(state=DISABLED)
                self.myLevelEight['value'] = 10
                self.animate8(0)
        except TypeError:
            pass

    def water9_go(self):

        try:
            if (not (self.is_fire8_animating and self.is_hurt1)):
                self.water9 = self.canvasX.create_image(150, 135, image=self.seq_water9[0])
            # if (not (self.is_water9_animating and self.is_hurt1)):
            # How to make it animate just one time ?
                self.anim_water9(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.water9)
                self.lblart9.configure(state=DISABLED)
                self.myLevelNine['value'] = 10
            self.animate9(0)
        except TypeError:
            pass

    def water10_go(self):

        try:
            if (not (self.is_water9_animating and self.is_hurt1)):
                self.water10 = self.canvasX.create_image(165, 135, image=self.seq_water10[0])
            # How to make it animate just one time ?
                self.anim_water10(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.water10)
                self.lblart10.configure(state=DISABLED)
                self.myLevelTen['value'] = 10
                self.animate10(0)
        except TypeError:
            pass

    def water11_go(self):

        try:
            if (not (self.is_water9_animating and self.is_hurt1)):
                self.water11 = self.canvasX.create_image(137, 110, image=self.seq_water11[0])
                # How to make it animate just one time ?
                self.anim_water11(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.water11)
                self.lblart11.configure(state=DISABLED)
                self.myLevelEleven['value'] = 10
                self.animate11(0)

        except TypeError:
            pass

    def water12_go(self):

        try:
            if (not (self.is_water9_animating and self.is_hurt1)):
                self.water12 = self.canvasX.create_image(165, 110, image=self.seq_water12[0])
            # How to make it animate just one time ?
                self.anim_water12(0)
                self.Hurt1(0)
                self.waithere(5600)
                self.canvasX.delete(self.water12)
                self.lblart12.configure(state=DISABLED)
                self.myLevelTwelve['value'] = 10
                self.animate12(0)
        except TypeError:
            pass

    def water13_go(self):
        try:
            if (not (self.is_water9_animating and self.is_hurt1)):
                self.water13 = self.canvasX.create_image(165, 130, image=self.seq_water13[0])
                # How to make it animate just one time ?
                self.anim_water13(0)
                self.Hurt1(0)
                self.waithere(5000)
                self.canvasX.delete(self.water13)
                self.lblart13.configure(state=DISABLED)
                self.myLevelThirteen['value'] = 10
                self.animate13(0)
        except TypeError:
            pass

    def water14_go(self):

        try:
            if (not (self.is_water9_animating and self.is_hurt1)):
                # How to make it animate just one time ?
                self.water14 = self.canvasX.create_image(165, 130, image=self.seq_water14[0])
                self.anim_water14(0)
                self.Hurt1(0)
                self.waithere(3000)
                self.canvasX.delete(self.water14)
                self.lblart14.configure(state=DISABLED)
                self.myLevelFourteen['value'] = 10
                self.animate14(0)
        except TypeError:
            pass

    def water15_go(self):

        try:
            if (not (self.is_water9_animating and self.is_hurt1)):
                self.water15 = self.canvasX.create_image(165, 130, image=self.seq_water15[0])
                # How to make it animate just one time ?
                self.anim_water15(0)
                self.Hurt1(0)
                self.waithere(3500)
                self.canvasX.delete(self.water15)
                self.lblart15.configure(state=DISABLED)
                self.myLevelFifteen['value'] = 10
                self.animate15(0)
        except TypeError:
            pass

    def water16_go(self):

        try:
            if (not (self.is_water9_animating and self.is_hurt1)):
                # How to make it animate just one time ?
                self.water16 = self.canvasX.create_image(165, 130, image=self.seq_water16[0])
                self.anim_water16(0)
                self.Hurt1(0)
                self.waithere(2000)
                self.canvasX.delete(self.water16)
                self.lblart16.configure(state=DISABLED)
                self.myLevelSixteen['value'] = 10
                self.animate16(0)
        except TypeError:
            pass

    def Student1PointOne(self):
        self.myLevelOne['value'] += 1
        self.countOne = int(self.countOne)
        self.countOne += 1
        self.lbl1Level.config(text=self.countOne)

        if self.myLevelOne['value'] >= 100:
            self.lblart1.configure(state=NORMAL)
        # if self.count == 0:
        # 	count20 = True
        # 	count40 = True
        # 	count60 = True
        # 	count80 = True
        # 	count100 = True
        try:
            if self.myLevelOne['value'] >= 0 and \
                    self.myLevelOne['value'] <= 20 and self.count20 == True:
                self.animate1(0)
                self.count20 = False
            elif self.myLevelOne['value'] > 20 and \
                    self.myLevelOne['value'] <= 40 and self.count40 == True:
                self.animate1(0)
                self.count40 = False
            elif self.myLevelOne['value'] > 40 and \
                    self.myLevelOne['value'] <= 60 and self.count60 == True:
                self.animate1(0)
                self.count60 = False
            elif self.myLevelOne['value'] > 60 and \
                    self.myLevelOne['value'] <= 80 and self.count80 == True:
                self.animate1(0)
                self.count80 = False
            elif self.myLevelOne['value'] > 80 and \
                    self.myLevelOne['value'] <= 100 and self.count100 == True:
                self.animate1(0)
                self.count100 = False

        except AttributeError:
            pass

    def Student1PointFive(self):
        self.myLevelOne['value'] += 5

        self.countOne = int(self.countOne)
        self.countOne += 5
        self.lbl1Level.config(text=self.countOne)

        if self.myLevelOne['value'] >= 100:
            self.lblart1.configure(state=NORMAL)

        try:
            if self.myLevelOne['value'] >= 0 and \
                    self.myLevelOne['value'] <= 20 and self.count20 == True:
                self.animate1(0)
                self.count20 = False
            elif self.myLevelOne['value'] > 20 and \
                    self.myLevelOne['value'] <= 40 and self.count40 == True:
                self.animate1(0)
                self.count40 = False
            elif self.myLevelOne['value'] > 40 and \
                    self.myLevelOne['value'] <= 60 and self.count60 == True:
                self.animate1(0)
                self.count60 = False
            elif self.myLevelOne['value'] > 60 and \
                    self.myLevelOne['value'] <= 80 and self.count80 == True:
                self.animate1(0)
                self.count80 = False
            elif self.myLevelOne['value'] > 80 and \
                    self.myLevelOne['value'] <= 100 and self.count100 == True:
                self.animate1(0)
                self.count100 = False

        except AttributeError:
            pass

    def Student1PointTen(self):
        self.myLevelOne['value'] += 10

        self.countOne = int(self.countOne)
        self.countOne += 10
        self.lbl1Level.config(text=self.countOne)

        if self.myLevelOne['value'] >= 100:
            self.lblart1.configure(state=NORMAL)

        try:
            if self.myLevelOne['value'] >= 0 and \
                    self.myLevelOne['value'] <= 20 and self.count20 == True:
                self.animate1(0)
                self.count20 = False
            elif self.myLevelOne['value'] > 20 and \
                    self.myLevelOne['value'] <= 40 and self.count40 == True:
                self.animate1(0)
                self.count40 = False
            elif self.myLevelOne['value'] > 40 and \
                    self.myLevelOne['value'] <= 60 and self.count60 == True:
                self.animate1(0)
                self.count60 = False
            elif self.myLevelOne['value'] > 60 and \
                    self.myLevelOne['value'] <= 80 and self.count80 == True:
                self.animate1(0)
                self.count80 = False
            elif self.myLevelOne['value'] > 80 and \
                    self.myLevelOne['value'] <= 100 and self.count100 == True:
                self.animate1(0)
                self.count100 = False
        except AttributeError:
            pass

    def Student1PointTwe(self):
        self.myLevelOne['value'] += 20

        self.countOne = int(self.countOne)
        self.countOne += 20
        self.lbl1Level.config(text=self.countOne)

        if self.myLevelOne['value'] >= 100:
            self.lblart1.configure(state=NORMAL)

        try:
            if self.myLevelOne['value'] >= 0 and \
                    self.myLevelOne['value'] <= 20 and self.count20 == True:
                self.animate1(0)
                self.count20 = False
            elif self.myLevelOne['value'] > 20 and \
                    self.myLevelOne['value'] <= 40 and self.count40 == True:
                self.animate1(0)
                self.count40 = False
            elif self.myLevelOne['value'] > 40 and \
                    self.myLevelOne['value'] <= 60 and self.count60 == True:
                self.animate1(0)
                self.count60 = False
            elif self.myLevelOne['value'] > 60 and \
                    self.myLevelOne['value'] <= 80 and self.count80 == True:
                self.animate1(0)
                self.count80 = False
            elif self.myLevelOne['value'] > 80 and \
                    self.myLevelOne['value'] <= 100 and self.count100 == True:
                self.animate1(0)
                self.count100 = False

        except AttributeError:
            pass

    def Student2PointOne(self):
        self.myLevelTwo['value'] += 1

        self.countTwo = int(self.countTwo)
        self.countTwo += 1
        self.lbl2Level.config(text=self.countTwo)

        if self.myLevelTwo['value'] >= 100:
            self.lblart2.configure(state=NORMAL)

        try:
            if self.myLevelTwo['value'] >= 0 and self.myLevelTwo['value'] <= 20 and self.count20 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 20 and self.myLevelTwo['value'] <= 40 and self.count40 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 40 and self.myLevelTwo['value'] <= 60 and self.count60 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 60 and self.myLevelTwo['value'] <= 80 and self.count80 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 80 and self.myLevelTwo['value'] <= 100 and self.count100 == True:
                self.animate2(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student2PointFive(self):
        self.myLevelTwo['value'] += 5

        self.countTwo = int(self.countTwo)
        self.countTwo += 5
        self.lbl2Level.config(text=self.countTwo)

        if self.myLevelTwo['value'] >= 100:
            self.lblart2.configure(state=NORMAL)

        try:
            if self.myLevelTwo['value'] >= 0 and self.myLevelTwo['value'] <= 20 and self.count20 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 20 and self.myLevelTwo['value'] <= 40 and self.count40 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 40 and self.myLevelTwo['value'] <= 60 and self.count60 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 60 and self.myLevelTwo['value'] <= 80 and self.count80 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 80 and self.myLevelTwo['value'] <= 100 and self.count100 == True:
                self.animate2(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student2PointTen(self):
        self.myLevelTwo['value'] += 10

        self.countTwo = int(self.countTwo)
        self.countTwo += 10
        self.lbl2Level.config(text=self.countTwo)

        if self.myLevelTwo['value'] >= 100:
            self.lblart2.configure(state=NORMAL)

        try:
            if self.myLevelTwo['value'] >= 0 and self.myLevelTwo['value'] <= 20 and self.count20 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 20 and self.myLevelTwo['value'] <= 40 and self.count40 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 40 and self.myLevelTwo['value'] <= 60 and self.count60 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 60 and self.myLevelTwo['value'] <= 80 and self.count80 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 80 and self.myLevelTwo['value'] <= 100 and self.count100 == True:
                self.animate2(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student2PointTwe(self):
        self.myLevelTwo['value'] += 20

        self.countTwo = int(self.countTwo)
        self.countTwo += 20
        self.lbl2Level.config(text=self.countTwo)

        if self.myLevelTwo['value'] >= 100:
            self.lblart2.configure(state=NORMAL)

        try:
            if self.myLevelTwo['value'] >= 0 and self.myLevelTwo['value'] <= 20 and self.count20 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 20 and self.myLevelTwo['value'] <= 40 and self.count40 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 40 and self.myLevelTwo['value'] <= 60 and self.count60 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 60 and self.myLevelTwo['value'] <= 80 and self.count80 == True:
                self.animate2(0)
            elif self.myLevelTwo['value'] > 80 and self.myLevelTwo['value'] <= 100 and self.count100 == True:
                self.animate2(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student3PointOne(self):

        self.myLevelThree['value'] += 1

        self.countThree = int(self.countThree)
        self.countThree += 1
        self.lbl3Level.config(text=self.countThree)

        if self.myLevelThree['value'] >= 100:
            self.lblart3.configure(state=NORMAL)

        try:

            if self.myLevelThree['value'] >= 0 and self.myLevelThree['value'] <= 20 and self.count20 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 20 and self.myLevelThree['value'] <= 40 and self.count40 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 40 and self.myLevelThree['value'] <= 60 and self.count60 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 60 and self.myLevelThree['value'] <= 80 and self.count80 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 80 and self.myLevelThree['value'] <= 100 and self.count100 == True:
                self.animate3(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student3PointFive(self):

        self.myLevelThree['value'] += 5

        self.countThree = int(self.countThree)
        self.countThree += 5
        self.lbl3Level.config(text=self.countThree)

        if self.myLevelThree['value'] >= 100:
            self.lblart3.configure(state=NORMAL)

        try:

            if self.myLevelThree['value'] >= 0 and self.myLevelThree['value'] <= 20 and self.count20 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 20 and self.myLevelThree['value'] <= 40 and self.count40 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 40 and self.myLevelThree['value'] <= 60 and self.count60 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 60 and self.myLevelThree['value'] <= 80 and self.count80 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 80 and self.myLevelThree['value'] <= 100 and self.count100 == True:
                self.animate3(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student3PointTen(self):
        self.myLevelThree['value'] += 10

        self.countThree = int(self.countThree)
        self.countThree += 10
        self.lbl3Level.config(text=self.countThree)

        if self.myLevelThree['value'] >= 100:
            self.lblart3.configure(state=NORMAL)

        try:
            if self.myLevelThree['value'] >= 0 and self.myLevelThree['value'] <= 20 and self.count20 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 20 and self.myLevelThree['value'] <= 40 and self.count40 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 40 and self.myLevelThree['value'] <= 60 and self.count60 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 60 and self.myLevelThree['value'] <= 80 and self.count80 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 80 and self.myLevelThree['value'] <= 100 and self.count100 == True:
                self.animate3(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student3PointTwe(self):
        self.myLevelThree['value'] += 20

        self.countThree = int(self.countThree)
        self.countThree += 20
        self.lbl3Level.config(text=self.countThree)

        if self.myLevelThree['value'] >= 100:
            self.lblart3.configure(state=NORMAL)

        try:
            if self.myLevelThree['value'] >= 0 and self.myLevelThree['value'] <= 20 and self.count20 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 20 and self.myLevelThree['value'] <= 40 and self.count40 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 40 and self.myLevelThree['value'] <= 60 and self.count60 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 60 and self.myLevelThree['value'] <= 80 and self.count80 == True:
                self.animate3(0)
            elif self.myLevelThree['value'] > 80 and self.myLevelThree['value'] <= 100 and self.count100 == True:
                self.animate3(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student4PointOne(self):
        self.myLevelFour['value'] += 1

        self.countFour = int(self.countFour)
        self.countFour += 20
        self.lbl4Level.config(text=self.countFour)

        if self.myLevelFour['value'] >= 100:
            self.lblart4.configure(state=NORMAL)

        try:
            if self.myLevelFour['value'] >= 0 and self.myLevelFour['value'] <= 20 and self.count20 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 20 and self.myLevelFour['value'] <= 40 and self.count40 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 40 and self.myLevelFour['value'] <= 60 and self.count60 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 60 and self.myLevelFour['value'] <= 80 and self.count80 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 80 and self.myLevelFour['value'] <= 100 and self.count100 == True:
                self.animate4(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student4PointFive(self):
        self.myLevelFour['value'] += 5

        self.countFour = int(self.countFour)
        self.countFour += 5
        self.lbl4Level.config(text=self.countFour)

        if self.myLevelFour['value'] >= 100:
            self.lblart4.configure(state=NORMAL)

        try:
            if self.myLevelFour['value'] >= 0 and self.myLevelFour['value'] <= 20 and self.count20 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 20 and self.myLevelFour['value'] <= 40 and self.count40 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 40 and self.myLevelFour['value'] <= 60 and self.count60 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 60 and self.myLevelFour['value'] <= 80 and self.count80 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 80 and self.myLevelFour['value'] <= 100 and self.count100 == True:
                self.animate4(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student4PointTen(self):
        self.myLevelFour['value'] += 10

        self.countFour = int(self.countFour)
        self.countFour += 10
        self.lbl4Level.config(text=self.countFour)

        if self.myLevelFour['value'] >= 100:
            self.lblart4.configure(state=NORMAL)
        try:
            if self.myLevelFour['value'] >= 0 and self.myLevelFour['value'] <= 20 and self.count20 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 20 and self.myLevelFour['value'] <= 40 and self.count40 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 40 and self.myLevelFour['value'] <= 60 and self.count60 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 60 and self.myLevelFour['value'] <= 80 and self.count80 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 80 and self.myLevelFour['value'] <= 100 and self.count100 == True:
                self.animate4(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student4PointTwe(self):
        self.myLevelFour['value'] += 20

        self.countFour = int(self.countFour)
        self.countFour += 20
        self.lbl4Level.config(text=self.countFour)

        if self.myLevelFour['value'] >= 100:
            self.lblart4.configure(state=NORMAL)
        try:
            if self.myLevelFour['value'] >= 0 and self.myLevelFour['value'] <= 20 and self.count20 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 20 and self.myLevelFour['value'] <= 40 and self.count40 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 40 and self.myLevelFour['value'] <= 60 and self.count60 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 60 and self.myLevelFour['value'] <= 80 and self.count80 == True:
                self.animate4(0)
            elif self.myLevelFour['value'] > 80 and self.myLevelFour['value'] <= 100 and self.count100 == True:
                self.animate4(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student5PointOne(self):
        self.myLevelFive['value'] += 1

        self.countFive = int(self.countFive)
        self.countFive += 1
        self.lbl5Level.config(text=self.countFive)

        if self.myLevelFive['value'] >= 100:
            self.lblart5.configure(state=NORMAL)

        try:
            if self.myLevelFive['value'] >= 0 and self.myLevelFive['value'] <= 20 and self.count20 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 20 and self.myLevelFive['value'] <= 40 and self.count40 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 40 and self.myLevelFive['value'] <= 60 and self.count60 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 60 and self.myLevelFive['value'] <= 80 and self.count80 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 80 and self.myLevelFive['value'] <= 100 and self.count100 == True:
                self.animate5(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student5PointFive(self):
        self.myLevelFive['value'] += 5

        self.countFive = int(self.countFive)
        self.countFive += 5
        self.lbl5Level.config(text=self.countFive)

        if self.myLevelFive['value'] >= 100:
            self.lblart5.configure(state=NORMAL)

        try:
            if self.myLevelFive['value'] >= 0 and self.myLevelFive['value'] <= 20 and self.count20 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 20 and self.myLevelFive['value'] <= 40 and self.count40 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 40 and self.myLevelFive['value'] <= 60 and self.count60 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 60 and self.myLevelFive['value'] <= 80 and self.count80 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 80 and self.myLevelFive['value'] <= 100 and self.count100 == True:
                self.animate5(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student5PointTen(self):
        self.myLevelFive['value'] += 10

        self.countFive = int(self.countFive)
        self.countFive += 10
        self.lbl5Level.config(text=self.countFive)

        if self.myLevelFive['value'] >= 100:
            self.lblart5.configure(state=NORMAL)

        try:
            if self.myLevelFive['value'] >= 0 and self.myLevelFive['value'] <= 20 and self.count20 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 20 and self.myLevelFive['value'] <= 40 and self.count40 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 40 and self.myLevelFive['value'] <= 60 and self.count60 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 60 and self.myLevelFive['value'] <= 80 and self.count80 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 80 and self.myLevelFive['value'] <= 100 and self.count100 == True:
                self.animate5(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student5PointTwe(self):
        self.myLevelFive['value'] += 20

        self.countFive = int(self.countFive)
        self.countFive += 20
        self.lbl5Level.config(text=self.countFive)

        if self.myLevelFive['value'] >= 100:
            self.lblart5.configure(state=NORMAL)

        try:
            if self.myLevelFive['value'] >= 0 and self.myLevelFive['value'] <= 20 and self.count20 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 20 and self.myLevelFive['value'] <= 40 and self.count40 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 40 and self.myLevelFive['value'] <= 60 and self.count60 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 60 and self.myLevelFive['value'] <= 80 and self.count80 == True:
                self.animate5(0)
            elif self.myLevelFive['value'] > 80 and self.myLevelFive['value'] <= 100 and self.count100 == True:
                self.animate5(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student6PointOne(self):
        self.myLevelSix['value'] += 1

        self.countSix = int(self.countSix)
        self.countSix += 1
        self.lbl6Level.config(text=self.countSix)

        if self.myLevelSix['value'] >= 100:
            self.lblart6.configure(state=NORMAL)

        try:
            if self.myLevelSix['value'] >= 0 and self.myLevelSix['value'] <= 20 and self.count20 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 20 and self.myLevelSix['value'] <= 40 and self.count40 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 40 and self.myLevelSix['value'] <= 60 and self.count60 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 60 and self.myLevelSix['value'] <= 80 and self.count80 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 80 and self.myLevelSix['value'] <= 100 and self.count100 == True:
                self.animate6(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student6PointFive(self):
        self.myLevelSix['value'] += 5

        self.countSix = int(self.countSix)
        self.countSix += 5
        self.lbl6Level.config(text=self.countSix)

        if self.myLevelSix['value'] >= 100:
            self.lblart6.configure(state=NORMAL)

        try:
            if self.myLevelSix['value'] >= 0 and self.myLevelSix['value'] <= 20 and self.count20 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 20 and self.myLevelSix['value'] <= 40 and self.count40 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 40 and self.myLevelSix['value'] <= 60 and self.count60 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 60 and self.myLevelSix['value'] <= 80 and self.count80 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 80 and self.myLevelSix['value'] <= 100 and self.count100 == True:
                self.animate6(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student6PointTen(self):
        self.myLevelSix['value'] += 10

        self.countSix = int(self.countSix)
        self.countSix += 10
        self.lbl6Level.config(text=self.countSix)

        if self.myLevelSix['value'] >= 100:
            self.lblart6.configure(state=NORMAL)
        try:
            if self.myLevelSix['value'] >= 0 and self.myLevelSix['value'] <= 20 and self.count20 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 20 and self.myLevelSix['value'] <= 40 and self.count40 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 40 and self.myLevelSix['value'] <= 60 and self.count60 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 60 and self.myLevelSix['value'] <= 80 and self.count80 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 80 and self.myLevelSix['value'] <= 100 and self.count100 == True:
                self.animate6(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student6PointTwe(self):
        self.myLevelSix['value'] += 20

        self.countSix = int(self.countSix)
        self.countSix += 20
        self.lbl6Level.config(text=self.countSix)

        if self.myLevelSix['value'] >= 100:
            self.lblart6.configure(state=NORMAL)
        try:
            if self.myLevelSix['value'] >= 0 and self.myLevelSix['value'] <= 20 and self.count20 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 20 and self.myLevelSix['value'] <= 40 and self.count40 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 40 and self.myLevelSix['value'] <= 60 and self.count60 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 60 and self.myLevelSix['value'] <= 80 and self.count80 == True:
                self.animate6(0)
            elif self.myLevelSix['value'] > 80 and self.myLevelSix['value'] <= 100 and self.count100 == True:
                self.animate6(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student7PointOne(self):
        self.myLevelSeven['value'] += 1

        self.countSeven = int(self.countSeven)
        self.countSeven += 1
        self.lbl7Level.config(text=self.countSeven)

        if self.myLevelSeven['value'] >= 100:
            self.lblart7.configure(state=NORMAL)

        try:
            if self.myLevelSeven['value'] >= 0 and self.myLevelSeven['value'] <= 20 and self.count20 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 20 and self.myLevelSeven['value'] <= 40 and self.count40 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 40 and self.myLevelSeven['value'] <= 60 and self.count60 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 60 and self.myLevelSeven['value'] <= 80 and self.count80 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 80 and self.myLevelSeven['value'] <= 100 and self.count100 == True:
                self.animate7(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student7PointFive(self):
        self.myLevelSeven['value'] += 5

        self.countSeven = int(self.countSeven)
        self.countSeven += 5
        self.lbl7Level.config(text=self.countSeven)

        if self.myLevelSeven['value'] >= 100:
            self.lblart7.configure(state=NORMAL)

        try:
            if self.myLevelSeven['value'] >= 0 and self.myLevelSeven['value'] <= 20 and self.count20 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 20 and self.myLevelSeven['value'] <= 40 and self.count40 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 40 and self.myLevelSeven['value'] <= 60 and self.count60 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 60 and self.myLevelSeven['value'] <= 80 and self.count80 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 80 and self.myLevelSeven['value'] <= 100 and self.count100 == True:
                self.animate7(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student7PointTen(self):
        self.myLevelSeven['value'] += 10

        self.countSeven = int(self.countSeven)
        self.countSeven += 10
        self.lbl7Level.config(text=self.countSeven)

        if self.myLevelSeven['value'] >= 100:
            self.lblart7.configure(state=NORMAL)

        try:
            if self.myLevelSeven['value'] >= 0 and self.myLevelSeven['value'] <= 20 and self.count20 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 20 and self.myLevelSeven['value'] <= 40 and self.count40 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 40 and self.myLevelSeven['value'] <= 60 and self.count60 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 60 and self.myLevelSeven['value'] <= 80 and self.count80 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 80 and self.myLevelSeven['value'] <= 100 and self.count100 == True:
                self.animate7(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student7PointTwe(self):
        self.myLevelSeven['value'] += 20

        self.countSeven = int(self.countSeven)
        self.countSeven += 20
        self.lbl7Level.config(text=self.countSeven)

        if self.myLevelSeven['value'] >= 100:
            self.lblart7.configure(state=NORMAL)

        try:
            if self.myLevelSeven['value'] >= 0 and self.myLevelSeven['value'] <= 20 and self.count20 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 20 and self.myLevelSeven['value'] <= 40 and self.count40 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 40 and self.myLevelSeven['value'] <= 60 and self.count60 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 60 and self.myLevelSeven['value'] <= 80 and self.count80 == True:
                self.animate7(0)
            elif self.myLevelSeven['value'] > 80 and self.myLevelSeven['value'] <= 100 and self.count100 == True:
                self.animate7(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student8PointOne(self):
        self.myLevelEight['value'] += 1

        self.countEight = int(self.countEight)
        self.countEight += 1
        self.lbl8Level.config(text=self.countEight)

        if self.myLevelEight['value'] >= 100:
            self.lblart8.configure(state=NORMAL)

        try:
            if self.myLevelEight['value'] >= 0 and self.myLevelEight['value'] <= 20 and self.count20 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 20 and self.myLevelEight['value'] <= 40 and self.count40 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 40 and self.myLevelEight['value'] <= 60 and self.count60 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 60 and self.myLevelEight['value'] <= 80 and self.count80 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 80 and self.myLevelEight['value'] <= 100 and self.count100 == True:
                self.animate8(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student8PointFive(self):
        self.myLevelEight['value'] += 5

        self.countEight = int(self.countEight)
        self.countEight += 5
        self.lbl8Level.config(text=self.countEight)

        if self.myLevelEight['value'] >= 100:
            self.lblart8.configure(state=NORMAL)

        try:
            if self.myLevelEight['value'] >= 0 and self.myLevelEight['value'] <= 20 and self.count20 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 20 and self.myLevelEight['value'] <= 40 and self.count40 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 40 and self.myLevelEight['value'] <= 60 and self.count60 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 60 and self.myLevelEight['value'] <= 80 and self.count80 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 80 and self.myLevelEight['value'] <= 100 and self.count100 == True:
                self.animate8(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student8PointTen(self):
        self.myLevelEight['value'] += 10

        self.countEight = int(self.countEight)
        self.countEight += 10
        self.lbl8Level.config(text=self.countEight)

        if self.myLevelEight['value'] >= 100:
            self.lblart8.configure(state=NORMAL)

        try:
            if self.myLevelEight['value'] >= 0 and self.myLevelEight['value'] <= 20 and self.count20 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 20 and self.myLevelEight['value'] <= 40 and self.count40 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 40 and self.myLevelEight['value'] <= 60 and self.count60 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 60 and self.myLevelEight['value'] <= 80 and self.count80 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 80 and self.myLevelEight['value'] <= 100 and self.count100 == True:
                self.animate8(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student8PointTwe(self):
        self.myLevelEight['value'] += 20

        self.countEight = int(self.countEight)
        self.countEight += 20
        self.lbl8Level.config(text=self.countEight)

        if self.myLevelEight['value'] >= 100:
            self.lblart8.configure(state=NORMAL)

        try:
            if self.myLevelEight['value'] >= 0 and self.myLevelEight['value'] <= 20 and self.count20 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 20 and self.myLevelEight['value'] <= 40 and self.count40 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 40 and self.myLevelEight['value'] <= 60 and self.count60 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 60 and self.myLevelEight['value'] <= 80 and self.count80 == True:
                self.animate8(0)
            elif self.myLevelEight['value'] > 80 and self.myLevelEight['value'] <= 100 and self.count100 == True:
                self.animate8(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student9PointOne(self):
        self.myLevelNine['value'] += 1

        self.countNine = int(self.countNine)
        self.countNine += 1
        self.lbl9Level.config(text=self.countNine)

        if self.myLevelNine['value'] >= 100:
            self.lblart9.configure(state=NORMAL)

        try:
            if self.myLevelNine['value'] >= 0 and self.myLevelNine['value'] <= 20 and self.count20 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 20 and self.myLevelNine['value'] <= 40 and self.count40 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 40 and self.myLevelNine['value'] <= 60 and self.count60 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 60 and self.myLevelNine['value'] <= 80 and self.count80 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 80 and self.myLevelNine['value'] <= 100 and self.count100 == True:
                self.animate9(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student9PointFive(self):
        self.myLevelNine['value'] += 5

        self.countNine = int(self.countNine)
        self.countNine += 5
        self.lbl9Level.config(text=self.countNine)

        if self.myLevelNine['value'] >= 100:
            self.lblart9.configure(state=NORMAL)

        try:
            if self.myLevelNine['value'] >= 0 and self.myLevelNine['value'] <= 20 and self.count20 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 20 and self.myLevelNine['value'] <= 40 and self.count40 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 40 and self.myLevelNine['value'] <= 60 and self.count60 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 60 and self.myLevelNine['value'] <= 80 and self.count80 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 80 and self.myLevelNine['value'] <= 100 and self.count100 == True:
                self.animate9(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student9PointTen(self):
        self.myLevelNine['value'] += 10

        self.countNine = int(self.countNine)
        self.countNine += 10
        self.lbl9Level.config(text=self.countNine)

        if self.myLevelNine['value'] >= 100:
            self.lblart9.configure(state=NORMAL)

        try:
            if self.myLevelNine['value'] >= 0 and self.myLevelNine['value'] <= 20 and self.count20 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 20 and self.myLevelNine['value'] <= 40 and self.count40 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 40 and self.myLevelNine['value'] <= 60 and self.count60 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 60 and self.myLevelNine['value'] <= 80 and self.count80 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 80 and self.myLevelNine['value'] <= 100 and self.count100 == True:
                self.animate9(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student9PointTwe(self):
        self.myLevelNine['value'] += 20

        self.countNine = int(self.countNine)
        self.countNine += 20
        self.lbl9Level.config(text=self.countNine)

        if self.myLevelNine['value'] >= 100:
            self.lblart9.configure(state=NORMAL)

        try:
            if self.myLevelNine['value'] >= 0 and self.myLevelNine['value'] <= 20 and self.count20 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 20 and self.myLevelNine['value'] <= 40 and self.count40 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 40 and self.myLevelNine['value'] <= 60 and self.count60 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 60 and self.myLevelNine['value'] <= 80 and self.count80 == True:
                self.animate9(0)
            elif self.myLevelNine['value'] > 80 and self.myLevelNine['value'] <= 100 and self.count100 == True:
                self.animate9(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student10PointOne(self):
        self.myLevelTen['value'] += 1

        self.countTen = int(self.countTen)
        self.countTen += 1
        self.lbl10Level.config(text=self.countTen)

        if self.myLevelTen['value'] >= 100:
            self.lblart10.configure(state=NORMAL)

        try:
            if self.myLevelTen['value'] >= 0 and self.myLevelTen['value'] <= 20 and self.count20 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 20 and self.myLevelTen['value'] <= 40 and self.count40 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 40 and self.myLevelTen['value'] <= 60 and self.count60 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 60 and self.myLevelTen['value'] <= 80 and self.count80 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 80 and self.myLevelTen['value'] <= 100 and self.count100 == True:
                self.animate10(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student10PointFive(self):
        self.myLevelTen['value'] += 5

        self.countTen = int(self.countTen)
        self.countTen += 5
        self.lbl10Level.config(text=self.countTen)

        if self.myLevelTen['value'] >= 100:
            self.lblart10.configure(state=NORMAL)

        try:
            if self.myLevelTen['value'] >= 0 and self.myLevelTen['value'] <= 20 and self.count20 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 20 and self.myLevelTen['value'] <= 40 and self.count40 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 40 and self.myLevelTen['value'] <= 60 and self.count60 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 60 and self.myLevelTen['value'] <= 80 and self.count80 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 80 and self.myLevelTen['value'] <= 100 and self.count100 == True:
                self.animate10(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student10PointTen(self):
        self.myLevelTen['value'] += 10

        self.countTen = int(self.countTen)
        self.countTen += 10
        self.lbl10Level.config(text=self.countTen)

        if self.myLevelTen['value'] >= 100:
            self.lblart10.configure(state=NORMAL)

        try:
            if self.myLevelTen['value'] >= 0 and self.myLevelTen['value'] <= 20 and self.count20 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 20 and self.myLevelTen['value'] <= 40 and self.count40 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 40 and self.myLevelTen['value'] <= 60 and self.count60 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 60 and self.myLevelTen['value'] <= 80 and self.count80 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 80 and self.myLevelTen['value'] <= 100 and self.count100 == True:
                self.animate10(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student10PointTwe(self):
        self.myLevelTen['value'] += 20

        self.countTen = int(self.countTen)
        self.countTen += 20
        self.lbl10Level.config(text=self.countTen)

        if self.myLevelTen['value'] >= 100:
            self.lblart10.configure(state=NORMAL)

        try:
            if self.myLevelTen['value'] >= 0 and self.myLevelTen['value'] <= 20 and self.count20 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 20 and self.myLevelTen['value'] <= 40 and self.count40 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 40 and self.myLevelTen['value'] <= 60 and self.count60 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 60 and self.myLevelTen['value'] <= 80 and self.count80 == True:
                self.animate10(0)
            elif self.myLevelTen['value'] > 80 and self.myLevelTen['value'] <= 100 and self.count100 == True:
                self.animate10(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student11PointOne(self):
        self.myLevelEleven['value'] += 1

        self.countEleven = int(self.countEleven)
        self.countEleven += 1
        self.lbl11Level.config(text=self.countEleven)

        if self.myLevelEleven['value'] >= 100:
            self.lblart11.configure(state=NORMAL)

        try:
            if self.myLevelEleven['value'] >= 0 and self.myLevelEleven['value'] <= 20 and self.count20 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 20 and self.myLevelEleven['value'] <= 40 and self.count40 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 40 and self.myLevelEleven['value'] <= 60 and self.count60 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 60 and self.myLevelEleven['value'] <= 80 and self.count80 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 80 and self.myLevelEleven['value'] <= 100 and self.count100 == True:
                self.animate11(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student11PointFive(self):
        self.myLevelEleven['value'] += 5

        self.countEleven = int(self.countEleven)
        self.countEleven += 5
        self.lbl11Level.config(text=self.countEleven)

        if self.myLevelEleven['value'] >= 100:
            self.lblart11.configure(state=NORMAL)

        try:
            if self.myLevelEleven['value'] >= 0 and self.myLevelEleven['value'] <= 20 and self.count20 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 20 and self.myLevelEleven['value'] <= 40 and self.count40 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 40 and self.myLevelEleven['value'] <= 60 and self.count60 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 60 and self.myLevelEleven['value'] <= 80 and self.count80 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 80 and self.myLevelEleven['value'] <= 100 and self.count100 == True:
                self.animate11(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student11PointTen(self):
        self.myLevelEleven['value'] += 10

        self.countEleven = int(self.countEleven)
        self.countEleven += 10
        self.lbl11Level.config(text=self.countEleven)

        if self.myLevelEleven['value'] >= 100:
            self.lblart11.configure(state=NORMAL)

        try:
            if self.myLevelEleven['value'] >= 0 and self.myLevelEleven['value'] <= 20 and self.count20 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 20 and self.myLevelEleven['value'] <= 40 and self.count40 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 40 and self.myLevelEleven['value'] <= 60 and self.count60 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 60 and self.myLevelEleven['value'] <= 80 and self.count80 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 80 and self.myLevelEleven['value'] <= 100 and self.count100 == True:
                self.animate11(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student11PointTwe(self):
        self.myLevelEleven['value'] += 20

        self.countEleven = int(self.countEleven)
        self.countEleven += 20
        self.lbl11Level.config(text=self.countEleven)

        if self.myLevelEleven['value'] >= 100:
            self.lblart11.configure(state=NORMAL)

        try:
            if self.myLevelEleven['value'] >= 0 and self.myLevelEleven['value'] <= 20 and self.count20 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 20 and self.myLevelEleven['value'] <= 40 and self.count40 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 40 and self.myLevelEleven['value'] <= 60 and self.count60 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 60 and self.myLevelEleven['value'] <= 80 and self.count80 == True:
                self.animate11(0)
            elif self.myLevelEleven['value'] > 80 and self.myLevelEleven['value'] <= 100 and self.count100 == True:
                self.animate11(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student12PointOne(self):
        self.myLevelTwelve['value'] += 1

        self.countTwelve = int(self.countTwelve)
        self.countTwelve += 1
        self.lbl12Level.config(text=self.countTwelve)

        if self.myLevelTwelve['value'] >= 100:
            self.lblart12.configure(state=NORMAL)

        try:
            if self.myLevelTwelve['value'] >= 0 and self.myLevelTwelve['value'] <= 20 and self.count20 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 20 and self.myLevelTwelve['value'] <= 40 and self.count40 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 40 and self.myLevelTwelve['value'] <= 60 and self.count60 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 60 and self.myLevelTwelve['value'] <= 80 and self.count80 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 80 and self.myLevelTwelve['value'] <= 100 and self.count100 == True:
                self.animate12(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student12PointFive(self):
        self.myLevelTwelve['value'] += 5

        self.countTwelve = int(self.countTwelve)
        self.countTwelve += 5
        self.lbl12Level.config(text=self.countTwelve)

        if self.myLevelTwelve['value'] >= 100:
            self.lblart12.configure(state=NORMAL)

        try:
            if self.myLevelTwelve['value'] >= 0 and self.myLevelTwelve['value'] <= 20 and self.count20 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 20 and self.myLevelTwelve['value'] <= 40 and self.count40 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 40 and self.myLevelTwelve['value'] <= 60 and self.count60 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 60 and self.myLevelTwelve['value'] <= 80 and self.count80 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 80 and self.myLevelTwelve['value'] <= 100 and self.count100 == True:
                self.animate12(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student12PointTen(self):
        self.myLevelTwelve['value'] += 10

        self.countTwelve = int(self.countTwelve)
        self.countTwelve += 10
        self.lbl12Level.config(text=self.countTwelve)

        if self.myLevelTwelve['value'] >= 100:
            self.lblart12.configure(state=NORMAL)

        try:
            if self.myLevelTwelve['value'] >= 0 and self.myLevelTwelve['value'] <= 20 and self.count20 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 20 and self.myLevelTwelve['value'] <= 40 and self.count40 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 40 and self.myLevelTwelve['value'] <= 60 and self.count60 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 60 and self.myLevelTwelve['value'] <= 80 and self.count80 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 80 and self.myLevelTwelve['value'] <= 100 and self.count100 == True:
                self.animate12(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student12PointTwe(self):
        self.myLevelTwelve['value'] += 20

        self.countTwelve = int(self.countTwelve)
        self.countTwelve += 20
        self.lbl12Level.config(text=self.countTwelve)

        if self.myLevelTwelve['value'] >= 100:
            self.lblart12.configure(state=NORMAL)

        try:
            if self.myLevelTwelve['value'] >= 0 and self.myLevelTwelve['value'] <= 20 and self.count20 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 20 and self.myLevelTwelve['value'] <= 40 and self.count40 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 40 and self.myLevelTwelve['value'] <= 60 and self.count60 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 60 and self.myLevelTwelve['value'] <= 80 and self.count80 == True:
                self.animate12(0)
            elif self.myLevelTwelve['value'] > 80 and self.myLevelTwelve['value'] <= 100 and self.count100 == True:
                self.animate12(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student13PointOne(self):
        self.myLevelThirteen['value'] += 1

        self.countThirteen = int(self.countThirteen)
        self.countThirteen += 1
        self.lbl13Level.config(text=self.countThirteen)

        if self.myLevelThirteen['value'] >= 100:
            self.lblart13.configure(state=NORMAL)

        try:
            if self.myLevelThirteen['value'] >= 0 and self.myLevelThirteen['value'] <= 20 and self.count20 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 20 and self.myLevelThirteen['value'] <= 40 and self.count40 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 40 and self.myLevelThirteen['value'] <= 60 and self.count60 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 60 and self.myLevelThirteen['value'] <= 80 and self.count80 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 80 and self.myLevelThirteen['value'] <= 100 and self.count100 == True:
                self.animate13(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student13PointFive(self):
        self.myLevelThirteen['value'] += 5

        self.countThirteen = int(self.countThirteen)
        self.countThirteen += 5
        self.lbl13Level.config(text=self.countThirteen)

        if self.myLevelThirteen['value'] >= 100:
            self.lblart13.configure(state=NORMAL)

        try:
            if self.myLevelThirteen['value'] >= 0 and self.myLevelThirteen['value'] <= 20 and self.count20 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 20 and self.myLevelThirteen['value'] <= 40 and self.count40 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 40 and self.myLevelThirteen['value'] <= 60 and self.count60 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 60 and self.myLevelThirteen['value'] <= 80 and self.count80 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 80 and self.myLevelThirteen['value'] <= 100 and self.count100 == True:
                self.animate13(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student13PointTen(self):
        self.myLevelThirteen['value'] += 10

        self.countThirteen = int(self.countThirteen)
        self.countThirteen += 10
        self.lbl13Level.config(text=self.countThirteen)

        if self.myLevelThirteen['value'] >= 100:
            self.lblart13.configure(state=NORMAL)

        try:
            if self.myLevelThirteen['value'] >= 0 and self.myLevelThirteen['value'] <= 20 and self.count20 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 20 and self.myLevelThirteen['value'] <= 40 and self.count40 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 40 and self.myLevelThirteen['value'] <= 60 and self.count60 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 60 and self.myLevelThirteen['value'] <= 80 and self.count80 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 80 and self.myLevelThirteen['value'] <= 100 and self.count100 == True:
                self.animate13(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student13PointTwe(self):
        self.myLevelThirteen['value'] += 20

        self.countThirteen = int(self.countThirteen)
        self.countThirteen += 20
        self.lbl13Level.config(text=self.countThirteen)

        if self.myLevelThirteen['value'] >= 100:
            self.lblart13.configure(state=NORMAL)

        try:
            if self.myLevelThirteen['value'] >= 0 and self.myLevelThirteen['value'] <= 20 and self.count20 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 20 and self.myLevelThirteen['value'] <= 40 and self.count40 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 40 and self.myLevelThirteen['value'] <= 60 and self.count60 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 60 and self.myLevelThirteen['value'] <= 80 and self.count80 == True:
                self.animate13(0)
            elif self.myLevelThirteen['value'] > 80 and self.myLevelThirteen['value'] <= 100 and self.count100 == True:
                self.animate13(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student14PointOne(self):
        self.myLevelFourteen['value'] += 1

        self.countFourteen = int(self.countFourteen)
        self.countFourteen += 1
        self.lbl14Level.config(text=self.countFourteen)

        if self.myLevelFourteen['value'] >= 100:
            self.lblart14.configure(state=NORMAL)

        try:
            if self.myLevelFourteen['value'] >= 0 and self.myLevelFourteen['value'] <= 20 and self.count20 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 20 and self.myLevelFourteen['value'] <= 40 and self.count40 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 40 and self.myLevelFourteen['value'] <= 60 and self.count60 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 60 and self.myLevelFourteen['value'] <= 80 and self.count80 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 80 and self.myLevelFourteen['value'] <= 100 and self.count100 == True:
                self.animate14(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student14PointFive(self):
        self.myLevelFourteen['value'] += 5

        self.countFourteen = int(self.countFourteen)
        self.countFourteen += 5
        self.lbl14Level.config(text=self.countFourteen)

        if self.myLevelFourteen['value'] >= 100:
            self.lblart14.configure(state=NORMAL)

        try:
            if self.myLevelFourteen['value'] >= 0 and self.myLevelFourteen['value'] <= 20 and self.count20 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 20 and self.myLevelFourteen['value'] <= 40 and self.count40 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 40 and self.myLevelFourteen['value'] <= 60 and self.count60 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 60 and self.myLevelFourteen['value'] <= 80 and self.count80 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 80 and self.myLevelFourteen['value'] <= 100 and self.count100 == True:
                self.animate14(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student14PointTen(self):
        self.myLevelFourteen['value'] += 10

        self.countFourteen = int(self.countFourteen)
        self.countFourteen += 10
        self.lbl14Level.config(text=self.countFourteen)

        if self.myLevelFourteen['value'] >= 100:
            self.lblart14.configure(state=NORMAL)

        try:
            if self.myLevelFourteen['value'] >= 0 and self.myLevelFourteen['value'] <= 20 and self.count20 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 20 and self.myLevelFourteen['value'] <= 40 and self.count40 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 40 and self.myLevelFourteen['value'] <= 60 and self.count60 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 60 and self.myLevelFourteen['value'] <= 80 and self.count80 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 80 and self.myLevelFourteen['value'] <= 100 and self.count100 == True:
                self.animate14(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student14PointTwe(self):
        self.myLevelFourteen['value'] += 20

        self.countFourteen = int(self.countFourteen)
        self.countFourteen += 20
        self.lbl14Level.config(text=self.countFourteen)

        if self.myLevelFourteen['value'] >= 100:
            self.lblart14.configure(state=NORMAL)

        try:
            if self.myLevelFourteen['value'] >= 0 and self.myLevelFourteen['value'] <= 20 and self.count20 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 20 and self.myLevelFourteen['value'] <= 40 and self.count40 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 40 and self.myLevelFourteen['value'] <= 60 and self.count60 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 60 and self.myLevelFourteen['value'] <= 80 and self.count80 == True:
                self.animate14(0)
            elif self.myLevelFourteen['value'] > 80 and self.myLevelFourteen['value'] <= 100 and self.count100 == True:
                self.animate14(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student15PointOne(self):
        self.myLevelFifteen['value'] += 1

        self.countFifteen = int(self.countFifteen)
        self.countFifteen += 1
        self.lbl15Level.config(text=self.countFifteen)

        if self.myLevelFifteen['value'] >= 100:
            self.lblart15.configure(state=NORMAL)

        try:
            if self.myLevelFifteen['value'] >= 0 and self.myLevelFifteen['value'] <= 20 and self.count20 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 20 and self.myLevelFifteen['value'] <= 40 and self.count40 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 40 and self.myLevelFifteen['value'] <= 60 and self.count60 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 60 and self.myLevelFifteen['value'] <= 80 and self.count80 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 80 and self.myLevelFifteen['value'] <= 100 and self.count100 == True:
                self.animate15(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student15PointFive(self):
        self.myLevelFifteen['value'] += 5

        self.countFifteen = int(self.countFifteen)
        self.countFifteen += 5
        self.lbl15Level.config(text=self.countFifteen)

        if self.myLevelFifteen['value'] >= 100:
            self.lblart15.configure(state=NORMAL)

        try:
            if self.myLevelFifteen['value'] >= 0 and self.myLevelFifteen['value'] <= 20 and self.count20 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 20 and self.myLevelFifteen['value'] <= 40 and self.count40 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 40 and self.myLevelFifteen['value'] <= 60 and self.count60 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 60 and self.myLevelFifteen['value'] <= 80 and self.count80 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 80 and self.myLevelFifteen['value'] <= 100 and self.count100 == True:
                self.animate15(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student15PointTen(self):
        self.myLevelFifteen['value'] += 10

        self.countFifteen = int(self.countFifteen)
        self.countFifteen += 10
        self.lbl15Level.config(text=self.countFifteen)

        if self.myLevelFifteen['value'] >= 100:
            self.lblart15.configure(state=NORMAL)

        try:
            if self.myLevelFifteen['value'] >= 0 and self.myLevelFifteen['value'] <= 20 and self.count20 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 20 and self.myLevelFifteen['value'] <= 40 and self.count40 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 40 and self.myLevelFifteen['value'] <= 60 and self.count60 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 60 and self.myLevelFifteen['value'] <= 80 and self.count80 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 80 and self.myLevelFifteen['value'] <= 100 and self.count100 == True:
                self.animate15(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student15PointTwe(self):
        self.myLevelFifteen['value'] += 20

        self.countFifteen = int(self.countFifteen)
        self.countFifteen += 20
        self.lbl15Level.config(text=self.countFifteen)

        if self.myLevelFifteen['value'] >= 100:
            self.lblart15.configure(state=NORMAL)

        try:
            if self.myLevelFifteen['value'] >= 0 and self.myLevelFifteen['value'] <= 20 and self.count20 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 20 and self.myLevelFifteen['value'] <= 40 and self.count40 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 40 and self.myLevelFifteen['value'] <= 60 and self.count60 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 60 and self.myLevelFifteen['value'] <= 80 and self.count80 == True:
                self.animate15(0)
            elif self.myLevelFifteen['value'] > 80 and self.myLevelFifteen['value'] <= 100 and self.count100 == True:
                self.animate15(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student16PointOne(self):
        self.myLevelSixteen['value'] += 1

        self.countSixteen = int(self.countSixteen)
        self.countSixteen += 1
        self.lbl16Level.config(text=self.countSixteen)

        if self.myLevelSixteen['value'] >= 100:
            self.lblart16.configure(state=NORMAL)

        try:
            if self.myLevelSixteen['value'] >= 0 and self.myLevelSixteen['value'] <= 20 and self.count20 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 20 and self.myLevelSixteen['value'] <= 40 and self.count40 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 40 and self.myLevelSixteen['value'] <= 60 and self.count60 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 60 and self.myLevelSixteen['value'] <= 80 and self.count80 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 80 and self.myLevelSixteen['value'] <= 100 and self.count100 == True:
                self.animate16(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student16PointFive(self):
        self.myLevelSixteen['value'] += 5

        self.countSixteen = int(self.countSixteen)
        self.countSixteen += 5
        self.lbl16Level.config(text=self.countSixteen)

        if self.myLevelSixteen['value'] >= 100:
            self.lblart16.configure(state=NORMAL)

        try:
            if self.myLevelSixteen['value'] >= 0 and self.myLevelSixteen['value'] <= 20 and self.count20 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 20 and self.myLevelSixteen['value'] <= 40 and self.count40 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 40 and self.myLevelSixteen['value'] <= 60 and self.count60 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 60 and self.myLevelSixteen['value'] <= 80 and self.count80 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 80 and self.myLevelSixteen['value'] <= 100 and self.count100 == True:
                self.animate16(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student16PointTen(self):
        self.myLevelSixteen['value'] += 10

        self.countSixteen = int(self.countSixteen)
        self.countSixteen += 10
        self.lbl16Level.config(text=self.countSixteen)

        if self.myLevelSixteen['value'] >= 100:
            self.lblart16.configure(state=NORMAL)

        try:
            if self.myLevelSixteen['value'] >= 0 and self.myLevelSixteen['value'] <= 20 and self.count20 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 20 and self.myLevelSixteen['value'] <= 40 and self.count40 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 40 and self.myLevelSixteen['value'] <= 60 and self.count60 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 60 and self.myLevelSixteen['value'] <= 80 and self.count80 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 80 and self.myLevelSixteen['value'] <= 100 and self.count100 == True:
                self.animate16(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass

    def Student16PointTwe(self):
        self.myLevelSixteen['value'] += 20

        self.countSixteen = int(self.countSixteen)
        self.countSixteen += 20
        self.lbl16Level.config(text=self.countSixteen)

        if self.myLevelSixteen['value'] >= 100:
            self.lblart16.configure(state=NORMAL)

        try:
            if self.myLevelSixteen['value'] >= 0 and self.myLevelSixteen['value'] <= 20 and self.count20 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 20 and self.myLevelSixteen['value'] <= 40 and self.count40 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 40 and self.myLevelSixteen['value'] <= 60 and self.count60 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 60 and self.myLevelSixteen['value'] <= 80 and self.count80 == True:
                self.animate16(0)
            elif self.myLevelSixteen['value'] > 80 and self.myLevelSixteen['value'] <= 100 and self.count100 == True:
                self.animate16(0)
            self.count20 = False
            self.count40 = False
            self.count60 = False
            self.count80 = False
            self.count100 = False
        except AttributeError:
            pass
        ##    def fire1_go(self):

    ##        pass
    ##    def fire2_go(self):
    ##        pass
    ##    def fire3_go(self):
    ##        pass
    ##    def fire4_go(self):
    ##        pass
    ##    def fire5_go(self):
    ##        pass
    ##    def fire6_go(self):
    ##        pass
    ##    def fire7_go(self):
    ##        pass
    ##    def fire8_go(self):
    ##        pass
    ##    def water9_go(self):
    ##        pass
    ##    def water10_go(self):
    ##        pass
    ##    def water11_go(self):
    ##        pass
    ##    def water12_go(self):
    ##        pass
    ##    def water13_go(self):
    ##        pass
    ##    def water14_go(self):
    ##        pass
    ##    def water15_go(self):
    ##        pass
    ##    def water16_go(self):
    ##        pass
    def animate1(self, counter):
        nanobot = self.myLevelOne['value']
        try:
            a = self.sequence_dead
            b = self.sequence_idle
            c = self.sequence_go
            d = self.sequence_go
            e = self.sequence_prev2

            if nanobot >= 0 and nanobot <= 20:
                self.canvas1.itemconfig(self.image1, image = a[counter])
                self.root.after(250, lambda: self.animate1((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas1.itemconfig(self.image1, image = b[counter])
                self.root.after(500, lambda: self.animate1((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas1.itemconfig(self.image1, image = c[counter])
                self.root.after(100, lambda: self.animate1((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas1.itemconfig(self.image1, image = d[counter])
                self.root.after(100, lambda: self.animate1((counter + 1) % len(d)))
            else:
                self.canvas1.itemconfig(self.image1, image = e[counter])
                self.root.after(100, lambda: self.animate1((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate2(self, counter):
        nanobot = self.myLevelTwo['value']
        try:

            a = self.sequence_dead_copper
            b = self.sequence_idle_copper
            c = self.sequence_go_copper
            d = self.sequence_go_copper
            e = self.sequence_prev2_copper

            if nanobot >= 0 and nanobot <= 20:
                self.canvas2.itemconfig(self.image2, image=a[counter])
                self.root.after(350, lambda: self.animate2((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas2.itemconfig(self.image2, image=b[counter])
                self.root.after(500, lambda: self.animate2((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas2.itemconfig(self.image2, image=c[counter])
                self.root.after(100, lambda: self.animate2((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas2.itemconfig(self.image2, image=d[counter])
                self.root.after(100, lambda: self.animate2((counter + 1) % len(d)))
            else:
                self.canvas2.itemconfig(self.image2, image=e[counter])
                self.root.after(100, lambda: self.animate2((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate3(self, counter):
        nanobot = self.myLevelThree['value']
        try:

            a = self.sequence_dead_copper
            b = self.sequence_idle_copper
            c = self.sequence_go_copper
            d = self.sequence_go_copper
            e = self.sequence_prev2_copper

            if nanobot >= 0 and nanobot <= 20:
                self.canvas3.itemconfig(self.image3, image=a[counter])
                self.root.after(450, lambda: self.animate3((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas3.itemconfig(self.image3, image=b[counter])
                self.root.after(500, lambda: self.animate3((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas3.itemconfig(self.image3, image=c[counter])
                self.root.after(100, lambda: self.animate3((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas3.itemconfig(self.image3, image=d[counter])
                self.root.after(100, lambda: self.animate3((counter + 1) % len(d)))
            else:
                self.canvas3.itemconfig(self.image3, image=e[counter])
                self.root.after(100, lambda: self.animate3((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate4(self, counter):
        nanobot = self.myLevelFour['value']
        try:
            a = self.sequence_dead_copper
            b = self.sequence_idle_copper
            c = self.sequence_go_copper
            d = self.sequence_go_copper
            e = self.sequence_prev2_copper

            if nanobot >= 0 and nanobot <= 20:
                self.canvas4.itemconfig(self.image4, image=a[counter])
                self.root.after(550, lambda: self.animate4((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas4.itemconfig(self.image4, image=b[counter])
                self.root.after(500, lambda: self.animate4((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas4.itemconfig(self.image4, image=c[counter])
                self.root.after(100, lambda: self.animate4((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas4.itemconfig(self.image4, image=d[counter])
                self.root.after(100, lambda: self.animate4((counter + 1) % len(d)))
            else:
                self.canvas4.itemconfig(self.image4, image=e[counter])
                self.root.after(100, lambda: self.animate4((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate5(self, counter):
        nanobot = self.myLevelFive['value']
        try:
            a = self.sequence_dead_copper
            b = self.sequence_idle_copper
            c = self.sequence_go_copper
            d = self.sequence_go_copper
            e = self.sequence_prev2_copper
            if nanobot >= 0 and nanobot <= 20:
                self.canvas5.itemconfig(self.image5, image=a[counter])
                self.root.after(650, lambda: self.animate5((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas5.itemconfig(self.image5, image=b[counter])
                self.root.after(500, lambda: self.animate5((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas5.itemconfig(self.image5, image=c[counter])
                self.root.after(100, lambda: self.animate5((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas5.itemconfig(self.image5, image=d[counter])
                self.root.after(100, lambda: self.animate5((counter + 1) % len(d)))
            else:
                self.canvas5.itemconfig(self.image5, image=e[counter])
                self.root.after(100, lambda: self.animate5((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate6(self, counter):
        nanobot = self.myLevelSix['value']
        try:
            if nanobot >= 0 and nanobot <= 20:
                self.canvas6.itemconfig(self.image6, image=self.sequence_dead[counter])
                self.root.after(750, lambda: self.animate6((counter + 1) % len(self.sequence_dead)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas6.itemconfig(self.image6, image=self.sequence_idle[counter])
                self.root.after(500, lambda: self.animate6((counter + 1) % len(self.sequence_idle)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas6.itemconfig(self.image6, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate6((counter + 1) % len(self.sequence_go)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas6.itemconfig(self.image6, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate6((counter + 1) % len(self.sequence_go)))
            else:
                self.canvas6.itemconfig(self.image6, image=self.sequence_prev2[counter])
                self.root.after(100, lambda: self.animate6((counter + 1) % len(self.sequence_prev2)))
        except IndexError:
            pass

    def animate7(self, counter):
        nanobot = self.myLevelSeven['value']
        try:
            a = self.sequence_dead_grape
            b = self.sequence_idle_grape
            c = self.sequence_go_grape
            d = self.sequence_go_grape
            e = self.sequence_prev2_grape

            if nanobot >= 0 and nanobot <= 20:
                self.canvas7.itemconfig(self.image7, image=a[counter])
                self.root.after(600, lambda: self.animate7((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas7.itemconfig(self.image7, image=b[counter])
                self.root.after(500, lambda: self.animate7((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas7.itemconfig(self.image7, image=c[counter])
                self.root.after(100, lambda: self.animate7((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas7.itemconfig(self.image7, image=d[counter])
                self.root.after(100, lambda: self.animate7((counter + 1) % len(d)))
            else:
                self.canvas7.itemconfig(self.image7, image=e[counter])
                self.root.after(100, lambda: self.animate7((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate8(self, counter):
        nanobot = self.myLevelEight['value']
        try:

            a = self.sequence_dead_grape
            b = self.sequence_idle_grape
            c = self.sequence_go_grape
            d = self.sequence_go_grape
            e = self.sequence_prev2_grape

            if nanobot >= 0 and nanobot <= 20:
                self.canvas8.itemconfig(self.image8, image=a[counter])
                self.root.after(620, lambda: self.animate8((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas8.itemconfig(self.image8, image=b[counter])
                self.root.after(500, lambda: self.animate8((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas8.itemconfig(self.image8, image=c[counter])
                self.root.after(100, lambda: self.animate8((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas8.itemconfig(self.image8, image=d[counter])
                self.root.after(100, lambda: self.animate8((counter + 1) % len(d)))
            else:
                self.canvas8.itemconfig(self.image8, image=e[counter])
                self.root.after(100, lambda: self.animate8((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate9(self, counter):
        nanobot = self.myLevelNine['value']
        try:

            a = self.sequence_dead_grape
            b = self.sequence_idle_grape
            c = self.sequence_go_grape
            d = self.sequence_go_grape
            e = self.sequence_prev2_grape

            if nanobot >= 0 and nanobot <= 20:
                self.canvas9.itemconfig(self.image9, image=a[counter])
                self.root.after(540, lambda: self.animate9((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas9.itemconfig(self.image9, image=b[counter])
                self.root.after(500, lambda: self.animate9((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas9.itemconfig(self.image9, image=c[counter])
                self.root.after(100, lambda: self.animate9((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas9.itemconfig(self.image9, image=d[counter])
                self.root.after(100, lambda: self.animate9((counter + 1) % len(d)))
            else:
                self.canvas9.itemconfig(self.image9, image=e[counter])
                self.root.after(100, lambda: self.animate9((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate10(self, counter):
        nanobot = self.myLevelTen['value']
        try:

            a = self.sequence_dead_david
            b = self.sequence_idle_david
            c = self.sequence_go_david
            d = self.sequence_go_grape
            e = self.sequence_prev2_grape

            if nanobot >= 0 and nanobot <= 20:
                self.canvas10.itemconfig(self.image10, image=a[counter])
                self.root.after(350, lambda: self.animate10((counter + 1) % len(a)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas10.itemconfig(self.image10, image=b[counter])
                self.root.after(500, lambda: self.animate10((counter + 1) % len(b)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas10.itemconfig(self.image10, image=c[counter])
                self.root.after(100, lambda: self.animate10((counter + 1) % len(c)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas10.itemconfig(self.image10, image=d[counter])
                self.root.after(100, lambda: self.animate10((counter + 1) % len(d)))
            else:
                self.canvas10.itemconfig(self.image10, image=e[counter])
                self.root.after(100, lambda: self.animate10((counter + 1) % len(e)))
        except IndexError:
            pass

    def animate11(self, counter):
        nanobot = self.myLevelEleven['value']
        try:
            if nanobot >= 0 and nanobot <= 20:
                self.canvas11.itemconfig(self.image11, image=self.sequence_dead[counter])
                self.root.after(750, lambda: self.animate11((counter + 1) % len(self.sequence_dead)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas11.itemconfig(self.image11, image=self.sequence_idle[counter])
                self.root.after(500, lambda: self.animate11((counter + 1) % len(self.sequence_idle)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas11.itemconfig(self.image11, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate11((counter + 1) % len(self.sequence_go)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas11.itemconfig(self.image11, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate11((counter + 1) % len(self.sequence_go)))
            else:
                self.canvas11.itemconfig(self.image11, image=self.sequence_prev2[counter])
                self.root.after(100, lambda: self.animate11((counter + 1) % len(self.sequence_prev2)))
        except IndexError:
            pass

    def animate12(self, counter):
        nanobot = self.myLevelTwelve['value']
        try:
            if nanobot >= 0 and nanobot <= 20:
                self.canvas12.itemconfig(self.image12, image=self.sequence_dead[counter])
                self.root.after(240, lambda: self.animate12((counter + 1) % len(self.sequence_dead)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas12.itemconfig(self.image12, image=self.sequence_idle[counter])
                self.root.after(500, lambda: self.animate12((counter + 1) % len(self.sequence_idle)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas12.itemconfig(self.image12, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate12((counter + 1) % len(self.sequence_go)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas12.itemconfig(self.image12, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate12((counter + 1) % len(self.sequence_go)))
            else:
                self.canvas12.itemconfig(self.image12, image=self.sequence_prev2[counter])
                self.root.after(100, lambda: self.animate12((counter + 1) % len(self.sequence_prev2)))
        except IndexError:
            pass

    def animate13(self, counter):
        nanobot = self.myLevelThirteen['value']
        try:
            if nanobot >= 0 and nanobot <= 20:
                self.canvas13.itemconfig(self.image13, image=self.sequence_dead[counter])
                self.root.after(240, lambda: self.animate13((counter + 1) % len(self.sequence_dead)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas13.itemconfig(self.image13, image=self.sequence_idle[counter])
                self.root.after(500, lambda: self.animate13((counter + 1) % len(self.sequence_idle)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas13.itemconfig(self.image13, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate13((counter + 1) % len(self.sequence_go)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas13.itemconfig(self.image13, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate13((counter + 1) % len(self.sequence_go)))
            else:
                self.canvas13.itemconfig(self.image13, image=self.sequence_prev2[counter])
                self.root.after(100, lambda: self.animate13((counter + 1) % len(self.sequence_prev2)))
        except IndexError:
            pass

    def animate14(self, counter):
        nanobot = self.myLevelFourteen['value']
        try:
            if nanobot >= 0 and nanobot <= 20:
                self.canvas14.itemconfig(self.image14, image=self.sequence_dead[counter])
                self.root.after(240, lambda: self.animate14((counter + 1) % len(self.sequence_dead)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas14.itemconfig(self.image14, image=self.sequence_idle[counter])
                self.root.after(500, lambda: self.animate14((counter + 1) % len(self.sequence_idle)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas14.itemconfig(self.image14, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate14((counter + 1) % len(self.sequence_go)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas14.itemconfig(self.image14, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate14((counter + 1) % len(self.sequence_go)))
            else:
                self.canvas14.itemconfig(self.image14, image=self.sequence_prev2[counter])
                self.root.after(100, lambda: self.animate14((counter + 1) % len(self.sequence_prev2)))
        except IndexError:
            pass

    def animate15(self, counter):
        nanobot = self.myLevelFifteen['value']
        try:
            if nanobot >= 0 and nanobot <= 20:
                self.canvas15.itemconfig(self.image15, image=self.sequence_dead[counter])
                self.root.after(240, lambda: self.animate15((counter + 1) % len(self.sequence_dead)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas15.itemconfig(self.image15, image=self.sequence_idle[counter])
                self.root.after(500, lambda: self.animate15((counter + 1) % len(self.sequence_idle)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas15.itemconfig(self.image15, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate15((counter + 1) % len(self.sequence_go)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas15.itemconfig(self.image15, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate15((counter + 1) % len(self.sequence_go)))
            else:
                self.canvas15.itemconfig(self.image15, image=self.sequence_prev2[counter])
                self.root.after(100, lambda: self.animate15((counter + 1) % len(self.sequence_prev2)))
        except IndexError:
            pass

    def animate16(self, counter):
        nanobot = self.myLevelSixteen['value']
        try:
            if nanobot >= 0 and nanobot <= 20:
                self.canvas16.itemconfig(self.image16, image=self.sequence_dead[counter])
                self.root.after(240, lambda: self.animate16((counter + 1) % len(self.sequence_dead)))
            elif nanobot > 20 and nanobot <= 40:
                self.canvas16.itemconfig(self.image16, image=self.sequence_idle[counter])
                self.root.after(500, lambda: self.animate16((counter + 1) % len(self.sequence_idle)))
            elif nanobot > 40 and nanobot <= 60:
                self.canvas16.itemconfig(self.image16, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate16((counter + 1) % len(self.sequence_go)))
            elif nanobot > 60 and nanobot <= 80:
                self.canvas16.itemconfig(self.image16, image=self.sequence_go[counter])
                self.root.after(100, lambda: self.animate16((counter + 1) % len(self.sequence_go)))
            else:
                self.canvas16.itemconfig(self.image16, image=self.sequence_prev2[counter])
                self.root.after(100, lambda: self.animate16((counter + 1) % len(self.sequence_prev2)))
        except IndexError:
            pass

    def eyes_open(self):
        self.OnebtnPointOne.configure(bg='black')
        self.OnebtnPointFive.configure(bg='black')
        self.OnebtnPointTen.configure(bg='black')
        self.OnebtnPointTwenty.configure(bg='black')

        self.NinebtnPointOne.configure(bg='black')
        self.NinebtnPointFive.configure(bg='black')
        self.NinebtnPointTen.configure(bg='black')
        self.NinebtnPointTwenty.configure(bg='black')

    def eyes_close1(self):

        self.OnebtnPointOne.configure(bg=self.eyes_close_col)
        self.OnebtnPointFive.configure(bg=self.eyes_close_col)
        self.OnebtnPointTen.configure(bg=self.eyes_close_col)
        self.OnebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.NinebtnPointOne.configure(bg=self.eyes_close_col)
        self.NinebtnPointFive.configure(bg=self.eyes_close_col)
        self.NinebtnPointTen.configure(bg=self.eyes_close_col)
        self.NinebtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close2(self):
        self.TwobtnPointOne.configure(bg=self.eyes_close_col)
        self.TwobtnPointFive.configure(bg=self.eyes_close_col)
        self.TwobtnPointTen.configure(bg=self.eyes_close_col)
        self.TwobtnPointTwenty.configure(bg=self.eyes_close_col)

        self.TenbtnPointOne.configure(bg=self.eyes_close_col)
        self.TenbtnPointFive.configure(bg=self.eyes_close_col)
        self.TenbtnPointTen.configure(bg=self.eyes_close_col)
        self.TenbtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close3(self):
        self.ThreebtnPointOne.configure(bg=self.eyes_close_col)
        self.ThreebtnPointFive.configure(bg=self.eyes_close_col)
        self.ThreebtnPointTen.configure(bg=self.eyes_close_col)
        self.ThreebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.ElevenbtnPointOne.configure(bg=self.eyes_close_col)
        self.ElevenbtnPointFive.configure(bg=self.eyes_close_col)
        self.ElevenbtnPointTen.configure(bg=self.eyes_close_col)
        self.ElevenbtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close4(self):
        self.FourbtnPointOne.configure(bg=self.eyes_close_col)
        self.FourbtnPointFive.configure(bg=self.eyes_close_col)
        self.FourbtnPointTen.configure(bg=self.eyes_close_col)
        self.FourbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.TwelvebtnPointOne.configure(bg=self.eyes_close_col)
        self.TwelvebtnPointFive.configure(bg=self.eyes_close_col)
        self.TwelvebtnPointTen.configure(bg=self.eyes_close_col)
        self.TwelvebtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close5(self):
        self.FivebtnPointOne.configure(bg=self.eyes_close_col)
        self.FivebtnPointFive.configure(bg=self.eyes_close_col)
        self.FivebtnPointTen.configure(bg=self.eyes_close_col)
        self.FivebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.ThirteenbtnPointOne.configure(bg=self.eyes_close_col)
        self.ThirteenbtnPointFive.configure(bg=self.eyes_close_col)
        self.ThirteenbtnPointTen.configure(bg=self.eyes_close_col)
        self.ThirteenbtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close6(self):
        self.SixbtnPointOne.configure(bg=self.eyes_close_col)
        self.SixbtnPointFive.configure(bg=self.eyes_close_col)
        self.SixbtnPointTen.configure(bg=self.eyes_close_col)
        self.SixbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.FourteenbtnPointOne.configure(bg=self.eyes_close_col)
        self.FourteenbtnPointFive.configure(bg=self.eyes_close_col)
        self.FourteenbtnPointTen.configure(bg=self.eyes_close_col)
        self.FourteenbtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close7(self):
        self.SevenbtnPointOne.configure(bg=self.eyes_close_col)
        self.SevenbtnPointFive.configure(bg=self.eyes_close_col)
        self.SevenbtnPointTen.configure(bg=self.eyes_close_col)
        self.SevenbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.FifteenbtnPointOne.configure(bg=self.eyes_close_col)
        self.FifteenbtnPointFive.configure(bg=self.eyes_close_col)
        self.FifteenbtnPointTen.configure(bg=self.eyes_close_col)
        self.FifteenbtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close8(self):
        self.EightbtnPointOne.configure(bg=self.eyes_close_col)
        self.EightbtnPointFive.configure(bg=self.eyes_close_col)
        self.EightbtnPointTen.configure(bg=self.eyes_close_col)
        self.EightbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.SixteenbtnPointOne.configure(bg=self.eyes_close_col)
        self.SixteenbtnPointFive.configure(bg=self.eyes_close_col)
        self.SixteenbtnPointTen.configure(bg=self.eyes_close_col)
        self.SixteenbtnPointTwenty.configure(bg=self.eyes_close_col)

    def eyes_close9(self):
        self.EightbtnPointOne.configure(bg='ghost white')
        self.EightbtnPointFive.configure(bg='black')
        self.EightbtnPointTen.configure(bg='black')
        self.EightbtnPointTwenty.configure(bg='black')

        self.SixteenbtnPointOne.configure(bg='black')
        self.SixteenbtnPointFive.configure(bg='black')
        self.SixteenbtnPointTen.configure(bg='black')
        self.SixteenbtnPointTwenty.configure(bg='ghost white')

    def eyes_close10(self):
        self.EightbtnPointOne.configure(bg='ghost white')
        self.EightbtnPointFive.configure(bg='black')
        self.EightbtnPointTen.configure(bg='black')
        self.EightbtnPointTwenty.configure(bg='black')

        self.SixteenbtnPointOne.configure(bg='black')
        self.SixteenbtnPointFive.configure(bg='black')
        self.SixteenbtnPointTen.configure(bg='black')
        self.SixteenbtnPointTwenty.configure(bg='ghost white')

        self.SevenbtnPointOne.configure(bg='ghost white')
        self.SevenbtnPointFive.configure(bg='black')
        self.SevenbtnPointTen.configure(bg='black')
        self.SevenbtnPointTwenty.configure(bg='black')

        self.FifteenbtnPointOne.configure(bg='black')
        self.FifteenbtnPointFive.configure(bg='black')
        self.FifteenbtnPointTen.configure(bg='black')
        self.FifteenbtnPointTwenty.configure(bg='ghost white')

    def eyes_close11(self):

        self.EightbtnPointOne.configure(bg='ghost white')
        self.EightbtnPointFive.configure(bg='black')
        self.EightbtnPointTen.configure(bg='black')
        self.EightbtnPointTwenty.configure(bg='black')

        self.SixteenbtnPointOne.configure(bg='black')
        self.SixteenbtnPointFive.configure(bg='black')
        self.SixteenbtnPointTen.configure(bg='black')
        self.SixteenbtnPointTwenty.configure(bg='ghost white')

        self.SevenbtnPointOne.configure(bg='ghost white')
        self.SevenbtnPointFive.configure(bg='black')
        self.SevenbtnPointTen.configure(bg='black')
        self.SevenbtnPointTwenty.configure(bg='black')

        self.FifteenbtnPointOne.configure(bg='black')
        self.FifteenbtnPointFive.configure(bg='black')
        self.FifteenbtnPointTen.configure(bg='black')
        self.FifteenbtnPointTwenty.configure(bg='ghost white')

        self.SixbtnPointOne.configure(bg='ghost white')
        self.SixbtnPointFive.configure(bg='black')
        self.SixbtnPointTen.configure(bg='black')
        self.SixbtnPointTwenty.configure(bg='black')

        self.FourteenbtnPointOne.configure(bg='black')
        self.FourteenbtnPointFive.configure(bg='black')
        self.FourteenbtnPointTen.configure(bg='black')
        self.FourteenbtnPointTwenty.configure(bg='ghost white')

        self.FivebtnPointOne.configure(bg='ghost white')
        self.FivebtnPointFive.configure(bg='ghost white')
        self.FivebtnPointTen.configure(bg='ghost white')
        self.FivebtnPointTwenty.configure(bg='ghost white')

        self.ThirteenbtnPointOne.configure(bg='ghost white')
        self.ThirteenbtnPointFive.configure(bg='ghost white')
        self.ThirteenbtnPointTen.configure(bg='ghost white')
        self.ThirteenbtnPointTwenty.configure(bg='ghost white')

    def eyes_close12(self):

        self.EightbtnPointOne.configure(bg='ghost white')
        self.EightbtnPointFive.configure(bg='black')
        self.EightbtnPointTen.configure(bg='black')
        self.EightbtnPointTwenty.configure(bg='black')

        self.SixteenbtnPointOne.configure(bg='black')
        self.SixteenbtnPointFive.configure(bg='black')
        self.SixteenbtnPointTen.configure(bg='black')
        self.SixteenbtnPointTwenty.configure(bg='ghost white')

        self.SevenbtnPointOne.configure(bg='ghost white')
        self.SevenbtnPointFive.configure(bg='black')
        self.SevenbtnPointTen.configure(bg='black')
        self.SevenbtnPointTwenty.configure(bg='black')

        self.FifteenbtnPointOne.configure(bg='black')
        self.FifteenbtnPointFive.configure(bg='black')
        self.FifteenbtnPointTen.configure(bg='black')
        self.FifteenbtnPointTwenty.configure(bg='ghost white')

        self.SixbtnPointOne.configure(bg='ghost white')
        self.SixbtnPointFive.configure(bg='black')
        self.SixbtnPointTen.configure(bg='black')
        self.SixbtnPointTwenty.configure(bg='black')

        self.FourteenbtnPointOne.configure(bg='black')
        self.FourteenbtnPointFive.configure(bg='black')
        self.FourteenbtnPointTen.configure(bg='black')
        self.FourteenbtnPointTwenty.configure(bg='ghost white')

        self.FivebtnPointOne.configure(bg='ghost white')
        self.FivebtnPointFive.configure(bg='ghost white')
        self.FivebtnPointTen.configure(bg='ghost white')
        self.FivebtnPointTwenty.configure(bg='ghost white')

        self.ThirteenbtnPointOne.configure(bg='ghost white')
        self.ThirteenbtnPointFive.configure(bg='ghost white')
        self.ThirteenbtnPointTen.configure(bg='ghost white')
        self.ThirteenbtnPointTwenty.configure(bg='ghost white')

        self.FourbtnPointOne.configure(bg='ghost white')
        self.FourbtnPointFive.configure(bg='ghost white')
        self.FourbtnPointTen.configure(bg='ghost white')
        self.FourbtnPointTwenty.configure(bg='ghost white')
        self.TwelvebtnPointOne.configure(bg='ghost white')
        self.TwelvebtnPointFive.configure(bg='ghost white')
        self.TwelvebtnPointTen.configure(bg='ghost white')
        self.TwelvebtnPointTwenty.configure(bg='ghost white')

    def eyes_close13(self):

        self.EightbtnPointOne.configure(bg='ghost white')
        self.EightbtnPointFive.configure(bg='black')
        self.EightbtnPointTen.configure(bg='gray10')
        self.EightbtnPointTwenty.configure(bg='gray10')
        self.SixteenbtnPointOne.configure(bg='gray10')
        self.SixteenbtnPointFive.configure(bg='gray10')
        self.SixteenbtnPointTen.configure(bg='black')
        self.SixteenbtnPointTwenty.configure(bg='ghost white')

        self.SevenbtnPointOne.configure(bg='ghost white')
        self.SevenbtnPointFive.configure(bg='black')
        self.SevenbtnPointTen.configure(bg='gray10')
        self.SevenbtnPointTwenty.configure(bg='gray10')
        self.FifteenbtnPointOne.configure(bg='gray10')
        self.FifteenbtnPointFive.configure(bg='gray10')
        self.FifteenbtnPointTen.configure(bg='black')
        self.FifteenbtnPointTwenty.configure(bg='ghost white')

        self.SixbtnPointOne.configure(bg='ghost white')
        self.SixbtnPointFive.configure(bg='black')
        self.SixbtnPointTen.configure(bg='black')
        self.SixbtnPointTwenty.configure(bg='black')
        self.FourteenbtnPointOne.configure(bg='black')
        self.FourteenbtnPointFive.configure(bg='black')
        self.FourteenbtnPointTen.configure(bg='black')
        self.FourteenbtnPointTwenty.configure(bg='ghost white')

        self.FivebtnPointOne.configure(bg='ghost white')
        self.FivebtnPointFive.configure(bg='ghost white')
        self.FivebtnPointTen.configure(bg='ghost white')
        self.FivebtnPointTwenty.configure(bg='ghost white')
        self.ThirteenbtnPointOne.configure(bg='ghost white')
        self.ThirteenbtnPointFive.configure(bg='ghost white')
        self.ThirteenbtnPointTen.configure(bg='ghost white')
        self.ThirteenbtnPointTwenty.configure(bg='ghost white')

        self.FourbtnPointOne.configure(bg='ghost white')
        self.FourbtnPointFive.configure(bg='ghost white')
        self.FourbtnPointTen.configure(bg='ghost white')
        self.FourbtnPointTwenty.configure(bg='ghost white')
        self.TwelvebtnPointOne.configure(bg='ghost white')
        self.TwelvebtnPointFive.configure(bg='ghost white')
        self.TwelvebtnPointTen.configure(bg='ghost white')
        self.TwelvebtnPointTwenty.configure(bg='ghost white')

        self.ThreebtnPointOne.configure(bg='ghost white')
        self.ThreebtnPointFive.configure(bg='ghost white')
        self.ThreebtnPointTen.configure(bg='ghost white')
        self.ThreebtnPointTwenty.configure(bg='ghost white')
        self.ElevenbtnPointOne.configure(bg='ghost white')
        self.ElevenbtnPointFive.configure(bg='ghost white')
        self.ElevenbtnPointTen.configure(bg='ghost white')
        self.ElevenbtnPointTwenty.configure(bg='ghost white')

    def eyes_close14(self):

        self.EightbtnPointOne.configure(bg='ghost white')
        self.EightbtnPointFive.configure(bg='black')
        self.EightbtnPointTen.configure(bg='gray10')
        self.EightbtnPointTwenty.configure(bg='gray10')
        self.SixteenbtnPointOne.configure(bg='gray10')
        self.SixteenbtnPointFive.configure(bg='gray10')
        self.SixteenbtnPointTen.configure(bg='black')
        self.SixteenbtnPointTwenty.configure(bg='ghost white')

        self.SevenbtnPointOne.configure(bg='ghost white')
        self.SevenbtnPointFive.configure(bg='black')
        self.SevenbtnPointTen.configure(bg='gray10')
        self.SevenbtnPointTwenty.configure(bg='gray10')
        self.FifteenbtnPointOne.configure(bg='gray10')
        self.FifteenbtnPointFive.configure(bg='gray10')
        self.FifteenbtnPointTen.configure(bg='black')
        self.FifteenbtnPointTwenty.configure(bg='ghost white')

        self.SixbtnPointOne.configure(bg='ghost white')
        self.SixbtnPointFive.configure(bg='black')
        self.SixbtnPointTen.configure(bg='black')
        self.SixbtnPointTwenty.configure(bg='black')
        self.FourteenbtnPointOne.configure(bg='black')
        self.FourteenbtnPointFive.configure(bg='black')
        self.FourteenbtnPointTen.configure(bg='black')
        self.FourteenbtnPointTwenty.configure(bg='ghost white')

        self.FivebtnPointOne.configure(bg='ghost white')
        self.FivebtnPointFive.configure(bg='ghost white')
        self.FivebtnPointTen.configure(bg='ghost white')
        self.FivebtnPointTwenty.configure(bg='ghost white')
        self.ThirteenbtnPointOne.configure(bg='ghost white')
        self.ThirteenbtnPointFive.configure(bg='ghost white')
        self.ThirteenbtnPointTen.configure(bg='ghost white')
        self.ThirteenbtnPointTwenty.configure(bg='ghost white')

        self.FourbtnPointOne.configure(bg='ghost white')
        self.FourbtnPointFive.configure(bg='ghost white')
        self.FourbtnPointTen.configure(bg='ghost white')
        self.FourbtnPointTwenty.configure(bg='ghost white')
        self.TwelvebtnPointOne.configure(bg='ghost white')
        self.TwelvebtnPointFive.configure(bg='ghost white')
        self.TwelvebtnPointTen.configure(bg='ghost white')
        self.TwelvebtnPointTwenty.configure(bg='ghost white')

        self.ThreebtnPointOne.configure(bg='ghost white')
        self.ThreebtnPointFive.configure(bg='ghost white')
        self.ThreebtnPointTen.configure(bg='ghost white')
        self.ThreebtnPointTwenty.configure(bg='ghost white')
        self.ElevenbtnPointOne.configure(bg='ghost white')
        self.ElevenbtnPointFive.configure(bg='ghost white')
        self.ElevenbtnPointTen.configure(bg='ghost white')
        self.ElevenbtnPointTwenty.configure(bg='ghost white')

        self.TwobtnPointOne.configure(bg='ghost white')
        self.TwobtnPointFive.configure(bg='ghost white')
        self.TwobtnPointTen.configure(bg='ghost white')
        self.TwobtnPointTwenty.configure(bg='ghost white')
        self.TenbtnPointOne.configure(bg='ghost white')
        self.TenbtnPointFive.configure(bg='ghost white')
        self.TenbtnPointTen.configure(bg='ghost white')
        self.TenbtnPointTwenty.configure(bg='ghost white')

    def blink_eyes(self, counter):
        eye_col_grey = 'ghost white'

        self.OnebtnPointOne.configure(bg=eye_col_grey)
        self.OnebtnPointFive.configure(bg=eye_col_grey)
        self.OnebtnPointTen.configure(bg=eye_col_grey)
        self.OnebtnPointTwenty.configure(bg=eye_col_grey)

        self.TwobtnPointOne.configure(bg=eye_col_grey)
        self.TwobtnPointFive.configure(bg=eye_col_grey)
        self.TwobtnPointTen.configure(bg=eye_col_grey)
        self.TwobtnPointTwenty.configure(bg=eye_col_grey)

        self.ThreebtnPointOne.configure(bg=eye_col_grey)
        self.ThreebtnPointFive.configure(bg=eye_col_grey)
        self.ThreebtnPointTen.configure(bg=eye_col_grey)
        self.ThreebtnPointTwenty.configure(bg=eye_col_grey)

        self.FourbtnPointOne.configure(bg=eye_col_grey)
        self.FourbtnPointFive.configure(bg=eye_col_grey)
        self.FourbtnPointTen.configure(bg=eye_col_grey)
        self.FourbtnPointTwenty.configure(bg=eye_col_grey)

        self.FivebtnPointOne.configure(bg=eye_col_grey)
        self.FivebtnPointFive.configure(bg=eye_col_grey)
        self.FivebtnPointTen.configure(bg=eye_col_grey)
        self.FivebtnPointTwenty.configure(bg=eye_col_grey)

        self.SixbtnPointOne.configure(bg=eye_col_grey)
        self.SixbtnPointFive.configure(bg=eye_col_grey)
        self.SixbtnPointTen.configure(bg=eye_col_grey)
        self.SixbtnPointTwenty.configure(bg=eye_col_grey)

        self.SevenbtnPointOne.configure(bg=eye_col_grey)
        self.SevenbtnPointFive.configure(bg=eye_col_grey)
        self.SevenbtnPointTen.configure(bg=eye_col_grey)
        self.SevenbtnPointTwenty.configure(bg=eye_col_grey)

        self.EightbtnPointOne.configure(bg=eye_col_grey)
        self.EightbtnPointFive.configure(bg=eye_col_grey)
        self.EightbtnPointTen.configure(bg=eye_col_grey)
        self.EightbtnPointTwenty.configure(bg=eye_col_grey)

        self.NinebtnPointOne.configure(bg=eye_col_grey)
        self.NinebtnPointFive.configure(bg=eye_col_grey)
        self.NinebtnPointTen.configure(bg=eye_col_grey)
        self.NinebtnPointTwenty.configure(bg=eye_col_grey)

        self.TenbtnPointOne.configure(bg=eye_col_grey)
        self.TenbtnPointFive.configure(bg=eye_col_grey)
        self.TenbtnPointTen.configure(bg=eye_col_grey)
        self.TenbtnPointTwenty.configure(bg=eye_col_grey)

        self.ElevenbtnPointOne.configure(bg=eye_col_grey)
        self.ElevenbtnPointFive.configure(bg=eye_col_grey)
        self.ElevenbtnPointTen.configure(bg=eye_col_grey)
        self.ElevenbtnPointTwenty.configure(bg=eye_col_grey)

        self.TwelvebtnPointOne.configure(bg=eye_col_grey)
        self.TwelvebtnPointFive.configure(bg=eye_col_grey)
        self.TwelvebtnPointTen.configure(bg=eye_col_grey)
        self.TwelvebtnPointTwenty.configure(bg=eye_col_grey)

        self.ThirteenbtnPointOne.configure(bg=eye_col_grey)
        self.ThirteenbtnPointFive.configure(bg=eye_col_grey)
        self.ThirteenbtnPointTen.configure(bg=eye_col_grey)
        self.ThirteenbtnPointTwenty.configure(bg=eye_col_grey)

        self.FourteenbtnPointOne.configure(bg=eye_col_grey)
        self.FourteenbtnPointFive.configure(bg=eye_col_grey)
        self.FourteenbtnPointTen.configure(bg=eye_col_grey)
        self.FourteenbtnPointTwenty.configure(bg=eye_col_grey)

        self.FifteenbtnPointOne.configure(bg=eye_col_grey)
        self.FifteenbtnPointFive.configure(bg=eye_col_grey)
        self.FifteenbtnPointTen.configure(bg=eye_col_grey)
        self.FifteenbtnPointTwenty.configure(bg=eye_col_grey)

        self.SixteenbtnPointOne.configure(bg=eye_col_grey)
        self.SixteenbtnPointFive.configure(bg=eye_col_grey)
        self.SixteenbtnPointTen.configure(bg=eye_col_grey)
        self.SixteenbtnPointTwenty.configure(bg=eye_col_grey)

    def blinking(self):
        self.eyes_close1()
        self.waithere(45)
        self.eyes_close2()
        self.waithere(45)
        self.eyes_close3()
        self.waithere(45)
        self.eyes_close4()
        self.waithere(45)
        self.eyes_close5()
        self.waithere(45)
        self.eyes_close6()
        self.waithere(45)
        self.eyes_close7()
        self.waithere(45)
        self.eyes_close8()
        self.waithere(45)
        self.eyes_close9()
        self.waithere(45)
        self.eyes_close10()
        self.waithere(45)
        self.eyes_close11()
        self.waithere(45)
        self.eyes_close12()
        self.waithere(45)
        self.eyes_close13()
        self.waithere(45)
        self.eyes_close14()
        self.waithere(45)

    def blink_eyes(self):
        eye_col_grey = 'ghost white'

        self.OnebtnPointOne.configure(bg=eye_col_grey)
        self.OnebtnPointFive.configure(bg=eye_col_grey)
        self.OnebtnPointTen.configure(bg=eye_col_grey)
        self.OnebtnPointTwenty.configure(bg=eye_col_grey)

        self.TwobtnPointOne.configure(bg=eye_col_grey)
        self.TwobtnPointFive.configure(bg=eye_col_grey)
        self.TwobtnPointTen.configure(bg=eye_col_grey)
        self.TwobtnPointTwenty.configure(bg=eye_col_grey)

        self.ThreebtnPointOne.configure(bg=eye_col_grey)
        self.ThreebtnPointFive.configure(bg=eye_col_grey)
        self.ThreebtnPointTen.configure(bg=eye_col_grey)
        self.ThreebtnPointTwenty.configure(bg=eye_col_grey)

        self.FourbtnPointOne.configure(bg=eye_col_grey)
        self.FourbtnPointFive.configure(bg=eye_col_grey)
        self.FourbtnPointTen.configure(bg=eye_col_grey)
        self.FourbtnPointTwenty.configure(bg=eye_col_grey)

        self.FivebtnPointOne.configure(bg=eye_col_grey)
        self.FivebtnPointFive.configure(bg=eye_col_grey)
        self.FivebtnPointTen.configure(bg=eye_col_grey)
        self.FivebtnPointTwenty.configure(bg=eye_col_grey)

        self.SixbtnPointOne.configure(bg=eye_col_grey)
        self.SixbtnPointFive.configure(bg=eye_col_grey)
        self.SixbtnPointTen.configure(bg=eye_col_grey)
        self.SixbtnPointTwenty.configure(bg=eye_col_grey)

        self.SevenbtnPointOne.configure(bg=eye_col_grey)
        self.SevenbtnPointFive.configure(bg=eye_col_grey)
        self.SevenbtnPointTen.configure(bg=eye_col_grey)
        self.SevenbtnPointTwenty.configure(bg=eye_col_grey)

        self.EightbtnPointOne.configure(bg=eye_col_grey)
        self.EightbtnPointFive.configure(bg=eye_col_grey)
        self.EightbtnPointTen.configure(bg=eye_col_grey)
        self.EightbtnPointTwenty.configure(bg=eye_col_grey)

        self.NinebtnPointOne.configure(bg=eye_col_grey)
        self.NinebtnPointFive.configure(bg=eye_col_grey)
        self.NinebtnPointTen.configure(bg=eye_col_grey)
        self.NinebtnPointTwenty.configure(bg=eye_col_grey)

        self.TenbtnPointOne.configure(bg=eye_col_grey)
        self.TenbtnPointFive.configure(bg=eye_col_grey)
        self.TenbtnPointTen.configure(bg=eye_col_grey)
        self.TenbtnPointTwenty.configure(bg=eye_col_grey)

        self.ElevenbtnPointOne.configure(bg=eye_col_grey)
        self.ElevenbtnPointFive.configure(bg=eye_col_grey)
        self.ElevenbtnPointTen.configure(bg=eye_col_grey)
        self.ElevenbtnPointTwenty.configure(bg=eye_col_grey)

        self.TwelvebtnPointOne.configure(bg=eye_col_grey)
        self.TwelvebtnPointFive.configure(bg=eye_col_grey)
        self.TwelvebtnPointTen.configure(bg=eye_col_grey)
        self.TwelvebtnPointTwenty.configure(bg=eye_col_grey)

        self.ThirteenbtnPointOne.configure(bg=eye_col_grey)
        self.ThirteenbtnPointFive.configure(bg=eye_col_grey)
        self.ThirteenbtnPointTen.configure(bg=eye_col_grey)
        self.ThirteenbtnPointTwenty.configure(bg=eye_col_grey)

        self.FourteenbtnPointOne.configure(bg=eye_col_grey)
        self.FourteenbtnPointFive.configure(bg=eye_col_grey)
        self.FourteenbtnPointTen.configure(bg=eye_col_grey)
        self.FourteenbtnPointTwenty.configure(bg=eye_col_grey)

        self.FifteenbtnPointOne.configure(bg=eye_col_grey)
        self.FifteenbtnPointFive.configure(bg=eye_col_grey)
        self.FifteenbtnPointTen.configure(bg=eye_col_grey)
        self.FifteenbtnPointTwenty.configure(bg=eye_col_grey)

        self.SixteenbtnPointOne.configure(bg=eye_col_grey)
        self.SixteenbtnPointFive.configure(bg=eye_col_grey)
        self.SixteenbtnPointTen.configure(bg=eye_col_grey)
        self.SixteenbtnPointTwenty.configure(bg=eye_col_grey)

    def Look_Straight(self):
        # Look Straight Ahead loa
        self.blink_eyes()

        self.OnebtnPointOne.configure(bg=self.eyes_close_col)
        self.OnebtnPointFive.configure(bg=self.eyes_close_col)
        self.OnebtnPointTen.configure(bg=self.eyes_close_col)
        self.OnebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.ThreebtnPointFive.configure(bg='black')
        self.ThreebtnPointTen.configure(bg='black')
        self.ThreebtnPointTwenty.configure(bg='black')

        self.FourbtnPointFive.configure(bg='black')
        self.FourbtnPointTen.configure(bg='black')
        self.FourbtnPointTwenty.configure(bg='black')

        self.FivebtnPointFive.configure(bg='black')
        self.FivebtnPointTen.configure(bg='black')
        self.FivebtnPointTwenty.configure(bg='black')

        self.ElevenbtnPointOne.configure(bg='black')
        self.ElevenbtnPointFive.configure(bg='black')
        self.ElevenbtnPointTen.configure(bg='black')

        self.TwelvebtnPointOne.configure(bg='black')
        self.TwelvebtnPointFive.configure(bg='black')
        self.TwelvebtnPointTen.configure(bg='black')

        self.ThirteenbtnPointOne.configure(bg='black')
        self.ThirteenbtnPointFive.configure(bg='black')
        self.ThirteenbtnPointTen.configure(bg='black')

        self.NinebtnPointOne.configure(bg=self.eyes_close_col)
        self.NinebtnPointFive.configure(bg=self.eyes_close_col)
        self.NinebtnPointTen.configure(bg=self.eyes_close_col)
        self.NinebtnPointTwenty.configure(bg=self.eyes_close_col)

    def defeat1(self):
        self.blink_eyes()

        self.OnebtnPointOne.configure(bg='grey')
        self.OnebtnPointFive.configure(bg='grey')
        self.OnebtnPointTen.configure(bg='grey')
        self.OnebtnPointTwenty.configure(bg='grey')

        self.NinebtnPointOne.configure(bg='grey')
        self.NinebtnPointFive.configure(bg='grey')
        self.NinebtnPointTen.configure(bg='grey')
        self.NinebtnPointTwenty.configure(bg='grey')

        self.TwobtnPointOne.configure(bg='grey')
        self.TwobtnPointFive.configure(bg='grey')
        self.TwobtnPointTen.configure(bg='grey')
        self.TwobtnPointTwenty.configure(bg='grey')

        self.TenbtnPointOne.configure(bg='grey')
        self.TenbtnPointFive.configure(bg='grey')
        self.TenbtnPointTen.configure(bg='grey')
        self.TenbtnPointTwenty.configure(bg='grey')

    def waitRand(self):
        var = IntVar()
        rand_var = random.randrange(1000, 10000, 1000)
        root.after(rand_var, var.set, 1)
        root.wait_variable(var)

    def waithere(self, dur):
        var = IntVar()
        root.after(dur, var.set, 1)
        root.wait_variable(var)

        self.is_fire1_animating = False
        self.is_fire2_animating = False
        self.is_fire3_animating = False
        self.is_fire4_animating = False
        self.is_fire5_animating = False
        self.is_fire6_animating = False
        self.is_fire7_animating = False
        self.is_fire8_animating = False
        self.is_water9_animating = False
        self.is_water10_animating = False
        self.is_water11_animating = False
        self.is_water12_animating = False
        self.is_water13_animating = False
        self.is_water14_animating = False
        self.is_water15_animating = False
        self.is_water16_animating = False

        self.is_hurt1 = False


    def blinking(self):
        self.eyes_close1()
        self.waithere(45)
        self.eyes_close2()
        self.waithere(45)
        self.eyes_close3()
        self.waithere(45)
        self.eyes_close4()
        self.waithere(45)
        self.eyes_close5()
        self.waithere(45)
        self.eyes_close6()
        self.waithere(45)
        self.eyes_close7()
        self.waithere(45)
        self.eyes_close8()
        self.waithere(45)
        self.eyes_close9()
        self.waithere(45)
        self.eyes_close10()
        self.waithere(45)
        self.eyes_close11()
        self.waithere(45)
        self.eyes_close12()
        self.waithere(45)
        self.eyes_close13()
        self.waithere(45)
        self.eyes_close14()
        self.waithere(45)

    def Look_Straight(self):
        # Look Straight Ahead
        self.blink_eyes()

        self.OnebtnPointOne.configure(bg=self.eyes_close_col)
        self.OnebtnPointFive.configure(bg=self.eyes_close_col)
        self.OnebtnPointTen.configure(bg=self.eyes_close_col)
        self.OnebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.ThreebtnPointFive.configure(bg='black')
        self.ThreebtnPointTen.configure(bg='black')
        self.ThreebtnPointTwenty.configure(bg='black')

        self.FourbtnPointFive.configure(bg='black')
        self.FourbtnPointTen.configure(bg='black')
        self.FourbtnPointTwenty.configure(bg='black')

        self.FivebtnPointFive.configure(bg='black')
        self.FivebtnPointTen.configure(bg='black')
        self.FivebtnPointTwenty.configure(bg='black')

        self.ElevenbtnPointOne.configure(bg='black')
        self.ElevenbtnPointFive.configure(bg='black')
        self.ElevenbtnPointTen.configure(bg='black')

        self.TwelvebtnPointOne.configure(bg='black')
        self.TwelvebtnPointFive.configure(bg='black')
        self.TwelvebtnPointTen.configure(bg='black')

        self.ThirteenbtnPointOne.configure(bg='black')
        self.ThirteenbtnPointFive.configure(bg='black')
        self.ThirteenbtnPointTen.configure(bg='black')

        self.NinebtnPointOne.configure(bg=self.eyes_close_col)
        self.NinebtnPointFive.configure(bg=self.eyes_close_col)
        self.NinebtnPointTen.configure(bg=self.eyes_close_col)
        self.NinebtnPointTwenty.configure(bg=self.eyes_close_col)

    def look_angry(self):


        self.OnebtnPointOne.configure(bg=self.eyes_close_col)
        self.OnebtnPointFive.configure(bg=self.eyes_close_col)
        self.OnebtnPointTen.configure(bg=self.eyes_close_col)
        self.OnebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.NinebtnPointOne.configure(bg=self.eyes_close_col)
        self.NinebtnPointFive.configure(bg=self.eyes_close_col)
        self.NinebtnPointTen.configure(bg=self.eyes_close_col)
        self.NinebtnPointTwenty.configure(bg=self.eyes_close_col)

        #self.waithere_2(70)

        self.TwobtnPointOne.configure(bg=self.eyes_close_col)
        self.TwobtnPointFive.configure(bg=self.eyes_close_col)
        self.TwobtnPointTen.configure(bg=self.eyes_close_col)
        self.TwobtnPointTwenty.configure(bg=self.eyes_close_col)

        self.TenbtnPointOne.configure(bg=self.eyes_close_col)
        self.TenbtnPointFive.configure(bg=self.eyes_close_col)
        self.TenbtnPointTen.configure(bg=self.eyes_close_col)
        self.TenbtnPointTwenty.configure(bg=self.eyes_close_col)

        #self.waithere_2(70)

        self.ThreebtnPointOne.configure(bg=self.eyes_close_col)
        self.ThreebtnPointFive.configure(bg=self.eyes_close_col)
        self.ThreebtnPointTen.configure(bg=self.eyes_close_col)
        self.ThreebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.ElevenbtnPointOne.configure(bg=self.eyes_close_col)
        self.ElevenbtnPointFive.configure(bg=self.eyes_close_col)
        self.ElevenbtnPointTen.configure(bg=self.eyes_close_col)
        self.ElevenbtnPointTwenty.configure(bg=self.eyes_close_col)

        #self.waithere_2(70)

        self.FourbtnPointOne.configure(bg=self.eyes_close_col)
        self.FourbtnPointFive.configure(bg=self.eyes_close_col)
        self.FourbtnPointTen.configure(bg=self.eyes_close_col)
        self.FourbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.TwelvebtnPointOne.configure(bg=self.eyes_close_col)
        self.TwelvebtnPointFive.configure(bg=self.eyes_close_col)
        self.TwelvebtnPointTen.configure(bg=self.eyes_close_col)
        self.TwelvebtnPointTwenty.configure(bg=self.eyes_close_col)

        #self.waithere_2(70)

        self.FivebtnPointOne.configure(bg=self.eyes_close_col)
        self.FivebtnPointFive.configure(bg=self.eyes_close_col)
        self.FivebtnPointTen.configure(bg=self.eyes_close_col)
        self.FivebtnPointTwenty.configure(bg=self.eyes_close_col)

        self.ThirteenbtnPointOne.configure(bg=self.eyes_close_col)
        self.ThirteenbtnPointFive.configure(bg=self.eyes_close_col)
        self.ThirteenbtnPointTen.configure(bg=self.eyes_close_col)
        self.ThirteenbtnPointTwenty.configure(bg=self.eyes_close_col)

        #self.waithere_2(70)

        self.SixbtnPointOne.configure(bg=self.eyes_close_col)
        self.SixbtnPointFive.configure(bg=self.eyes_close_col)
        self.SixbtnPointTen.configure(bg=self.eyes_close_col)
        self.SixbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.FourteenbtnPointOne.configure(bg=self.eyes_close_col)
        self.FourteenbtnPointFive.configure(bg=self.eyes_close_col)
        self.FourteenbtnPointTen.configure(bg=self.eyes_close_col)
        self.FourteenbtnPointTwenty.configure(bg=self.eyes_close_col)

        #self.waithere_2(70)

        self.SevenbtnPointOne.configure(bg=self.eyes_close_col)
        self.SevenbtnPointFive.configure(bg=self.eyes_close_col)
        self.SevenbtnPointTen.configure(bg=self.eyes_close_col)
        self.SevenbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.FifteenbtnPointOne.configure(bg=self.eyes_close_col)
        self.FifteenbtnPointFive.configure(bg=self.eyes_close_col)
        self.FifteenbtnPointTen.configure(bg=self.eyes_close_col)
        self.FifteenbtnPointTwenty.configure(bg=self.eyes_close_col)

        self.EightbtnPointFive.configure(bg='black')
        self.EightbtnPointTen.configure(bg='black')
        self.EightbtnPointTwenty.configure(bg='black')

        self.SixteenbtnPointOne.configure(bg='black')
        self.SixteenbtnPointFive.configure(bg='black')
        self.SixteenbtnPointTen.configure(bg='black')




if __name__ == '__main__':
    root = Tk()
    application = studentRecords(root)
    root.mainloop()
