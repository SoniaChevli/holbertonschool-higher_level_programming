-- creates the table unique_id
CREATE IF NOT EXSISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);