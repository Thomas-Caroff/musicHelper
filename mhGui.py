import dataManager as dm
import tkinter as tk

def generateGui():
    global root
    root = tk.Tk()
    root.wm_title('Music Helper v0.0.1b')
    canvas = tk.Canvas(root)
    canvas.pack()
    quitButton = tk.Button(root, text='Quit', command=closeRoot)
    quitButton.pack(side='bottom')
    root.mainloop()



def closeRoot():
    root.destroy()

if __name__ == '__main__':
    generateGui()