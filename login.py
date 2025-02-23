import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bcrypt

logged_in_user = None  # Global variable to track logged-in user
# --- Connect to MySQL ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Change to your MySQL username
    password="root",  # Change to your MySQL password
    database="user_management"
)
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Signup & Login System")

# Configure row and column weights for expansion
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# --- Create Frames ---
signup_frame = tk.Frame(root, bg="lightblue")
signup_frame.grid(row=0, column=0, sticky="news")

login_frame = tk.Frame(root, bg="lightgreen")
login_frame.grid(row=0, column=0, sticky="news")

dashboard_frame = tk.Frame(root, bg="lightgray")
dashboard_frame.grid(row=0, column=0, sticky="news")

# Function to switch frames
def show_frame(frame):
    if frame == dashboard_frame and logged_in_user is None:
        messagebox.showwarning("Access Denied", "You must log in first!")
        return  # Prevent unauthorized access
    frame.tkraise()


def signup():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    
    if username and password:  # Check if fields are not empty
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()
            messagebox.showinfo("Success", "Signup Successful! Now login.")
            show_frame(login_frame)  # Switch to login page
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists! Try another.")
    else:
        messagebox.showwarning("Warning", "All fields are required!")


# --- Login Function ---
logged_in_user = None  # Global variable to track logged-in user

def login():
    global logged_in_user
    username = login_username_entry.get()
    password = login_password_entry.get()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    
    if user:
        logged_in_user = username  # Store the logged-in user
        show_frame(dashboard_frame)  # Move to the dashboard
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    

def logout():
    # Clear the input fields (optional)
    login_username_entry.delete(0, tk.END)
    login_password_entry.delete(0, tk.END)
    
    # Show the login page
    show_frame(login_frame)

def exit_app():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()  # Closes the application

def on_enter(e):
    e.widget.config(bg="darkblue", fg="white")

def on_leave(e):
    e.widget.config(bg="blue", fg="white")

def on_enter_green(e):
    e.widget.config(bg="darkgreen", fg="white")

def on_leave_green(e):
    e.widget.config(bg="green", fg="white")

def on_enter_red(e):
    e.widget.config(bg="darkred", fg="white")

def on_leave_red(e):
    e.widget.config(bg="red", fg="white")


# Create a frame for signup form
signup_form = tk.Frame(signup_frame, relief="ridge", borderwidth=3)
signup_form.grid(row=0, column=0, padx=20, pady=20)

# Signup Page Layout with padding
tk.Label(signup_form, text="New Username:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
signup_username_entry = tk.Entry(signup_form)
signup_username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(signup_form, text="New Password:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
signup_password_entry = tk.Entry(signup_form, show="*")
signup_password_entry.grid(row=1, column=1, padx=10, pady=10)

signup_button = tk.Button(signup_form, text="Sign Up", command=signup, bg="green", fg="white", padx=5, pady=5)
signup_button.grid(row=2, column=0, columnspan=2, pady=10)


login_redirect_button = tk.Button(signup_form, text="Back to Login", command=lambda: show_frame(login_frame), bg="blue", fg="white", padx=5, pady=5)
login_redirect_button.grid(row=3, column=0, columnspan=2, pady=5)

exit_button_signup = tk.Button(signup_form, text="Exit", command=exit_app, bg="red", fg="white", padx=5, pady=5)
exit_button_signup.grid(row=4, column=0, columnspan=2, pady=10)

# event on hover 
login_redirect_button.bind("<Enter>", on_enter_green)
login_redirect_button.bind("<Leave>", on_leave_green)


#exit option for all pages/ frames

exit_button_login = tk.Button(login_frame, text="Exit", command=exit_app)
exit_button_login.grid(row=0,column=10)

exit_button_signup = tk.Button(signup_frame, text="Exit", command=exit_app)
exit_button_signup.grid(row=0,column=10)

exit_button_dashboard = tk.Button(dashboard_frame, text="Exit", command=exit_app)
exit_button_dashboard.grid(row=0,column=10)



# Create a frame for login form
login_form = tk.Frame(login_frame, relief="ridge", borderwidth=3)
login_form.grid(row=0, column=0, padx=20, pady=20)

# Login Page Layout with padding
tk.Label(login_form, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
login_username_entry = tk.Entry(login_form)
login_username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_form, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
login_password_entry = tk.Entry(login_form, show="*")
login_password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(login_form, text="Login", command=login, bg="green", fg="white", padx=5, pady=5)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

signup_redirect_button = tk.Button(login_form, text="Sign Up", command=lambda: show_frame(signup_frame), bg="blue", fg="white", padx=5, pady=5)
signup_redirect_button.grid(row=3, column=0, columnspan=2, pady=5)
signup_redirect_button.bind("<Enter>", on_enter)
signup_redirect_button.bind("<Leave>", on_leave)

exit_button_login = tk.Button(login_form, text="Exit", command=exit_app, bg="red", fg="white", padx=5, pady=5)
exit_button_login.grid(row=4, column=0, columnspan=2, pady=10)
exit_button_login.bind("<Enter>", on_enter_red)
exit_button_login.bind("<Leave>", on_leave_red)


# Dashboard Page Layout with .grid()
tk.Label(dashboard_frame, text="Welcome to the Dashboard!").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

logout_button = tk.Button(dashboard_frame, text="Logout", command=lambda: show_frame(login_frame))
logout_button.grid(row=1, column=0, columnspan=2, pady=10)

exit_button_dashboard = tk.Button(dashboard_frame, text="Exit", command=exit_app)
exit_button_dashboard.grid(row=2, column=0, columnspan=2, pady=10)


# Show Signup Page Initially
signup_frame.tkraise()

# Start the Tkinter event loop
root.mainloop()
