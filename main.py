import PIL
import cv2
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import os
import tensorflow as tf
root = tk.Tk()
root.geometry("1100x500")
root.title('Znajdź koteczka!')
root.config(background="#252525")
obrazek = None
obrazek2 = None
gray = None
my_cascade = cv2.CascadeClassifier("cascade_cats8/cascade.xml")
cascade=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

def odswiez(self):
    #odświeżanie aplikacji
    print("ODŚWIEŻ")
    self.destroy()
    self.__init__()
    rootSetup()

def rootSetup():
    #tutaj jest zdefiniowany cały wygląd aplikacji
    gora=tk.Frame(root, width=640, height=100,background="#E8EDED")
    gora.grid(row=0, column=0, padx=10, pady=2, sticky=N )
    tk.Label(gora, text="Co i jak?", font=("Helvetica", 14), background="#E8EDED").grid(row=0, column=0, padx=10, pady=2)
    Instrukcja = tk.Label(gora,text="Wgraj zdjecie i zobacz jak z problemem znalezienia koteczka poradzi sobie \n"
                          "wytrenowany model klasyfikacji Haara, i ten udostępniony przez bibliotekę cv", font=("Helvetica",10))
    Instrukcja.grid(row=1,column=0, padx=10,pady=10)
    przyciski1 = tk.Frame(gora, width=200, height=200, background="#E8EDED")
    przyciski1.grid(row=2, column=0, padx=10, pady=2)
    wybierzBtn = tk.Button(przyciski1, text="WYBIERZ", command=Wybierz, background="#85A19D", font=("Helvetica", 12))
    wybierzBtn.grid(row=0, column=0, padx=20, pady=15)
    zamienBtn = tk.Button(przyciski1, text="ZNAJDŹ KOTKI", command=Znajdz, background="#85A19D",
                          font=("Helvetica", 12))
    zamienBtn.grid(row=0, column=1, padx=20, pady=15)
    plikFrame = tk.Frame(gora, width=200, height=200,background="#E8EDED")
    plikFrame.grid(row=3, column=0, padx=30, pady=2)
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#ECE4DB", background="#E8EDED")
    combo = ttk.Combobox(plikFrame,font=("Helvetica",10))
    combo['values'] = ("PNG", "JPG")
    combo.grid(column=0, row=0)
    combo.current(0)
    nazwaPl = tk.Text(plikFrame, width=25, height=1, takefocus=0,font=("Helvetica",10),background="#ECE4DB")
    nazwaPl.grid(row=0, column=1, padx=10, pady=2)
    nazwaPl.insert(0.0, "nowy_plik")
    zapiszFrame = tk.Frame(gora, width=200, height=100,background="#E8EDED")
    zapiszFrame.grid(row=4, column=0, padx=10, pady=2)
    zapiszBtn = tk.Button(zapiszFrame, text="ZAPISZ",background="#85A19D", font=("Helvetica",12),
                          command=lambda *args: Zapisz(nazwaPl.get("1.0", 'end-1c'), combo.get()))
    zapiszBtn.grid(row=0, column=0, padx=20, pady=15)
    prawaKolumna = tk.Frame(root, width=200, height=600,background="#E8EDED")
    prawaKolumna.grid(row=0, column=1, padx=10, pady=2, sticky=N + S)
    tk.Label(prawaKolumna, text="Zaimplementowany klasyfikator", font=("Helvetica", 14), background="#E8EDED").grid(row=0, column=0, padx=10,pady=2)
    prawaKolumna2 = tk.Frame(root, width=200, height=600, background="#E8EDED")
    prawaKolumna2.grid(row=0, column=2, padx=10, pady=2, sticky=N + S)
    tk.Label(prawaKolumna2, text="Klasyfikator z biblioteki cv2", font=("Helvetica", 14), background="#E8EDED").grid(
        row=0, column=0, padx=10, pady=2)

    if obrazek2 is not None:
        b, g, r = cv2.split(obrazek2)
        imgDisplay = cv2.merge((r, g, b))
        im = Image.fromarray(imgDisplay)
        imgtk = ImageTk.PhotoImage(image=im)
        label = tk.Label(prawaKolumna2, image=imgtk)
        label.grid(row=1,column=0,padx=10,pady=10)
    if obrazek is not None: #jeśli podano obrazki, to go wczytaj i wyświetl
        b, g, r = cv2.split(obrazek)
        imgDisplay2 = cv2.merge((r, g, b))
        im2 = Image.fromarray(imgDisplay2)
        imgtk2 = ImageTk.PhotoImage(image=im2)
        label = tk.Label(prawaKolumna, image=imgtk2)
        label.grid(row=1,column=0,padx=10,pady=10)

    root.mainloop()

def Wybierz(): #funkcja wczytująca obrazek
    filename = filedialog.askopenfilename(initialdir='/assets/', title="Select photo", filetypes=[
        ("image", ".png"),
        ("image", ".jpg"),
    ])
    global obrazek, obrazek2
    obrazek2 = cv2.imread(filename, -1)
    obrazek = cv2.imread(filename, -1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    odswiez(root)

def Znajdz():
    gray = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
    faces = my_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(24, 24),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("Found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(obrazek, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gray = cv2.cvtColor(obrazek, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(24, 24),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("Found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(obrazek2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    odswiez(root)


def Zapisz(nazwa, typ): #zapis obrazka do pliku
    if typ == "PNG":
        cv2.imwrite("%s.png" % nazwa, obrazek)
    elif typ == "JPG":
        cv2.imwrite("%s.jpg" % nazwa, obrazek)


rootSetup()