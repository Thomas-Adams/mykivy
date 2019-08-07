from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.widget import Widget

from models import connect, Country

Builder.load_string('''
<SelectableButton>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableButton'            
    SelectableRecycleGridLayout:
        cols: 3
        default_size: None, dp(26)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class CountryView(Widget):
    country = ObjectProperty(None)
    label_name = ObjectProperty(None)
    label_abbr = ObjectProperty(None)
    label_phone = ObjectProperty(None)

    def __init__(self, country=None):
        super(CountryView, self).__init__()
        if not country is None:
            self.set_country(country)

    def set_country(self, country):
        self.country = country
        self.label_abbr = Label(text='[color=ffffff]' + country.abbr + '[/color]', markup=True)
        self.label_abbr.size = self.label_abbr.texture_size

        self.label_name = Label(text='[color=ffffff]' + country.name + '[/color]', markup=True)
        self.label_name.size = self.label_name.texture_size

        self.label_phone = Label(text='[color=ffffff]' + country.phone + '[/color]', markup=True)
        self.label_phone.size = self.label_phone.texture_size

        self.add_widget(self.label_abbr)
        self.add_widget(self.label_name)
        self.add_widget(self.label_phone)


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def on_press(self):
        pass

    def update_changes(self, txt):
        self.text = txt


class RV(RecycleView):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        for country in Country.select():
            self.data_items.append(country.name)
            self.data_items.append(country.abbr)
            self.data_items.append(country.phone)
        self.data = [{'text': str(x)} for x in self.data_items]


class TestApp(App):
    def build(self):
        return RV()


if __name__ == '__main__':
    connect()
    TestApp().run()
