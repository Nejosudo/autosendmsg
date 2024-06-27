from tkinter import *
import index as sd

class MainWindow():
    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.title("NS-AutoSendMessages")
        self.setupUi()
        self.root.mainloop()
    
    def setupUi(self):
        self.validateInfo = True
        self.framePrinc = Frame(self.root)
        self.framePrinc.pack()

        labelInfo = Label(master=self.framePrinc,text="A continuación encontraras recuadro para escribir el mensaje que deseas enviar")
        labelInfo.pack()

        #box horizontal de almacenar entrada y buton de agregar entradas
        self.frameH = Frame(master=self.framePrinc)
        self.frameH.pack()
        #Entrada 
        labelText = Label(master=self.frameH,text="Mensaje", font="Arial 6")
        labelText.grid(column=0,row=0,rowspan=1)
        self.entryText = Entry(master=self.frameH)
        self.entryText.grid(column=0,row=1)

        labelCantidad = Label(master=self.frameH,text="Cantidad",font="Arial 6")
        labelCantidad.grid(column=1,row=0,rowspan=1)

        self.entryCantidad = Entry(master=self.frameH,width=5)
        self.entryCantidad.grid(column=1,row=1)

        btonIniciar = Button(master=self.frameH,text="Enviar",command=lambda: self.sendMessages())
        btonIniciar.grid(column=0,row=2,columnspan=2)
        self.labelInfo2 = Label(master=self.framePrinc, text="")
        
    def sendMessages(self):
        self.labelInfo2.config(text="En 5 segundos inicia la secuencia de envio de mensajes.")
        self.labelInfo2.pack()
        try:
            msg = self.entryText.get()
            count = int(self.entryCantidad.get())
            sd.sendMessage(msg,count)
        except ValueError:
            self.labelInfo2.config(text="Debes ingresar un valor númerico en cantidad.")
            self.labelInfo2.pack()
if __name__ == "__main__":
    app = MainWindow()