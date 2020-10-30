-- Question 06
SELECT 
    ShotName, EpisodeCode, NumberOfRenders
FROM
    shot
WHERE
    EpisodeCode = 'EP101'
ORDER BY NumberOfRenders ASC;