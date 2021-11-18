-- dont list rows without names
SELECT IF EXISTS `name`, `score`
FROM `second_table`
ORDER BY `score` DESC;
