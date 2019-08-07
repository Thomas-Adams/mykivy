from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty, StringProperty
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.widget import Widget

countries = [{'code': '1', 'name': 'Afghanistan', 'dial': '93'}, {'code': '2', 'name': 'Albania', 'dial': '355'},
             {'code': '3', 'name': 'Algeria', 'dial': '213'}, {'code': '4', 'name': 'American Samoa', 'dial': '1684'},
             {'code': '5', 'name': 'Andorra', 'dial': '376'}, {'code': '6', 'name': 'Angola', 'dial': '244'},
             {'code': '7', 'name': 'Anguilla', 'dial': '1264'}, {'code': '8', 'name': 'Antarctica', 'dial': ''},
             {'code': '9', 'name': 'Antigua and Barbuda', 'dial': '1268'},
             {'code': '10', 'name': 'Argentina', 'dial': '54'}, {'code': '11', 'name': 'Armenia', 'dial': '374'},
             {'code': '12', 'name': 'Aruba', 'dial': '297'}, {'code': '13', 'name': 'Australia', 'dial': '61'},
             {'code': '14', 'name': 'Austria', 'dial': '43'}, {'code': '15', 'name': 'Azerbaijan', 'dial': '994'},
             {'code': '16', 'name': 'Bahamas', 'dial': '1242'}, {'code': '17', 'name': 'Bahrain', 'dial': '973'},
             {'code': '18', 'name': 'Bangladesh', 'dial': '880'}, {'code': '19', 'name': 'Barbados', 'dial': '1246'},
             {'code': '20', 'name': 'Belarus', 'dial': '375'}, {'code': '21', 'name': 'Belgium', 'dial': '32'},
             {'code': '22', 'name': 'Belize', 'dial': '501'}, {'code': '23', 'name': 'Benin', 'dial': '229'},
             {'code': '24', 'name': 'Bermuda', 'dial': '1441'}, {'code': '25', 'name': 'Bhutan', 'dial': '975'},
             {'code': '26', 'name': 'Bolivia', 'dial': '591'},
             {'code': '27', 'name': 'Bosnia and Herzegovina', 'dial': '387'},
             {'code': '28', 'name': 'Botswana', 'dial': '267'}, {'code': '29', 'name': 'Bouvet Island', 'dial': '55'},
             {'code': '30', 'name': 'Brazil', 'dial': '55'},
             {'code': '31', 'name': 'British Indian Ocean Territory', 'dial': '246'},
             {'code': '32', 'name': 'Brunei', 'dial': '673'}, {'code': '33', 'name': 'Bulgaria', 'dial': '359'},
             {'code': '34', 'name': 'Burkina Faso', 'dial': '226'}, {'code': '35', 'name': 'Burundi', 'dial': '257'},
             {'code': '36', 'name': 'Cambodia', 'dial': '855'}, {'code': '37', 'name': 'Cameroon', 'dial': '237'},
             {'code': '38', 'name': 'Canada', 'dial': '1'}, {'code': '39', 'name': 'Cape Verde', 'dial': '238'},
             {'code': '40', 'name': 'Cayman Islands', 'dial': '1345'},
             {'code': '41', 'name': 'Central African Republic', 'dial': '236'},
             {'code': '42', 'name': 'Chad', 'dial': '235'}, {'code': '43', 'name': 'Chile', 'dial': '56'},
             {'code': '44', 'name': 'China', 'dial': '86'}, {'code': '45', 'name': 'Christmas Island', 'dial': '61'},
             {'code': '46', 'name': 'Cocos (Keeling) Islands', 'dial': '61'},
             {'code': '47', 'name': 'Colombia', 'dial': '57'}, {'code': '48', 'name': 'Comoros', 'dial': '269'},
             {'code': '49', 'name': 'Congo', 'dial': '242'}, {'code': '50', 'name': 'Cook Islands', 'dial': '682'},
             {'code': '51', 'name': 'Costa Rica', 'dial': '506'}, {'code': '52', 'name': 'Croatia', 'dial': '385'},
             {'code': '53', 'name': 'Cuba', 'dial': '53'}, {'code': '54', 'name': 'Cyprus', 'dial': '357'},
             {'code': '55', 'name': 'Czech Republic', 'dial': '420'}, {'code': '56', 'name': 'Denmark', 'dial': '45'},
             {'code': '57', 'name': 'Djibouti', 'dial': '253'}, {'code': '58', 'name': 'Dominica', 'dial': '1767'},
             {'code': '59', 'name': 'Dominican Republic', 'dial': '1849'},
             {'code': '60', 'name': 'East Timor', 'dial': '670'}, {'code': '61', 'name': 'Ecuador', 'dial': '593'},
             {'code': '62', 'name': 'Egypt', 'dial': '20'}, {'code': '63', 'name': 'El Salvador', 'dial': '503'},
             {'code': '64', 'name': 'Equatorial Guinea', 'dial': '240'},
             {'code': '65', 'name': 'Eritrea', 'dial': '291'}, {'code': '66', 'name': 'Estonia', 'dial': '372'},
             {'code': '67', 'name': 'Ethiopia', 'dial': '251'},
             {'code': '68', 'name': 'Falkland Islands', 'dial': '500'},
             {'code': '69', 'name': 'Faroe Islands', 'dial': '298'},
             {'code': '70', 'name': 'Fiji Islands', 'dial': '679'}, {'code': '71', 'name': 'Finland', 'dial': '358'},
             {'code': '72', 'name': 'France', 'dial': '33'}, {'code': '73', 'name': 'French Guiana', 'dial': '594'},
             {'code': '74', 'name': 'French Polynesia', 'dial': '689'},
             {'code': '75', 'name': 'French Southern territories', 'dial': '262'},
             {'code': '76', 'name': 'Gabon', 'dial': '241'}, {'code': '77', 'name': 'Gambia', 'dial': '220'},
             {'code': '78', 'name': 'Georgia', 'dial': '995'}, {'code': '79', 'name': 'Germany', 'dial': '49'},
             {'code': '80', 'name': 'Ghana', 'dial': '233'}, {'code': '81', 'name': 'Gibraltar', 'dial': '350'},
             {'code': '82', 'name': 'Greece', 'dial': '30'}, {'code': '83', 'name': 'Greenland', 'dial': '299'},
             {'code': '84', 'name': 'Grenada', 'dial': '1473'}, {'code': '85', 'name': 'Guadeloupe', 'dial': '590'},
             {'code': '86', 'name': 'Guam', 'dial': '1671'}, {'code': '87', 'name': 'Guatemala', 'dial': '502'},
             {'code': '88', 'name': 'Guinea', 'dial': '224'}, {'code': '89', 'name': 'Guinea-Bissau', 'dial': '245'},
             {'code': '90', 'name': 'Guyana', 'dial': '592'}, {'code': '91', 'name': 'Haiti', 'dial': '509'},
             {'code': '92', 'name': 'Heard Island and McDonald Islands', 'dial': '672'},
             {'code': '93', 'name': 'Holy See (Vatican City State)', 'dial': '379'},
             {'code': '94', 'name': 'Honduras', 'dial': '504'}, {'code': '95', 'name': 'Hong Kong', 'dial': '852'},
             {'code': '96', 'name': 'Hungary', 'dial': '36'}, {'code': '97', 'name': 'Iceland', 'dial': '354'},
             {'code': '98', 'name': 'India', 'dial': '91'}, {'code': '99', 'name': 'Indonesia', 'dial': '62'},
             {'code': '100', 'name': 'Iran', 'dial': '98'}, {'code': '101', 'name': 'Iraq', 'dial': '964'},
             {'code': '102', 'name': 'Ireland', 'dial': '353'}, {'code': '103', 'name': 'Israel', 'dial': '972'},
             {'code': '104', 'name': 'Italy', 'dial': '39'}, {'code': '105', 'name': 'Ivory Coast', 'dial': '225'},
             {'code': '106', 'name': 'Jamaica', 'dial': '1876'}, {'code': '107', 'name': 'Japan', 'dial': '81'},
             {'code': '108', 'name': 'Jordan', 'dial': '962'}, {'code': '109', 'name': 'Kazakhstan', 'dial': '7'},
             {'code': '110', 'name': 'Kenya', 'dial': '254'}, {'code': '111', 'name': 'Kiribati', 'dial': '686'},
             {'code': '112', 'name': 'Kuwait', 'dial': '965'}, {'code': '113', 'name': 'Kyrgyzstan', 'dial': '996'},
             {'code': '114', 'name': 'Laos', 'dial': '856'}, {'code': '115', 'name': 'Latvia', 'dial': '371'},
             {'code': '116', 'name': 'Lebanon', 'dial': '961'}, {'code': '117', 'name': 'Lesotho', 'dial': '266'},
             {'code': '118', 'name': 'Liberia', 'dial': '231'},
             {'code': '119', 'name': 'Libyan Arab Jamahiriya', 'dial': '218'},
             {'code': '120', 'name': 'Liechtenstein', 'dial': '423'},
             {'code': '121', 'name': 'Lithuania', 'dial': '370'}, {'code': '122', 'name': 'Luxembourg', 'dial': '352'},
             {'code': '123', 'name': 'Macao', 'dial': '853'}, {'code': '124', 'name': 'North Macedonia', 'dial': '389'},
             {'code': '125', 'name': 'Madagascar', 'dial': '261'}, {'code': '126', 'name': 'Malawi', 'dial': '265'},
             {'code': '127', 'name': 'Malaysia', 'dial': '60'}, {'code': '128', 'name': 'Maldives', 'dial': '960'},
             {'code': '129', 'name': 'Mali', 'dial': '223'}, {'code': '130', 'name': 'Malta', 'dial': '356'},
             {'code': '131', 'name': 'Marshall Islands', 'dial': '692'},
             {'code': '132', 'name': 'Martinique', 'dial': '596'}, {'code': '133', 'name': 'Mauritania', 'dial': '222'},
             {'code': '134', 'name': 'Mauritius', 'dial': '230'}, {'code': '135', 'name': 'Mayotte', 'dial': '262'},
             {'code': '136', 'name': 'Mexico', 'dial': '52'},
             {'code': '137', 'name': 'Micronesia, Federated States of', 'dial': '691'},
             {'code': '138', 'name': 'Moldova', 'dial': '373'}, {'code': '139', 'name': 'Monaco', 'dial': '377'},
             {'code': '140', 'name': 'Mongolia', 'dial': '976'}, {'code': '141', 'name': 'Montserrat', 'dial': '1664'},
             {'code': '142', 'name': 'Morocco', 'dial': '212'}, {'code': '143', 'name': 'Mozambique', 'dial': '258'},
             {'code': '144', 'name': 'Myanmar', 'dial': '95'}, {'code': '145', 'name': 'Namibia', 'dial': '264'},
             {'code': '146', 'name': 'Nauru', 'dial': '674'}, {'code': '147', 'name': 'Nepal', 'dial': '977'},
             {'code': '148', 'name': 'Netherlands', 'dial': '31'},
             {'code': '149', 'name': 'Netherlands Antilles', 'dial': '599'},
             {'code': '150', 'name': 'New Caledonia', 'dial': '687'},
             {'code': '151', 'name': 'New Zealand', 'dial': '64'}, {'code': '152', 'name': 'Nicaragua', 'dial': '505'},
             {'code': '153', 'name': 'Niger', 'dial': '227'}, {'code': '154', 'name': 'Nigeria', 'dial': '234'},
             {'code': '155', 'name': 'Niue', 'dial': '683'}, {'code': '156', 'name': 'Norfolk Island', 'dial': '672'},
             {'code': '157', 'name': 'North Korea', 'dial': '850'},
             {'code': '158', 'name': 'Northern Ireland', 'dial': '44'},
             {'code': '159', 'name': 'Northern Mariana Islands', 'dial': '1670'},
             {'code': '160', 'name': 'Norway', 'dial': '47'}, {'code': '161', 'name': 'Oman', 'dial': '968'},
             {'code': '162', 'name': 'Pakistan', 'dial': '92'}, {'code': '163', 'name': 'Palau', 'dial': '680'},
             {'code': '164', 'name': 'Palestine', 'dial': '970'}, {'code': '165', 'name': 'Panama', 'dial': '507'},
             {'code': '166', 'name': 'Papua New Guinea', 'dial': '675'},
             {'code': '167', 'name': 'Paraguay', 'dial': '595'}, {'code': '168', 'name': 'Peru', 'dial': '51'},
             {'code': '169', 'name': 'Philippines', 'dial': '63'}, {'code': '170', 'name': 'Pitcairn', 'dial': '64'},
             {'code': '171', 'name': 'Poland', 'dial': '48'}, {'code': '172', 'name': 'Portugal', 'dial': '351'},
             {'code': '173', 'name': 'Puerto Rico', 'dial': '1939'}, {'code': '174', 'name': 'Qatar', 'dial': '974'},
             {'code': '175', 'name': 'Reunion', 'dial': '262'}, {'code': '176', 'name': 'Romania', 'dial': '40'},
             {'code': '177', 'name': 'Russian Federation', 'dial': '7'},
             {'code': '178', 'name': 'Rwanda', 'dial': '250'}, {'code': '179', 'name': 'Saint Helena', 'dial': '290'},
             {'code': '180', 'name': 'Saint Kitts and Nevis', 'dial': '1869'},
             {'code': '181', 'name': 'Saint Lucia', 'dial': '1758'},
             {'code': '182', 'name': 'Saint Pierre and Miquelon', 'dial': '508'},
             {'code': '183', 'name': 'Saint Vincent and the Grenadines', 'dial': '1784'},
             {'code': '184', 'name': 'Samoa', 'dial': '685'}, {'code': '185', 'name': 'San Marino', 'dial': '378'},
             {'code': '186', 'name': 'Sao Tome and Principe', 'dial': '239'},
             {'code': '187', 'name': 'Saudi Arabia', 'dial': '966'}, {'code': '188', 'name': 'Senegal', 'dial': '221'},
             {'code': '189', 'name': 'Seychelles', 'dial': '248'},
             {'code': '190', 'name': 'Sierra Leone', 'dial': '232'}, {'code': '191', 'name': 'Singapore', 'dial': '65'},
             {'code': '192', 'name': 'Slovakia', 'dial': '421'}, {'code': '193', 'name': 'Slovenia', 'dial': '386'},
             {'code': '194', 'name': 'Solomon Islands', 'dial': '677'},
             {'code': '195', 'name': 'Somalia', 'dial': '252'}, {'code': '196', 'name': 'South Africa', 'dial': '27'},
             {'code': '197', 'name': 'South Georgia and the South Sandwich Islands', 'dial': '500'},
             {'code': '198', 'name': 'South Korea', 'dial': '82'},
             {'code': '199', 'name': 'South Sudan', 'dial': '211'}, {'code': '200', 'name': 'Spain', 'dial': '34'},
             {'code': '201', 'name': 'Sri Lanka', 'dial': '94'}, {'code': '202', 'name': 'Sudan', 'dial': '249'},
             {'code': '203', 'name': 'Suriname', 'dial': '597'},
             {'code': '204', 'name': 'Svalbard and Jan Mayen', 'dial': '47'},
             {'code': '205', 'name': 'Swaziland', 'dial': '268'}, {'code': '206', 'name': 'Sweden', 'dial': '46'},
             {'code': '207', 'name': 'Switzerland', 'dial': '41'}, {'code': '208', 'name': 'Syria', 'dial': '963'},
             {'code': '209', 'name': 'Tajikistan', 'dial': '992'}, {'code': '210', 'name': 'Tanzania', 'dial': '255'},
             {'code': '211', 'name': 'Thailand', 'dial': '66'},
             {'code': '212', 'name': 'The Democratic Republic of Congo', 'dial': '243'},
             {'code': '213', 'name': 'Togo', 'dial': '228'}, {'code': '214', 'name': 'Tokelau', 'dial': '690'},
             {'code': '215', 'name': 'Tonga', 'dial': '676'},
             {'code': '216', 'name': 'Trinidad and Tobago', 'dial': '1868'},
             {'code': '217', 'name': 'Tunisia', 'dial': '216'}, {'code': '218', 'name': 'Turkey', 'dial': '90'},
             {'code': '219', 'name': 'Turkmenistan', 'dial': '993'},
             {'code': '220', 'name': 'Turks and Caicos Islands', 'dial': '1649'},
             {'code': '221', 'name': 'Tuvalu', 'dial': '688'}, {'code': '222', 'name': 'Uganda', 'dial': '256'},
             {'code': '223', 'name': 'Ukraine', 'dial': '380'},
             {'code': '224', 'name': 'United Arab Emirates', 'dial': '971'},
             {'code': '225', 'name': 'United Kingdom', 'dial': '44'},
             {'code': '226', 'name': 'United States', 'dial': '1'},
             {'code': '227', 'name': 'United States Minor Outlying Islands', 'dial': '246'},
             {'code': '228', 'name': 'Uruguay', 'dial': '598'}, {'code': '229', 'name': 'Uzbekistan', 'dial': '998'},
             {'code': '230', 'name': 'Vanuatu', 'dial': '678'}, {'code': '231', 'name': 'Venezuela', 'dial': '58'},
             {'code': '232', 'name': 'Vietnam', 'dial': '84'},
             {'code': '233', 'name': 'Virgin Islands, British', 'dial': '1284'},
             {'code': '234', 'name': 'Virgin Islands, U.S.', 'dial': '1'},
             {'code': '235', 'name': 'Wallis and Futuna', 'dial': '681'},
             {'code': '236', 'name': 'Western Sahara', 'dial': '212'}, {'code': '237', 'name': 'Yemen', 'dial': '967'},
             {'code': '238', 'name': 'Yugoslavia', 'dial': '38'}, {'code': '239', 'name': 'Zambia', 'dial': '260'},
             {'code': '240', 'name': 'Zimbabwe', 'dial': '263'}]

Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<SelectableCountryWidget>:
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size    
    BoxLayout:
        orientation: 'horizontal'
        spacing: 2
        Label:
            text: 'Test'
            size: (40,40)
            size_hint_x: 0.1
            color: get_color_from_hex('#FFFFFF')
        Label:
            text: root.name
            size: (500,40)
            size_hint_x: 0.7
        Label:
            text: root.dial
            size: (60,40)
            size_hint_x: 0.2
            

