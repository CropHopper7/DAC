
import tkinter as tk
import sqlite3
from tkcalendar import DateEntry
doctors = {
    "Medicine": ["Dr.J Ghosh", "Dr. P Kumar"],
    "Orthopedic": ["Dr.Tousif Ahamed", "Dr.B Dutta"],
    "Neurologist": ["Dr.T Paul", "Dr.R Melon"],
    "Gynaecologist": ["Dr.S Dey", "Dr.K Perry"],
    "ENT": ["Dr.R Tagore", "Dr.Sumit Ghosh"],
    "Dental": ["Dr.B P Boiragi", "Dr. Jessica Dutta"],
    "Cardiologist": ["Dr. William Shakespeare", "Dr. Emma Ghosh"]
}

def book_appointment():
    conn= sqlite3.connect("sqlite.db")
   # cursor = conn.cursor()
   # cursor.execute (insert into appoinment(patient_name , doctor_specialization, doctor_name , date, time))

    patient_name = name_entry.get()
    doctor_specialization = specialization_entry.get()
    doctor_name = doctor_entry.get()
    #date = date_entry.get()
    date = date_entry.get_date().strftime('%d-%m-%Y')
    time = time_entry.get()
    
    # Open new window
    appointment_window = tk.Toplevel(root)
    appointment_window.geometry("1200x500")
    appointment_window.title("Appointment Details")
    appointment_window.configure(background='steelblue')

    # Display appointment details
    appointment_label = tk.Label(appointment_window, text="Congratulations, you have successfully booked an appointment!", font=('Arial', 20), bg='steelblue', fg='white')
    appointment_label.pack(pady=(20, 30))

    # Create table to display appointment details
    table_frame = tk.Frame(appointment_window)
    table_frame.pack()

    # Add table headings
    heading_labels = ['Patient Name', 'Doctor Specialization', 'Doctor Name', 'Date', 'Time']
    for i, heading in enumerate(heading_labels):
        tk.Label(table_frame, text=heading, font=('Arial', 16, 'bold'), bg='lightblue', relief='solid', width=15, padx=10, pady=5).grid(row=0, column=i)

    # Add appointment details to table
    details = [patient_name, doctor_specialization, doctor_name, date, time]
    for i, detail in enumerate(details):
     tk.Label(table_frame, text=detail, font=('Arial', 14), bg='white', relief='solid', width=15, padx=10, pady=5).grid(row=1, column=i)
def update_doctors_options(*args):
        
    # Clear current doctor options
    doctor_menu["menu"].delete(0, "end")
    
    # Get selected specialization
    specialization = specialization_entry.get()

    # Get doctors for selected specialization
    specialization_doctors = doctors.get(specialization, [])

    # Add doctors to menu
    for doctor in specialization_doctors:
        doctor_menu["menu"].add_command(label=doctor, command=lambda doctor=doctor: doctor_entry.config(text=doctor))
    if not doctor_entry.get():
            doctor_entry.insert(0, doctor)
root = tk.Tk()
root.geometry("900x600")
root.title("Doctor Appointment")
root.configure(background='lightblue')

hospital_label = tk.Label(root, text="JIS CLINICS", font=('', 56, 'bold'), bg='steelblue')
hospital_label.pack()

input_frame = tk.Frame(root, bg='steelblue')
input_frame.pack(pady=30)

name_label = tk.Label(input_frame, text="Patient Name:", font=('Arial',25), bg='steelblue', anchor='w')
name_label.grid(row=0, column=0, padx=(30, 10), pady=10, sticky='w')

name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=(10, 30), pady=10)

doctor_label = tk.Label(input_frame, text="Doctor Name:", font=('Arial',25), bg='steelblue', anchor='w')
doctor_label.grid(row=2, column=0, padx=(30, 10), pady=10, sticky='w')

doctor_entry = tk.Entry(input_frame)
doctor_menu = tk.OptionMenu(input_frame, doctor_entry, "")
doctor_menu.grid(row=2, column=1, padx=(10, 30), pady=10)

specialization_label = tk.Label(input_frame, text="Doctor Specialization:", font=('Arial',25), bg='steelblue', anchor='w')
specialization_label.grid(row=1, column=0, padx=(30, 10), pady=10, sticky='w')

specialization_entry = tk.StringVar()
specialization_entry.set("Select Specialization")
specialization_menu = tk.OptionMenu(input_frame, specialization_entry, "Medicine", "Orthopedic", "Neurologist", "Gynaecologist", "ENT", "Dental", "Cardiologist")
specialization_menu.grid(row=1, column=1, padx=(10, 30), pady=10)

date_label = tk.Label(input_frame, text="Appointment Date:", font=('Arial',25), bg='steelblue', anchor='w')
date_label.grid(row=3, column=0, padx=(30, 10), pady=10, sticky='w')

#date_entry = tk.Entry(input_frame)
#date_entry.grid(row=3, column=1, padx=(10, 30), pady=10)
date_entry = DateEntry(input_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=3, column=1, padx=(10, 30), pady=10)

time_label = tk.Label(input_frame, text="Appointment Time:", font=('Arial',25), bg='steelblue', anchor='w')
time_label.grid(row=4, column=0, padx=(30, 10), pady=10, sticky='w')

time_entry = tk.Entry(input_frame)
time_entry.grid(row=4, column=1, padx=(10, 30), pady=10)

book_button = tk.Button(root, text="Book Appointment", command=book_appointment, bg='blue', fg='white')
book_button.pack(side='bottom')
specialization_entry.trace("w", update_doctors_options)
root.mainloop()
