SELECT class from (

SELECT count(*) as student_count, class
from Courses GROUP by class
) as student_counts
WHERE student_count > 4