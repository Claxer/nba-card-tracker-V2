import customtkinter as ctk

from database.database import create_database
from ui.dashboard import Dashboard
from ui.add_card import AddCard
from ui.collection import Collection

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("NBA Card Collection Tracker")

        self.geometry("1400x800")

        self.minsize(
            1200,
            700
        )

        create_database()

        self.build_sidebar()

        self.show_dashboard()

    def build_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        title = ctk.CTkLabel(
            self.sidebar,
            text="🏀 NBA Tracker",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=(30, 40)
        )

        dashboard_button = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            width=180,
            command=self.show_dashboard
        )

        dashboard_button.pack(
            pady=8
        )

        collection_button = ctk.CTkButton(
            self.sidebar,
            text="Collection",
            width=180,
            command=self.show_collection
        )

        collection_button.pack(
            pady=8
        )

        add_card_button = ctk.CTkButton(
            self.sidebar,
            text="Add Card",
            width=180,
            command=self.show_add_card
        )

        add_card_button.pack(
            pady=8
        )

        statistics_button = ctk.CTkButton(
            self.sidebar,
            text="Statistics",
            width=180
        )

        statistics_button.pack(
            pady=8
        )

        # Settings button

        settings_button = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            width=180
        )

        settings_button.pack(
            pady=8
        )

    def clear_page(self):

        for widget in self.winfo_children():

            if widget != self.sidebar:

                widget.destroy()

    def show_dashboard(self):

        self.clear_page()

        self.dashboard = Dashboard(
            self
        )

        self.dashboard.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def show_collection(self):

        self.clear_page()

        self.collection = Collection(
            self,
            on_collection_changed=self.refresh_dashboard
        )

        self.collection.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def show_add_card(self):

        self.clear_page()

        self.add_card_page = AddCard(
            self,
            on_card_added=self.refresh_dashboard
        )

        self.add_card_page.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def refresh_dashboard(self):

        self.show_dashboard()


if __name__ == "__main__":

    app = App()

    app.mainloop()