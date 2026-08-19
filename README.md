# 🏀 NBA Card Tracker V2

A desktop application built with Python that allows users to manage and track their personal NBA card collection.

The NBA Card Tracker lets users add cards, record card information, track purchase prices and current values, calculate profit or loss, and view their collection through a simple graphical interface.

## 📌 Description

NBA Card Tracker V2 is an improved version of the original NBA Card Tracker project.

The goal of this project is to create a simple digital collection manager for NBA card collectors. Instead of keeping card information manually in a notebook or spreadsheet, users can store their cards inside the application and easily view their collection and its estimated value.

The application uses SQLite to store card information locally.

## ✨ Features

### 🃏 Card Management

- Add NBA cards to your collection
- View all collected cards
- Edit existing card information
- Delete cards
- Record card quantity
- Add notes about each card

### 📋 Card Information

Each card can contain:

- Player name
- Team
- Card year
- Brand
- Card set
- Card number
- Parallel
- Grade
- Purchase price
- Current value
- Quantity
- Notes
- Card image

### 💰 Collection Value

The application calculates:

- Total number of cards
- Total money invested
- Current collection value
- Total profit or loss
- Return on investment (ROI)
- Most valuable card

### 📊 Dashboard

The dashboard provides an overview of the collection, including:

- Cards owned
- Collection value
- Money invested
- Profit/Loss
- ROI
- Most valuable card

## 🛠️ Technologies Used

- Python 3
- CustomTkinter
- SQLite
- Pillow (PIL)
- Tkinter
- pathlib
- shutil

## 📂 Project Structure

```text
nba-card-tracker-v2/
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── ui/
│   ├── __init__.py
│   ├── add_card.py
│   ├── collection.py
│   ├── dashboard.py
│   └── edit_card.py
│
├── images/
│   └── card images
│
├── cards.db
├── main.py
