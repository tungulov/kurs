USE kurs;

CREATE TABLE IF NOT EXISTS User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,

    profession VARCHAR(255) NOT NULL,
    employees_date DATE,
    fired_date DATE,

    role VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Ship_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Ship (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ship_name VARCHAR(255) NOT NULL,
    tonnage INT NOT NULL,
    home_port VARCHAR(255) NOT NULL,
    ship_type_id INTEGER NOT NULL,
    FOREIGN KEY (ship_type_id) REFERENCES Ship_types(id)
);

CREATE TABLE IF NOT EXISTS Brigade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    work_date DATE NOT NULL,
    ship_id INTEGER NOT NULL,
    status text,
    FOREIGN KEY (ship_id) REFERENCES Ship(id)
);



CREATE TABLE IF NOT EXISTS BrigadeEmployees(
    id INT AUTO_INCREMENT PRIMARY KEY,
    brigade_id int NOT NULL,
    employer_id int NOT NULL,
    hours INT NOT NULL,
    FOREIGN KEY (brigade_id) REFERENCES Brigade(id),
    FOREIGN KEY (employer_id) REFERENCES User(id)
);

