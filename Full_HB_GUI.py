import customtkinter as ctk 
from tkinter import messagebox  
from Holobank_engine import Holobank

bank = Holobank()
bank.load_from_file()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("1000x800")

app.title('Imeprial HoloNet Terminal')
#app.iconbitmap('DarthStarkillerHB.ico') to add custom image when im able to 
try:
    app.after(200, lambda: app.iconbitmap('DarthStarkillerHB.ico'))
except:
    pass

def filter_by_era(selected_era):

    for widget in display_frame.winfo_children():
         widget.destroy()
   
    categories = {
        "CHARACTERS": bank.char,
        "VEHICLES": bank.Vehicles,
        "CRUISERS": bank.Cruisers
    }     
    found_any = False 
    for cat_name, cat_dict in categories.items():
         if selected_era in cat_dict:
            era_data = cat_dict[selected_era]
            for faction, names in era_data.items():
                for name, details in names.items():
                    found_any = True

                    entry = ctk.CTkLabel(display_frame,
                                        text=f'[{cat_name}] {name} - {faction}',
                                        anchor='w', font=('Courier', 12),
                                        cursor="hand2")
                    entry.pack(fill='x', padx=10, pady=2)

                    entry.bind("<Button-1>", lambda event, n=name, d=details: 
                               messagebox.showinfo(f"HoloNet: {n}", d.get('data','Bio Not Available')))
                  
  
    if not found_any:
       ctk.CTkLabel(display_frame, text="NO RECORDS WERE FOUND IN THIS ERA").pack(pady=20)

def run_search():
    target = search_entry.get().strip().upper()
    cat = category_dropdown.get().lower()        
    if target:

        bank.search_records(cat, target)
        messagebox.showinfo("HoloNet", f"Search For {target} Sent To Terminal Archives..")
    else:
        messagebox.showwarning("Error", "Enter A Name To Scan.")

def submit_character():
    e = add_era_entry.get()
    f = add_fact_entry.get()
    n = add_name_entry.get()
    d = add_data_entry.get()

    if e and f and n:
       
        bank.add_character(e, f, n, d)
        messagebox.showinfo("Imperial Records", f"Entry For {n} Have Been Recorded.")
        
       
        for entry in [add_era_entry, add_fact_entry, add_name_entry, add_data_entry]:
            entry.delete(0, 'end')
    else:
        messagebox.showwarning("Incomplete Data", "Era, Faction, And Name Are Required!") 

input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=20, padx=20, fill="x")

ctk.CTkLabel(input_frame, text="ADD NEW RECORD:", font=("Courier", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

add_era_entry = ctk.CTkEntry(input_frame, placeholder_text="Era (e.g. Clone Wars)")
add_era_entry.grid(row=1, column=0, padx=5, pady=5)

add_fact_entry = ctk.CTkEntry(input_frame, placeholder_text="Faction")
add_fact_entry.grid(row=1, column=1, padx=5, pady=5)

add_name_entry = ctk.CTkEntry(input_frame, placeholder_text="Name")
add_name_entry.grid(row=2, column=0, padx=5, pady=5)

add_data_entry = ctk.CTkEntry(input_frame, placeholder_text="Bio/Data", width=250)
add_data_entry.grid(row=2, column=1, padx=5, pady=5)


submit_btn = ctk.CTkButton(input_frame, text="UPLOAD TO HOLOBANK", fg_color="green", command=submit_character)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)               



top_bar = ctk.CTkFrame(app)  
top_bar.pack(pady=20, padx=20, fill="x")

category_dropdown = ctk.CTkOptionMenu(top_bar, values=["Characters", "Vehicles", "Cruisers"], width=100)
category_dropdown.pack(side="left", padx=10)

search_entry = ctk.CTkEntry(top_bar, placeholder_text="Search Archives...", width=250)
search_entry.pack(side="left", padx=10)
search_btn = ctk.CTkButton(top_bar, text="SCAN", command=run_search)
search_btn.pack(side="left", padx=10)

era_frame = ctk.CTkFrame(app)
era_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(era_frame, text= 'FILTER BY ERA:').pack(side="left", padx=10)

for era in bank.era_list:
    btn = ctk.CTkButton(era_frame, text=era, width=100, font=("Courier", 10), 
                        command=lambda e=era: filter_by_era(e))
    btn.pack(side="left",padx=5, pady=5)

display_frame = ctk.CTkScrollableFrame(app, width=550, height=400, label_text="ARCHIVE DATA")
display_frame.pack(pady=20, padx=20)

exit_btn = ctk.CTkButton(app, text= "SECURE ARCHIVES AND EXIT", fg_color="red", 
                        command=lambda: [bank.save_in_file(), app.destroy()])
exit_btn.pack(side="bottom", pady=20)

app.protocol("WM_DELETE_WINDOW", lambda: [bank.save_in_file(), app.destroy()])

app.mainloop()