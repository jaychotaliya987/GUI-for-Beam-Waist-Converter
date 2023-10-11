from tkinter import *


############################ ----CALCULATION PART---- #################################################


# Define the conversions

def FWHM_to_RMS(FWHM):
    """Converts FWHM to RMS"""
    return FWHM * 0.6

def FWHM_to_esq(FWHM):
    """Converts FWHM to esq"""
    return FWHM * 1.177

def esq_to_RMS(esq):
    """Converts esq to RMS"""
    return esq * 0.6

def esq_to_FWHM(esq):
    """Converts esq to FWHM"""
    return esq / 0.6

def RMS_to_FWHM(RMS):
    """Converts RMS to FWHM"""
    return RMS / 0.6

def RMS_to_esq(RMS):
    """Converts RMS to esq"""
    return RMS / (0.6 * 1.77)


def is_float_or_int(x):
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
        # Return zero
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
            # Return zero
            return 0
    except ValueError:
        # Display an error message
        print("Please enter a valid number for RMS")
        # Return zero
        return 0

def UI_esq():
    """Returns the user input for esq"""
    try:
        # Check if the input is a number
        if is_float_or_int(text3.get()):
            # Convert the input to float
            esq = float(text3.get())
            # Return the input
            return esq
        else:
            # Display an error message
            print("Please enter a valid number for esq")
            # Return zero
            return 0
    except ValueError:
        # Display an error message
        print("Please enter a valid number for esq")
        # Return zero
        return 0


#if user input in text1(FWHM) then calculate the values of RMS and 1/e^2
def Calculations():
    """Updates the GUI with calculated values based on user input"""
    
    # Get the user input for FWHM
    FWHM = UI_FWHM()
    
    if FWHM > 0:
        # Disable other text boxes
        #text2.config(state="disabled")
        #text3.config(state="disabled")
        
        # Calculate RMS and esq from FWHM
        RMS = FWHM_to_RMS(FWHM)
        esq = FWHM_to_esq(FWHM)
        
        # Delete previous values in other text boxes
        text2.delete(0, "end")
        text3.delete(0, "end")
        
        # Insert calculated values in other text boxes
        text2.insert(1, RMS)
        text3.insert(2, esq)
        
    else:
        # Get the user input for RMS
        RMS = UI_RMS()
        
        if RMS > 0:
            # Disable other text boxes
            #text1.config(state="disabled")
            #text3.config(state="disabled")
            
            # Calculate FWHM and esq from RMS
            FWHM = RMS_to_FWHM(RMS)
            esq = RMS_to_esq(RMS)
            
            # Delete previous values in other text boxes
            text1.delete(0, "end")
            text3.delete(0, "end")
            
            # Insert calculated values in other text boxes
            text1.insert(0, FWHM)
            text3.insert(2, esq)
            
        else:
            # Get the user input for esq
            esq = UI_esq()
            
            if esq > 0:
                # Disable other text boxes
                #text1.config(state="disabled")
                #text2.config(state="disabled")
                
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
    
    root.after(1000, Update)


############################ ----GUI PART---- #################################################



# Create a root window
root = Tk()

# Set the title of the window
root.title ("GUI for Beam Waist Converter")

# Create a label
label = Label(root, text="Enter The Value Of Any One Beam Waist Parameter", font= ('Arial', 18))

# Creating label for Textboxes
label1 = Label(root, text="FWHM", font= ('Arial', 10))
label2 = Label(root, text="RMS", font= ('Arial', 10))
label3 = Label(root, text="1/e^2", font= ('Arial', 10))

# Create three text boxes with default values 
text1 = Entry(root, width=25)
text2 = Entry(root, width=25)
text3 = Entry(root, width=25)

text1.insert( 0, "Enter The Value Of FWHM")
text2.insert( 1, "Enter The Value Of RMS")
text3.insert( 2, "Enter The Value Of 1/e^2")

# Create two buttons: one for reset and one for exit 
button_reset = Button(root, text= "Reset", command = Reset ,font = ('Arial', 18))
button_exit = Button(root, text= "Exit", command = root.destroy ,font = ('Arial', 18))
button_calculate = Button(root, text= "Calculate", command = Calculations ,font = ('Arial', 18))

# Position the widgets using grid 

label.grid(row=0, column=0, columnspan=3)

label1.grid(row=1, column=0)
label2.grid(row=1, column=1)
label3.grid(row=1, column=2)

text1.grid(row=2, column=0)
text2.grid(row=2, column=1)
text3.grid(row=2, column=2)

button_reset.grid(row=3, column=0)
button_exit.grid(row=3,column=2)
#button_calculate.grid(row=3, column=1)

Update()
# Start the main loop 
root.mainloop()
