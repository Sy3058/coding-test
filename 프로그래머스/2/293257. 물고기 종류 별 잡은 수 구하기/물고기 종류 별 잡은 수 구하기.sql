-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT, N.FISH_NAME
FROM FISH_NAME_INFO N
JOIN FISH_INFO I
ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY N.FISH_TYPE, N.FISH_NAME
ORDER BY FISH_COUNT DESC