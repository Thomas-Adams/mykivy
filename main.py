from kivy.uix.gridlayout import GridLayout


class ContactForm(GridLayout):

    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        self.cols = 2
        self.rows =10


    def add_controls(self):
        pass







