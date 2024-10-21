-- 코드를 작성해주세요
SELECT A.ID, COALESCE(B.COUNT, 0) AS CHILD_COUNT -- B에 있는 값 중 COUNT를 고름 이때 NULL이면 0으로 변환
FROM ECOLI_DATA A
    LEFT JOIN 
    (
        SELECT PARENT_ID, COUNT(*) AS COUNT
        FROM ECOLI_DATA
        GROUP BY PARENT_ID
        HAVING PARENT_ID IS NOT NULL -- PARENT_ID가 NULL이 아닌 값들을 PARENT_ID를 기준으로 그룹화
    ) B -- PARENT_ID를 부모로 가지는 테이블을 B로 정의
    ON A.ID = B.PARENT_ID
ORDER BY ID