from tkinter import *
import tkinter as tk
# from geopy.geocoders import Nominatim
from tkinter import messagebox
# from timezonefinder import TimezoneFinder
# from datetime import datetime
import requests
# import pytz

# Create the main window
root = Tk()
root.title("Weather App")
root.geometry('900x500+300+200')
root.resizable(False, False)

# OpenWeather API Key (Replace with your API key)
API_KEY = "d491d7bcda9b09a6125db80558ded812"

def getWeather():
    city = text_field.get()

    if not city:
        messagebox.showwarning("Warning", "Please enter a city name!")
        return        
        # Fetch weather data
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
            # Extract necessary details
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        pressure = weather_data["main"]["pressure"]
        description = weather_data["weather"][0]["description"]

            # Display data in labels
        t.config(text=f"{temperature}°C")
        h.config(text=f"{humidity}%")
        w.config(text=f"{wind_speed} m/s")
        p.config(text=f"{pressure} hPa")
        d.config(text=description.capitalize())
    else:
        messagebox.showerror("Error", "Weather data not found!")

# inserting and deleting default text from input field 
def on_entry_click(event):
    if text_field.get() == "Enter City Name":
        text_field.delete(0, tk.END)  # Remove placeholder text
        text_field.config(fg="white")  # Change text color to white

def on_focus_out(event):
    if text_field.get() == "":
        text_field.insert(0, "Enter City Name")  # Restore placeholder
        text_field.config(fg="grey")  # Change text color to grey


# Search Box
search_image = PhotoImage(file='copy of search.png')
myImage = Label(root, image=search_image)
myImage.place(x=20, y=20)

text_field = tk.Entry(root, justify='center', width=17, font=('poppins', 25, 'bold'), bg="#404040", border=0, fg='white')
text_field.place(x=50, y=40)
text_field.bind("<FocusIn>", on_entry_click)  # Remove placeholder when clicked
text_field.bind("<FocusOut>", on_focus_out)  # Restore placeholder if empty
text_field.focus()

search_icon = PhotoImage(file='copy of search_icon.png')
myImage_Icon = Button(root, image=search_icon, borderwidth=0, cursor='hand2', bg='#404040', command=getWeather)
myImage_Icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file='copy of logo.png')
logo = Label(root, image=logo_image)
logo.place(x=150, y=100)

# Button Box
frame_Image = PhotoImage(file='copy of box.png')
frame_Myimage = Label(root, image=frame_Image)
frame_Myimage.pack(padx=5, pady=5, side=BOTTOM)

# Labels
label1 = Label(root, text='WIND', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(root, text='HUMIDITY', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=240, y=400)

label3 = Label(root, text='DESCRIPTION', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=420, y=400)

label4 = Label(root, text='PRESSURE', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)

t = Label(root, font=('arial', 70, 'bold'), fg='#ee666d')
t.place(x=400, y=150)

c = Label(root, font=('arial', 15, 'bold'))
c.place(x=400, y=250)

w = Label(root, text='.....', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=120, y=430)

h = Label(root, text='.....', font=('arial', 20, 'bold'), bg='#1ab5ef')
h.place(x=280, y=430)

d = Label(root, text='.....', font=('arial', 20, 'bold'), bg='#1ab5ef')
d.place(x=450, y=430)

p = Label(root, text='.....', font=('arial', 20, 'bold'), bg='#1ab5ef')
p.place(x=670, y=430)

root.mainloop()
