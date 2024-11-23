import customtkinter as ctk

ctk.set_default_color_theme("theme.json")
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"

class MenuApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("App with Fixed Menu")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.geometry("600x600")
        
        self.menu_frame = ctk.CTkFrame(self, corner_radius=0, width=300)
        self.menu_frame.pack(side="left", fill="y", pady=(10,10), padx=10)
        
        self.content_frame = ctk.CTkFrame(self, width=screen_width, height=screen_height, corner_radius=0)
        self.content_frame.pack(side="right", pady=10, padx=(0, 10))
        
        self.menu_buttons = []
        self.create_menu()

        self.frames = {}
        
        for ScreenClass in (HomeScreen, SettingsScreen, AboutScreen):
            frame = ScreenClass(parent=self.content_frame, controller=self)
            self.frames[ScreenClass] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.show_screen(HomeScreen)
    
    def create_menu(self):
        menu_items = [
            ("Home", HomeScreen),
            ("Settings", SettingsScreen),
            ("About", AboutScreen)
        ]
        
        for text, screen_class in menu_items:
            button = ctk.CTkButton(
                self.menu_frame, 
                text=text, 
                command=lambda screen=screen_class: self.show_screen(screen),
                corner_radius=0,
                font=("Arial", 18)
            )

            button.pack(fill="x", pady=1)
            self.menu_buttons.append(button)
    
    def show_screen(self, screen_class):
        frame = self.frames[screen_class]
        frame.tkraise()

class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Welcome to the Home Screen", font=("Arial", 24))
        label.pack(pady=50, padx=50)

class SettingsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Settings Screen", font=("Arial", 24))
        label.pack(pady=50, padx=50)

class AboutScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="About Screen", font=("Arial", 24))
        label.pack(pady=50, padx=50)

if __name__ == "__main__":
    app = MenuApp()
    app.mainloop()