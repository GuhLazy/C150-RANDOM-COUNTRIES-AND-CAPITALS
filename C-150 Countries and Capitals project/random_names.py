from tkinter import *
root = Tk()

root.title("Countries and Capitals")
root.geometry("500x500")

enter_countries= Entry(root)
enter_countries.place(relx=0.6, rely=0.4, anchor = CENTER)

enter_Capitals= Entry(root)
enter_Capitals.place(relx=0.6, rely=0.4, anchor = CENTER)

country_label = Label(root)
capital_label = Label(root)
random_country_label = Label(root)
random_city_label = Label(root)

country_list = Label(root)
city_list = Label()

country_list["text"] = "Country name: " + str(country_list)
city_list["text"] = "Country name: " + str(city_list)