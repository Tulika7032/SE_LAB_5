"""Inventory Management System."""

import json
import logging
from datetime import datetime

logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add an item and quantity to stock."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid input: item=%s, qty=%s", item, qty)
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

def remove_item(item, qty):
    """Remove an item quantity from stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed %s completely from stock", item)
    except KeyError:
        logging.error("Item '%s' not found in stock", item)
    except Exception as e:
        logging.exception("Unexpected error removing item '%s': %s", item, e)

def get_qty(item):
    """Return quantity of the given item."""
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Loaded stock data from %s", file)
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty stock.", file)
        stock_data = {}
    except json.JSONDecodeError:
        logging.error("Failed to parse %s. Invalid JSON format.", file)

def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Saved stock data to %s", file)
    except Exception as e:
        logging.exception("Error saving data to %s: %s", file, e)

def print_data():
    """Print current inventory stock."""
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")

def check_low_items(threshold=5):
    """Return list of items below threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]

def main():
    """Main function for demonstration."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    logging.info("Program executed successfully without eval()")

if __name__ == "__main__":
    main()
