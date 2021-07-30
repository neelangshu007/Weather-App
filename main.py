from tkinter import *
from PIL import ImageTk, Image
import requests


# Formatting display text
def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_str = 'City: %s \nCondition: %s \nTemperature (°C): %s' % (name, description, temperature)
        icon_name = weather['weather'][0]['icon']
        display['text'] = final_str
        open_image(icon_name)

    except:
        final_str = 'Problem in retrieving information'
        display['text'] = final_str


# Getting Weather info Function
def get_weather(city):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"  # Rapidapi Weather URL

    params = {"q": city, "units": "metric"}  # Parameters/Queries to search for

    headers = {
        'x-rapidapi-key': "9d4ab43b98msh1e3040e5fa2244ep1f64c5jsn28dad4e5c37d",  # Api Key
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"  # Api Host
    }

    response = requests.request("GET", url, headers=headers, params=params)  # Response form the website through api

    weather = response.json()  # json object {dict}
    # print(type(weather))
    # print(response.json())
    format_response(weather)


# Open Image Function
def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


root = Tk()
root.title("Weather App")  # GUI Name
root.iconbitmap("assests/sun_icon.ico")  # GUI Icon

# Background Image
background_image = ImageTk.PhotoImage(Image.open("assests/appbg.jpeg"))

# Background Label
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Size of the window
root.geometry("800x700")

# Top Frame containing input\entry field and search button
top_frame = Frame(root, bg="#EAFC03", bd=5)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Entry box for get weather info
input_field = Entry(top_frame, font=('Helvetica', 20))
input_field.place(relwidth=0.67, relheight=1)

# Search Button
button = Button(top_frame, text="Get Weather", font=('Helvetica', 15), command=lambda: get_weather(input_field.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# Lower Frame containing display area and canvas
lower_frame = Frame(root, bg="#EAFC03", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

# Display area for current weather info
bg_color = 'white'
display = Label(lower_frame, font=('Helvetica', 25), bg=bg_color, bd=4)
display.place(relwidth=1, relheight=1)

# Canvas containing the current weather icon/image
weather_icon = Canvas(display, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
