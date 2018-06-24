-- creates the database hbtn_0d_usa and the table cities
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE cities (
       id INT NOT NULL UNIQUE AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES id,
       PRIMARY KEY (id)
)
