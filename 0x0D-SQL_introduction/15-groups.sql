-- lists the number of records with the same score in the table
SELECT name, count(score) as number FROM second_table GROUP by name, score;
