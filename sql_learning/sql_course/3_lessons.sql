-- SELECT 
-- MATH ::decimal
-- ALIAS AS
-- SELECT DISTINCT 

SELECT * FROM employee; 

SELECT * FROM "Track";

SELECT "Milliseconds", "Bytes" FROM "Track";

SELECT "Milliseconds", "Bytes", "Milliseconds" / CAST("Bytes" AS DECIMAL), "Milliseconds"::decimal / "Bytes"
FROM "Track";

SELECT DISTINCT "AlbumId"
FROM "Track";



