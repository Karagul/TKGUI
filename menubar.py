

import Tkinter as Tk 

class MenuBar(Tk.Menu):

    def __init__(self, root):

        Tk.Menu.__init__(self, root)

        self.add_command(label='Generate Code', command=self.generate)

    def save_code(self, code):

        _file = tkFile.asksaveasfile(mode='w', defaultextension=".txt")

        if _file is None:

            return

        saved_text = str(code.get(1.0, Tk.END))

        saved_file.write(saved_text)
        _file.close()


    def generate(self):

        widgets = self.get_widgets()

        env = jinja2.Environment()

        template = env.template('master_template.py')

        final_template = template.render(object_array=widgets)

        self.save_code(final_template)


