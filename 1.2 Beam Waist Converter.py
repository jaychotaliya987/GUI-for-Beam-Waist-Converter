from tkinter import *
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import customtkinter as ctk


############################ ----CALCULATION PART---- #################################################
FWHM_1 = 0
RMS_1 = 0
esq_1 = 0

# Define the conversions
def FWHM_to_RMS(FWHM):
    """RMS = FWHM/1.55"""
    return FWHM / (1.55)

def FWHM_to_esq(FWHM):
    """esq = FWHM/1.17"""
    return FWHM * 0.15

def RMS_to_FWHM(RMS):
    """FWHM = RMS * 1.55"""
    return RMS * 1.55

def RMS_to_esq(RMS):
    """esq = RMS * 1.324"""
    return RMS * (1.324)

def esq_to_FWHM(esq):
    """FWHM = esq * 1.17"""
    return esq * 1.17

def esq_to_RMS(esq):
    """RMS = esq / 1.324"""
    return esq / 1.324



def is_float_or_int(x):
  """Returns True if x is a float or an integer, False otherwise"""
  try:
    float(x)
    return True
  except:
    return False
  

#get the user input and store it in the variable

def UI_FWHM():
    """Returns the user input for FWHM"""
    try:
        # Check if the input is a number
        if is_float_or_int(text1.get()):
            # Convert the input to float
            FWHM = float(text1.get())
            # Return the input
            return FWHM
        else:
            # Display an error message
            print("Please enter a valid number for FWHM")
            # Return zero
            return 0
    except ValueError:
        # Display an error message
        print("Please enter a valid number for FWHM")
        return 0

def UI_RMS():
    """Returns the user input for RMS"""
    try:
        # Check if the input is a number
        if is_float_or_int(text2.get()):
            # Convert the input to float
            RMS = float(text2.get())
            # Return the input
            return RMS
        else:
            # Display an error message
            print("Please enter a valid number for RMS")
            return 0
    except ValueError:
        # Display an error message
        print("Please enter a valid number for RMS")
        return 0

def UI_esq():
    """Returns the user input for esq"""
    try:
        # Check if the input is a number
        if is_float_or_int(text3.get()):
            # Convert the input to float
            esq = float(text3.get())
            return esq
        else:
            # Display an error message
            print("Please enter a valid number for esq")
            return 0       
    except ValueError:
        # Display an error message
        print("Please enter a valid number for esq")
        return 0


def Calculations():
    """Updates the GUI with calculated values based on user input"""
    


    if FWHM_1 == 1:
        FWHM = UI_FWHM()

        # Calculate RMS and esq from FWHM
        RMS = FWHM_to_RMS(FWHM)
        esq = FWHM_to_esq(FWHM)
        
        # Delete previous values in other text boxes
        text2.delete(0, "end")
        text3.delete(0, "end")
        
        # Insert calculated values in other text boxes
        text2.insert(1, RMS)
        text3.insert(2, esq)
        

    if RMS_1 == 1:
        RMS = UI_RMS()

        # Calculate FWHM and esq from RMS
        FWHM = RMS_to_FWHM(RMS)
        esq = RMS_to_esq(RMS)
            
        # Delete previous values in other text boxes
        text1.delete(0, "end")
        text3.delete(0, "end")
            
        # Insert calculated values in other text boxes
        text1.insert(0, FWHM)
        text3.insert(2, esq)
            
          
    if esq_1 == 1:
        esq = UI_esq()

                
        # Calculate FWHM and RMS from esq
        FWHM = esq_to_FWHM(esq)
        RMS = esq_to_RMS(esq)
                
        # Delete previous values in other text boxes
        text1.delete(0, "end")
        text2.delete(0, "end")
        # Insert calculated values in other text boxes
        text1.insert(0, FWHM)
        text2.insert(1, RMS)
    
# Create a function to clear all values when reset button is clicked            
def Reset():
    """Clears all values and enables all text boxes"""
    
    # Delete all values in all text boxes 
    text1.delete(0, "end")
    text2.delete(0, "end")
    text3.delete(0, "end")
    
    # Enable all text boxes 
    text1.config(state="normal")
    text2.config(state="normal")
    text3.config(state="normal")

# Create a function to update GUI every second using after() method   
def Update():
    """Updates GUI every second"""
    Calculations()
    root.after(100, Update)

###########################################-----GRAPHS------#######################################################################


