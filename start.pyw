from tkinter import *
import os
import webbrowser

path = "pics/logo.png"
parentwindow = Tk()
parentwindow.geometry('800x400')
parentwindow.title("HiOS Launcher")
parentwindow.iconbitmap("icons/house.ico")
parentwindow.configure(bg='black')
parentwindow.resizable(False, False)


#button1 = Button(parentwindow,width=20,font=("calibri",15),text="Launch HiOS(TM)",command=OpenUrl(url))

title = Label(parentwindow, text="Welcome to HiOS(tm) Launcher.", fg='white', bg='black', font=("Segoe UI", 30, 'bold'))
title.place(x=40, y=50)

subheading = Label(parentwindow, text="This program launches HiOS(tm) by The Highland Cafe(tm).", fg='white', bg='black', font=("Segoe UI", 10))
subheading.place(x=40, y=105)

launch_hios = Button(parentwindow, text="Launch HiOS(tm)", font=("Segoe UI", 13, 'bold', 'underline'), command=lambda: webbrowser.open('loading.html'), height="1", width="20")
launch_hios.place(x=40, y=150)

launch_staffportal = Button(parentwindow, text="Access Staff Portal", font=("Segoe UI", 13), command=lambda: webbrowser.open('staffportal_loading.html'), height="1", width="20")
launch_staffportal.place(x=280, y=150)

view_dev_website = Button(parentwindow, text="Visit our website", font=("Segoe UI", 9), command=lambda: webbrowser.open('https://sites.google.com/view/nuggetos'), width="13")
view_dev_website.place(x=40, y=360)

feedback = Button(parentwindow, text="Send Feedback", font=("Segoe UI", 9), command=lambda: webbrowser.open('https://forms.gle/5BREmSR8oziWtKrj8'), width="13")
feedback.place(x=150, y=360)

about_launcher = Button(parentwindow, text="About Program", font=("Segoe UI", 9), command=lambda: webbrowser.open('about_hios_launcher.html'), width="13")
about_launcher.place(x=260, y=360)

copyrt = Label(parentwindow, text="Copyright (c) The Highland Cafe(tm). All Rights Reserved", fg='white', bg='black')
copyrt.place(x=40, y=330)

parentwindow.mainloop()
