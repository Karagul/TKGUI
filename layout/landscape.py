import Tkinter as Tk 
import widgets

class LandscapeWindow(Tk.Canvas):

    ''' Handles all button actions for placing
        each widget onto the canvas
    '''

    def __init__(self, root, width=0, height=0):
        
        Tk.Canvas.__init__(self, root, width=width, height=height)

        # Used in editor.py for placement
        self._funcs = {"Button" : self.Button, 
                       "Checkbutton" : self.Checkbutton, 
                       "Entry" : self.Entry,
                       "Label" : self.Label, 
                       "Listbox" : self.Listbox, 
                       "Plot" : self.Plot,
                       "Radiobutton" : self.Radiobutton, 
                       "Scale" : self.Scale, 
                       "Scrollbar" : self.Scrollbar, 
                       "Text" : self.Text, 
                       "Spinbox" : self.Spinbox}

        self.config(bg='grey')
        self.width = width
        self.height = height

        NUM_OF_LINES = 40

        TOP = self.height
        BOTTOM = 0

        delta_x = self.width / NUM_OF_LINES

        # Drawing vertial lines
        for i in xrange(NUM_OF_LINES):

            x = int(self.width / NUM_OF_LINES)

            self.create_line(delta_x * i, BOTTOM, delta_x * i, TOP)

        delta_y = self.height / NUM_OF_LINES

        # Drawing horizontal lines
        for i in xrange(NUM_OF_LINES + 1):

            y = int(self.height / NUM_OF_LINES) 

            self.create_line(0, delta_y * i, self.width, delta_y * i)

    def Button(self):

        obj = widgets._Button(self, text="Button")
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)

    def Checkbutton(self):

        obj = widgets._Checkbutton(self, text="Checkbutton")
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)

    def Entry(self):

        obj = widgets._Entry(self, text="Entry")
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)

    def Label(self):

        obj = widgets._Label(self, text="Label")
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)

    def Listbox(self):

        obj = widgets._Listbox(self)
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)

    def Plot(self):

        obj = widgets._Plot(self)
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)

    def Radiobutton(self):

        obj = widgets._Radiobutton(self, text="Radio Button")
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)

    def Scale(self):
        # ttk 
        obj = widgets._Scale(self, from_=0, to=5, orient=Tk.HORIZONTAL)
        # obj['state'] = 'disabled'
        obj.place(x=0, y=0) 

    def Scrollbar(self):

        obj = widgets._Scrollbar(self)
        #obj['state'] = 'disabled'
        obj.place(x=0, y=0) 

    def Spinbox(self):

        obj = widgets._Spinbox(self)
        obj['state'] = 'disabled'
        obj.place(x=0, y=0)  
    
    def Text(self):

        obj = widgets._Text(self)
        obj['state'] = 'disabled'
        obj.place(x=0, y=0) 
