-- creates the database hbtn_0d_us and the table states
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE IF NOT EXISTS states (
       id INT NOT NULL UNIQUE AUTO_INCREMENT;
       name VARCHAR(256) NOT NULL;
       PRIMARY KEY (ID);
);