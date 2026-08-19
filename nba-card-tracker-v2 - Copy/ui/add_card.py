import customtkinter as ctk
from tkinter import messagebox, filedialog
from pathlib import Path
import shutil

from database.database import add_card


class AddCard(ctk.CTkFrame):

    def __init__(self, master, on_card_added=None):
        super().__init__(master)

        self.on_card_added = on_card_added

        self.image_path = ""

        self.build_page()

    def build_page(self):

        title = ctk.CTkLabel(
            self,
            text="Add New NBA Card",
            font=("Arial", 30, "bold")
        )

        title.pack(
            anchor="w",
            padx=40,
            pady=(30, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Enter the details of your card below.",
            font=("Arial", 15)
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 20)
        )

        form = ctk.CTkFrame(self)

        form.pack(
            padx=40,
            pady=10,
            fill="x"
        )

        ctk.CTkLabel(
            form,
            text="Player"
        ).grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 5),
            sticky="w"
        )

        self.player_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="LeBron James"
        )

        self.player_entry.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Team"
        ).grid(
            row=0,
            column=1,
            padx=20,
            pady=(20, 5),
            sticky="w"
        )

        self.team_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="Los Angeles Lakers"
        )

        self.team_entry.grid(
            row=1,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Year"
        ).grid(
            row=0,
            column=2,
            padx=20,
            pady=(20, 5),
            sticky="w"
        )

        self.year_entry = ctk.CTkEntry(
            form,
            width=180,
            placeholder_text="2024"
        )

        self.year_entry.grid(
            row=1,
            column=2,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Brand"
        ).grid(
            row=2,
            column=0,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.brand_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="Panini"
        )

        self.brand_entry.grid(
            row=3,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Set"
        ).grid(
            row=2,
            column=1,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.set_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="Prizm"
        )

        self.set_entry.grid(
            row=3,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Card Number"
        ).grid(
            row=2,
            column=2,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.card_number_entry = ctk.CTkEntry(
            form,
            width=180,
            placeholder_text="#1"
        )

        self.card_number_entry.grid(
            row=3,
            column=2,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Parallel"
        ).grid(
            row=4,
            column=0,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.parallel_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="Silver"
        )

        self.parallel_entry.grid(
            row=5,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Grade"
        ).grid(
            row=4,
            column=1,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.grade_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="PSA 10 / Raw"
        )

        self.grade_entry.grid(
            row=5,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Quantity"
        ).grid(
            row=4,
            column=2,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.quantity_entry = ctk.CTkEntry(
            form,
            width=180,
            placeholder_text="1"
        )

        self.quantity_entry.insert(
            0,
            "1"
        )

        self.quantity_entry.grid(
            row=5,
            column=2,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Purchase Price ($)"
        ).grid(
            row=6,
            column=0,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.purchase_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="100.00"
        )

        self.purchase_entry.grid(
            row=7,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Current Value ($)"
        ).grid(
            row=6,
            column=1,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.value_entry = ctk.CTkEntry(
            form,
            width=280,
            placeholder_text="150.00"
        )

        self.value_entry.grid(
            row=7,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            form,
            text="Notes"
        ).grid(
            row=8,
            column=0,
            padx=20,
            pady=(10, 5),
            sticky="w"
        )

        self.notes_entry = ctk.CTkTextbox(
            form,
            width=600,
            height=100
        )

        self.notes_entry.grid(
            row=9,
            column=0,
            columnspan=2,
            padx=20,
            pady=(0, 20)
        )

        image_button = ctk.CTkButton(
            form,
            text="📷 Choose Card Image",
            width=200,
            height=40,
            command=self.choose_image
        )

        image_button.grid(
            row=8,
            column=2,
            padx=20,
            pady=(10, 10)
        )

        save_button = ctk.CTkButton(
            self,
            text="💾 SAVE CARD",
            width=250,
            height=50,
            font=("Arial", 16, "bold"),
            command=self.save_card
        )

        save_button.pack(
            pady=25
        )

        self.image_label = ctk.CTkLabel(
            form,
            text="No image selected"
        )

        self.image_label.grid(
            row=9,
            column=2,
            padx=20,
            pady=10
        )

    def choose_image(self):

        file_path = filedialog.askopenfilename(
            title="Select NBA Card Image",
            filetypes=[
                (
                    "Image Files",
                    "*.png *.jpg *.jpeg *.webp"
                )
            ]
        )

        if not file_path:
            return

        self.image_path = file_path

        file_name = Path(file_path).name

        self.image_label.configure(
            text=f"Selected: {file_name}"
        )

    def save_card(self):

        player = self.player_entry.get().strip()
        team = self.team_entry.get().strip()
        year = self.year_entry.get().strip()
        brand = self.brand_entry.get().strip()
        card_set = self.set_entry.get().strip()
        card_number = self.card_number_entry.get().strip()
        parallel = self.parallel_entry.get().strip()
        grade = self.grade_entry.get().strip()

        purchase_price = self.purchase_entry.get().strip()
        current_value = self.value_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        notes = self.notes_entry.get(
            "1.0",
            "end"
        ).strip()

        if not player:
            messagebox.showerror(
                "Missing Information",
                "Please enter the player name."
            )
            return

        if not year:
            messagebox.showerror(
                "Missing Information",
                "Please enter the card year."
            )
            return

        try:

            year = int(year)

            purchase_price = float(
                purchase_price or 0
            )

            current_value = float(
                current_value or 0
            )

            quantity = int(
                quantity or 1
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Information",
                "Year, prices, and quantity must be numbers."
            )

            return

        saved_image = ""
        if self.image_path:
            images_folder = Path("images")

            images_folder.mkdir(
                exist_ok=True
            )

            source = Path(
                self.image_path
            )

            destination = (
                    images_folder /
                    source.name
            )

            shutil.copy2(
                source,
                destination
            )

            saved_image = str(
                destination
            )
        add_card(
            player,
            team,
            year,
            brand,
            card_set,
            card_number,
            parallel,
            grade,
            purchase_price,
            current_value,
            quantity,
            notes,
            saved_image
        )

        messagebox.showinfo(
            "Card Added",
            f"{player} has been added to your collection!"
        )

        self.clear_form()

        if self.on_card_added:
            self.on_card_added()

    def clear_form(self):

        self.player_entry.delete(
            0,
            "end"
        )

        self.team_entry.delete(
            0,
            "end"
        )

        self.year_entry.delete(
            0,
            "end"
        )

        self.brand_entry.delete(
            0,
            "end"
        )

        self.set_entry.delete(
            0,
            "end"
        )

        self.card_number_entry.delete(
            0,
            "end"
        )

        self.parallel_entry.delete(
            0,
            "end"
        )

        self.grade_entry.delete(
            0,
            "end"
        )

        self.quantity_entry.delete(
            0,
            "end"
        )

        self.quantity_entry.insert(
            0,
            "1"
        )

        self.purchase_entry.delete(
            0,
            "end"
        )

        self.value_entry.delete(
            0,
            "end"
        )

        self.notes_entry.delete(
            "1.0",
            "end"
        )