def gaussian(A, x, mu, sig):
	return A * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def plot():
    """Plot Gaussian distribution based on user input"""
    FWHM = UI_FWHM()
    RMS = UI_RMS()
    esq = UI_esq()
    A = 2*FWHM
    mu = FWHM / 2.355  # Calculate mu from FWHM
    sig = FWHM / (2 * 2.355)  # Calculate sigma (std. deviation) from FWHM

    x = np.linspace(mu - 3 * sig, mu + 3 * sig, 100)
    y = gaussian(A, x, mu, sig)

    # Create a frame to contain the figure
    plot_frame = ctk.CTkFrame(master=root)
    plot_frame.grid(row=3, column=1, padx=10, pady=10)

    fig = Figure(figsize=(5, 5), dpi=110)
    plot1 = fig.add_subplot(111)
    line_FWHM = np.zeros(100) + FWHM
    line_esq = np.zeros(100) + esq
    line_RMS = np.zeros(100) + RMS
 
    for i in range (len(y)):
        if y[i] < line_FWHM [i] :
            line_FWHM[i] = np.nan
        if y[i] < line_esq [i] :
            line_esq[i] = np.nan
        if y[i] < line_RMS [i] :
            line_RMS[i] = np.nan
    
    xlabel = "Distance (mm)"
    ylabel = "Intensity (W/m^2)"
    title = "Gaussian Beam Profile"

    plot1.set_xlabel(xlabel)
    plot1.set_ylabel(ylabel)
    plot1.set_title(title)
    plot1.grid(True)
    
    plot1.plot(x, line_FWHM, label = "FWHM", color = "red")
    plot1.plot(x, line_esq, label = "1/e^2", color = "green")
    plot1.plot(x, line_RMS, label = "RMS", color = "orange")
    plot1.plot(x, y, label = "Gaussian", linewidth = 2)
    plot1.legend()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Create the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, plot_frame)
    toolbar.update()
    canvas.get_tk_widget().pack()


############################ ----GUI PART---- #################################################



# Create a root window
root = ctk.CTk()
ctk.set_default_color_theme("green")

#set icon
photo = PhotoImage(file = "/home/raged_pi/Physics/Masters/SoSe 2023/Ultra Short 2023/GUI/logo.png")
root.iconphoto(False, photo)

# Set the title of the window
root.title ("GUI for Beam Waist Converter")

# Create a label
label = ctk.CTkLabel(root, text="Enter The Value Of Any One Beam Waist Parameter", font= ('Arial', 22))

# Creating label for Textboxes
label1 = ctk.CTkLabel(root, text="FWHM (mm)", font= ('Arial', 18))
label2 = ctk.CTkLabel(root, text="RMS (mm)", font= ('Arial', 18))
label3 = ctk.CTkLabel(root, text="1/e^2 (mm)", font= ('Arial', 18))

# Create three text boxes with default values 
text1 = ctk.CTkEntry(root, width=250,
                               corner_radius=2, justify = "center")
text2 = ctk.CTkEntry(root, width=250,
                               corner_radius=2, justify = "center")
text3 = ctk.CTkEntry(root, width=250,
                               corner_radius=2, justify = "center")

text1.insert( 0, "Enter The Value Of FWHM")
text2.insert( 1, "Enter The Value Of RMS")
text3.insert( 2, "Enter The Value Of 1/e^2")

# Create two buttons: one for reset and one for exit 
button_reset = ctk.CTkButton(root, text= "Reset", command = Reset ,font = ('Arial', 18) )
button_exit = ctk.CTkButton(root, text= "Exit", command = root.destroy ,font = ('Arial', 18) )
button_plot = ctk.CTkButton(master = root,command = plot,text = "Plot",font = ('Arial', 18))


label.grid(row=0, column=0, columnspan=3, padx=50, pady=20)
root.grid_columnconfigure(0, weight=10)
root.grid_columnconfigure(1, weight=10)
root.grid_columnconfigure(2, weight=10)

label1.grid(row=1, column=0, padx=20, pady=5)
label2.grid(row=1, column=1, padx=20, pady=5)
label3.grid(row=1, column=2, padx=20, pady=5)

text1.grid(row=2, column=0, padx=20, pady=5)
text2.grid(row=2, column=1, padx=20, pady=5)
text3.grid(row=2, column=2, padx=20, pady=5)


#button_calculate.grid(row=3, column=1)
button_reset.grid(row=4, column=0,padx=20, pady=20)
button_exit.grid(row=4,column=2, padx=20, pady=20)
button_plot.grid(row=4, column=1, padx=20, pady=20)

# Create a function to clear the text boxes when they are clicked
def clear_text1(event):
    global FWHM_1
    global RMS_1
    global esq_1
    text1.delete(0, "end")

    FWHM_1 = TRUE
    RMS_1 = FALSE
    esq_1 = FALSE

def clear_text2(event):
    global FWHM_1
    global RMS_1
    global esq_1
    text2.delete(0, "end")
    FWHM_1 = FALSE
    RMS_1 = TRUE
    esq_1 = FALSE

def clear_text3(event):
    global FWHM_1
    global RMS_1
    global esq_1
    text3.delete(0, "end")
    FWHM_1 = FALSE
    RMS_1 = FALSE
    esq_1 = TRUE
    

# Bind the functions to the left mouse button click events
text1.bind("<Button-1>", clear_text1)
text2.bind("<Button-1>", clear_text2)
text3.bind("<Button-1>", clear_text3)

Update()

# Start the main loop 
root.mainloop()
