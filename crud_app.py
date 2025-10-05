import psycopg2

hostname = "localhost"
database = "midterm"
username = "postgres"
pwd = "mypassword"
port_id = 5432


def connect():
    return psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )


def create_customer():
    full_name = input("Enter full name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone = input("Enter phone: ")
    address = input("Enter address: ")

    conn = connect()
    cur = conn.cursor()

    print("\nBefore insert:")
    cur.execute("SELECT * FROM customers;")
    for row in cur.fetchall():
        print(row)

    cur.execute("""
        INSERT INTO customers (full_name, email, password, phone, address)
        VALUES (%s, %s, %s, %s, %s)
    """, (full_name, email, password, phone, address))
    conn.commit()

    print("\nAfter insert:")
    cur.execute("SELECT * FROM customers;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def read_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def read_by_id():
    customer_id = input("Enter customer ID: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers WHERE customer_id = %s;", (customer_id,))
    record = cur.fetchone()
    if record:
        print(record)
    else:
        print("Customer not found.")
    cur.close()
    conn.close()


def update_customer():
    customer_id = input("Enter customer ID to update: ")
    new_email = input("Enter new email: ")

    conn = connect()
    cur = conn.cursor()

    print("\nBefore update:")
    cur.execute("SELECT * FROM customers WHERE customer_id = %s;", (customer_id,))
    print(cur.fetchone())

    cur.execute("UPDATE customers SET email = %s WHERE customer_id = %s;", (new_email, customer_id))
    conn.commit()

    print("\nAfter update:")
    cur.execute("SELECT * FROM customers WHERE customer_id = %s;", (customer_id,))
    print(cur.fetchone())

    cur.close()
    conn.close()


def delete_customer():
    customer_id = input("Enter customer ID to delete: ")

    conn = connect()
    cur = conn.cursor()

    print("\nBefore delete:")
    cur.execute("SELECT * FROM customers;")
    for row in cur.fetchall():
        print(row)

    cur.execute("DELETE FROM customers WHERE customer_id = %s;", (customer_id,))
    conn.commit()

    print("\nAfter delete:")
    cur.execute("SELECT * FROM customers;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def complex_select():
    print("\n===== COMPLEX CUSTOMER SEARCH =====")
    print("You can leave any field empty to skip that condition.\n")

    name_start = input("Enter starting letter(s) of full name (e.g. B): ").strip()
    address_part = input("Enter part of address to search (e.g. 'Astana'): ").strip()
    email_end = input("Enter email ending (e.g. '.com', '.ru', '.kz'): ").strip()

    query = "SELECT * FROM customers WHERE 1=1"
    params = []

    if name_start:
        query += " AND full_name ILIKE %s"
        params.append(name_start + '%')

    if address_part:
        query += " AND address ILIKE %s"
        params.append('%' + address_part + '%')

    if email_end:
        query += " AND email ILIKE %s"
        params.append('%' + email_end)

    conn = connect()
    cur = conn.cursor()
    cur.execute(query, tuple(params))
    rows = cur.fetchall()

    print("\nSearch results:")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No customers found with given filters.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    while True:
        print("\n===== CUSTOMER MANAGEMENT APP =====")
        print("1. Create new customer")
        print("2. Read all customers")
        print("3. Read customer by ID")
        print("4. Update customer email by ID")
        print("5. Delete customer by ID")
        print("6. Complex customer search (custom filters)")
        print("0. Exit")

        choice = input("Enter choice (0-6): ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            read_all()
        elif choice == "3":
            read_by_id()
        elif choice == "4":
            update_customer()
        elif choice == "5":
            delete_customer()
        elif choice == "6":
            complex_select()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
