-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY LIKE 'FRONT%') & SKILL_CODE > 0
ORDER BY ID