CREATE DATABASE user_management;

USE user_management;

CREATE TABLE users1 (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,  -- Adjusted length for hashed passwords
    email VARCHAR(100),
    full_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Corrected INSERT statement with quotes around string values
INSERT INTO users1 (username, password, email, full_name)
VALUES ('Jon_smith12', 'hashedpassword', 'jonsmith@gmail.com', 'Jon Smith');

SELECT * FROM users1;
