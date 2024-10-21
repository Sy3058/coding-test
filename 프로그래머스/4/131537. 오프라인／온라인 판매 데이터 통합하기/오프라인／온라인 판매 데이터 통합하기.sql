-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3 -- ONLINE_SALE에서 2022년 3월에 판매된 데이터만 출력
UNION -- 쿼리의 결과를 합치고 중복된 ROW 제거
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT -- OFFLINE_SALE의 USER_ID는 NULL로 표시
FROM OFFLINE_SALE
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 3
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID