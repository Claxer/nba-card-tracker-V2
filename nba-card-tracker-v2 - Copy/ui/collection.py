import customtkinter as ctk
from database.database import get_all_cards, delete_card
from tkinter import messagebox


class Collection(ctk.CTkFrame):

    def __init__(self, master, on_collection_changed=None):
        super().__init__(master)

        self.on_collection_changed = on_collection_changed

        self.build_page()
        self.load_cards()

    def build_page(self):

        title = ctk.CTkLabel(
            self,
            text="My NBA Card Collection",
            font=("Arial", 30, "bold")
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="View and manage all of your collected cards.",
            font=("Arial", 15)
        )

        subtitle.pack(
            anchor="w",
            padx=30,
            pady=(0, 20)
        )

        search_frame = ctk.CTkFrame(self)

        search_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 15)
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=350,
            height=40,
            placeholder_text="🔍 Search player, team, set..."
        )

        self.search_entry.pack(
            side="left",
            padx=15,
            pady=15
        )

        search_button = ctk.CTkButton(
            search_frame,
            text="Search",
            width=100,
            height=40,
            command=self.search_cards
        )

        search_button.pack(
            side="left",
            padx=5
        )

        clear_button = ctk.CTkButton(
            search_frame,
            text="Clear",
            width=100,
            height=40,
            command=self.clear_search
        )

        clear_button.pack(
            side="left",
            padx=5
        )

        self.scroll_frame = ctk.CTkScrollableFrame(
            self
        )

        self.scroll_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )

    def load_cards(self, cards=None):

        # Remove existing cards

        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        if cards is None:
            cards = get_all_cards()


        if not cards:

            empty_label = ctk.CTkLabel(
                self.scroll_frame,
                text="No cards in your collection yet.",
                font=("Arial", 20)
            )

            empty_label.pack(
                pady=100
            )

            return

        for card in cards:

            self.create_card_item(card)

    def create_card_item(self, card):

        card_id = card[0]
        player = card[1]
        team = card[2]
        year = card[3]
        brand = card[4]
        card_set = card[5]
        card_number = card[6]
        parallel = card[7]
        grade = card[8]
        purchase_price = card[9]
        current_value = card[10]
        quantity = card[11]
        notes = card[12]


        profit = (
            current_value - purchase_price
        ) * quantity

        frame = ctk.CTkFrame(
            self.scroll_frame
        )

        frame.pack(
            fill="x",
            padx=10,
            pady=8
        )

        player_label = ctk.CTkLabel(
            frame,
            text=player,
            font=("Arial", 20, "bold")
        )

        player_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(15, 5),
            sticky="w"
        )

        info = (
            f"{year} {brand} {card_set}  •  "
            f"{parallel or 'Base'}  •  "
            f"{grade or 'Raw'}"
        )

        info_label = ctk.CTkLabel(
            frame,
            text=info,
            font=("Arial", 14)
        )

        info_label.grid(
            row=1,
            column=0,
            padx=20,
            pady=(0, 15),
            sticky="w"
        )

        team_label = ctk.CTkLabel(
            frame,
            text=f"Team: {team or 'N/A'}"
        )

        team_label.grid(
            row=0,
            column=1,
            padx=20
        )

        quantity_label = ctk.CTkLabel(
            frame,
            text=f"Qty: {quantity}"
        )

        quantity_label.grid(
            row=1,
            column=1,
            padx=20
        )

        value_label = ctk.CTkLabel(
            frame,
            text=f"${current_value:,.2f}",
            font=("Arial", 20, "bold")
        )

        value_label.grid(
            row=0,
            column=2,
            padx=20
        )

        profit_label = ctk.CTkLabel(
            frame,
            text=f"Profit: ${profit:,.2f}",
            font=("Arial", 14)
        )

        profit_label.grid(
            row=1,
            column=2,
            padx=20
        )

        # Edit button

        edit_button = ctk.CTkButton(
            frame,
            text="✏️ Edit",
            width=100,
            command=lambda: self.edit_card(card)
        )

        edit_button.grid(
            row=0,
            column=3,
            padx=10,
            pady=(10, 5)
        )

        delete_button = ctk.CTkButton(
            frame,
            text="🗑 Delete",
            width=100,
            command=lambda: self.delete_card(card_id)
        )

        delete_button.grid(
            row=1,
            column=3,
            padx=10,
            pady=(5, 10)
        )

    def search_cards(self):

        search_text = (
            self.search_entry
            .get()
            .strip()
            .lower()
        )

        if not search_text:

            self.load_cards()

            return

        cards = get_all_cards()

        filtered_cards = []

        for card in cards:

            player = str(card[1]).lower()
            team = str(card[2]).lower()
            brand = str(card[4]).lower()
            card_set = str(card[5]).lower()

            if (
                search_text in player
                or search_text in team
                or search_text in brand
                or search_text in card_set
            ):

                filtered_cards.append(card)

        self.load_cards(
            filtered_cards
        )

    def clear_search(self):

        self.search_entry.delete(
            0,
            "end"
        )

        self.load_cards()

    def edit_card(self, card):

        from ui.edit_card import EditCard

        self.pack_forget()

        self.edit_page = EditCard(
            self.master,
            card,
            on_card_updated=self.return_to_collection
        )

        self.edit_page.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    def return_to_collection(self):

        if hasattr(self, "edit_page"):
            self.edit_page.destroy()

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.load_cards()

        if self.on_collection_changed:
            self.on_collection_changed()

    def delete_card(self, card_id):

        confirm = messagebox.askyesno(
            "Delete Card",
            "Are you sure you want to delete this card?"
        )

        if not confirm:
            return

        delete_card(
            card_id
        )

        self.load_cards()

        if self.on_collection_changed:
            self.on_collection_changed()