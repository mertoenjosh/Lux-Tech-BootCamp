#! /usr/bin/python3

# importing of libraries
from tkinter import *
from pytube import YouTube

root =Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Downloader")

Label(root, text = 'Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here: ', font='arial 15 bold').place(x=160, y=60)
text_box = Entry(root, width = 50, textvariable = link).place(x = 32, y = 100)

def download():
    url = YouTube(str(link.get()))
    video = url.streams.get_by_resolution("720p")
    video.download()
    Label(root, text = 'DOWNLOADED', font='arial 15').place(x=180, y=210)

Button(root,text = 'DOWNLOAD', font='arial 15 bold', bg='skyblue', padx = 2, command = download).place(x = 180, y = 150)

root.mainloop()

