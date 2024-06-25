import math
import cv2
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
global calculated
calculated = 0

def openFile():
    global my_image_resized
    global my_image
    filename = filedialog.askopenfilename(initialdir=os.getcwd() + "\images", title="Wybierz plik", filetypes=(("BMP Files *.bmp", "*.bmp"), ("All Files *.*", "*.*")))
    img = cv2.imread(filename)
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, img_th = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY)
    my_image = Image.fromarray(img_th)
    my_image_resized = ImageTk.PhotoImage(my_image.resize((276, 276), Image.Resampling.LANCZOS))
    labelOfImage1.configure(image=my_image_resized, bg="white")
    labelOfImage1.image = my_image_resized
    startAlgorithmButton.configure(state="active")

def resultRotation(rotation, resultImage):
    couter = 0
    x, y = my_image.size
    result_0 = Image.new('RGBA',(x, y))
    result_45 = Image.new('RGBA',(x, y))
    result_90 = Image.new('RGBA',(x, y))
    result_135 = Image.new('RGBA',(x, y))

    if rotation == 0:
        for i in range(x - 1):
            for j in range(y - 1):
                if my_image.getpixel((i, j)) < 1:
                    resultImage.putpixel((i, j), (0, 0, 0))
                if j < y - 1:
                    if my_image.getpixel((i, j)) < my_image.getpixel((i, j + 1)):
                        result_0.putpixel((i, j), (255, 0, 0))
                        resultImage.putpixel((i-1, j-1), (147, 246, 0))
                        resultImage.putpixel((i-1, j), (147, 246, 0))
                        resultImage.putpixel((i-1, j+1), (147, 246, 0))
                        resultImage.putpixel((i, j-1), (147, 246, 0))
                        resultImage.putpixel((i, j), (147, 246, 0))
                        resultImage.putpixel((i, j+1), (147, 246, 0))
                        resultImage.putpixel((i+1, j-1), (147, 246, 0))
                        resultImage.putpixel((i+1, j), (147, 246, 0))
                        resultImage.putpixel((i+1, j+1), (147, 246, 0))
                        couter += 1
        return result_0, couter, resultImage
    elif rotation == 45:
        for i in range(x - 1):
            for j in range(y - 1):
                if i > 0 or j < y - 1:
                    if my_image.getpixel((i, j)) < my_image.getpixel((i - 1, j + 1)):
                        result_45.putpixel((i, j), (255, 0, 0))
                        resultImage.putpixel((i-1, j-1), (147, 246, 0))
                        resultImage.putpixel((i-1, j), (147, 246, 0))
                        resultImage.putpixel((i-1, j+1), (147, 246, 0))
                        resultImage.putpixel((i, j-1), (147, 246, 0))
                        resultImage.putpixel((i, j), (147, 246, 0))
                        resultImage.putpixel((i, j+1), (147, 246, 0))
                        resultImage.putpixel((i+1, j-1), (147, 246, 0))
                        resultImage.putpixel((i+1, j), (147, 246, 0))
                        resultImage.putpixel((i+1, j+1), (147, 246, 0))
                        couter += 1
        return result_45, couter, resultImage
    elif rotation == 90:
        for i in range(x - 1):
            for j in range(y - 1):
                if i > 0:
                    if my_image.getpixel((i, j)) < my_image.getpixel((i - 1, j)):
                        result_90.putpixel((i, j), (255, 0, 0))
                        resultImage.putpixel((i-1, j-1), (147, 246, 0))
                        resultImage.putpixel((i-1, j), (147, 246, 0))
                        resultImage.putpixel((i-1, j+1), (147, 246, 0))
                        resultImage.putpixel((i, j-1), (147, 246, 0))
                        resultImage.putpixel((i, j), (147, 246, 0))
                        resultImage.putpixel((i, j+1), (147, 246, 0))
                        resultImage.putpixel((i+1, j-1), (147, 246, 0))
                        resultImage.putpixel((i+1, j), (147, 246, 0))
                        resultImage.putpixel((i+1, j+1), (147, 246, 0))
                        couter += 1
        return result_90, couter, resultImage
    elif rotation == 135:
        for i in range(x - 1):
            for j in range(y - 1):
                if i > 0 or j > 0:
                    if my_image.getpixel((i, j)) < my_image.getpixel((i - 1, j - 1)):
                        result_135.putpixel((i, j), (255, 0, 0))
                        resultImage.putpixel((i-1, j-1), (147, 246, 0))
                        resultImage.putpixel((i-1, j), (147, 246, 0))
                        resultImage.putpixel((i-1, j+1), (147, 246, 0))
                        resultImage.putpixel((i, j-1), (147, 246, 0))
                        resultImage.putpixel((i, j), (147, 246, 0))
                        resultImage.putpixel((i, j+1), (147, 246, 0))
                        resultImage.putpixel((i+1, j-1), (147, 246, 0))
                        resultImage.putpixel((i+1, j), (147, 246, 0))
                        resultImage.putpixel((i+1, j+1), (147, 246, 0))
                        couter += 1
        return result_135, couter, resultImage
    else:
        raise ValueError

