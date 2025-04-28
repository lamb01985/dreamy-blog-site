-- TODO: Write an SQL statement to create the "post" table as 
-- depicted in the included entity relationship diagram(ERD)


-- TODO: Write an SQL statement to insert several sample blog
-- posts into the database.
DROP TABLE IF EXISTS post;

CREATE TABLE post (
    id SERIAL PRIMARY KEY, 
    author VARCHAR(255),
    title VARCHAR(255),
    body TEXT,
    posted_date DATE
);

INSERT INTO post (author, title, body, posted_date)
VALUES 
    ('Janine', 'Life is a drag', 'Daria had it all figured out', '2025-01-30'),
    ('Glennon', 'Code all night', 'I love building websites, code is art', '2025-04-27'),
    ('Henry', 'I''d like to visit Portugal', 'I hear Lisbon is beautifiul this time of year', '2025-03-30');
