from selenium import webdriver
import time
import threading
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import pyperclip

global cheated
cheated = False

def test_and_checker(class_name, team_name):
    global cheated
    import firebase_admin
    from firebase_admin import credentials, firestore
    from firebase_admin import db

    service_account_data = {}

    cred = credentials.Certificate(service_account_data)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://hitnext-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

    firestore_client = firestore.client()
    doc_ref = firestore_client.collection(class_name).document(team_name)

    def read_from_firebase(path):
        ref = db.reference(path)
        data = ref.get()
        return data

    start = read_from_firebase('/test/start')
    while not start:
        start = read_from_firebase('/test/start')

    driver = webdriver.Chrome()

    url = "https://kid-one-spaniel.ngrok-free.app"  
    driver.get(url)

    previous_url = driver.current_url

    team_progress = {}
    try:
        while True:
            current_url = driver.current_url

            if cheated:
                team_progress['cheated'] = True
                doc_ref.set(team_progress)
                driver.quit()

            if current_url != previous_url:
                previous_url = current_url  
                if current_url not in team_progress:
                    team_progress[current_url] = str(datetime.now())
                    doc_ref.set(team_progress)

            end = read_from_firebase('/test/end')
            if end:
                driver.quit()

            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        driver.quit()

def cheating_checker():
    global cheated
    pyperclip.copy('')
    while not cheated:
        try:
            pyperclip.copy('')
        except Exception as e:
            print(f"Error accessing clipboard: {e}")
        time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login to HitNext")
    root.geometry("300x200")

    tk.Label(root, text="Classroom Number:").pack(pady=5)

    class_number_options = ["CR001", "CR201", "CR301", "CR401"]

    selected_class_number = tk.StringVar()
    selected_class_number.set(class_number_options[0]) 

    class_number_menu = tk.OptionMenu(root, selected_class_number, *class_number_options)
    class_number_menu.pack(pady=5)

    tk.Label(root, text="Team Name:").pack(pady=5)
    team_name_entry = tk.Entry(root)
    team_name_entry.pack(pady=5)

    def submit():
        class_number = selected_class_number.get() 
        team_name = team_name_entry.get()

        if class_number and team_name:
            messagebox.showinfo("Input Submitted", f"Class Number: {class_number}\nTeam Name: {team_name}")
            root.destroy() 

            run_test = threading.Thread(target=test_and_checker, args=(class_number, team_name,))
            run_test.start()
            cheating_check = threading.Thread(target=cheating_checker,)
            cheating_check.start()

        else:
            messagebox.showwarning("Input Error", "Please fill in both fields.")

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=20)

    root.mainloop()