def startAlgorithm():
    global calculated
    global currentIcon
    calculated = 1
    x, y = my_image.size
    resultImage = Image.new('RGBA',(x, y))
    img_0 = resultRotation(0, resultImage)
    img_45 = resultRotation(45, img_0[2])
    img_90 = resultRotation(90, img_45[2])
    img_135 = resultRotation(135, img_90[2])
    
    croftonResult = math.pi / 4 * (1*(img_0[1] + img_90[1]) + 1/math.sqrt(2) * (img_45[1] + img_135[1]))

    resultImage_0 = ImageTk.PhotoImage(img_0[0].resize((230, 230), Image.Resampling.LANCZOS))
    resultImage_45 = ImageTk.PhotoImage(img_45[0].resize((230, 230), Image.Resampling.LANCZOS))
    resultImage_90 = ImageTk.PhotoImage(img_90[0].resize((230, 230), Image.Resampling.LANCZOS))
    resultImage_135 = ImageTk.PhotoImage(img_135[0].resize((230, 230), Image.Resampling.LANCZOS))
    resultImage2 = ImageTk.PhotoImage(img_135[2].resize((230, 230), Image.Resampling.LANCZOS))

    labelOfResult1.configure(image=resultImage_0, bg="white")
    labelOfResult1.image = resultImage_0
    labelOfResult2.configure(image=resultImage_45, bg="white")
    labelOfResult2.image = resultImage_45
    labelOfResult3.configure(image=resultImage_90, bg="white")
    labelOfResult3.image = resultImage_90
    labelOfResult4.configure(image=resultImage_135, bg="white")
    labelOfResult4.image = resultImage_135
    if currentIcon == 1:
        labelOfTextCouter1.configure(text="Wynik: " + str(img_0[1]) + "px")
        labelOfTextCouter2.configure(text="Wynik: " + str(img_45[1]) + "px")
        labelOfTextCouter3.configure(text="Wynik: " + str(img_90[1]) + "px")
        labelOfTextCouter4.configure(text="Wynik: " + str(img_135[1]) + "px")
        labelOfTextResult.configure(text="Wynik końcowy:\n" + str(round(croftonResult, 2)) + "px")
    else:
        labelOfTextCouter1.configure(text="Result: " + str(img_0[1]) + "px")
        labelOfTextCouter2.configure(text="Result: " + str(img_45[1]) + "px")
        labelOfTextCouter3.configure(text="Result: " + str(img_90[1]) + "px")
        labelOfTextCouter4.configure(text="Result: " + str(img_135[1]) + "px")
        labelOfTextResult.configure(text="Final result:\n" + str(round(croftonResult, 2)) + "px")
    
    labelOfImage2.configure(image=resultImage2, bg="white")
    labelOfImage2.image = resultImage2

# Zmiana języka programu
def changeLanguage():
    global calculated
    global currentIcon
    if currentIcon == 1:
        sciezka = os.getcwd() + "\icons\\pol.png"
        polIcon = PhotoImage(file = sciezka)
        changeLanguageButton.configure(image=polIcon)
        changeLanguageButton.image = polIcon
        currentIcon = 2

        labelOfTitle.configure(text="Crofton\n  Formula")
        openFileButton.configure(text="Open File")
        labelOfTextTitle1.configure(text="Projection 0°")
        labelOfTextTitle2.configure(text="Projection 45°")
        labelOfTextTitle3.configure(text="Projection 90°")
        labelOfTextTitle4.configure(text="Projection 135°")
        startAlgorithmButton.configure(text="Calculate\nthe projection")
        if calculated != 0:
            startAlgorithm()
    elif currentIcon == 2:
        sciezka = os.getcwd() + "\icons\\ang.png"
        angIcon = PhotoImage(file = sciezka)
        changeLanguageButton.configure(image=angIcon)
        changeLanguageButton.image = angIcon
        currentIcon = 1

        labelOfTitle.configure(text="Metoda\n  Croftona")
        openFileButton.configure(text="Otwórz plik")
        labelOfTextTitle1.configure(text="Rzut 0°")
        labelOfTextTitle2.configure(text="Rzut 45°")
        labelOfTextTitle3.configure(text="Rzut 90°")
        labelOfTextTitle4.configure(text="Rzut 135°")
        startAlgorithmButton.configure(text="Oblicz\nrzuty")
        if calculated != 0:
            startAlgorithm()

# Tworzenie okna
root = Tk()
root.title('Crofton')
root.geometry("1024x576")
root.minsize(height=576, width=1024)

# Ustawienie kolumn w oknie
Grid.columnconfigure(root, 0, weight=15)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=25)
Grid.columnconfigure(root, 2, weight=15)

