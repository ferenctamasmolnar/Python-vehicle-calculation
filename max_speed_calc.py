import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
from tkinter import messagebox
from tkinter import ttk

def validate_entry(text):
    return text.isdecimal()

# Tkinter initialization
root = tk.Tk()
root.geometry('1200x900')
root.title("Max Speed Calculation App")

# Set background color for the window
root.configure(bg='#f0f0f0')

fig, ax = plt.subplots()

# Frame to hold the plot
frame = tk.Frame(root, bg='#f0f0f0')
label = tk.Label(root, text="Max Speed Calculation", font=('Helvetica', 18, 'bold'), bg='#f0f0f0', fg='#333333')
label.pack(pady=20)

# Canvas for the plot
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=22, pady=10)

frame.place(relx=0.27, rely=0.1, anchor='n', width=650, height=400)

ax.set_xlabel("Axle speed [n]")
ax.set_ylabel("Axle Torque [Nm]")
ax.set_title("Performance curve plot")
ax.legend()

def button_clicked():
    fn = askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if fn:
        try:
            dataframe1 = pd.read_excel(fn)
            print(dataframe1)
            
            # Clear previous text
            T.delete(1.0, tk.END)
            T.insert(tk.END, dataframe1)
            
            # Check if there are enough columns to plot
            if dataframe1.shape[1] >= 2:
                ax.clear()
                ax.plot(dataframe1.iloc[:, 0], dataframe1.iloc[:, 1], label="Motor Torque")
                ax.plot(dataframe1.iloc[:, 0], dataframe1.iloc[:, 2], label="Generator Torque")
                ax.set_xlabel("Axle speed [n]")
                ax.set_ylabel("Axle Torque [Nm]")
                ax.set_title("Performance curve plot")
                ax.legend()
                canvas.draw()  # Update the plot
            else:
                T.insert(tk.END, "\nError: The Excel file should have at least two columns of data.")
        except Exception as e:
            print(f"Error reading file: {e}")
            T.insert(tk.END, "Failed to load file.\n")

# Text widget to display the content of the DataFrame
T = tk.Text(root, height=15, width=40, font=('Helvetica', 12), bg='#f5f5f5', fg='#333333', relief=tk.SUNKEN, bd=2)
T.place(relx=0.27, rely=0.65, anchor='n')

# Button to load the file
button = tk.Button(root, text="Import Excel File", command=button_clicked, font=('Helvetica', 14), bg='#4CAF50', fg='white', relief=tk.RAISED, bd=3)
button.place(relx=0.27, rely=0.55, anchor='n', width=200)

#parameters
def submit(): 
    # Get the input from both text boxes 
    vmass = entry1.get() 
    wradius = entry2.get()
    farea = entry3.get() 
    dragcoeff = entry4.get() 
    rollres = entry5.get() 
    gratio = entry6.get() 
    weightfa = entry7.get() 
    weightra = entry8.get() 
    cog = entry9.get() 
    wheelb = entry10.get()  

# Create the first label and text box 
label1 = tk.Label(root, text="Vehicle mass:",font=('Helvetica', 10, 'bold')) 
label1.place(relx=0.65, rely = 0.1, anchor='n') 
entry1 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry1.insert(0,"1200")  
entry1.place(relx=0.65, rely = 0.125, anchor = 'n')
 
# Create the second label and text box 
label2 = tk.Label(root, text="Tire w:",font=('Helvetica', 10, 'bold')) 
label2.place(relx=0.65, rely = 0.15, anchor = 'n') 
entry2 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry),"%S"))
entry2.insert(0,float("0.352")) 
entry2.place(relx=0.65, rely = 0.175, anchor = 'n') 
 
label3 = tk.Label(root, text="Frontal area:",font=('Helvetica', 10, 'bold')) 
label3.place(relx=0.65, rely = 0.2, anchor='n') 
entry3 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry3.insert(0,"2.713") 
entry3.place(relx=0.65, rely = 0.225, anchor='n')

label4 = tk.Label(root, text="Drag:",font=('Helvetica', 10, 'bold')) 
label4.place(relx=0.65, rely = 0.25, anchor='n') 
entry4 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry4.insert(0,"0.313") 
entry4.place(relx=0.65, rely = 0.275, anchor='n')

label5 = tk.Label(root, text="Rolling:",font=('Helvetica', 10, 'bold')) 
label5.place(relx=0.65, rely = 0.3, anchor='n') 
entry5 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry5.insert(0,"0.008") 
entry5.place(relx=0.65, rely = 0.325, anchor='n')

label6 = tk.Label(root, text="Gear ratio:",font=('Helvetica', 10, 'bold')) 
label6.place(relx=0.85, rely = 0.1, anchor='n') 
entry6 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry6.insert(0,"1") 
entry6.place(relx=0.85, rely = 0.125, anchor='n')

label7 = tk.Label(root, text="Weight on front axle:",font=('Helvetica', 10, 'bold')) 
label7.place(relx=0.85, rely = 0.15, anchor='n') 
entry7 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry7.insert(0,"48") 
entry7.place(relx=0.85, rely = 0.175, anchor='n')

label8 = tk.Label(root, text="Weight on rear axle:",font=('Helvetica', 10, 'bold')) 
label8.place(relx=0.85, rely = 0.2, anchor='n') 
entry8 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry8.insert(0,"52") 
entry8.place(relx=0.85, rely = 0.225, anchor='n')

label9 = tk.Label(root, text="CoG:",font=('Helvetica', 10, 'bold')) 
label9.place(relx=0.85, rely = 0.25, anchor='n') 
entry9 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry9.insert(0,"0.51") 
entry9.place(relx=0.85, rely = 0.275, anchor='n')

label10 = tk.Label(root, text="Wheelbase:",font=('Helvetica', 10, 'bold')) 
label10.place(relx=0.85, rely = 0.3, anchor='n') 
entry10 = tk.Entry(root,justify='center',validate="key",
    validatecommand=(root.register(validate_entry), "%S"))
entry10.insert(0,"2.89") 
entry10.place(relx=0.85, rely = 0.325, anchor='n')

# Create a submit button 
submit_button = tk.Button(root, text="Submit", command=submit,font=('Helvetica', 14), bg='#4CAF50', fg='white', relief=tk.RAISED, bd=3) 
submit_button.place(relx=0.75, rely = 0.4, anchor = 'n')

label11 = tk.Label(root, text="Parameters",font=('Helvetica', 16, 'bold'))
label11.place(relx=0.75, rely = 0.06, anchor='n')  

def on_closing():
    print("Closing the program...")
    root.quit()  # Closes the Tkinter main loop
    root.destroy()  # Destroys the Tkinter window
    sys.exit()  # Exits the entire program

# Bind the window close button (X) to the custom on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
