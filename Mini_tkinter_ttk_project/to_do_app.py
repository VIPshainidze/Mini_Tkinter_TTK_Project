from tkinter.ttk import *
from tkinter import Tk, StringVar, IntVar, END, PhotoImage, DISABLED, NORMAL
from tkinter import Label as TkLabel  # tkinter.ttk-ს Label ვიჯეტთან რო არ აირიოს
from tkinter import Text as TKText
from tkinter import messagebox as msg
from PIL import Image, ImageTk
from datetime import date
from random import randint
from smtplib import SMTP
from copy import deepcopy


# # ქვედა 3 ხაზი ფოტოების ტიპებთან საჩალიჩო კოდია
# filename = r'Blue_Cubes.jpg'
# img = Image.open(filename)
# img.save('Blue_Cubes.png')

sender, server = None, None


class Project:

    user_data = None
    generated_code = None
    deadline = None

    @staticmethod
    def sign_in():
        username = LBF_1_E_1.get()
        password = LBF_1_E_2.get()

        with open("user_data.txt", encoding="utf-8") as data:
            data = data.read().split()

            if [username, password] == data:
                NB.tab(1, state="normal")
                NB.select(tab_2)
                string_var_1.set("")
                string_var_1.set("შესვლა ნებადართულია")
                LBF_1_LB_3.configure(fg="green")

            else:

                if data != []:

                    if username != data[0] and password != data[1]:
                        string_var_1.set("")
                        string_var_1.set("მომხმარებლის ლოგინი და პაროლი არასწორია!")
                        LBF_1_LB_3.configure(fg="red")

                    elif username != data[0]:
                        string_var_1.set("")
                        string_var_1.set("მომხმარებლის სახელი არასწორია")
                        LBF_1_LB_3.configure(fg="red")

                    else:
                        string_var_1.set("")
                        LBF_1_LB_3.configure(fg="red")
                        string_var_1.set("მომხმარებლის პაროლი არასწორია")

                else:
                    string_var_1.set("")
                    LBF_1_LB_3.configure(fg="red")
                    string_var_1.set("მომხმარებლი არ არსებობს")


    @staticmethod
    def lbf_2_radio_1():
        LBF_2_i_var_2.set(0)

    @staticmethod
    def lbf_2_radio_2():
        LBF_2_i_var_1.set(0)

    @staticmethod
    def click_registration():
        if name_e.get() != "" and surname_e.get() != "" and email_e.get() != "" and username_e.get() != "" and \
                password_e.get() != "" and (LBF_2_i_var_1.get() != 0 or LBF_2_i_var_2.get() != 0) and \
                LBF_2_t_var_1.get() != "წელი" and LBF_2_t_var_2.get() != "თვე" and LBF_2_t_var_3.get() != "დღე":
            status_string_var.set("")
            status_label.configure(fg="green")
            status_string_var.set(f"რეგისტრაცია წარმატებულია. USER: {username_e.get()}")

            name_1 = name_e.get()
            surname_1 = surname_e.get()
            email_1 = email_e.get()
            username_1 = username_e.get()
            password_1 = password_e.get()
            gender_1 = None
            if LBF_2_i_var_1.get():
                gender_1 = "ქალი"
            elif LBF_2_i_var_2.get():
                gender_1 = "კაცი"
            birth_year = LBF_2_t_var_1.get()
            birth_month = LBF_2_t_var_2.get()
            birth_day = LBF_2_t_var_3.get()
            Project.user_data = {
                "სახელი": name_1,
                "გვარი": surname_1,
                "იმეილი": email_1,
                "სქესი": gender_1,
                "დაბადების დღე": birth_day,
                "დაბადების თვე": birth_month,
                "დაბადების წელი": birth_year,
                "დაბადების თარიღი": date(int(birth_year), int(birth_month), int(birth_day)),
                "ექაუნთი": {
                    "მომხმარებელი": username_1,
                    "პაროლი": password_1
                }
            }

            with open("user_data.txt", "w+") as user_base:
                user_base.write(f"{username_1} {password_1}")

            Project.click_reset()

        else:
            status_string_var.set("")
            status_label.configure(fg="#e0410b")
            status_string_var.set("გთხოვთ შეავსოთ ყველა ველი")

    @staticmethod
    def click_reset():
        name_e.delete(0, END)
        surname_e.delete(0, END)
        email_e.delete(0, END)
        username_e.delete(0, END)
        password_e.delete(0, END)
        LBF_2_i_var_1.set(-1)
        LBF_2_i_var_2.set(-1)
        LBF_2_t_var_1.set("წელი")
        LBF_2_t_var_2.set("თვე")
        LBF_2_t_var_3.set("დღე")
        username_e.delete(0, END)
        password_e.delete(0, END)

    @staticmethod
    def reset_password():
        code = randint(1000, 9999)
        Project.generated_code = deepcopy(code)

        """
        უსაფრთხოების დონის დასაწევი ლინკი ჯიმეილისთის.
        https://myaccount.google.com/u/2/lesssecureapps?pli=1&pageId=none
        """

        senders_list = ["Mails here"]
        passwords_list = ["Passwords here"]

        def main_fun():
            sender = senders_list[0]
            server = SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, passwords_list[0])
            server.sendmail(sender, Project.user_data["იმეილი"], str(Project.generated_code))

        main_fun()

    @staticmethod
    def agree_reset_code():
        if str(reset_password_code_e.get()) == str(Project.generated_code):
            agree_password_e.configure(state="normal")

    @staticmethod
    def update_password():
        password_1_1 = agree_password_e.get()
        reset_status.configure(fg="green")
        reset_password_string_var.set("პაროლი განახლებულია")
        with open("user_data.txt", "w+") as base_update:
            base_update.write(f"{Project.user_data['ექაუნთი']['მომხმარებელი']} {password_1_1}")

    @staticmethod
    def add_todo():
        NB.tab(2, state=NORMAL)
        NB.select(tab_3)
        todo_name = tab_2_title_e.get()
        year = tab_2_Combo_1.get()
        month = tab_2_Combo_2.get()
        day = tab_2_Combo_3.get()
        hour = tab_2_Combo_4.get()
        minute = tab_2_Combo_5.get()
        about = tab_2_about.get(0.0, END)

        Project.deadline = {
            "სახელი": todo_name,
            "წელი": year,
            "თვე": month,
            "დღე": day,
            "სთ": hour,
            "წთ": minute,
            "აღწერა": about
        }

        todo_1_l_str.set(todo_name)
        todo_1_1_l_str.set(f"{str(year)}/{str(month)}/{str(day)}  {str(hour)}:{str(minute)} სთ")
        about_1_t.insert(0.0, about)
        tab_2_title_e.delete(0, END)
        tab_2_t_var_1.set("წელი")
        tab_2_t_var_2.set("თვე")
        tab_2_t_var_3.set("დღე")
        tab_2_t_var_4.set("სთ")
        tab_2_t_var_5.set("წთ")
        tab_2_about.delete(0.0, END)

    @staticmethod
    def todo_done():
        NB.tab(3, state=NORMAL)
        NB.select(tab_4)
        todo_1_l_str_1.set(f"{str(Project.deadline['სახელი'])}")
        todo_1_1_l_str_1.set("წარმატებით შესრულდა")
        about_1_t_1.insert(0.0, str(Project.deadline['აღწერა']))
        about_1_t_1.configure(state=DISABLED)

        Project.todo_del()
        pass

    @staticmethod
    def todo_del():
        todo_1_l_str.set("")
        todo_1_1_l_str.set("")
        about_1_t.delete(0.0, END)

    @staticmethod
    def todo_del_tab_4():
        really = msg.askyesnocancel("შეკითხვა", "ნამდვილად გსუურთ წაშლა?")
        if really:
            todo_1_l_str_1.set("")
            todo_1_1_l_str_1.set("")
            about_1_t_1.configure(state=NORMAL)
            about_1_t_1.delete(0.0, END)
            about_1_t_1.configure(state=DISABLED)

        else:
            pass

    @staticmethod
    def binder_1(event_1):
        NB.select(tab_2)

    @staticmethod
    def sign_in_binder(event_2):
        Project.sign_in()


