-- 코드를 입력하세요
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE MONTH(START_DATE) IN (8, 9, 10) AND CAR_ID IN 
(
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) IN (8,9,10)
    GROUP BY CAR_ID
    HAVING COUNT(HISTORY_ID) >= 5
)
GROUP BY MONTH, CAR_ID
HAVING RECORDS > 0 -- 특정 월의 총 대여 횟수가 0인 경우는 제외
ORDER BY MONTH, CAR_ID DESC