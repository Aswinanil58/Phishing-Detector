import tkinter as tk
from tkinter import messagebox
from websiteverifier import everything_in_one  # Import the function


class PhishingDetector(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.link_field = tk.Entry(self, width=25)
        self.submit_link_button = tk.Button(self, text="Submit Link", command=self.submit_link)

        # Set default font size for the entire application
        default_font = ("Arial", 20)
        self.option_add("*Font", default_font)

        # Set layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add components to the frame with labels and buttons
        tk.Label(self, text="Enter link:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.link_field.grid(row=0, column=1, padx=10, pady=10)
        self.submit_link_button.grid(row=1, column=0, columnspan=2, pady=10)

    def submit_link(self):
        link = self.link_field.get()

        try:
            is_phishing = everything_in_one(link)  # Call the function from your code file
            print("is phisphing:",is_phishing)
            if is_phishing == 1:
                self.show_scam_popup("The website is legitimate.")
            elif is_phishing == 2:
                self.show_legitimate_popup("Cannot find hash data")
            else:
                self.show_legitimate_popup("Suspected Phisphing link")

        except Exception as ex:
            print(ex)

    def show_legitimate_popup(self, message):
        messagebox.showinfo("Legitimate", message)

    def show_scam_popup(self, message):
        messagebox.showwarning("Warning", message)

if __name__ == "__main__":
    app = PhishingDetector()
    app.mainloop()