# <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>>
# <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>>
# <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>> <<< TKINTER >>>
win = Tk()
win.title("ToDoPy")
img = PhotoImage(file="")
win.iconbitmap("1_adNxNe6AEVq4YPsMru7JeA@2x (1).ico")
win.geometry("500x700+1400+300")
win.resizable(width=False, height=False)
win.configure(bg="#9900ff")

style = Style()
style.configure("BW.TLabel", foreground="black", background="#9900ff")
style_2 = Style()
style_2.configure("TFrame", background="#4a3985")

NB = Notebook(win)

tab_1 = Frame(NB, style="TFrame")
tab_2 = Frame(NB, style="TFrame")
tab_3 = Frame(NB, style="TFrame")
tab_4 = Frame(NB, style="TFrame")

NB.add(tab_1, text="ToDoPy", underline=0)
NB.add(tab_2, text="ToDo-ს დამატება", underline=0, state=DISABLED)
NB.add(tab_3, text="ყველა ToDo", underline=0, state=DISABLED)
NB.add(tab_4, text="შესრულებული ToDo-ები", underline=0, state=DISABLED)


# <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>>
# <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>>
# <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>> <<< TAB 4 >>>
TAB_4_LBF_1_1 = LabelFrame(tab_4, text="ToDo N-1")
todo_1_1 = Label(TAB_4_LBF_1_1, text="ToDo: ")
todo_1_1_1 = Label(TAB_4_LBF_1_1, text="დედლაინი: ")

