import pywhatkit
from datetime import datetime
# --------------------------------------------------
# FUNCTION: Generate Bill Text
# --------------------------------------------------
def generate_bill(items):
    bill = ""
    bill += "********* SUPERMARKET BILL *********\n"
    bill += f"DATE: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
    bill += "-------------------------------------\n"
    total = 0

    for item in items:
        name = item["name"]
        qty = item["qty"]
        price = item["price"]
        category = item["category"]

        amount = qty * price
        total += amount

        bill += f"{name} ({category})\n"
        bill += f"  Qty: {qty} × ₹{price} = ₹{amount}\n"

    gst = total * 0.05    # 5% GST
    grand_total = total + gst

    bill += "-------------------------------------\n"
    bill += f"SUB TOTAL     : ₹{total}\n"
    bill += f"GST (5%)      : ₹{gst:.2f}\n"
    bill += f"TOTAL AMOUNT  : ₹{grand_total:.2f}\n"
    bill += "*************************************\n"

    return bill


# --------------------------------------------------
# FUNCTION: Send Bill on WhatsApp Automatically
# --------------------------------------------------
def send_bill_whatsapp_auto(bill_text, phone_number):
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone_number,
        message=bill_text,
        wait_time=20 # seconds to wait before sending
    )
    print("\nBill Sent Successfully via WhatsApp!")


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------
items = []

n = int(input("Enter number of items: "))

for i in range(n):
    print(f"\nItem {i + 1}:")
    name = input("Enter item name: ")
    category = input("Enter item type/category (e.g., Grocery, Dairy, Snacks): ")
    qty = float(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    items.append({"name": name, "category": category, "qty": qty, "price": price})

# Step 1: Generate text bill
bill_text = generate_bill(items)


print("\nGenerated Bill:\n")
print(bill_text)

# Step 2: Send automatically on WhatsApp
phone = input("Enter WhatsApp number with country code (e.g., +91XXXXXXXXXX): ")
send_bill_whatsapp_auto(bill_text, phone)

