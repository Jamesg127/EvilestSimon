CREATE TABLE player (
     playerName varchar(255) NOT NULL PRIMARY KEY
);

CREATE TABLE runInfo (
     id INTEGER PRIMARY KEY,
     playerName varchar(255) REFERENCES player(playerName),
     score INTEGER CHECK (score >= 0),
     timeTaken DECIMAL(10, 2) CHECK (timeTaken >= 0)
);

ALTER TABLE player
ADD COLUMN bestRunId INTEGER REFERENCES runInfo(id); 

CREATE TABLE colors (
     runId INTEGER REFERENCES runInfo(id) ON DELETE CASCADE,
     round INTEGER NOT NULL CHECK (round >= 1),
     color varchar(255) NOT NULL CHECK (color IN('red','green','yellow','blue','fail')),
     timeTaken DECIMAL(10,2) NOT NULL CHECK (timeTaken >= 0), 
     PRIMARY KEY (runId, round)
);
