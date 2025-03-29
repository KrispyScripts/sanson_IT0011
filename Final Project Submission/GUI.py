import os # Import os para makita yung signup_records.txt sa operating system nyo
import tkinter as tk # Import tkinter para sa GUI
from tkinter import messagebox, ttk # Import messagebox at ttk para sa mga pop-up at table

# Defines the path to record files
RECORDS_FILE = os.path.join(os.path.dirname(__file__), "signup_records.txt")

class SignUpSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Aster Risk Database - Sign-Up System") # Window title
        self.root.geometry("600x400") # Window size
        
        self.records = [] # List to store sign-up records
        self.load_records() # Load existing records from file
        self.create_main_menu() # Creates the main menu

    def create_main_menu(self): # Main menu creation
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Aster Risk", font=("Arial", 16, "bold")).pack(pady=5)
        tk.Label(self.root, text="Sign-Up Database System", font=("Arial", 14)).pack(pady=10)
        
        tk.Button(self.root, text="New Sign-Up", width=20, command=self.show_signup_form).pack(pady=10)
        tk.Button(self.root, text="View All Sign-Ups", width=20, command=self.show_all_records).pack(pady=10)
        tk.Button(self.root, text="Search Sign-Ups", width=20, command=self.show_search_form).pack(pady=10)
        tk.Button(self.root, text="Exit System", width=20, command=self.exit_program).pack(pady=10)

    def show_signup_form(self): # Sign-up form creation
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Button(self.root, text="← Back to Main Menu", command=self.create_main_menu).pack(anchor="nw", padx=10, pady=10)
        tk.Label(self.root, text="Aster Risk - New Sign-Up Form", font=("Arial", 14)).pack(pady=10)
        
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        first_name_entry = tk.Entry(form_frame)
        first_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(form_frame, text="Middle Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        middle_name_entry = tk.Entry(form_frame)
        middle_name_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(form_frame, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        last_name_entry = tk.Entry(form_frame)
        last_name_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(form_frame, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        birthday_entry = tk.Entry(form_frame)
        birthday_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(form_frame, text="Gender:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        gender_var = tk.StringVar()
        gender_var.set("Male")
        tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").grid(row=4, column=1, padx=10, pady=5, sticky="w")
        tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").grid(row=5, column=1, padx=10, pady=5, sticky="w")
        
        def submit_record(): # Submit the sign-up record
            record = {
                "first_name": first_name_entry.get(),
                "middle_name": middle_name_entry.get(),
                "last_name": last_name_entry.get(),
                "birthday": birthday_entry.get(),
                "gender": gender_var.get()
            }
            
            self.records.append(record)
            self.save_records()
            messagebox.showinfo("Success", "Sign-up record added successfully!")
            
            first_name_entry.delete(0, tk.END)
            middle_name_entry.delete(0, tk.END)
            last_name_entry.delete(0, tk.END)
            birthday_entry.delete(0, tk.END)
            gender_var.set("Male")
        
        tk.Button(self.root, text="Submit Sign-Up", command=submit_record).pack(pady=20)

    def show_all_records(self): ## Display all sign-up records
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Button(self.root, text="← Back to Main Menu", command=self.create_main_menu).pack(anchor="nw", padx=10, pady=10)
        tk.Label(self.root, text="Aster Risk - All Sign-Up Records", font=("Arial", 14)).pack(pady=10)
        
        if not self.records:
            tk.Label(self.root, text="No sign-up records found.").pack()
            return
        
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=20, padx=10, fill="both", expand=True)
        
        tree = ttk.Treeview(table_frame, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show="headings")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Name", text="Middle Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Birthday", text="Birthday")
        tree.heading("Gender", text="Gender")
        
        for record in self.records:
            tree.insert("", "end", values=(
                record["first_name"],
                record["middle_name"],
                record["last_name"],
                record["birthday"],
                record["gender"]
            ))
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)

    def show_search_form(self): ## Search form creation
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Button(self.root, text="← Back to Main Menu", command=self.create_main_menu).pack(anchor="nw", padx=10, pady=10)
        tk.Label(self.root, text="Aster Risk - Search Sign-Ups", font=("Arial", 14)).pack(pady=10)
        
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=20)
        
        tk.Label(search_frame, text="Search by Last Name:").grid(row=0, column=0, padx=10, pady=5)
        search_entry = tk.Entry(search_frame)
        search_entry.grid(row=0, column=1, padx=10, pady=5)
        
        results_frame = tk.Frame(self.root)
        results_frame.pack(pady=20, padx=10, fill="both", expand=True)
        
        def perform_search(): ## Perform the search based on the last name
            for widget in results_frame.winfo_children():
                widget.destroy()
            
            search_term = search_entry.get().lower()
            matches = [record for record in self.records if search_term in record["last_name"].lower()]
            
            if not matches:
                tk.Label(results_frame, text="No matching sign-up records found.").pack()
                return
            
            tree = ttk.Treeview(results_frame, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show="headings")
            tree.heading("First Name", text="First Name")
            tree.heading("Middle Name", text="Middle Name")
            tree.heading("Last Name", text="Last Name")
            tree.heading("Birthday", text="Birthday")
            tree.heading("Gender", text="Gender")
            
            for record in matches:
                tree.insert("", "end", values=(
                    record["first_name"],
                    record["middle_name"],
                    record["last_name"],
                    record["birthday"],
                    record["gender"]
                ))
            
            scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            tree.pack(fill="both", expand=True)
        
        tk.Button(self.root, text="Search Sign-Ups", command=perform_search).pack(pady=10)

    def load_records(self): ## Load existing sign-up records from file
        with open(RECORDS_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    parts = line.strip().split(",")
                    if len(parts) == 5:
                        self.records.append({
                            "first_name": parts[0],
                            "middle_name": parts[1],
                            "last_name": parts[2],
                            "birthday": parts[3],
                            "gender": parts[4]
                        })

    def save_records(self): ## Save sign-up records to file
        with open(RECORDS_FILE, "w") as file:
            for record in self.records:
                line = f"{record['first_name']},{record['middle_name']},{record['last_name']},{record['birthday']},{record['gender']}\n"
                file.write(line)

    def exit_program(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = SignUpSystem(root)
    root.mainloop()