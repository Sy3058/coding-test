-- 코드를 입력하세요
SELECT O.PRODUCT_ID, P.PRODUCT_NAME, (SUM(O.AMOUNT) * P.PRICE) AS TOTAL_SALES
FROM FOOD_ORDER O
    JOIN FOOD_PRODUCT P
    ON O.PRODUCT_ID = P.PRODUCT_ID
    WHERE O.PRODUCE_DATE LIKE '2022-05%'
GROUP BY O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, O.PRODUCT_ID;
