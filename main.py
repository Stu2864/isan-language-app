"""
Simple Isaan Language Learning App
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class IsaanLanguageApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title
        title = Label(
            text='สวัสดี! Isaan Language Learning',
            font_size=24,
            bold=True,
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(title)
        
        # Welcome message
        welcome = Label(
            text='Welcome to your Isaan Language App!\n\n'
                 'This app will help you learn Isaan/Thai phrases.',
            font_size=16,
            halign='center',
            valign='middle'
        )
        main_layout.add_widget(welcome)
        
        # Interactive section
        interactive_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        interactive_layout.bind(minimum_height=interactive_layout.setter('height'))
        
        # Phrase input
        phrase_input = TextInput(
            hint_text='Enter an Isaan/Thai phrase...',
            size_hint_y=None,
            height=40
        )
        interactive_layout.add_widget(phrase_input)
        
        # Response label
        response_label = Label(
            text='Your phrase will appear here',
            size_hint_y=None,
            height=40
        )
        interactive_layout.add_widget(response_label)
        
        # Submit button
        submit_btn = Button(
            text='Submit Phrase',
            size_hint_y=None,
            height=50
        )
        submit_btn.bind(on_press=lambda x: setattr(response_label, 'text', phrase_input.text))
        interactive_layout.add_widget(submit_btn)
        
        # Scroll view for interactive layout
        scroll = ScrollView()
        scroll.add_widget(interactive_layout)
        main_layout.add_widget(scroll)
        
        return main_layout

if __name__ == '__main__':
    IsaanLanguageApp().run()
