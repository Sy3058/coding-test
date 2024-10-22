-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
    LEFT JOIN ANIMAL_INS I
    ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL -- OUTS에만 있으면 JOIN 후 INS에는 NULL 값이 할당됨
ORDER BY O.ANIMAL_ID