-- lists the number of records with the same score in the table
SELECT score, COUNT(*) as number FROM second_table GROUP by score ORDER BY number DESC;