todo_1_l_str_1 = StringVar()
todo_1_1_l_str_1 = StringVar()
todo_1_l_1 = Label(TAB_4_LBF_1_1, textvariable=todo_1_l_str_1)
todo_1_1_l_1 = Label(TAB_4_LBF_1_1, textvariable=todo_1_1_l_str_1)
about_1_l_1 = Label(TAB_4_LBF_1_1, text="შესახებ: ")
about_1_t_1 = TKText(TAB_4_LBF_1_1, width=25, height=3, state=NORMAL)

img_2_1 = Image.open("images.ico")
img_2_1 = img_2_1.resize((130, 130), )
ttk_img_2_1 = ImageTk.PhotoImage(img_2_1)
img_label_2_1 = Label(TAB_4_LBF_1_1, image=ttk_img_2_1)
todo_b_2_1 = Button(TAB_4_LBF_1_1, text="DEL", width=15, command=Project.todo_del_tab_4)

todo_b_2_1.bind("<Button-1><Button-3>", Project.binder_1)
# TAB_3  LABEL_FRAME -- 1  GRID/PACK START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TAB_4_LBF_1_1.pack(side="top", fill="x", padx=10, pady=10)

img_label_2_1.grid(rowspan=10, column=0)
todo_1_1.grid(row=0, column=1, padx=10, pady=0, sticky="W")
todo_1_1_1.grid(row=1, column=1, padx=10, pady=0, sticky="W")
todo_1_l_1.grid(row=0, column=1, sticky="W", padx=100)
todo_1_1_l_1.grid(row=1, column=1, sticky="W", padx=100)
about_1_l_1.grid(row=2, column=1, padx=10, pady=0, sticky="W")
about_1_t_1.grid(row=2, column=1, padx=100, pady=10, sticky="W")
todo_b_2_1.grid(row=8, column=1, sticky="W", padx=204)

# >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<<
# >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<<
# >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<< >>> TAB 4 <<<


# <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>>
# <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>>
# <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>> <<< TAB 3 >>>
TAB_3_LBF_1_1 = LabelFrame(tab_3, text="ToDo N-1")
todo_1 = Label(TAB_3_LBF_1_1, text="ToDo: ")
todo_1_1 = Label(TAB_3_LBF_1_1, text="დედლაინი: ")

