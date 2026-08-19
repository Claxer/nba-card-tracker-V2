import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "cards.db"


def connect_database():
    return sqlite3.connect(DATABASE_PATH)


def create_database():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            player TEXT NOT NULL,
            team TEXT,

            year INTEGER NOT NULL,

            brand TEXT,
            card_set TEXT,
            card_number TEXT,

            parallel TEXT,
            grade TEXT,

            purchase_price REAL DEFAULT 0,
            current_value REAL DEFAULT 0,

            quantity INTEGER DEFAULT 1,

            notes TEXT,
            image_path TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def add_card(
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
    image_path
):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO cards (
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
            image_path
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
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
        image_path
    ))

    connection.commit()
    connection.close()


def get_all_cards():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM cards
        ORDER BY id DESC
    """)

    cards = cursor.fetchall()

    connection.close()

    return cards


def delete_card(card_id):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM cards WHERE id = ?",
        (card_id,)
    )

    connection.commit()
    connection.close()

def get_collection_stats():
    """Calculate collection statistics."""

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COALESCE(SUM(quantity), 0),
            COALESCE(SUM(purchase_price * quantity), 0),
            COALESCE(SUM(current_value * quantity), 0)
        FROM cards
    """)

    result = cursor.fetchone()

    connection.close()

    total_cards = result[0]
    total_invested = result[1]
    total_value = result[2]

    profit_loss = total_value - total_invested

    return (
        total_cards,
        total_invested,
        total_value,
        profit_loss
    )


def get_most_valuable_card():
    """Return the most valuable card in the collection."""

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT player, year, brand, card_set, current_value
        FROM cards
        ORDER BY current_value DESC
        LIMIT 1
    """)

    card = cursor.fetchone()

    connection.close()

    return card

def update_card(
    card_id,
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
):
    """Update an existing card."""

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE cards
        SET
            player = ?,
            team = ?,
            year = ?,
            brand = ?,
            card_set = ?,
            card_number = ?,
            parallel = ?,
            grade = ?,
            purchase_price = ?,
            current_value = ?,
            quantity = ?,
            notes = ?
        WHERE id = ?
    """, (
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
        card_id
    ))

    connection.commit()
    connection.close()