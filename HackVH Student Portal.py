from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton

Window.size = (800, 600)

screen_layout = """
Screen:
    NavigationLayout:
        ScreenManager:
            MenuScreen:
            PhysicalScreen:
            MentalScreen:
            EnglishScreen:
            SwimTeamScreen:
            BreathingExercisesScreen:
                
<MenuScreen>
    name: "menu"
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (800, 80)
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        elevation: 11

        MDLabel:
            text: "Student Portal"
            halign: "center"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: (33 / 256, 150 / 256, 243 / 256, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}

    MDIconButton:
        icon: "menu"
        pos_hint: {'center_x': 0.05, 'center_y': 0.95}
        on_release: nav_drawer.set_state()
            
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.17, 'center_y': 0.7}
        elevation: 10
        MDLabel:
            text: "PHYSICS"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        elevation: 10
        MDLabel:
            text: "MATH"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        #on_touch_down: nav()
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.83, 'center_y': 0.7}
        elevation: 10
        
        MDLabel:
            text: "ENGLISH"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDFlatButton: 
        text: ""
        size_hint: (0.27, 0.255)
        pos_hint: {'center_x': 0.83, 'center_y': 0.7}
        on_release: root.manager.current = "english"
    
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.17, 'center_y': 0.3}
        elevation: 10
        MDLabel:
            text: "HISTORY"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        elevation: 10
        MDLabel:
            text: "BIOLOGY"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.83, 'center_y': 0.3}
        elevation: 10
        MDLabel:
            text: "CHEMISTRY"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
    BoxLayout:
        orientation: "vertical"
        Widget:
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: "vertical"
            padding: "15dp"
            spacing: "15dp"
                
            Image:
                source: "profilePic1.png"
                    
            MDLabel:
                text: "                  Name: Arya Tawara"
                font_style: "Subtitle1"
                theme_text_color: "Primary"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
                
            MDLabel:
                text: "       Email-ID: aryatawara@gmail.com"
                font_style: "Subtitle1"
                theme_text_color: "Primary"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
            
            MDFillRoundFlatButton:
                text: "Physical Well-Being"
                size_hint: (0.5, 0.2)
                pos_hint: {'center_x': 0.5}
                on_release: root.manager.current = 'physical'
                
            MDFillRoundFlatButton:
                text: "Mental Health"
                size_hint: (0.5, 0.2)
                pos_hint: {'center_x': 0.5}
                on_release: root.manager.current = 'mental'
                    
            ScrollView:

<EnglishScreen>
    name: "english"
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (800, 80)
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        elevation: 11

        MDLabel:
            text: "English"
            halign: "center"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: (33 / 256, 150 / 256, 243 / 256, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (600, 55)
        pos_hint: {'center_x': 0.5, 'center_y': 0.79}
        elevation: 11
        MDLabel:
            halign: "center"
            text: "Teacher: Rachel Miller"
            font_style: "Subtitle1"
            bold: True
            theme_text_color: "Primary"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            halign: "center"
            text: "Grade: A+"
            font_style: "Subtitle1"
            bold: True
            theme_text_color: "Primary"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            halign: "center"
            text: "Assignments Due: 0"
            font_style: "Subtitle1"
            bold: True
            theme_text_color: "Primary"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (250, 120)
        pos_hint: {'center_x': 0.281, 'center_y': 0.6}
        elevation: 11
    
    MDLabel:
        halign: "center"
        text: "Homework Assignments:"
        font_style: "H6"
        theme_text_color: "Primary"
        pos_hint: {'center_x': 0.281, 'center_y': 0.667}
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (600, 275)
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        elevation: 11
        BoxLayout:
            orientation: 'vertical'
            spacing: "7dp"
            OneLineListItem:
                text: "About Me Essay                                                                                                    10/10"
            OneLineListItem:
                text: "Student Debate Essay                                                                                          10/10"
            OneLineListItem:
                text: "Creative Writing Essay                                                                                         10/10"
            OneLineListItem:
                text: "Summary Paragraph                                                                                            10/10"
            OneLineListItem:
                text: "Persuasive Writing Essay                                                                                    10/10"
            ScrollView:

        
    MDFillRoundFlatButton:
        text: "BACK"
        on_release: root.manager.current = "menu"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        size_hint: (0.12, 0.06)

<PhysicalScreen>
    name: "physical"
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (800, 80)
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        elevation: 11

        MDLabel:
            text: "Physical Well-Being"
            halign: "center"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: (33 / 256, 150 / 256, 243 / 256, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            
    MDIconButton:
        icon: "menu"
        pos_hint: {'center_x': 0.05, 'center_y': 0.95}
        on_release: nav_drawer.set_state()
            
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.17, 'center_y': 0.7}
        elevation: 10
        MDLabel:
            text: "Swim Team"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDFlatButton: 
        text: ""
        size_hint: (0.27, 0.255)
        pos_hint: {'center_x': 0.17, 'center_y': 0.7}
        on_release: root.manager.current = "swimTeam"
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        elevation: 10
        MDLabel:
            text: "Water Polo Team"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.83, 'center_y': 0.7}
        elevation: 10
        MDLabel:
            text: "Tennis Team"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.17, 'center_y': 0.3}
        elevation: 10
        MDLabel:
            text: "Soccer Club"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        elevation: 10
        MDLabel:
            text: "Basketball Team"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 155)
        pos_hint: {'center_x': 0.83, 'center_y': 0.3}
        elevation: 10
        MDLabel:
            text: "Dance Club"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
    BoxLayout:
        orientation: "vertical"
        Widget:
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: "vertical"
            padding: "15dp"
            spacing: "15dp"
                
            Image:
                source: "profilePic1.png"
                    
            MDLabel:
                text: "                  Name: Arya Tawara"
                font_style: "Subtitle1"
                theme_text_color: "Primary"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
                
            MDLabel:
                text: "       Email-ID: aryatawara@gmail.com"
                font_style: "Subtitle1"
                theme_text_color: "Primary"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
            
            MDFillRoundFlatButton:
                text: "Home"
                size_hint: (0.5, 0.2)
                pos_hint: {'center_x': 0.5}
                on_release: root.manager.current = 'menu'
                
                
            MDFillRoundFlatButton:
                text: "Mental Health"
                size_hint: (0.5, 0.2)
                pos_hint: {'center_x': 0.5}
                on_release: root.manager.current = 'mental'
                    
            ScrollView:

<SwimTeamScreen>
    name: "swimTeam"
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (800, 80)
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        elevation: 11

        MDLabel:
            text: "Swim Team"
            halign: "center"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: (33 / 256, 150 / 256, 243 / 256, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (600, 55)
        pos_hint: {'center_x': 0.5, 'center_y': 0.79}
        elevation: 11
        MDLabel:
            halign: "center"
            text: "Coach: Timothy Shane"
            font_style: "Subtitle1"
            bold: True
            theme_text_color: "Primary"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            halign: "center"
            text: "Members: 32"
            font_style: "Subtitle1"
            bold: True
            theme_text_color: "Primary"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            halign: "center"
            text: "Location: Aquatic Center"
            font_style: "Subtitle1"
            bold: True
            theme_text_color: "Primary"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (170, 120)
        pos_hint: {'center_x': 0.231, 'center_y': 0.6}
        elevation: 11
    
    MDLabel:
        halign: "center"
        text: "Practice Dates:"
        font_style: "H6"
        theme_text_color: "Primary"
        pos_hint: {'center_x': 0.231, 'center_y': 0.667}
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (600, 275)
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        elevation: 11
        BoxLayout:
            orientation: 'vertical'
            spacing: "7dp"
            OneLineListItem:
                text: "First Day Practice                                                                                                    4/12"
            OneLineListItem:
                text: "Freestyle Practice                                                                                                    4/19"
            OneLineListItem:
                text: "Diving Practice                                                                                                        4/26"
            OneLineListItem:
                text: "Game Prep                                                                                                                 5/1"
            OneLineListItem:
                text: "Backstroke Practice                                                                                                  5/7"
            ScrollView:

    MDFillRoundFlatButton:
        text: "BACK"
        on_release: root.manager.current = "physical"
        pos_hint: {'center_x': 0.4, 'center_y': 0.1}
        size_hint: (0.12, 0.06)    
        
    MDFillRoundFlatButton:
        text: "SIGN UP"
        pos_hint: {'center_x': 0.6, 'center_y': 0.1}
        size_hint: (0.12, 0.06)
        on_release: app.dialog_show()
        
<MentalScreen>
    name: "mental"
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (800, 80)
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        elevation: 11

        MDLabel:
            text: "Mental Health"
            halign: "center"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: (33 / 256, 150 / 256, 243 / 256, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    
    MDIconButton:
        icon: "menu"
        pos_hint: {'center_x': 0.05, 'center_y': 0.95}
        on_release: nav_drawer.set_state()
        
        
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (225, 70)
        pos_hint: {'center_x': 0.203, 'center_y': 0.795}
        elevation: 10
        
    MDLabel:
        text: "Feeling Stressed?"
        font_style: "H5"
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.205, 'center_y': 0.815}
        theme_text_color: "Primary"    
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (700, 180)
        pos_hint: {'center_x': 0.5, 'center_y': 0.625}
        elevation: 10
    
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 135)
        pos_hint: {'center_x': 0.22, 'center_y': 0.625}
        elevation: 10
        MDLabel:
            text: "Breathing Exercises"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
        
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 135)
        pos_hint: {'center_x': 0.78, 'center_y': 0.625}
        elevation: 10
        
        MDLabel:
            text: "Meditation"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDFlatButton: 
        text: ""
        size_hint: (0.255, 0.225)
        pos_hint: {'center_x': 0.22, 'center_y': 0.625}
        on_release: root.manager.current = "breathingExer"        
      
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (180, 70)
        pos_hint: {'center_x': 0.825, 'center_y': 0.365}
        elevation: 10
    MDLabel:
        text: "Feeling Sad?"
        font_style: "H5"
        bold: True
        halign: 'center'
        pos_hint: {'center_x': 0.827, 'center_y': 0.385}
        theme_text_color: "Primary"    
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (700, 180)
        pos_hint: {'center_x': 0.5, 'center_y': 0.195}
        elevation: 10
        
    MDCard:
        focus_behavior: True
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 135)
        pos_hint: {'center_x': 0.22, 'center_y': 0.195}
        elevation: 10
        MDLabel:
            text: "Mood Booster"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
            
    MDCard:
        focus_behavior: True
        #on_touch_down: nav()
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (210, 135)
        pos_hint: {'center_x': 0.78, 'center_y': 0.195}
        elevation: 10
        
        MDLabel:
            text: "Other Activities"
            font_style: "H6"
            halign: "center"
            theme_text_color: "Primary"
            #theme_text_color: "Custom"
            #text_color: (33/256, 150/256, 243/256, 1)
        
    BoxLayout:
        orientation: "vertical"
        Widget:
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: "vertical"
            padding: "15dp"
            spacing: "15dp"
                
            Image:
                source: "profilePic1.png"
                    
            MDLabel:
                text: "                  Name: Arya Tawara"
                font_style: "Subtitle1"
                theme_text_color: "Primary"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
                
            MDLabel:
                text: "       Email-ID: aryatawara@gmail.com"
                font_style: "Subtitle1"
                theme_text_color: "Primary"
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
            
            MDFillRoundFlatButton:
                text: "Home"
                size_hint: (0.5, 0.2)
                pos_hint: {'center_x': 0.5}
                on_release: root.manager.current = 'menu'
                    
            MDFillRoundFlatButton:
                text: "Physical Well-Being"
                size_hint: (0.5, 0.2)
                pos_hint: {'center_x': 0.5}
                on_release: root.manager.current = 'physical'
                
            ScrollView:
            
<BreathingExercisesScreen>
    name: "breathingExer"
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (800, 80)
        pos_hint: {'center_x': 0.5, 'center_y': 0.96}
        elevation: 11

        MDLabel:
            text: "Breathing Exercises"
            halign: "center"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: (33 / 256, 150 / 256, 243 / 256, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (160, 60)
        pos_hint: {'center_x': 0.25, 'center_y': 0.8}
        elevation: 11
        MDLabel:
            text: 'Reduce Stress'
            theme_text_color: "Primary"
            halign: "center"
            bold: True
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (160, 60)
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        elevation: 11
        MDLabel:
            text: ' Lower Blood Pressure '
            theme_text_color: "Primary"
            halign: "center"
            bold: True
            
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (160, 60)
        pos_hint: {'center_x': 0.75, 'center_y': 0.8}
        elevation: 11
        MDLabel:
            text: 'Improve Sleep' 
            theme_text_color: "Primary"
            halign: "center"
            bold: True
    
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (160, 60)
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        elevation: 11
        MDLabel:
            text: 'Procedure' 
            font_style: "H5"
            theme_text_color: "Primary"
            halign: "center"
            bold: True
            
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (180, 80)
        pos_hint: {'center_x': 0.23, 'center_y': 0.3}
        elevation: 11
        MDLabel:
            text: 'Take in a deep breath' 
            theme_text_color: "Primary"
            halign: "center"
            bold: True
            
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (180, 80)
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        elevation: 11
        MDLabel:
            text: '  Hold your breath for  five seconds' 
            theme_text_color: "Primary"
            halign: "center"
            bold: True
            
    MDCard:
        border_radius: 10
        radius: [10]
        size_hint: (None, None)
        size: (180, 80)
        pos_hint: {'center_x': 0.77, 'center_y': 0.3}
        elevation: 11
        MDLabel:
            text: 'Slowy exhale. Repeat until you feel calm' 
            theme_text_color: "Primary"
            halign: "center"
            bold: True
    
    MDFillRoundFlatButton:
        text: "BACK"
        on_release: root.manager.current = "mental"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        size_hint: (0.12, 0.06) 
"""


class BreathingExercisesScreen(Screen):
    pass


class SwimTeamScreen(Screen):
    pass


class EnglishScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class PhysicalScreen(Screen):
    pass


class MentalScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(PhysicalScreen(name="physical"))
sm.add_widget(MentalScreen(name="mental"))
sm.add_widget(EnglishScreen(name="english"))
sm.add_widget(SwimTeamScreen(name="swimTeam"))
sm.add_widget(BreathingExercisesScreen(name="breathingExer"))


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(screen_layout)

        return screen

    def dialog_show(self):
        self.dialog = MDDialog(text="Congratulations! You have just become the newest member of our Swim Team. We hope you have a great time. More details will be emailed to you soon!",
                               size_hint=(0.8, 1.0), auto_dismiss=False, buttons=[MDFillRoundFlatButton(text="Close", on_release=lambda x: self.dialog_handler(x))])
        self.dialog.open()

    def dialog_handler(self, widget):
        if widget.__class__.__name__ == "MDFillRoundFlatButton":
            self.dialog.dismiss()


if __name__ == "__main__":
    App().run()