todo_1_l_str = StringVar()
todo_1_1_l_str = StringVar()
todo_1_l = Label(TAB_3_LBF_1_1, textvariable=todo_1_l_str)
todo_1_1_l = Label(TAB_3_LBF_1_1, textvariable=todo_1_1_l_str)
about_1_l = Label(TAB_3_LBF_1_1, text="შესახებ: ")
about_1_t = TKText(TAB_3_LBF_1_1, width=25, height=3, state=NORMAL)

img_2 = Image.open("adobe-color.ico")
img_2 = img_2.resize((130, 130), )
ttk_img_2 = ImageTk.PhotoImage(img_2)
img_label_2 = Label(TAB_3_LBF_1_1, image=ttk_img_2)

todo_b_1 = Button(TAB_3_LBF_1_1, text="DONE", width=15, command=Project.todo_done)
todo_b_2 = Button(TAB_3_LBF_1_1, text="DEL", width=15, command=Project.todo_del)
# TAB_3  LABEL_FRAME -- 1  GRID/PACK START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TAB_3_LBF_1_1.pack(side="top", fill="x", padx=10, pady=10)

img_label_2.grid(rowspan=10, column=0)
todo_1.grid(row=0, column=1, padx=10, pady=0, sticky="W")
todo_1_1.grid(row=1, column=1, padx=10, pady=0, sticky="W")
todo_1_l.grid(row=0, column=1, sticky="W", padx=100)
todo_1_1_l.grid(row=1, column=1, sticky="W", padx=100)
about_1_l.grid(row=2, column=1, padx=10, pady=0, sticky="W")
about_1_t.grid(row=2, column=1, padx=100, pady=10, sticky="W")
todo_b_1.grid(row=8, column=1, sticky="w", padx=99)
todo_b_2.grid(row=8, column=1, sticky="W", padx=204)
# TAB_3  LABEL_FRAME -- 1  GRID/PACK END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<<
# >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<<
# >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<< >>> TAB 3 <<<


# <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>>
# <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>>
# <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>> <<< TAB 2 >>>
TAB_2_LBF_1_1 = LabelFrame(tab_2, text="მოგესალმებით ToDo-ში!")

my_img = Image.open("1_adNxNe6AEVq4YPsMru7JeA@2x (1).ico")
my_img = my_img.resize((200, 200), )
tk_img = ImageTk.PhotoImage(my_img)
tab_2_img_label = Label(TAB_2_LBF_1_1, image=tk_img, compound="bottom", text="მოგესალმებით ToDo-ში!").pack()

TAB_2_LBF_1_2 = LabelFrame(tab_2, text="შექმენი ახლი ToDo")
tab_2_title = Label(TAB_2_LBF_1_2, text="ToDo-ს დასახელება: ")

tab_2_deadline = Label(TAB_2_LBF_1_2, text="მიუთითეთ დედლაინი: ")
tab_2_t_var_1 = StringVar()
tab_2_t_var_2 = StringVar()
tab_2_t_var_3 = StringVar()
tab_2_t_var_4 = StringVar()
tab_2_t_var_5 = StringVar()
tab_2_t_var_1.set("წელი")
tab_2_t_var_2.set("თვე")
tab_2_t_var_3.set("დღე")
tab_2_t_var_4.set("სთ")
tab_2_t_var_5.set("წთ")
tab_2_Combo_1 = Combobox(
    TAB_2_LBF_1_2,
    values=list(range(2020, 2030)),
    state="readonly",
    textvariable=tab_2_t_var_1,
    width=6
)
tab_2_Combo_2 = Combobox(
    TAB_2_LBF_1_2,
    values=list(range(1, 13)),
    state="readonly",
    textvariable=tab_2_t_var_2,
    width=5
)
tab_2_Combo_3 = Combobox(
    TAB_2_LBF_1_2,
    values=list(range(1, 32)),
    state="readonly",
    textvariable=tab_2_t_var_3,
    width=5
)
tab_2_Combo_4 = Combobox(
    TAB_2_LBF_1_2,
    values=list(range(1, 25)),
    state="readonly",
    textvariable=tab_2_t_var_4,
    width=3
)
tab_2_Combo_5 = Combobox(
    TAB_2_LBF_1_2,
    values=list(range(0, 61)),
    state="readonly",
    textvariable=tab_2_t_var_5,
    width=3
)

