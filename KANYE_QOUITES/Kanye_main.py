from tkinter import *
import requests
response={}
bg = "#E8630A"
def get_qoutes():
    global response
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    Quotes = response.json()["quote"]
    canavs.itemconfig(text,text=Quotes)

window = Tk()
window.title("Kanye qoutes")
window.config(padx=50,pady=50,bg=bg)
canavs = Canvas(width=300,height=414)
canavs.config(bg=bg,highlightthickness=0)
bg_Img_file = PhotoImage(file="background.png")
canavs.create_image(150,207,image=bg_Img_file)
text = canavs.create_text(150,207,text="Quotes",width=250,font=("Arial",20,"bold"))
canavs.grid(row=0,column=0)

button_img_file = PhotoImage(file="kanye.png")
button = Button(image=button_img_file,highlightthickness=0,bg=bg,command=get_qoutes)
button.grid(row=1,column=0)
window.mainloop()