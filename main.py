
import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

from api import get_exchange_rate
from db import init_db, insert_conversion, fetch_history
from utils import format_currency

def display_menu():
    print("\n💱 Currency Converter App 💱")
    print("1. Convert Currency")
    print("2. View Conversion History")
    print("3. Exit")

def convert_currency():
    base = input("Enter base currency (e.g. USD): ")
    target = input("Enter target currency (e.g. EUR): ")
    try:
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print("Invalid amount!")
        return

    result = get_exchange_rate(base, target, amount)
    if result is not None:
        print(f"\n✅ {amount} {base.upper()} = {format_currency(result)} {target.upper()}")
        insert_conversion(base, target, amount, result)
    else:
        print("Failed to fetch conversion.")

def show_history():
    history = fetch_history()
    if not history:
        print("No history found.")
        return

    print("\n📜 Last 10 Conversions:")
    for row in history:
        print(f"{row[4]}: {row[2]} {row[1]} → {format_currency(row[4])} {row[2]}")

def main():
    init_db()
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            convert_currency()
        elif choice == '2':
            show_history()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
