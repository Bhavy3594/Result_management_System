import datetime
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import sqlite3
from tkinter import messagebox
import math  # Importing math for trigonometric functions


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("RMS Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        # Background Color
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)
        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # Login Frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(
            login_frame,
            text="LOGIN HERE",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="#08A3D2",
        ).place(x=250, y=50)

        email = Label(
            login_frame,
            text="EMAIL ADDRESS",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="gray",
        ).place(x=250, y=150)

        self.txt_email = Entry(
            login_frame,
            font=("times new roman", 15),
            bg="lightgray",
        )
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_ = Label(
            login_frame,
            text="PASSWORD",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="gray",
        ).place(x=250, y=250)

        self.txt_pass_ = Entry(
            login_frame,
            font=("times new roman", 15),
            bg="lightgray",
            show="*",  # Hides the password entry for security
        )
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_login = Button(
            login_frame,
            text="Login",
            font=("times new roman", 20, "bold"),
            fg="white",
            bd=0,
            bg="#B00857",
            cursor="hand2",
            command=self.login,
        ).place(x=250, y=380, width=180, height=40)

        # Clock
        self.lbl = Label(
            self.root,
            text="\nIndia Clock",
            font=("Book Antiqua", 25, "bold"),
            fg="white",
            compound=BOTTOM,
            bg="#081923",
            bd=0,
        )
        self.lbl.place(x=90, y=120, height=450, width=350)
        self.working()

    def login(self):
        email = self.txt_email.get()
        password = self.txt_pass_.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute(
                    "SELECT * FROM register WHERE email=? AND password=?",
                    (email, password),
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid USERNAME & PASSWORD", parent=self.root
                    )
                else:
                    messagebox.showinfo(
                        "Success", f"Welcome: {email}", parent=self.root
                    )
                    self.root.destroy()
                    from dashboard import RMS

                    RMS.run()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png").resize((300, 300), Image.LANCZOS)
        clock.paste(bg, (50, 50))

        origin = 200, 200

        # Hour hand
        draw.line(
            (
                origin,
                200 + 50 * math.sin(math.radians(hr)),
                200 - 50 * math.cos(math.radians(hr)),
            ),
            fill="#DF005E",
            width=4,
        )
        # Minute hand
        draw.line(
            (
                origin,
                200 + 80 * math.sin(math.radians(min_)),
                200 - 80 * math.cos(math.radians(min_)),
            ),
            fill="white",
            width=3,
        )
        # Second hand
        draw.line(
            (
                origin,
                200 + 100 * math.sin(math.radians(sec_)),
                200 - 100 * math.cos(math.radians(sec_)),
            ),
            fill="yellow",
            width=2,
        )
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def working(self):
        now = datetime.datetime.now()
        hr = (now.hour % 12) * 30  # 360 degrees divided by 12 hours
        min_ = now.minute * 6  # 360 degrees divided by 60 minutes
        sec_ = now.second * 6  # 360 degrees divided by 60 seconds
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(1000, self.working)

    @staticmethod
    def run():
        root = Tk()
        obj = LoginWindow(root)
        root.mainloop()


if __name__ == "__main__":
    LoginWindow.run()