<CountryRecycleView>:
    viewclass: 'SelectableCountryWidget'
    SelectableRecycleBoxLayout:
        orientation: 'vertical'
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        spacing: dp(2)
        multiselect: True
        touch_multiselect: True            
        
''')


class CountryWidget(Widget):
    code = StringProperty()
    name = StringProperty()
    dial = StringProperty()

    def __init__(self, **kwargs):
        if 'code' in kwargs:
            self.code = kwargs.get('code')
            setattr(self, 'code', kwargs.get('code'))
        if 'name' in kwargs:
            self.name = kwargs.get('name')
            setattr(self, 'name', kwargs.get('name'))
        if 'dial' in kwargs:
            self.dial = kwargs.get('dial')
            setattr(self, 'dial', kwargs.get('dial'))
        super(CountryWidget, self).__init__()


class SelectableCountryWidget(RecycleDataViewBehavior, CountryWidget):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(SelectableCountryWidget, self).__init__(**kwargs)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        super(SelectableCountryWidget, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        print(datetime.now(), self.name, self.code, self.dial)
        if super(SelectableCountryWidget, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    """
    placehoder
    """


class CountryRecycleView(RecycleView):
    data = ListProperty([])

    def __init__(self, **kwargs):
        super(CountryRecycleView, self).__init__(**kwargs)
        self.get_data_items()

    def get_data_items(self):
        self.data = countries


class TestApp(App):
    def build(self):
        return CountryRecycleView()


if __name__ == '__main__':
    TestApp().run()
