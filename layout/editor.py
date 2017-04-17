import Tkinter as Tk
import ttk
import landscape as lscape 


class Screen(Tk.Canvas):


    ''' Main UI Layout class for producing the editor
    '''

    def __init__(self, root, width=0, height=0):

        Tk.Canvas.__init__(self, root, width=width, height=height)

        self.root = root

        LEFT_SIDE = int(0.2 * width)
        RIGHT_SIDE = int(0.8 * width)
        BOTTOM = 0
        TOP = height

        # List found from https://tkinter.unpythonic.net/wiki/Widgets
        self.__WIDGETS__ = ["Button",
                       #"Canvas",
                       "Checkbutton",
                       "Entry",
                       #"Frame",
                       "Label",
                       "Listbox",
                       #"Menu",
                       #"Menubutton",
                       'Plot',
                       "Radiobutton",
                       "Scale",
                       "Scrollbar",
                       "Text",
                       "Spinbox",

                       # Added to Tkinter 8.3 
                       #"PanedWindow",
                       #"LabelFrame"
                       #"OptionMenu",
                       ]

        # Calculating vertical center of the column on the right
        CENTER_RIGHT = int(RIGHT_SIDE + width) / 2.

        # Because the left edges will align in the center, I have
        # to shift them back

        HALF_RIGHT_CENTER = int(RIGHT_SIDE + CENTER_RIGHT) / 2.

        VERT_SPACING = 40

        self.drawing_canvas = lscape.LandscapeWindow(self, width=RIGHT_SIDE - LEFT_SIDE, height=height)
        self.drawing_canvas.place(x=LEFT_SIDE, y=0)

        self.buttons = []

        # Place buttons on right side for adding widgets
        for idx, widget, in enumerate(self.__WIDGETS__):

            button = Tk.Button(self, text=widget)
            button.place(x=HALF_RIGHT_CENTER, y= VERT_SPACING * idx)
            button.config(width=10, height=2)
            self.buttons.append(button)

        # Add commands to each button
        for button, name in zip(self.buttons, self.__WIDGETS__):

            button.config(command=self.drawing_canvas._funcs[name])
        
        self.menubar = Tk.Menu(self)

        menu = Tk.Menu(self.menubar)
        self.menubar.add_cascade(label= "File",menu=menu)

        menu.add_command(label="New")
        menu.add_command(label="Open")
        menu.add_command(label="Save")

        menu = Tk.Menu(self.menubar)
        self.menubar.add_cascade(label= "Code", menu=menu)
        menu.add_command(label="Generate", command=self.generate_code)


        self.root.config(menu=self.menubar)      
                
    def generate_code(self):
        
        import jinja2
        import tkFileDialog
        import tkMessageBox

        objects = self.get_widgets()

        ifile = open('__master_template__.py', 'r')

        template = jinja2.Template(ifile.read())

        output = template.render(object_array = objects, enumerated_objects = enumerate(objects))

        if self.unique_tags():

            with tkFileDialog.asksaveasfile(mode='w', defaultextension=".py") as _file:

                if _file is None:

                    return

                _file.write(output)

        else:

            tkMessageBox.showinfo("Error", "Tag names are not unique.")

    def get_widgets(self):

        widget_array = []
        for widget in self.drawing_canvas.winfo_children():
            
            widget_properties = {}             
            widget_properties["class_name"] = widget.__class__.__name__
            widget_properties['x'] = widget.winfo_x()
            widget_properties['y'] = widget.winfo_y()
            widget_properties['tag'] = widget.tag
            widget_array.append(widget_properties)

        return widget_array

    def unique_tags(self):

        objects = self.get_widgets()
        tag_array = []

        for obj in objects:

            tag_array.append(obj['tag'])

        if len(tag_array) == len(set(tag_array)):

            return True

        return False
