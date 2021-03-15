from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, askdirectory
from time import time, sleep
import pandas as pd
import os
import datetime
from datetime import datetime
from PIL import ImageTk
from PIL import Image
import PIL.Image
from tkinter import ttk, filedialog
from tkinter import messagebox


class job:
    def __init__(self, root):
        self.root = root

        self.root.title('GESTION DE FLUX MECANIQUE')
        self.z = '0'
        self.x = 600
        self.y = 700
        self.root.geometry('%sx%s' % (self.x, self.y))
        root.resizable(width=0, height=0)
        fp = open("im.jpeg", "rb")
        img = PIL.Image.open(fp)
        img = img.resize((600, 700))

        self.limage = ImageTk.PhotoImage(img)

        self.label2 = Label(self.root, image=self.limage)
        self.label2.grid(row=0, column=0)
        self.button = Button(self.root, text="COMMENCER", width=35, bg="white", height=2,
                             command=lambda: self.debut())
        self.button.place(x=190, y=600)
        self.cb = "#dadce0"

        self.cb2 = "white"
        self.cf = "black"
        self.esimultem = StringVar()
        self.esimul0 = StringVar()
        self.esimul1 = StringVar()
        self.esimul2 = StringVar()
        self.esimul3 = StringVar()
        self.esimul4 = StringVar()
        self.esimul5 = StringVar()
        self.esimul6 = StringVar()
        self.esimul7 = StringVar()
        self.esimul8 = StringVar()
        self.epostpro1 = StringVar()
        self.epostpro2 = StringVar()
        self.epostpro3 = StringVar()
        self.file_path = StringVar()
        self.vtime = StringVar()
        self.esolv1 = StringVar()
        self.esolv2 = StringVar()
        self.esolv3 = StringVar()
        self.esolv4 = StringVar()

    def debut(self):  # page de démarage
        self.label2.destroy()
        self.button.destroy()
        self.create_frame1()
        self.create_frame2()
        self.create_button()

    def create_frame1(self):  # creation frame1 ou se trouve les button pre-processeur solver ....
        self.f1 = Frame(self.root, width=self.x, height=25, bg="white")
        self.f1.grid(row=0, column=0)
        self.f1.grid_propagate(0)

    def create_frame2(self):  # creation frame1 ou se trouve les button pre-processeur solver ....
        self.f2 = Frame(self.root, width=self.x, height=self.y - 20, bg=self.cb2)
        self.f2.grid(row=1, column=0)
        self.f2.grid_propagate(0)

    def create_button(self):  # creation frame1 ou se trouve les button pre-processeur solver ....
        self.button_pre_processing = Button(self.f1, text="PRE-PROCESSING", bg=self.cb,
                                            command=lambda: self.Preprocessing(), relief=GROOVE, width=18, fg=self.cf)
        self.button_pre_processing.place(x=20, y=0)
        self.button_solver = Button(self.f1, text="SOLVER", bg=self.cb, command=lambda: self.Solver(), width=18,
                                    fg=self.cf)
        self.button_solver.place(x=300, y=0)
        self.button_simulation = Button(self.f1, text="SIMULATION", command=lambda: self.Simulation(), bg=self.cb,
                                        width=18, fg=self.cf)
        self.button_simulation.place(x=160, y=0)
        self.button_post_proccessing = Button(self.f1, text="POST-PROCESSING", bg=self.cb,
                                              command=lambda: self.Postprocessing(), width=18, fg=self.cf)
        self.button_post_proccessing.place(x=440., y=0)
        ##### pour changement des  couleur auto ################
        # self.button_pre_processing.bind("<Enter>", lambda event: self.on_enter(self.button_pre_processing))
        # self.button_pre_processing.bind("<Leave>", lambda event: self.on_leave(self.button_pre_processing))
        # self.button_solver.bind("<Enter>", lambda event: self.on_enter(self.button_solver))
        # self.button_solver.bind("<Leave>", lambda event: self.on_leave(self.button_solver))
        # self.button_simulation.bind("<Enter>", lambda event: self.on_enter(self.button_simulation))
        # self.button_simulation.bind("<Leave>", lambda event: self.on_leave(self.button_simulation))
        # self.button_post_proccessing.bind("<Enter>", lambda event: self.on_enter(self.button_post_proccessing))
        # self.button_post_proccessing.bind("<Leave>", lambda event: self.on_leave(self.button_post_proccessing))
        ####################################################################

    def set_emplacement(self, v):

        # self.FILETYPES = [("text files", "*.xlsx")]
        self.chemin1 = (askdirectory())

        if self.chemin1 != '':
            print("ok")

        if v == 1:
            self.chemin = self.chemin1 + '/' + self.epostpro1.get() + ".dat"
            self.epostpro1.set(self.chemin)
            outfile = open(self.chemin, "w")
        if v == 2:
            self.chemin = self.chemin1 + '/' + self.epostpro2.get() + ".dat"
            self.epostpro2.set(self.chemin)
            outfile = open(self.chemin, "w")

        if v == 3:
            self.chemin = self.chemin1 + '/' + self.epostpro3.get() + ".vtu"
            self.epostpro3.set(self.chemin)
            outfile = open(self.chemin, "w")

    def save(self):
        import pyeuler3d.config as config
        cfg= config.config("ab",SPEED_OPTION=config.SPD_OPTION_MACH )
        cfg.write2file( "ABR")
        return
        outfile = open("fichier_test.txt", "w")
        vl = StringVar()
        ma = StringVar()
        vl.set("0")
        ma.set("0")
        if self.esimul0.get() == "VELOCITY":
            vl.set("1")
        if self.esimul0.get() == "MACH":
            ma.set("1")
        outfile.write("-------------------------------------------------------------------------------\n"
                      "%%%%%%%%%%%%%%%%     EES2D Software Input file    %%%%%%%%%%%%%%%%%%%%% \n\n"
                      "Author : EES2D GUI\n" \
                      "Simulation Title :  \n" \
                      f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

                      "-------------------------------------------------------------------------------\n"
                      "\nSTART\n\n"
                      "------------------- PRE-PROCESSING CONTROL -------------------\n\n"
                      "MESH_FORMAT = SU2 \n\n"
                      "MESH FILE " + self.file_path.get() + "\n\n"

                                                            "MESH_TYPE = UNSTRUCTURED\n\n"
                                                            "------------------- SIMULATION CONTROL -------------------\n\n" +
                      "SPEED_OPTION: " + self.esimul0.get() + "\n\n" +
                      "SPEED VALUE: " + self.esimul1.get() + "\n\n" +
                      "VELOCITY = " + vl.get() + "\n\n" +
                      "MACH = " + ma.get() + "\n\n"
                                             "AOA = " + self.esimul2.get() + "\n\n"
                                                                             "AIRFLOW_PRESSURE = " + self.esimul3.get() + "\n\n" +  # + "Pa"
                      "AIRFLOW_TEMPERATURE =" + self.esimultem.get() + "\n\n"  # + " K" 

                                                                       "ANGLE OF ATTAQUE: " + self.esimul2.get() + "\n\n" +  # + "Deg"
                      "AIRFLOW_VISCOSITY = " + self.esimul4.get() + "\n\n" +  # + "Ns/m^2"
                      "AIRFLOW_DENSITY" + self.esimul5.get() + "\n\n" +  # + "Kg/m^3"

                      "GAMMA = " + self.esimul6.get() + "\n\n" +
                      "GAS_CONSTANT = " + self.esimul7.get() + "\n\n" +  # + "J/Kg.X"
                      "SPECIFIC_HEAT = " + self.esimul8.get() + "\n\n" +  # + "J/Kg.K"
                      "------------------- SOLVER CONTROL -------------------\n\n" +
                      "SCHEME = ROE\n\n" +
                      "TIME_INTEGRATION = " + self.vtime.get() + "\n\n"
                                                                 "CFL = " + self.esolv1.get() + "\n\n" +
                      "MIN_RESIDUAL = " + self.esolv2.get() + "\n\n" +
                      "MAX_ITER = " + self.esolv3.get() + "\n\n" +
                      "OPEMMP_THREADS_NUM = " + self.esolv4.get() + "\n\n" +
                      "------------------- POST-PROCESSING CONTROL -------------------\n\n" +
                      "RESIDUAL_FILE = " + self.epostpro2.get() + "\n\n" +
                      "PRESSURE_FILE = " + self.epostpro1.get() + "\n\n" +
                      "OUTPUT_FORMAT = VTK\n\n"
                      "OUTPUT_FILE = " + self.epostpro3.get() + "\n\n" +
                      "GENERATE_LOG = YES\n\n" +
                      "END")
        outfile.write("\n")
        outfile.close()
        messagebox.showinfo('info', 'les info sont bien \n enregistrées')

    def on_enter(self, event):  # pour change la coleur des button lorsque on les cursor

        event['background'] = '#85C1E9'

    def on_leave(self, event):  # pour change la coleur des button lorsque on les cursor
        event['background'] = self.cb

    def ReadFile1(self, f, w):

        name1 = askopenfilename(initialdir="/",
                                filetypes=(("Text File", "*." + f + ""), ("All Files", "*.*")),
                                title="Choose a file."
                                )
        # Using try in case user types in unknown file or closes without choosing a file.
        print("name", name1)
        try:
            with open(name1, 'x') as UseFile:
                print(name1)
                w.set(name1)
        except:
            print("No file exists")
            w.set(name1)

    def OpenFile1(self):
        name1 = askopenfilename(initialdir="/",
                                filetypes=(("Text File", "*.su2"), ("All Files", "*.*")),
                                title="Choose a file."
                                )
        path = os.getcwd()
        print(name1 + path)
        self.file_path.set(name1)
        # Using try in case user types in unknown file or closes without choosing a file.
        try:
            with open(name1, 'r') as UseFile:
                print(name1)
        except:
            print("No file exists")

    def Solver(self):

        self.f2.destroy()
        self.create_frame2()
        self.button_solver.configure(bg="white")
        self.button_simulation.configure(bg=self.cb)
        self.button_post_proccessing.configure(bg=self.cb)
        self.button_pre_processing.configure(bg=self.cb)

        labelsolv1 = Label(self.f2, font=("Arial", 10),
                           text="TIME INTEGRATION:")
        labelsolv1.place(x=50, y=100)
        listeProduits = ["Runge-Kutta", "Explicite EULER"]
        # 3) - Création de la Combobox via la méthode ttk.Combobox()

        listeCombo = ttk.Combobox(self.f2, values=listeProduits, textvariable=self.vtime)
        # 4) - Choisir l'élément qui s'affiche par défaut
        # listeCombo.current(0)
        listeCombo.place(x=250, y=100)
        labelsolv2 = Label(self.f2, font=("Arial", 10),
                           text="CFL:", )
        labelsolv2.place(x=50, y=200)

        entrysolv2 = Entry(self.f2, textvariable=self.esolv1, width="50")
        entrysolv2.place(x=250, y=200)
        labelsolv3 = Label(self.f2, font=("Arial", 10),
                           text="MAXIMAL RESIDUEL:")
        labelsolv3.place(x=50, y=300)

        entrysolv3 = Entry(self.f2, textvariable=self.esolv2, width="30")
        entrysolv3.place(x=250, y=300)

        labelsolv4 = Label(self.f2, font=("Arial", 10),
                           text="MAX ITERACTIONS NUMBER:")
        labelsolv4.place(x=50, y=400)

        entrysolv4 = Entry(self.f2, textvariable=self.esolv3, width="30")
        entrysolv4.place(x=250, y=400)

        labelsolv5 = Label(self.f2, font=("Arial", 10),
                           text="NUMBER OF THREA:")
        labelsolv5.place(x=50, y=500)

        entrysolv5 = Entry(self.f2, textvariable=self.esolv4, width="30")
        entrysolv5.place(x=250, y=500)
        boutonc_1 = Button(self.f2, font=("Arial", 10), text="RUN SOLVER", background=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command='')
        boutonc_1.place(x=150, y=600)

        boutonc_2 = Button(self.f2, font=("Arial", 10), text="CONTROLE GENERATE FILE", bg=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command=lambda: "")
        boutonc_2.place(x=300, y=600)

        ##### pour changement des  couleur auto ################
        boutonc_1.bind("<Enter>", lambda event: self.on_enter(boutonc_1))
        boutonc_1.bind("<Leave>", lambda event: self.on_leave(boutonc_1))
        boutonc_2.bind("<Enter>", lambda event: self.on_enter(boutonc_2))
        boutonc_2.bind("<Leave>", lambda event: self.on_leave(boutonc_2))
        ####################################################################

    def Preprocessing(self):

        def save_info():
            entry_info = self.file_path.get()
            print(entry_info)
            # file = open("fichier_test.txt", "w")

        self.f2.destroy()
        self.create_frame2()
        self.button_solver.configure(bg=self.cb)
        self.button_simulation.configure(bg=self.cb)
        self.button_post_proccessing.configure(bg=self.cb)
        self.button_pre_processing.configure(bg='white')
        label1 = Label(self.f2, font=("Arial", 10),
                       text="MESH FILE \n (SU2 FORMAT):")
        label1.place(x=80, y=200)

        self.entry1 = Entry(self.f2, textvariable=self.file_path, width="30")
        self.entry1.place(x=200, y=200)

        open_button = Button(self.f2, font=("Arial", 10), text="...", command=lambda: self.OpenFile1(), underline=0)
        open_button.place(x=400, y=200)

        boutonc_1 = Button(self.f2, font=("Arial", 10), text="RUN SOLVER", background=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command='')
        boutonc_1.place(x=150, y=400)

        boutonc_2 = Button(self.f2, font=("Arial", 10), text="CONTROLE GENERATE FILE", bg=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command=lambda: save_info())
        boutonc_2.place(x=300, y=400)
        ##### pour changement des  couleur auto ################
        boutonc_1.bind("<Enter>", lambda event: self.on_enter(boutonc_1))
        boutonc_1.bind("<Leave>", lambda event: self.on_leave(boutonc_1))
        boutonc_2.bind("<Enter>", lambda event: self.on_enter(boutonc_2))
        boutonc_2.bind("<Leave>", lambda event: self.on_leave(boutonc_2))
        ####################################################################

    def Simulation(self):

        self.f2.destroy()
        self.create_frame2()
        self.button_solver.configure(bg=self.cb)
        self.button_simulation.configure(bg='white')
        self.button_post_proccessing.configure(bg=self.cb)
        self.button_pre_processing.configure(bg=self.cb)
        labelsimul1 = Label(self.f2, font=("Arial", 10),
                            text="Speed Type:")
        labelsimul1.place(x=50, y=50)

        listeProduits = ["MACH", "VELOCITY"]
        # 3) - Création de la Combobox via la méthode ttk.Combobox()
        # self.esimul0.set("MACH")
        self.listeCombo1 = ttk.Combobox(self.f2, values=listeProduits, textvariable=self.esimul0)
        # 4) - Choisir l'élément qui s'affiche par défaut
        # self.listeCombo1.current(0)
        self.listeCombo1.place(x=300, y=50)

        labelsimul2 = Label(self.f2, font=("Arial", 10),
                            text="SPEED VALUE:")
        labelsimul2.place(x=50, y=100)

        entrysimul2 = Entry(self.f2, textvariable=self.esimul1, width="30")
        entrysimul2.place(x=300, y=100)

        labelsimul3 = Label(self.f2, font=("Arial", 10),
                            text="ANGLE OF ATTAQUE:")
        labelsimul3.place(x=50, y=150)

        entrysimul3 = Entry(self.f2, textvariable=self.esimul2, width="30")
        entrysimul3.place(x=300, y=150)

        labelsimul4 = Label(self.f2, font=("Arial", 10),
                            text="Deg")
        labelsimul4.place(x=500, y=150)

        labelsimul5 = Label(self.f2, font=("Arial", 10),
                            text="PRESSURE:")
        labelsimul5.place(x=50, y=200)

        self.esimul3.set("101325")
        entrysimul5 = Entry(self.f2, textvariable=self.esimul3, width="30")
        entrysimul5.place(x=300, y=200)

        labelsimul6 = Label(self.f2, font=("Arial", 10),
                            text="Pa")
        labelsimul6.place(x=500, y=200)

        #########tem
        labelsimul55 = Label(self.f2, font=("Arial", 10),
                             text="TEMPERATURE:")
        labelsimul55.place(x=50, y=250)

        self.esimultem.set("288.15")
        entrysimul55 = Entry(self.f2, textvariable=self.esimultem, width="30")
        entrysimul55.place(x=300, y=250)

        labelsimul66 = Label(self.f2, font=("Arial", 10),
                             text="K")
        labelsimul66.place(x=500, y=250)

        #########

        labelsimul7 = Label(self.f2, font=("Arial", 10),
                            text="VISCOSITY:")
        labelsimul7.place(x=50, y=300)

        self.esimul4.set('1.853e-5')
        entrysimul6 = Entry(self.f2, textvariable=self.esimul4, width="30")
        entrysimul6.place(x=300, y=300)

        labelsimul8 = Label(self.f2, font=("Arial", 10),
                            text="Ns/m^2")
        labelsimul8.place(x=500, y=300)

        labelsimul9 = Label(self.f2, font=("Arial", 10),
                            text="DENSITY:")
        labelsimul9.place(x=50, y=350)

        self.esimul5.set('1.2886')
        entrysimul7 = Entry(self.f2, textvariable=self.esimul5, width="30")
        entrysimul7.place(x=300, y=350)

        labelsimul10 = Label(self.f2, font=("Arial", 10),
                             text="Kg/m^3")
        labelsimul10.place(x=500, y=350)

        labelsimul11 = Label(self.f2, font=("Arial", 10),
                             text="GAMMA:")
        labelsimul11.place(x=50, y=400)  #

        self.esimul6.set("1.4")
        entrysimul8 = Entry(self.f2, textvariable=self.esimul6, width="30")
        entrysimul8.place(x=300, y=400)  #

        labelsimul12 = Label(self.f2, font=("Arial", 10),
                             text="GAS CONSTANT:")
        labelsimul12.place(x=50, y=450)

        self.esimul7.set("287.058")
        entrysimul9 = Entry(self.f2, textvariable=self.esimul7, width="30")
        entrysimul9.place(x=300, y=450)

        labelsimul13 = Label(self.f2, font=("Arial", 10),
                             text="J/Kg.X")
        labelsimul13.place(x=500, y=450)

        labelsimul14 = Label(self.f2, font=("Arial", 10),
                             text="SPECIFIC HEATH:")
        labelsimul14.place(x=50, y=500)

        self.esimul8.set('1004.7')
        entrysimul10 = Entry(self.f2, textvariable=self.esimul8, width="30")
        entrysimul10.place(x=300, y=500)

        labelsimul15 = Label(self.f2, font=("Arial", 10),
                             text="J/Kg.K")
        labelsimul15.place(x=500, y=500)

        def save_info():
            simentry1_info = self.esimul1.get()
            simentry2_info = self.esimul2.get()
            simentry3_info = self.esimul3.get()
            simentry4_info = self.esimul4.get()
            simentry5_info = self.esimul5.get()
            simentry6_info = self.esimul6.get()
            simentry7_info = self.esimul7.get()
            simentry8_info = self.esimul8.get()
            print(simentry1_info)
            print(simentry2_info)
            print(simentry3_info)
            print(simentry4_info)

            print(simentry5_info)
            print(simentry6_info)
            print(simentry7_info)
            print(simentry8_info)

        boutonc_1 = Button(self.f2, font=("Arial", 10), text="RUN SOLVER", background=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command='')
        boutonc_1.place(x=150, y=600)

        boutonc_2 = Button(self.f2, font=("Arial", 10), text="CONTROLE GENERATE FILE", bg=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command=lambda: save_info())
        boutonc_2.place(x=300, y=600)

        ##### pour changement des  couleur auto ################
        boutonc_1.bind("<Enter>", lambda event: self.on_enter(boutonc_1))
        boutonc_1.bind("<Leave>", lambda event: self.on_leave(boutonc_1))
        boutonc_2.bind("<Enter>", lambda event: self.on_enter(boutonc_2))
        boutonc_2.bind("<Leave>", lambda event: self.on_leave(boutonc_2))
        ####################################################################

    def Postprocessing(self):

        self.f2.destroy()
        self.create_frame2()
        self.button_solver.configure(bg=self.cb)
        self.button_simulation.configure(bg=self.cb)
        self.button_post_proccessing.configure(bg='white')
        self.button_pre_processing.configure(bg=self.cb)
        labelpostproces1 = Label(self.f2, font=("Arial", 10),
                                 text="Pressure File:")
        labelpostproces1.place(x=50, y=100)

        entrypostproces1 = Entry(self.f2, textvariable=self.epostpro1, width="50", )
        entrypostproces1.place(x=200, y=100)

        open_buttonpost1 = Button(self.f2, font=("Arial", 10), text="...", command=lambda: self.set_emplacement(1))
        open_buttonpost1.place(x=550, y=100)

        labelprocess2 = Label(self.f2, font=("Arial", 10),
                              text="RESIDUAL FILE:")
        labelprocess2.place(x=50, y=200)

        entrypostproces2 = Entry(self.f2, textvariable=self.epostpro2, width="50")
        entrypostproces2.place(x=200, y=200)

        open_buttonpost2 = Button(self.f2, font=("Arial", 10), text="...", command=lambda: self.set_emplacement(2))
        open_buttonpost2.place(x=550, y=200)

        labelprocess3 = Label(self.f2, font=("Arial", 10),
                              text="OUTPUT VTK FILE:")
        labelprocess3.place(x=50, y=300)

        entrypostproces3 = Entry(self.f2, textvariable=self.epostpro3, width="50")
        entrypostproces3.place(x=200, y=300)

        open_buttonpost3 = Button(self.f2, font=("Arial", 10), text="...", command=lambda: self.set_emplacement(3))
        open_buttonpost3.place(x=550, y=300)

        def save_info():
            proentry1_info = self.epostpro1.get()
            proentry2_info = self.epostpro2.get()
            proentry3_info = self.epostpro3.get()
            print(proentry1_info)
            print(proentry2_info)
            print(proentry3_info)

        boutonc_1 = Button(self.f2, font=("Arial", 10), text="RUN SOLVER", background=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command='')
        boutonc_1.place(x=150, y=600)

        boutonc_2 = Button(self.f2, font=("Arial", 10), text="CONTROLE GENERATE FILE", bg=self.cb, fg=self.cf,
                           borderwidth=2, relief='ridge', command=lambda: self.save())
        boutonc_2.place(x=300, y=600)

        ##### pour changement des  couleur auto ################
        boutonc_1.bind("<Enter>", lambda event: self.on_enter(boutonc_1))
        boutonc_1.bind("<Leave>", lambda event: self.on_leave(boutonc_1))
        boutonc_2.bind("<Enter>", lambda event: self.on_enter(boutonc_2))
        boutonc_2.bind("<Leave>", lambda event: self.on_leave(boutonc_2))
        ####################################################################


if __name__ == '__main__':
    root = Tk()
    job(root)
    root.mainloop()