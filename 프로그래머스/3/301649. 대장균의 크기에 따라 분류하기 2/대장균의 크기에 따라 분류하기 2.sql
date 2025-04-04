-- 코드를 작성해주세요
SELECT A.ID,
CASE
    WHEN A.P <= 0.25 THEN 'CRITICAL' -- 상위 25%
    WHEN A.P <= 0.5 THEN 'HIGH'
    WHEN A.P <= 0.75 THEN 'MEDIUM'
    ELSE 'LOW'
END AS COLONY_NAME
FROM 
(
    SELECT ID,
    PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS P
    FROM ECOLI_DATA
) AS A
ORDER BY A.ID