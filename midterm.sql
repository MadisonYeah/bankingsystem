CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE,
    account_type VARCHAR(20) CHECK (account_type IN ('Savings', 'Checking')),
    balance NUMERIC(12,2) DEFAULT 0 CHECK (balance >= 0),
    opened_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES accounts(account_id) ON DELETE CASCADE,
    transaction_type VARCHAR(20) CHECK (transaction_type IN ('Deposit', 'Withdrawal', 'Transfer')),
    amount NUMERIC(12,2) NOT NULL CHECK (amount > 0),
    description TEXT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cards (
    card_id SERIAL PRIMARY KEY,
    account_id INT NOT NULL REFERENCES accounts(account_id) ON DELETE CASCADE,
    card_number VARCHAR(16) UNIQUE NOT NULL,
    card_type VARCHAR(20) CHECK (card_type IN ('Debit', 'Credit')),
    expiration_date DATE NOT NULL,
    cvv CHAR(3) NOT NULL
);

CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id) ON DELETE CASCADE,
    amount NUMERIC(12,2) NOT NULL,
    interest_rate NUMERIC(5,2) NOT NULL,
    start_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Closed', 'Overdue'))
);

CREATE TABLE loan_payments (
    payment_id SERIAL PRIMARY KEY,
    loan_id INT NOT NULL REFERENCES loans(loan_id) ON DELETE CASCADE,
    payment_date DATE NOT NULL,
    amount NUMERIC(12,2) NOT NULL
);

INSERT INTO customers (full_name, email, password, phone, address)
VALUES
('Man Man', 'man@man.kz', 'manman', '111-111-111', 'Astana'),
('Woman Woman', 'woman@woman.kz', 'womanwoman', '111-111-222', 'Almaty'),
('Abai Kunanbaev', 'abai@edu.kz', 'abaibol', '111-111-333', 'Semei'),
('Spider Man', 'spidey@gmail.com', 'spiderman', '111-111-444', 'New York'),
('Yerkanat Amangeldi', 'amangeldi@mail.ru', 'amangeldi', '111-111-555', 'Karaganda'),
('Thor Bjornson', 'thor@thunder.com', 'thorthor', '111-111-666', 'Asgard'),
('Blue Guy', 'imblue@daba.dee', 'dabudai', '111-111-777', 'Andromeda'),
('Stan Lee', 'marvel@mail.com', 'leelee', '111-111-888', 'Heaven'),
('Vladimmir Putin', 'putin@mail.ru', 'rusiabest', '111-111-999', 'Moscow'),
('Bat Man', 'bat@man.kz', 'batcar', '111-222-111', 'Gotham'),
('Black Ninja', 'ninja@dot.com', 'blackblack', '111-222-222', 'Africa');

SELECT * FROM customers;