-- dont list rows without names
SELECT `name`, `score`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
