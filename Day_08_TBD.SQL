-- 20251208_171401 : need to find a way for union find in SQL



drop table if exists #input

select s_id = 1, s = '162,817,812' into #input union all
select s_id = 2, s = '57,618,57' union all
select s_id = 3, s = '906,360,560' union all
select s_id = 4, s = '592,479,940' union all
select s_id = 5, s = '352,342,300' union all
select s_id = 6, s = '466,668,158' union all
select s_id = 7, s = '542,29,236' union all
select s_id = 8, s = '431,825,988' union all
select s_id = 9, s = '739,650,466' union all
select s_id = 10, s = '52,470,668' union all
select s_id = 11, s = '216,146,977' union all
select s_id = 12, s = '819,987,18' union all
select s_id = 13, s = '117,168,530' union all
select s_id = 14, s = '805,96,715' union all
select s_id = 15, s = '346,949,466' union all
select s_id = 16, s = '970,615,88' union all
select s_id = 17, s = '941,993,340' union all
select s_id = 18, s = '862,61,35' union all
select s_id = 19, s = '984,92,344' union all
select s_id = 20, s = '425,690,689'  


drop table if exists #base 

; with input as 
(
    select s_id, s = s+',' from #input
)
, cte as 
( select s_id, id = 1,  d = cast( left(s, charindex(',', s)-1) as bigint) , rem = SUBSTRING(s, CHARINDEX(',', s)+1, len(s)), og = s from input
    union all
  select s_id, id + 1,   cast(  left(rem, CHARINDEX(',', rem)-1)  as bigint)  , SUBSTRING(rem, CHARINDEX(',', rem)+1, len(rem)), og  from cte 
  where CHARINDEX(',', rem) > 0
)
select s_id, id , d, og
 into #base
 from cte
order by 1 


; with base as (
select distinct 
a_s_id = a.s_id
, b_s_id =  b.s_id 
-- , a.id
-- , b.id 
-- , a.d
-- , b.d 
, a = a.og 
, b = b.og 
, cost = sum( power(a.d  - b.d, 2) ) over(partition by a.s_id , b.s_id)
 from #base a inner join #base b 
on a.s_id < b.s_id and a.id = b.id 
) 
, ordered as (
select  
rn = ROW_NUMBER() over(order by cost)
, a_s_id = '`' + cast(a_s_id as varchar) + '`'
, b_s_id  ='`' + cast(b_s_id as varchar) + '`'
, a
, b
, cost
from base
) 
,top10 as 
(select 
  rn = '`'+ cast(rn as varchar(max)) + '`'
  , a_s_id 
  , b_s_id
  , a
  , b
  , cost
 from ordered where rn <= 10
)  -- select * from top10 order by cost   ; 
, cte as (
  select 
  rn
  , a_s_id
  , b_s_id
  , a
  , b
  , id_path = cast ( a_s_id + b_s_id  as varchar(max))
  , rn_path = rn
  , og  = rn
  from top10 
  union all 
  select 
  b.rn
  , c.b_s_id
  , b.b_s_id 
  , c.b
  , b.a
  , cast( id_path + b.b_s_id  as varchar(max))
  , c.og
  from top10 b inner join cte c
  on   c.b_s_id = b.a_s_id  
)
select * from cte 