tab_2_about_1 = Label(TAB_2_LBF_1_2, text="შეიყვანეთ ToDo-ს აღწერა")

tab_2_title_e = Entry(TAB_2_LBF_1_2, width=41)

tab_2_about = TKText(TAB_2_LBF_1_2, width=40, height=6)

tab_2_add_b = Button(TAB_2_LBF_1_2, width=40, text="ToDo-ს დამატება", command=Project.add_todo)

# TAB_1  LABEL_FRAME -- 1  GRID/PACK START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TAB_2_LBF_1_1.pack(side="top", expand=True, fill="both", padx=10, pady=10)

TAB_2_LBF_1_2.pack(side="top", expand=True, fill="both", padx=10, pady=10)

tab_2_title.grid(row=0, column=0, sticky="W", padx=10, pady=10)
tab_2_deadline.grid(row=1, column=0, sticky="W", padx=10, pady=6)
tab_2_about_1.grid(row=2, column=0, sticky="W", padx=10, pady=6)
tab_2_about.grid(row=3, columnspan=3, sticky="W", padx=10, ipady=2)

tab_2_Combo_1.grid(row=1, column=0, sticky="W", padx=200)
tab_2_Combo_2.grid(row=1, column=0, sticky="W", padx=260)
tab_2_Combo_3.grid(row=1, column=0, sticky="W", padx=314)
tab_2_Combo_4.grid(row=1, column=0, sticky="W", padx=368)
tab_2_Combo_5.grid(row=1, column=0, sticky="W", padx=410)
tab_2_title_e.grid(row=0, column=0, sticky="W", padx=200)
tab_2_add_b.grid(row=4, column=0, sticky="W", padx=88, pady=15)
# TAB_1  LABEL_FRAME -- 1  GRID/PACK END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<<
# >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<<
# >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<< >>> TAB 2 <<<


# <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>>
# <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>>
# <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>> <<< TAB 1 >>>

# Label Frame N-1 START   <<< LABEL 1 >>>   <<< LABEL 1 >>>   <<< LABEL 1 >>>   <<< LABEL 1 >>>   <<< LABEL 1 >>>
TAB_1_LBF_1_1 = LabelFrame(tab_1, text="სისტემაში შესვლა")

LBF_1_LB_1 = Label(TAB_1_LBF_1_1, text="მომხმარებლის სახელი: ")
LBF_1_LB_2 = Label(TAB_1_LBF_1_1, text="მომხმარებლის პაროლი: ")

LBF_1_E_1 = Entry(TAB_1_LBF_1_1, width=36)
LBF_1_E_2 = Entry(TAB_1_LBF_1_1, width=36, show="*")

LBF_1_B_2 = Button(TAB_1_LBF_1_1, text="შესვლა", command=Project.sign_in)

string_var_1 = StringVar()
string_var_1.set("სისტემაში შესვლის ნებართვა")
LBF_1_LB_3 = TkLabel(TAB_1_LBF_1_1, textvariable=string_var_1, fg="blue")
LBF_1_B_2.bind("<Return>", Project.sign_in_binder)
# Label Frame N-1 END


# Label Frame N-2 START   <<< LABEL 2 >>>   <<< LABEL 2 >>>   <<< LABEL 2 >>>   <<< LABEL 2 >>>   <<< LABEL 2 >>>
TAB_1_LBF_1_2 = LabelFrame(tab_1, text="რეგისტრაცია")

