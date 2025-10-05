 PostgreSQL CRUD Command-Line App

 Description
This is a command-line application built in Python that connects to a PostgreSQL database and performs full CRUD (Create, Read, Update, Delete) operations on the **customers** table.  
It also demonstrates SQL injection safety and includes one complex SELECT query with multiple conditions.

---

 Prerequisites
Before running this project, make sure you have:
- **Python 3.10+**
- **PostgreSQL** installed and running locally
- The **psycopg2** library (install with `pip install psycopg2`)

---

 Environment Variables
You can change the database connection in the script:
```python
hostname = "localhost"
database = "midterm"
username = "postgres"
pwd = "mypassword"
port_id = 5432
