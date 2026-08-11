import psycopg2


dbname = 'hillel_2026'
user = 'postgres'
password = '123'
host = 'localhost'
port = '5432'


try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")


    cursor = connection.cursor()

# Create categories table__________________________________________________________________
    cursor.execute("""
        CREATE TABLE categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL);
    """)

# Create products table____________________________________________________________________
    cursor.execute("""
        CREATE TABLE products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            description VARCHAR(255),
            price DECIMAL(10, 2) NOT NULL,
            isavailable BOOLEAN,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id));
    """)
    print("Tables created successfully!")

# Insert categories__________________________________________________________________
    cursor.execute("""INSERT INTO categories (name)
                   VALUES
                   ('Electronics'), ('Clothes'), ('Books')""")

# Insert products___________________________________________________________________________
    cursor.execute("""INSERT INTO products  (name, description, price, isavailable, category_id)
    Values
    ('Laptop', 'Gaming laptop', 1500.00, TRUE, 1),
    ('T-shirt', 'Cotton T-shirt', 25.50, TRUE, 2),
    ('Python Book', 'Programming book', 40.00, TRUE, 3)
    """)

    connection.commit()
    print("Data inserted successfully!")

# JOIN________________________________________________________________________________
    cursor.execute("""
           SELECT
               products.name,
               products.description,
               products.price,
               categories.name AS category
           FROM products
           JOIN categories
               ON products.category_id = categories.id
       """)

    result = cursor.fetchall()

    print("Products with categories:")

    for row in result:
        print(row)




except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")