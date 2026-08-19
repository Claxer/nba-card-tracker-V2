import customtkinter as ctk
from tkinter import messagebox

from database.database import update_card


class EditCard(ctk.CTkFrame):

    def __init__(self, master, card, on_card_updated=None):

        super().__init__(master)

        self.card = card
        self.on_card_updated = on_card_updated

        self.build_page()

        self.load_card_data()

    # -------------------------
    # BUILD PAGE
    # -------------------------

    def build_page(self):

        title = ctk.CTkLabel(
            self,
            text="Edit NBA Card",
            font=("Arial", 30, "bold")
        )

        title.pack(
            anchor="w",
            padx=40,
            pady=(30, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Update the information for this card.",
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

        # Player
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
            width=280
        )

        self.player_entry.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        # Team
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
            width=280
        )

        self.team_entry.grid(
            row=1,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        # Year
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
            width=180
        )

        self.year_entry.grid(
            row=1,
            column=2,
            padx=20,
            pady=(0, 15)
        )

        # Brand
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
            width=280
        )

        self.brand_entry.grid(
            row=3,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        # Set
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
            width=280
        )

        self.set_entry.grid(
            row=3,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        # Card number
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
            width=180
        )

        self.card_number_entry.grid(
            row=3,
            column=2,
            padx=20,
            pady=(0, 15)
        )

        # Parallel
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
            width=280
        )

        self.parallel_entry.grid(
            row=5,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        # Grade
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
            width=280
        )

        self.grade_entry.grid(
            row=5,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        # Quantity
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
            width=180
        )

        self.quantity_entry.grid(
            row=5,
            column=2,
            padx=20,
            pady=(0, 15)
        )

        # Purchase price
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
            width=280
        )

        self.purchase_entry.grid(
            row=7,
            column=0,
            padx=20,
            pady=(0, 15)
        )

        # Current value
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
            width=280
        )

        self.value_entry.grid(
            row=7,
            column=1,
            padx=20,
            pady=(0, 15)
        )

        # Notes
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

        # Save
        save_button = ctk.CTkButton(
            self,
            text="💾 SAVE CHANGES",
            width=250,
            height=50,
            font=("Arial", 16, "bold"),
            command=self.save_changes
        )

        save_button.pack(
            pady=25
        )

    # -------------------------
    # LOAD DATA
    # -------------------------

    def load_card_data(self):

        card = self.card

        self.player_entry.insert(0, card[1] or "")
        self.team_entry.insert(0, card[2] or "")
        self.year_entry.insert(0, card[3] or "")
        self.brand_entry.insert(0, card[4] or "")
        self.set_entry.insert(0, card[5] or "")
        self.card_number_entry.insert(0, card[6] or "")
        self.parallel_entry.insert(0, card[7] or "")
        self.grade_entry.insert(0, card[8] or "")

        self.purchase_entry.insert(
            0,
            card[9] or 0
        )

        self.value_entry.insert(
            0,
            card[10] or 0
        )

        self.quantity_entry.insert(
            0,
            card[11] or 1
        )

        if card[12]:

            self.notes_entry.insert(
                "1.0",
                card[12]
            )

    # -------------------------
    # SAVE CHANGES
    # -------------------------

    def save_changes(self):

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

        update_card(
            self.card[0],
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
            notes
        )

        messagebox.showinfo(
            "Card Updated",
            f"{player} has been updated successfully!"
        )

        if self.on_card_updated:

            self.on_card_updated()