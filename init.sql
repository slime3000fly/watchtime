-- Creating the "Login" table
CREATE TABLE Login (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password VARCHAR
);

-- Creating the "WatchTimeData" table
CREATE TABLE WatchTimeData (
    data_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Login(id),
    data_date DATE
);

-- Creating the "AppData" table
CREATE TABLE AppData (
    app_id SERIAL PRIMARY KEY,
    app_name TEXT
);

-- Creating the "AppTime" table
CREATE TABLE AppTime (
    id SERIAL PRIMARY KEY,
    data_id INTEGER REFERENCES WatchTimeData(data_id),
    app_id INTEGER REFERENCES AppData(app_id),
    time_spent INTEGER
);
