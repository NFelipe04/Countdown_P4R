import tkinter as tk
from countdown import countdown
import cv2
from PIL import Image, ImageTk


def criar_interface():


    janela = tk.Tk()

    janela.title("Persona 4 Revival")
    janela.geometry("1900x1200")

    intro = cv2.VideoCapture("assets/midia/Intro.mp4")


    canvas = tk.Canvas(
        janela,
        highlightthickness = 0
    )

    canvas.pack(
        fill = "both",
        expand = True
    )



    #BACKGROUND-PROGRAMA
#=======================================================================================================================

    background = tk.PhotoImage(file="assets/midia/ClassroomP4R.png")

    logo = Image.open("assets/midia/P4R_Logo.png")
    logo = logo.resize((400, 262))
    logo = ImageTk.PhotoImage(logo)


    # Background
    canvas.create_image(
        0,
        0,
        image = background,
        anchor = "nw"
    )

    # Titulo
    canvas.create_text(
        950,
        150,
        text = "PERSONA 4\nREVIVAL",
        font = ("o Ryokan Std E", 32, "bold"),
        fill = "black",
        justify = "center"
    )

    # Contador
    contador = canvas.create_text(
        950,
        350,
        text = "Carregando...",
        font = ("o Ryokan Std E", 50, "bold"),
        fill = "black",
        justify = "center"
    )

    # Data
    canvas.create_text(
        950,
        500,
        text = "FEBRUARY 18, 2027",
        font = ("o Ryokan Std E", 18),
        fill = "black"
    )

    # Logo p4R
    canvas.create_image(
        1400,
        1000,
        image = logo,
        anchor = "sw"
        
    )

    #Intro PROGRAMA
#===================================================================================================
    # coloca o frame no canvas            
    video_id = canvas.create_image(
    0,
    0,
    anchor = "nw"
    )

    def start_intro():
        
        start, frame = intro.read()

        if not start:
            
            intro.release()
            canvas.delete(video_id)
            return

        # openCV de BGR -> RGB
        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # openCV -> pillow
        imagem = Image.fromarray(frame)


        #   fazer resize do video  #

            


        # pillow -> TK
        imagem = ImageTk.PhotoImage(imagem)           
    
        canvas.itemconfig(
            video_id,
            image = imagem
        )

        # Mantem a imagem na memoria pro garbage collector nao mandar tudo pro espaco
        canvas.imagem = imagem

        # Proximo frame / do video com os milisegundos de cada frame (20)
        janela.after(
            20,
            start_intro
        )


    def atualizar_contador():

        dias, horas, minutos, segundos = countdown()

        canvas.itemconfig(
            contador,
            text=f"{dias} DAYS\n"
                 f"{horas:02}:{minutos:02}:{segundos:02}"
        )

        janela.after(1000, atualizar_contador)

    start_intro()
    
    atualizar_contador()
    janela.mainloop()