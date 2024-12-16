import tkinter
import pyshorteners

#define root window
root = tkinter.Tk()
root.title('shortener app')
root.geometry("500x200")

#functions to used in buttons
def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url_entry.get())
    
    print(short_entry.insert(0,short_url))
def clean_entry():
    url_entry.delete(0, tkinter.END) 
    short_entry.delete(0,tkinter.END) # Limpia el contenido del Entry
    

#define the label,buttons,text_entry
url_label = tkinter.Label(root,text='Enter the URL')
url_entry = tkinter.Entry(root)
short_label = tkinter.Label(root,text='your short url')
short_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root,text='Short URL',command=shorten)
clear_entry_url = tkinter.Button(root,text='clear',command=clean_entry)


#packing all elements 
url_label.pack()
url_entry.pack()
short_label.pack()
short_entry.pack()
shorten_button.pack()
clear_entry_url.pack()



#loop for window still open
root.mainloop()