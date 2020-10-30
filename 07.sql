-- Question 07
SELECT 
    t1.EpisodeCode, sum(NumberOfRenders) NumberOfRenders, sum(NumberOfAnimatics) NumberOfAnimatics
FROM
    shot AS t1
        JOIN
    episode AS t2 ON t1.EpisodeCode = t2.EpisodeCode
group by EpisodeCode;