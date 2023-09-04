#https://kanye.rest/
#https://api.kanye.rest/
#{"quote":"My greatest pain in life is that I will never be able to see myself perform live."}
import requests
from tkinter import *

kanye_quote = requests.get(url="https://api.kanye.rest/")
quote = kanye_quote.json()["quote"]
print(quote)

def get_quote():
    kanye_quote = requests.get(url="https://api.kanye.rest/")
    quote = kanye_quote.json()["quote"]
    print(quote)

window = Tk()
window.title("Kanye Quote")
window.config(padx=50, pady=50)

canvas1 = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas1.create_image(150, 207, image=background_img)
background_image1 = PhotoImage(file="background.png")
canvas1.create_image(150, 207, image = background_image1)
quote_text = canvas1.create_text(150, 150 , text=quote,  width=250)
canvas1.grid(row=0, column=0)

window.mainloop()