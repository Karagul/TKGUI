
{# TEMPLATE USED FOR GENERATING GUI #}

try:
    import Tkinter as Tk

except:

    import tkinter as Tk

import ttk 


{% for i in object_array %}

{% if i['class_name'] == '_Button' %}

class {{ i['tag'] }}(Tk.Button):

    def __init__(self, root, *args, **kwargs):

        Tk.Button.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Checkbutton' %}

class {{ i['tag'] }}(Tk.Checkbutton):

    def __init__(self, root, *args, **kwargs):

        Tk.Checkbutton.__init__(self, root, *args, **kwargs)

        self.x = {{  i['x']  }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Entry' %}

class {{ i['tag'] }}(Tk.Entry):

    def __init__(self, root, *args, **kwargs):

        Tk.Entry.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Label' %}

class {{ i['tag'] }}(Tk.Label):

    def __init__(self, root, *args, **kwargs):

        Tk.Label.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Listbox' %}

class {{ i['tag'] }}(Tk.Listbox):

    def __init__(self, root, *args, **kwargs):

        Tk.Listbox.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Radiobutton' %}

class {{ i['tag'] }}(Tk.Radiobutton):

    def __init__(self, root, *args, **kwargs):

        Tk.Radiobutton.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}


{% elif i['class_name'] == '_Plot' %}

class {{ i['tag'] }}(Tk.Canvas):

    def __init__(self, root, width=100, height=100, **kwargs):


        Tk.Canvas.__init__(self, root, width=width, height=height)
        
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        
        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

    def plot(self, x, y):

        self.axes.plot(x,y)


{% elif i['class_name'] == '_Scale' %}

class {{ i['tag'] }}(ttk.Scale):

    def __init__(self, root, *args, **kwargs):

        Tk.Scale.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Scrollbar' %}

class {{ i['tag'] }}(Tk.Scrollbar):

    def __init__(self, root, *args, **kwargs):

        Tk.Scrollbar.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Spinbox' %}

class {{ i['tag'] }}(Tk.Spinbox):

    def __init__(self, root, *args, **kwargs):

        Tk.Spinbox.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}

{% elif i['class_name'] == '_Text' %}

class {{ i['tag'] }}(Tk.Text):

    def __init__(self, root, *args, **kwargs):

        Tk.Text.__init__(self, root, *args, **kwargs)

        self.x = {{ i['x'] }}
        self.y = {{ i['y'] }}


{% endif %}


{% endfor %}

class Master_Canvas(Tk.Canvas):

    def __init__(self, root, width=720, height=800, *args, **kwargs):

        Tk.Canvas.__init__(self, root, width=width, height=height, *args, **kwargs)

        self.objects = []

    def append_object(self, _object):

        self.objects.append(_object)


    def render(self):

        for i in self.objects:

            i.place(x=i.x, y=i.y)


if __name__ == '__main__':
    
    root = Tk.Tk()
    master = Master_Canvas(root)
    master.pack()


    {% for i, j in enumerated_objects %}

    master.append_object({{ j['tag'] }}(master))
    {% endfor %}

    master.render()

    root.mainloop()






