name = Label(TAB_1_LBF_1_2, text="შეიყვანეთ სახელი: ")
surname = Label(TAB_1_LBF_1_2, text="შეიყვანეთ გვარი: ")
email = Label(TAB_1_LBF_1_2, text="შეიყვანეთ ელ.მისამართი: ")
username = Label(TAB_1_LBF_1_2, text="მომხმარებლის სახელი: ")
password = Label(TAB_1_LBF_1_2, text="აირჩიეთ პაროლი: ")

gender = Label(TAB_1_LBF_1_2, text="აირჩიეთ სქესი: ")
LBF_2_i_var_1 = IntVar()
LBF_2_i_var_2 = IntVar()
LBF_2_Radio_1 = Radiobutton(TAB_1_LBF_1_2, text="ქალი", variable=LBF_2_i_var_1, value=1, command=Project.lbf_2_radio_1)
LBF_2_Radio_2 = Radiobutton(TAB_1_LBF_1_2, text="კაცი", variable=LBF_2_i_var_2, value=1, command=Project.lbf_2_radio_2)

LBF_2_t_var_1 = StringVar()
LBF_2_t_var_2 = StringVar()
LBF_2_t_var_3 = StringVar()
LBF_2_t_var_1.set("წელი")
LBF_2_t_var_2.set("თვე")
LBF_2_t_var_3.set("დღე")
LBF_2_Combo_1 = Combobox(
    TAB_1_LBF_1_2,
    values=list(range(1930, 2021)),
    state="readonly",
    textvariable=LBF_2_t_var_1,
    width=9
)
LBF_2_Combo_2 = Combobox(
    TAB_1_LBF_1_2,
    values=list(range(1, 13)),
    state="readonly",
    textvariable=LBF_2_t_var_2,
    width=6
)
LBF_2_Combo_3 = Combobox(
    TAB_1_LBF_1_2,
    values=list(range(1, 32)),
    state="readonly",
    textvariable=LBF_2_t_var_3,
    width=6
)
birth_date = Label(TAB_1_LBF_1_2, text="დაბადების თარიღი: ")

name_e = Entry(TAB_1_LBF_1_2, width=36)
surname_e = Entry(TAB_1_LBF_1_2, width=36)
email_e = Entry(TAB_1_LBF_1_2, width=36)
username_e = Entry(TAB_1_LBF_1_2, width=36)
password_e = Entry(TAB_1_LBF_1_2, width=36)

registration_b = Button(TAB_1_LBF_1_2, text="რეგისტრაცია", command=Project.click_registration)

reset_b = Button(TAB_1_LBF_1_2, text="Reset", command=Project.click_reset)

status_string_var = StringVar()
status_string_var.set("რეგისტრაციის სტატუსი")
status_label = TkLabel(TAB_1_LBF_1_2, textvariable=status_string_var, fg="blue")
# Label Frame N-2 END


# Label Frame N-3 START   <<< LABEL 3 >>>   <<< LABEL 3 >>>   <<< LABEL 3 >>>   <<< LABEL 3 >>>   <<< LABEL 3 >>>
TAB_1_LBF_1_3 = LabelFrame(tab_1, text="პაროლის აღდგენა")

reset_password_b = Button(TAB_1_LBF_1_3, text="პაროლის აღდგენა/განახლება", command=Project.reset_password)
code_agree_b = Button(TAB_1_LBF_1_3, text="დადასტურება", command=Project.agree_reset_code)
agree_password_b = Button(TAB_1_LBF_1_3, text="დადასტურება", command=Project.update_password)

reset_password_code = Label(TAB_1_LBF_1_3, text="შეიყვანეთ ელ.ფოსტაზე მიღებული კოდი: ")
agree_password = Label(TAB_1_LBF_1_3, text="შეიყვანეთ ახალი პაროლი: ")
reset_password_string_var = StringVar()
reset_password_string_var.set("განახლების სტატუსი")
reset_status = TkLabel(TAB_1_LBF_1_3, textvariable=reset_password_string_var, fg="blue")

