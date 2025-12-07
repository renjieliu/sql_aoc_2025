drop table if exists #input 

select s_id = 1	, s = '.......S.......' into #input
union all select s_id = 2	, s = '...............'
union all select s_id = 3	, s = '.......^.......'
union all select s_id = 4	, s = '...............'
union all select s_id = 5	, s = '......^.^......'
union all select s_id = 6	, s = '...............'
union all select s_id = 7	, s = '.....^.^.^.....'
union all select s_id = 8	, s = '...............'
union all select s_id = 9	, s = '....^.^...^....'
union all select s_id = 10	, s = '...............'
union all select s_id = 11	, s = '...^.^...^.^...'
union all select s_id = 12	, s = '...............'
union all select s_id = 13	, s = '..^...^.....^..'
union all select s_id = 14	, s = '...............'
union all select s_id = 15	, s = '.^.^.^.^.^...^.'
union all select s_id = 16	, s = '...............'


select * from #input


; with cte as
(
    select r = s_id, c = 1, ch = left(s, 1), rem = SUBSTRING(s, 2 , len(s)) from #input 
    union all 
    select r, c+1, left(rem, 1), SUBSTRING(rem, 2, len(rem))  from cte  
    where len(rem) > 0    
)
select * from cte 
order by r, c
option (maxrecursion 0)
 



-- 20251207_090511 
--- Stop here  - the issue is to look back the previous line, and update before continue
-- Right now, I can only think of using a custom function for string manipulation