# Wstawienie kolumn do okna
leftFrame = Frame(root, bg="#a5a58d")
leftFrame.grid(row=0, column=0, sticky="nsew")
middleFrame = Frame(root, bg="#b7b7a4")
middleFrame.grid(row=0, column=1, sticky="nsew")
rightFrame = Frame(root, bg="#a5a58d")
rightFrame.grid(row=0, column=2, sticky="nsew")

# Wstawienie elementów do pierwszej kolumny
labelOfTitle = Label(leftFrame, bg="#a5a58d", text="Metoda\n  Croftona", font=("Georgia", 26))
labelOfTitle.place(relwidth=0.55, relheight=0.12, relx = 0.04, rely=0.05, )
labelOfImage1 = Label(leftFrame, bg="#a5a58d", bd=2, relief='solid') 
labelOfImage1.place(relwidth=0.8, relheight=0.39, relx = 0.1, rely=0.22)
openFileButton = Button(leftFrame, text="Otwórz plik", command=openFile, font=("Arial", 14))
openFileButton.place(relwidth=0.5, relheight=0.1, relx = 0.25, rely=0.85)

# Wstawienie elementów do drugiej kolumny
labelOfTextTitle1 = Label(middleFrame, bg="#b7b7a4", text="Rzut 0°", font=("Arial", 16))
labelOfTextTitle1.place(relwidth=0.32, relheight=0.04, relx = 0.12, rely=0.003)
labelOfResult1 = Label(middleFrame, bg="#b7b7a4", bd=2, relief='solid')
labelOfResult1.place(relwidth=0.4, relheight=0.32, relx = 0.06, rely=0.045)
labelOfTextCouter1 = Label(middleFrame, bg="#b7b7a4", font=("Arial", 14))
labelOfTextCouter1.place(relwidth=0.25, relheight=0.04, relx = 0.15, rely=0.365)
labelOfTextTitle2 = Label(middleFrame, bg="#b7b7a4", text="Rzut 45°", font=("Arial", 16))
labelOfTextTitle2.place(relwidth=0.32, relheight=0.04, relx = 0.6, rely=0.003)
labelOfResult2 = Label(middleFrame, bg="#b7b7a4", bd=2, relief='solid')
labelOfResult2.place(relwidth=0.4, relheight=0.32, relx = 0.54, rely=0.045)
labelOfTextCouter2 = Label(middleFrame, bg="#b7b7a4", font=("Arial", 14))
labelOfTextCouter2.place(relwidth=0.25, relheight=0.04, relx = 0.63, rely=0.365)
labelOfTextTitle3 = Label(middleFrame, bg="#b7b7a4", text="Rzut 90°", font=("Arial", 16))
labelOfTextTitle3.place(relwidth=0.32, relheight=0.04, relx = 0.12, rely=0.435)
labelOfResult3 = Label(middleFrame, bg="#b7b7a4", bd=2, relief='solid')
labelOfResult3.place(relwidth=0.4, relheight=0.32, relx = 0.06, rely=0.48)
labelOfTextCouter3 = Label(middleFrame, bg="#b7b7a4", font=("Arial", 14))
labelOfTextCouter3.place(relwidth=0.25, relheight=0.04, relx = 0.15, rely=0.8)
labelOfTextTitle4 = Label(middleFrame, bg="#b7b7a4", text="Rzut 135°", font=("Arial", 16))
labelOfTextTitle4.place(relwidth=0.32, relheight=0.04, relx = 0.6, rely=0.435)
labelOfResult4 = Label(middleFrame, bg="#b7b7a4", bd=2, relief='solid')
labelOfResult4.place(relwidth=0.4, relheight=0.32, relx = 0.54, rely=0.48)
labelOfTextCouter4 = Label(middleFrame, bg="#b7b7a4", font=("Arial", 14))
labelOfTextCouter4.place(relwidth=0.25, relheight=0.04, relx = 0.63, rely=0.8)
startAlgorithmButton = Button(middleFrame, text="Oblicz \nRzuty", command=startAlgorithm, state="disabled", font=("Arial", 14))
startAlgorithmButton.place(relwidth=0.5, relheight=0.1, relx = 0.25, rely=0.85)

# Wstawienie elementów do trzeciej kolumny
currentIcon = 1
sciezka = os.getcwd() + "\icons\\ang.png"
photo = PhotoImage(file = sciezka)
changeLanguageButton = Button(rightFrame, image=photo, command=changeLanguage)
changeLanguageButton.place(width=48, height=32, relx = 0.7, rely=0.02)
changeLanguageButton.image = photo
labelOfImage2 = Label(rightFrame, bg="#a5a58d", bd=2, relief='solid')
labelOfImage2.place(relwidth=0.8, relheight=0.39, relx = 0.1, rely=0.22)
labelOfTextResult = Label(rightFrame, bg="#a5a58d", font=("Arial", 24))
labelOfTextResult.place(relwidth=0.85, relheight=0.12, relx = 0.07, rely=0.64)

# Zapakowanie wszystkiego do okna
root.mainloop()