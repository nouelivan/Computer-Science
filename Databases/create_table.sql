-- Table creation and alterations.


CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);


INSERT INTO friends(id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends(id, name, birthday)
VALUES (2, 'Tetiana Danylko', '1993-01-05');

INSERT INTO friends(id, name, birthday)
VALUES (3, 'Javier Nouel', '1995-11-22');


UPDATE friends
SET name = 'Storm'
WHERE id = 1;


ALTER TABLE friends
ADD COLUMN email TEXT;


UPDATE friends
SET email = 'javier@gmail.com'
WHERE id = 3;

UPDATE friends
SET email = 'tetiana@gmail.com'
WHERE id = 2;


DELETE FROM friends
WHERE id = 1;

SELECT * FROM friends;

