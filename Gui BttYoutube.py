import tkinter as tk
from tkinter import *
from pytube import YouTube
import os

def Download_Video():     
 
  yt =YouTube(str(link.get()))

  video = yt.streams.filter(only_audio=True).first()
  out_file = video.download(output_path=".")
  base, ext = os.path.splitext(out_file)

  new_file = base + '.mp3'
  os.rename(out_file, new_file)
  tk.Label(window, text = 'hawka tsab f nafes blasa li feha ena !', font = 'arial 15',fg="White",bg="#EC7063").place(x= 10 , y = 140)  

window = tk.Tk()
window.geometry("600x200")
window.config(bg="white")
window.resizable(width=False,height=False)
window.title('Ahmed-Btt YouTube Downloader')
 
link = tk.StringVar()
tk.Label(window,text = '               Ahmed-Btt YouTube Downloader              ', font ='arial 20 bold',fg="White",bg="Black").pack()
tk.Label(window, text = '7ot lena adresse mte3 video w asber chwy :', font = 'arial 20 bold',fg="Black",bg="#EC7063").place(x= 5 , y = 60)
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="lightgreen").place(x = 5, y = 100)
tk.Button(window,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=385 ,y = 140)
 
window.mainloop()
