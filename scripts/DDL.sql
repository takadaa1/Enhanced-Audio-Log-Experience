CREATE TABLE users (
userID serial PRIMARY KEY,
username VARCHAR(250),
password VARCHAR(250)
);

CREATE TABLE administrator (
userID INT NOT NULL,
permissions BOOLEAN DEFAULT TRUE,
FOREIGN KEY(userID)
      REFERENCES users (userID)
);

CREATE TABLE interview (
id serial PRIMARY KEY,
title VARCHAR(250) NOT NULL,
date DATE NOT NULL,
audio TEXT NOT NULL,
thumbnail TEXT NOT NULL,
script TEXT,
uID INT NOT NULL,
FOREIGN KEY (uID)
      REFERENCES users (userID)
);

CREATE TABLE assets (
FiD INT NOT NULL,
timestamp VARCHAR(8),
hyperlink TEXT,
image TEXT,
text TEXT,
FOREIGN KEY (FiD)
      REFERENCES interview (id)
);
