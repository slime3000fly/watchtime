-- Tworzenie tabeli "Logowanie"
CREATE TABLE Logowanie (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password CHAR
);

-- Tworzenie tabeli "DaneWatchTime"
CREATE TABLE DaneWatchTime (
    data_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Logowanie(id),
    data_date DATE
);

-- Tworzenie tabeli "DaneAplikacji"
CREATE TABLE DaneAplikacji (
    app_id SERIAL PRIMARY KEY,
    app_name TEXT
);

-- Tworzenie tabeli "CzasAplikacji"
CREATE TABLE CzasAplikacji (
    id SERIAL PRIMARY KEY,
    data_id INTEGER REFERENCES DaneWatchTime(data_id),
    app_id INTEGER REFERENCES DaneAplikacji(app_id),
    czas INTEGER
);
