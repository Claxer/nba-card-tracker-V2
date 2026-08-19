import customtkinter as ctk

from database.database import (
    get_collection_stats,
    get_most_valuable_card
)


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.build_page()

    # -------------------------
    # BUILD PAGE
    # -------------------------

    def build_page(self):

        title = ctk.CTkLabel(
            self,
            text="NBA Card Collection Dashboard",
            font=("Arial", 30, "bold")
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Overview of your current NBA card collection.",
            font=("Arial", 15)
        )

        subtitle.pack(
            anchor="w",
            padx=30,
            pady=(0, 20)
        )

        self.build_statistics()

        self.build_most_valuable()

        self.build_summary()

    # -------------------------
    # STATISTICS
    # -------------------------

    def build_statistics(self):

        stats_frame = ctk.CTkFrame(
            self
        )

        stats_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        (
            total_cards,
            total_invested,
            total_value,
            profit_loss
        ) = get_collection_stats()

        cards = [
            (
                "🃏 Cards Owned",
                f"{total_cards}"
            ),
            (
                "💰 Collection Value",
                f"${total_value:,.2f}"
            ),
            (
                "💵 Money Invested",
                f"${total_invested:,.2f}"
            ),
            (
                "📈 Profit / Loss",
                f"${profit_loss:,.2f}"
            )
        ]

        for i, (title, value) in enumerate(cards):

            box = ctk.CTkFrame(
                stats_frame,
                width=250,
                height=140
            )

            box.grid(
                row=0,
                column=i,
                padx=10,
                pady=15,
                sticky="nsew"
            )

            box.grid_propagate(False)

            title_label = ctk.CTkLabel(
                box,
                text=title,
                font=("Arial", 16)
            )

            title_label.pack(
                pady=(25, 10)
            )

            value_label = ctk.CTkLabel(
                box,
                text=value,
                font=("Arial", 28, "bold")
            )

            value_label.pack()

    # -------------------------
    # MOST VALUABLE CARD
    # -------------------------

    def build_most_valuable(self):

        card = get_most_valuable_card()

        frame = ctk.CTkFrame(
            self
        )

        frame.pack(
            fill="x",
            padx=30,
            pady=15
        )

        title = ctk.CTkLabel(
            frame,
            text="🏆 Most Valuable Card",
            font=("Arial", 20, "bold")
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )

        if card:

            player = card[0]
            year = card[1]
            brand = card[2]
            card_set = card[3]
            value = card[4]

            card_text = (
                f"{player}\n"
                f"{year} {brand} {card_set}"
            )

            card_label = ctk.CTkLabel(
                frame,
                text=card_text,
                font=("Arial", 18)
            )

            card_label.pack(
                anchor="w",
                padx=25,
                pady=5
            )

            value_label = ctk.CTkLabel(
                frame,
                text=f"${value:,.2f}",
                font=("Arial", 28, "bold")
            )

            value_label.pack(
                anchor="w",
                padx=25,
                pady=(5, 20)
            )

        else:

            empty_label = ctk.CTkLabel(
                frame,
                text="You haven't added any cards yet.",
                font=("Arial", 16)
            )

            empty_label.pack(
                padx=25,
                pady=(5, 20)
            )

    # -------------------------
    # SUMMARY
    # -------------------------

    def build_summary(self):

        frame = ctk.CTkFrame(
            self
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(5, 20)
        )

        title = ctk.CTkLabel(
            frame,
            text="Collection Overview",
            font=("Arial", 20, "bold")
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )

        (
            total_cards,
            total_invested,
            total_value,
            profit_loss
        ) = get_collection_stats()

        if total_invested > 0:

            roi = (
                profit_loss /
                total_invested
            ) * 100

        else:

            roi = 0

        summary_text = (
            f"Your collection contains "
            f"{total_cards} card(s).\n\n"

            f"Total invested: "
            f"${total_invested:,.2f}\n\n"

            f"Current collection value: "
            f"${total_value:,.2f}\n\n"

            f"Profit / Loss: "
            f"${profit_loss:,.2f}\n\n"

            f"Return on Investment: "
            f"{roi:.2f}%"
        )

        summary = ctk.CTkLabel(
            frame,
            text=summary_text,
            font=("Arial", 17),
            justify="left"
        )

        summary.pack(
            anchor="w",
            padx=25,
            pady=10
        )