reset_password_code_e = Entry(TAB_1_LBF_1_3, width=7)
agree_password_e = Entry(TAB_1_LBF_1_3, width=23, state="disabled")
# Label Frame N-3 END


NB.pack(side="top", expand=1, fill="both", padx=10, pady=10)

# TAB_1  LABEL_FRAME -- 1  GRID/PACK START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TAB_1_LBF_1_1.pack(side="top", expand=0, fill="both", padx=10, pady=10)

LBF_1_LB_1.grid(row=0, column=0, sticky="W", padx=10, pady=10)
LBF_1_LB_2.grid(row=1, column=0, sticky="W", padx=10)
LBF_1_LB_3.grid(row=3, columnspan=2, sticky="W", padx=10, pady=4)
LBF_1_E_1.grid(row=0, column=0, sticky="W", padx=210)
LBF_1_E_2.grid(row=1, column=0, sticky="W", padx=210)
LBF_1_B_2.grid(row=2, column=0, sticky="W", padx=170, pady=4)
# TAB_1  LABEL_FRAME -- 1  GRID/PACK END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# TAB_1  LABEL_FRAME -- 2  GRID/PACK START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TAB_1_LBF_1_2.pack(side="top", expand=1, fill="both", padx=10, pady=10)

name.grid(row=0, column=0, sticky="W", padx=10, pady=10)
surname.grid(row=1, column=0, sticky="W", padx=10, pady=0)
gender.grid(row=2, column=0, sticky="W", padx=10, pady=10)
birth_date.grid(row=3, column=0, sticky="W", padx=10, pady=0)
name_e.grid(row=0, column=0, sticky="W", padx=210)
surname_e.grid(row=1, column=0, sticky="W", padx=210)
LBF_2_Radio_1.grid(row=2, column=0, sticky="W", padx=210)
LBF_2_Radio_2.grid(row=2, column=0, sticky="W", padx=280)
LBF_2_Combo_1.grid(row=3, column=0, sticky="W", padx=210)
LBF_2_Combo_2.grid(row=3, column=0, sticky="W", padx=300)
LBF_2_Combo_3.grid(row=3, column=0, sticky="W", padx=370)
email.grid(row=4, column=0, sticky="W", padx=10, pady=10)
email_e.grid(row=4, column=0, sticky="W", padx=210)
username.grid(row=5, column=0, sticky="W", padx=10, pady=0)
username_e.grid(row=5, column=0, sticky="W", padx=210)
password.grid(row=6, column=0, sticky="W", padx=10, pady=10)
password_e.grid(row=6, column=0, sticky="W", padx=210)
registration_b.grid(row=7, column=0, sticky="W", padx=100, ipadx=20)
reset_b.grid(row=7, column=0, sticky="W", padx=240, ipadx=20)
status_label.grid(row=8, column=0, sticky="W", padx=10, pady=7)
# TAB_1  LABEL_FRAME -- 2  GRID/PACK END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# TAB_1  LABEL_FRAME -- 3  GRID/PACK START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TAB_1_LBF_1_3.pack(side="top", expand=2, fill="both", padx=10, pady=10)

reset_password_b.grid(row=0, column=0, sticky="W", padx=135, pady=5)
reset_password_code.grid(row=1, column=0, sticky="W", padx=10, pady=0)
agree_password.grid(row=2, column=0, sticky="W", padx=10)
reset_status.grid(row=3, column=0, sticky="W", padx=10)
reset_password_code_e.grid(row=1, column=0, sticky="W", padx=274, pady=10)
agree_password_e.grid(row=2, column=0, sticky="W", padx=180)
code_agree_b.grid(row=1, column=0, sticky="W", padx=335)
agree_password_b.grid(row=2, column=0, sticky="W", padx=335)
# TAB_1  LABEL_FRAME -- 3  GRID/PACK END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<<
# >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<<
# >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<< >>> TAB 1 <<<

win.mainloop()
