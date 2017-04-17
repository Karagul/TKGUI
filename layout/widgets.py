import Tkinter as Tk
import ttk

''' This file contains the base functions 
    and buttons for each widget to add
    to the canvas.
'''


#   The code for moving the widgets was found here
#   https://bytes.com/topic/python/answers/26927-moving-widgets-tkinter

class Base(object):

    ''' This class is used for distributing
    all of the manipulative functions into the widgets
    '''

    def __init__(self):

        self.__winX = 0
        self.__winY = 0
        self.__lastX = 0
        self.__lastY = 0
        self.tag_label = None # shows the tag
        self.tag = None # Actual mark tag
        self.tag_entry = None  # Change the tag

        self.METHOD_BINDS = {"<B1-Motion>" : self.moveWindow,
                             "<ButtonPress-1>" : self.startMoveWindow,
                             "<Double-Button-1>" : self.editTag,
                             "<Double-Button-2>" : self.destroyAll,
                             "<Enter>" : self.dispTag,
                             "<Leave>" : self.hideTag}

    def destroyEntry(self, event):

        if self.tag_entry.get():

            self.tag = self.tag_entry.get()

            self.tag_entry.destroy()

    def destroyAll(self, event):

        if self.tag_entry:

            self.tag_entry.destroy()

        if self.tag_label:

            self.tag_label.destroy()

        self.destroy()

    def dispTag(self, event):

        if self.tag_label:

            self.tag_label.destroy()

        color = "#E3F72A"

        if self.tag:

            self.tag_label = Tk.Text(self.root, width=len(self.tag), height=1, bg=color, highlightbackground=color)
            self.tag_label.insert(Tk.INSERT, self.tag)

        else:
            self.tag_label = Tk.Text(self.root, width=len("<NO TAG>"), height=1, bg=color)
            self.tag_label.insert(Tk.INSERT, "<NO TAG>")


        self.tag_label.place(x=self.__winX + 20, y=self.__winY + 20)
        self.tag_label['state'] = 'disabled'

    def editTag(self, event):

        if self.tag_entry:

            self.tag_entry.destroy()

        self.tag_entry = Tk.Entry(self.root)

        if self.tag:

            self.tag_entry.insert(0, self.tag)
            self.tag_entry.bind("<Return>", self.destroyEntry)

        else:

            self.tag_entry.insert(0, "<NO TAG>")
            self.tag_entry.bind("<Return>", self.destroyEntry)

        self.tag_entry.place(x=self.__winX + 10, y=self.__winY + 10)

    def hideTag(self, event):

        if self.tag_label:

            self.tag_label.destroy()

            self.tag_label = None

    def moveWindow(self, event):

        self.root.update_idletasks()

        ## Use root coordinates to compute offset for inside window coordinates
        self.__winX += event.x_root - self.__lastX
        self.__winY += event.y_root - self.__lastY

        ## Remember last coordinates
        self.__lastX, self.__lastY = event.x_root, event.y_root

        ## Move inside window
        self.place_configure(x=self.__winX, y=self.__winY)

    def startMoveWindow(self, event):

        ## When the movement starts, record current root coordinates
        self.__lastX, self.__lastY = event.x_root, event.y_root

class _Button(Base, Tk.Button):

    def __init__(self, root, **kwargs):

        Tk.Button.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Checkbutton(Base, Tk.Checkbutton):

    def __init__(self, root, **kwargs):

        Tk.Checkbutton.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Entry(Base, Tk.Entry):

    def __init__(self, root, **kwargs):
        
        Tk.Entry.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Label(Base, Tk.Label):

    def __init__(self, root, **kwargs):
        
        Tk.Label.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Listbox(Base, Tk.Listbox):

    def __init__(self, root, **kwargs):

        Tk.Listbox.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Plot(Base,): # FIX THIS UP

    def __init__(self, root, **kwargs):
        
        Tk.Plot.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Radiobutton(Base, Tk.Radiobutton):

    def __init__(self, root, **kwargs):

        Tk.Radiobutton.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Scale(Base, Tk.Scale):

    def __init__(self, root, **kwargs):
        
        Tk.Scale.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Scrollbar(Base, Tk.Scrollbar):

    def __init__(self, root, **kwargs):
        
        Tk.Scrollbar.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Spinbox(Base, Tk.Spinbox):

    def __init__(self, root, **kwargs):
        
        Tk.Spinbox.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)

class _Text(Base, Tk.Text):

    def __init__(self, root, **kwargs):
        
        Tk.Text.__init__(self, root, **kwargs)
        Base.__init__(self)
        
        self.root = root

        for key, val in self.METHOD_BINDS.iteritems():

            self.bind(key, val)





