drop table if exists #input 

-- select s = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124' 
select s = '288352-412983,743179-799185,7298346751-7298403555,3269-7729,3939364590-3939433455,867092-900135,25259-67386,95107011-95138585,655569300-655755402,9372727140-9372846709,986003-1032361,69689-125217,417160-479391,642-1335,521359-592037,7456656494-7456690478,38956690-39035309,1-18,799312-861633,674384-733730,1684-2834,605744-666915,6534997-6766843,4659420-4693423,6161502941-6161738969,932668-985784,901838-922814,137371-216743,47446188-47487754,117-403,32-77,35299661-35411975,7778-14058,83706740-83939522' 
into #input 

drop table if exists #base 

select 
rn = ROW_NUMBER() over(order by x.VALUE)
, x.VALUE
, starting = left(x.[value], pos-1)
, ending = SUBSTRING(x.[value] , pos +1, len(x.[value])) 
into #base 
from #input
    cross apply (select * from string_split(s, ',')) x 
    cross apply (select pos = CHARINDEX('-', x.[value]) ) p


--- to generate all the possible from the first half: if length = 1, take it all.

drop table if exists #res1

; with cte as
(select 
rn 
, starting
, ending
, curr = cast ( case when len(starting) = 1 then starting else left(starting, len(starting) / 2)  end as varchar(max))
, found = cast(NULL as bigint)
from #base 

union all 

select
rn
, starting
, ending
, curr = cast ( cast(curr as bigint) + 1  as varchar(max))
, found = cast(curr + curr as bigint)
from cte 
where cast(curr + curr as bigint) <= cast(ending as bigint)
)
select * into #res1 from cte 
option (maxrecursion 0)

-- 40055209690
select ans_1 = sum(found) from #res1  
where found between cast(starting as bigint) and cast(ending as bigint)
 



----------- Part 2 -----------
-- Take all the possible numbers, generate a repeating look up table. 
-- Join to find all the repeating number, and sum the distinct ones. for 8888, it could be '8' * 4 or '88' * 2. But it's the same number

-- to circumvent the double loop, using a prebuilt table instead

drop table if exists #maxx
 
select 
mx = max(cast(curr as int))
, mx_length = max(len(ending)) 
into #maxx  from #res1 

drop table if exists #all_n 


-- select * from #maxx

; with cte as 
(select n = 1 
 union all 
select n + 1 from cte
where n < ( select mx from #maxx) )

select * into #all_n
from cte 
option(maxrecursion 0)


-- this is to get all the possible repeating numbers

drop table if exists #total_repeating 

; with repeat_cte as 
(select 
n
, rep = 2
, curr = cast( REPLICATE(cast( n as varchar), 2) as bigint)
from #all_n
-- where n <= 100
union all 
select
n
, rep + 1
, curr = cast( REPLICATE(cast(n as varchar), rep+1) as bigint)
from repeat_cte 
where rep + 1 <= (select mx_length from #maxx ) / len(cast(n as varchar))
)
select * into  #total_repeating  from repeat_cte



-- 50857215650
select ans_2 =  sum(distinct tr.curr) from #base b inner join #total_repeating tr 
on tr.curr between cast(b.starting as bigint) and cast(b.ending as bigint)






