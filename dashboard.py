import datetime
from math import cos, radians, sin
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox
import sqlite3


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # ===== Icons =====
        self.logo_dash = ImageTk.PhotoImage(
            file="images/logo_p.png"
        )

        # ===== Title =====
        title = Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
        ).place(x=0, y=0, relwidth=1, height=50)

        # ===== Menu =====
        M_Frame = LabelFrame(
            self.root, text="Menus", font=("times new roman", 15), bg="white"
        )
        M_Frame.place(x=10, y=70, width=1330, height=80)

        Button(
            M_Frame,
            text="Course",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_course,
        ).place(x=20, y=5, width=200, height=40)

        Button(
            M_Frame,
            text="Student",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_student,
        ).place(x=230, y=5, width=200, height=40)

        Button(
            M_Frame,
            text="Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_result,
        ).place(x=450, y=5, width=200, height=40)

        Button(
            M_Frame,
            text="View Student Results",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_report,
        ).place(x=670, y=5, width=200, height=40)

        Button(
            M_Frame,
            text="Logout",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.logout,
        ).place(x=890, y=5, width=200, height=40)

        Button(
            M_Frame,
            text="Exit",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.exit_,
        ).place(x=1110, y=5, width=200, height=40)

        # ===== Content Window =====
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)

        # ===== Update Details =====
        self.lbl_course = self.create_status_label(
            "Total Courses\n[ 0 ]", 400, "#e43b06"
        )
        self.lbl_student = self.create_status_label(
            "Total Students\n[ 0 ]", 710, "#0676ad"
        )
        self.lbl_result = self.create_status_label(
            "Total Results\n[ 0 ]", 1020, "#038074"
        )

        # Clock
        self.lbl_clock = Label(
            self.root,
            text="\nIndia Clock",
            font=("Book Antiqua", 25, "bold"),
            fg="white",
            compound=BOTTOM,
            bg="#081923",
            bd=0,
        )
        self.lbl_clock.place(x=20, y=180, height=450, width=350)
        self.working()

        # ===== Footer =====
        footer = Label(
            self.root,
            text="SRMS - Student Result Management System\nContact Us for any Technical Issue: 987xxxx01",
            font=("goudy old style", 12, "bold"),
            bg="#262626",
            fg="white",
        ).pack(side=BOTTOM, fill=X)
        self.update_details()

    def create_status_label(self, text, x, bg):
        lbl = Label(
            self.root,
            text=text,
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg=bg,
            fg="white",
        )
        lbl.place(x=x, y=530, width=300, height=100)
        return lbl

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            # Fetch and update total courses
            cur.execute("SELECT * FROM course")
            total_courses = len(cur.fetchall())
            self.lbl_course.config(text=f"Total Courses \n[{total_courses}]")

            # Fetch and update total students
            cur.execute("SELECT * FROM student")
            total_students = len(cur.fetchall())
            self.lbl_student.config(text=f"Total Students \n[{total_students}]")

            # Fetch and update total results
            cur.execute("SELECT * FROM result")
            total_results = len(cur.fetchall())
            self.lbl_result.config(text=f"Total Results \n[{total_results}]")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

        # Schedule the method to run again after 3 seconds (3000 milliseconds)
        self.root.after(3000, self.update_details)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png").resize(
            (300, 300), Image.LANCZOS
        )
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line(
            (origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))),
            fill="#DF005E",
            width=4,
        )
        draw.line(
            (origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))),
            fill="white",
            width=3,
        )
        draw.line(
            (origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))),
            fill="yellow",
            width=2,
        )
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def working(self):
        now = datetime.datetime.now()
        hr = (now.hour % 12) * 30
        min_ = now.minute * 6
        sec_ = now.second * 6
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(
            file="images/clock_new.png"
        )
        self.lbl_clock.config(image=self.img)
        self.lbl_clock.after(1000, self.working)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        ResultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        ReportClass(self.new_win)

    def logout(self):
        if messagebox.askyesno(
            "Confirm", "Do you really want to Logout?", parent=self.root
        ):
            self.root.destroy()
            from login import LoginWindow

            LoginWindow.run()

    def exit_(self):
        if messagebox.askyesno(
            "Confirm", "Do you really want to Exit?", parent=self.root
        ):
            self.root.destroy()

    @staticmethod
    def run():
        from tkinter import Tk

        root = Tk()
        obj = RMS(root)
        root.mainloop()


if __name__ == "__main__":
    RMS.run()
