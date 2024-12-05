import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk


root = tk.Tk()

Height = 400
Width = 500

def test_fun(entry):
    # print("button clicked!")
    print("This is your entry:",entry)

#b924c900d4912ff6771ccedd2080b8d3
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try: 
        name = (weather['name'])
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp'] 
        country = weather['sys']['country'] 
        final_Str = 'City: %s \nConditions: %s \nTemperature(°C): %s \nCountry: %s' %(name,desc,temp,country)
    except:
          final_Str ="There is no city exist with this name!"
    
    return final_Str

def get_weather(city):
    weather_key = "b924c900d4912ff6771ccedd2080b8d3"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key,'q':city,'units': 'metric'}
    response = requests.get(url,params=params)
    weather = response.json()
    # print("\n\n\n\n\nYour country is\n\n\n\n",weather['sys']['country'])
    label['text'] = format_response(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img



canvas = tk.Canvas(root,height=Height,width=Width)
bg_image = tk.PhotoImage(file="landscape.png")
bg_lable = tk.Label(root,image=bg_image)
bg_lable.place(relx=0,relheight=1,relwidth=1)
canvas.pack()


frame = tk.Frame(root,bg="#ffe6b3",bd=5) 
# frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.6)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")

entry = tk.Entry(frame,font=('Cascadia Mono',15))
# entry.pack()
# entry.place(relx=0.8,rely=0,relheight=0.25,relwidth=0.29)
entry.place(relheight=1,relwidth=0.65)

# button = tk.Button(frame,text="Test button",fg="blue",bg="gray")
# button.pack()
# button.place(relx=0,rely=0,relheight=0.25,relwidth=0.23)
button = tk.Button(frame,text="Get Weather",font=('Cascadia Mono',8),command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root,bg="#ffe6b3",bd=5)
lower_frame.place(relx=0.5,rely=0.27,relwidth=0.75,relheight=0.5,anchor="n") 

label = tk.Label(lower_frame,font=('Cascadia Mono',14),anchor='nw',justify='left',bd=5,bg='white')
label.place(relheight=1,relwidth=1)


weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)




# label = tk.Label(frame,text="This is your label",bg="#1affc6",fg="#ff3385")
# label.pack()
#label.grid(row=0,column=0)
# label.place(relx=0.3,rely=0,relheight=0.25,relwidth=0.42)


# print(tk.font.families())

root.mainloop()