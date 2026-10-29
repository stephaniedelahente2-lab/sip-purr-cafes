# Sip and Purr Cafe Stock and sales Management System

products = {}
sales=[]
sales_records =[]

def add_product():
    name = input("Enter product name: ").title()
    
    if name in products:
        print("Products already exists!")
        return
    
    price = int(input("Enter product price: "))
    quantity = int(input("Enter stock quantity: "))
    low_stock = int(input("Enter low-stock level: "))
    
    products[name] = {
        "price": price,
        "quantity": quantity,
        "low_stock": low_stock
    }
    
    print("Product added successfully!")
    
    
def view_products():
    print("\n=== AVAILABLE PRODUCTS ===")
    
    if not products:
        print("No products available.")
        return
    
    for name, item in products.items():
        print(f"Product: {name}")
        print(f"Price: PHP {item['price']:.2f}")
        print(f"Stock: {item['quantity']}")
        
        if item["quantity"] <= item["low_stock"]:
            print("WARNING: Low stock!")
            
        print("--------------------------")
        
        
def update_stock():
    name = input("Enter product name: ").title()
    
    if name not in products:
        print("Product not found!")
        return
     
    amount = int(input("Enter quantity to add: "))
    
    if amount <= 0:
        print("Quantity must be positive.")
        return
    
    products[name]["quantity"] += amount
    print("Stock update successfully!")
    
def record_sale():
    name = input("Enter product name: ").title()
    
    if name not in products:
        print("Product not found!")
        return
    
    quantity = int(input("Enter quantity sold: "))
    
    if quantity <= 0:
        print("Quantity must be positive.")
        return
    
    if quantity > products[name]["quantity"]:
        print("Not enough stock available!")
        return
    
    total = quantity * products[name]["price"]
    products[name]["quantity"] -= quantity
    
    sales_records.append({
        "product": name,
        "quantity": quantity,
        "total": total
    })
    
    print(f"Sale successful!")
    print(f"Total amount: PHP {float(total):.2F}")
    
    if products[name]["quantity"] <= products[name]["low_stock"]:
        print("WARNING; Product is running low on stock!")
        
def view_report():
    print("\n--- SALES RECORT ---")
    
    if not sales:
        print("No sales recorded.")
        return
    
    total_sales = 0
    
    for sale in sales:
        print(
            f"{sale['product']} | "
            f"Quantity: {sale['quantity']} | "
            f"Total: PHP {sale['total']:.2f}"
        )
        total_sales += sale ["total"]
    print(f"Total Sales: PHP{total_sales:.2F}")
    
    
def main():
    while True:
        print("\n=== SIP AND PURR CAFE ===")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Stock")
        print("4. Record Sale")
        print("5. View Sales Report")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            record_sale()
        elif choice == "5":
            view_report()
        elif choice == "6":
            print(" Thank you for using Sip and Purr Cafe System!")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
        
        
        
        
        
