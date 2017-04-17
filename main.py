import Tkinter as Tk
import layout.editor as editor

if __name__ == '__main__':
    
    root = Tk.Tk()
    
    app = editor.Screen(root, width=1200, height=800)

    app.pack()

    root.mainloop()
