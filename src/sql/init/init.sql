USE kurs;

CREATE TABLE IF NOT EXISTS User_INTERNAL (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS User_EXTERNAL (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS Ship_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Ships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ship_name VARCHAR(255) NOT NULL,
    tonnage INT NOT NULL,
    home_port VARCHAR(255) NOT NULL,
    ship_type_id INTEGER NOT NULL,
    FOREIGN KEY (ship_type_id) REFERENCES Ship_types(id)
);

CREATE TABLE IF NOT EXISTS Registration_card (
    id INT AUTO_INCREMENT PRIMARY KEY,
    arrival_date DATE NOT NULL,
    leaving_date DATE NOT NULL,
    ship_id int NOT NULL,
    employer_id int NOT NULL,
    FOREIGN KEY (ship_id) REFERENCES Ships(id),
    FOREIGN KEY (employer_id) REFERENCES User_EXTERNAL(id)
);