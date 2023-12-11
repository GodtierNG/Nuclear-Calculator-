#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:37:47 2023

@author: alinegahdar
"""
# import the tkinter interface
import tkinter as tk
from tkinter import messagebox


# calculate the effiecny, fuel mass and power per fuel of diffrent reactors the function mainly takes an input value in Mega watts  and then creates an output in watts for the further calculations

def calculate_eff():
    try:
        thermal_p_out = float(thermal_p_in.get()) * 1e6  # Convert MW to W for numerical reasons this part is the input of the thermal output of a reactor 
        
        electrical_p_out = float(electrical_p_in.get()) * 1e6  # Convert MW to W electrical power generated in the proccess
        fuel_mass = float(fuel_mass_in.get()) * 1e4  # Convert 10^4 kg to kg the amount of fuel going to the reactor can be caluclated by this in watts 
        number_of_fuel_rods = float(rods_in.get()) * 1e4  # Convert 10^4 to actual number
        enrichment_value = float(enrichment_in.get()) # percent of the enriched uranium atom

        efficiency = (electrical_p_out / thermal_p_out) * 100 # get the eff by dividing the electricity  thermal output by the  thermal generated 
        mass_uranium_235 = fuel_mass * (enrichment_value / 100) # calculate the mass of uranim based on the totall fuel mass and the enriched amount 
        power_per_fuel_rod = electrical_p_out / number_of_fuel_rods

        # Update the labels with the calculated data all to 2 sf 
        efficiency_label.config(text=f"Efficiency: {efficiency:.2f}%") #efficiency in percent 
        uranium_mass_label.config(text=f"Mass of Uranium-235: {mass_uranium_235:.2f} kg") # mass lable for uranium 
        power_per_rod_label.config(text=f"Power per Fuel Rod: {power_per_fuel_rod:.2f} W") # power rod lables 
        
# raise an error if an invalid number is enterd or a number which cant be calculated raise an error message 
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid number in the box.")


# main window pop
root = tk.Tk()
root.title("Nuclear Reactor calculator ")

# Define the labels and define the entry for the user 

# lable and entry for thermal power 
tk.Label(root, text="Thermal Power Output (MW):").grid(row=0, column=0)
thermal_p_in = tk.Entry(root)
thermal_p_in.grid(row=0, column=1)
thermal_p_in.insert(0, "4200")

# lable and entery for the electrical power generated 

tk.Label(root, text="Electrical Power Output (MW):").grid(row=1, column=0)
electrical_p_in = tk.Entry(root)
electrical_p_in.grid(row=1, column=1)
electrical_p_in.insert(0, "1000")


#  lable and entery for the Fuel mass 
tk.Label(root, text="Fuel Mass (10^4 kg):").grid(row=2, column=0)
fuel_mass_in = tk.Entry(root)
fuel_mass_in.grid(row=2, column=1)
fuel_mass_in.insert(0, "8.60")


# lable and entry for number of fuel rods
tk.Label(root, text="Number of Fuel Rods (10^4):").grid(row=3, column=0)
rods_in = tk.Entry(root)
rods_in.grid(row=3, column=1)
rods_in.insert(0, "2.70")

#lable and entery for the percnt of entriched U 235
tk.Label(root, text="Enrichment (% Uranium-235):").grid(row=4, column=0)
enrichment_in = tk.Entry(root)
enrichment_in.grid(row=4, column=1)
enrichment_in.insert(0, "5")




# Button for performing the calculations 
calculate_button = tk.Button(root, text="Calculate", command=calculate_eff)
calculate_button.grid(row=5, column=0, columnspan=2)

# Labels to display the results for the calculation of the eff Mass of uranium and power per each fuel rod  
efficiency_label = tk.Label(root, text="Efficiency: ")
efficiency_label.grid(row=6, column=0, columnspan=2)

uranium_mass_label = tk.Label(root, text="Mass of Uranium-235: ")
uranium_mass_label.grid(row=7, column=0, columnspan=2)

power_per_rod_label = tk.Label(root, text="Power per Fuel Rod: ")
power_per_rod_label.grid(row=8, column=0, columnspan=2)

# Start the main loop
root.mainloop()
