-- 코드를 입력하세요
SET @hour := -1; -- 변수 선언, 1씩 늘릴 것이므로 -1부터 시작해야 0부터 시작하게 됨

SELECT (@hour := @hour + 1) as HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23 -- @hour+1이므로 23에서 끝남