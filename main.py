import customtkinter

# Set appearance mode and default theme
customtkinter.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create the main application window
class HelloWorldApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Hello World - CustomTkinter")
        self.geometry("400x300")

        # Create a label
        self.label = customtkinter.CTkLabel(
            self, text="Hello, World!", font=("Arial", 24)
        )
        self.label.pack(pady=20)

        # Create a button to exit the app
        self.button = customtkinter.CTkButton(
            self, text="Exit", command=self.close_app
        )
        self.button.pack(pady=20)

    def close_app(self):
        self.destroy()


# Run the app
if __name__ == "__main__":
    app = HelloWorldApp()
    app.mainloop()