(*CIS 425 Homework 1*)
(*Olivia Pannell*)


(* #1 Takes two dates and evaluates to true or false. It evalates to true if the first argument is a date that comes before the second argument. (If the two dates are the same, the result is false.)*)

fun is_older(x1 : (int * int * int), x2 : (int * int * int))=
    if #1 x1  > #1 x2
    then false
    else if #1 x1 < #1 x2
    then true
    else
	if #2 x1 > #2 x2
	then false
	else if #2 x1 < #2 x2
	then true
	else
		if #3 x1 >= #3 x2
		then false
		else true

(* #2 Takes a list of dates and a month (i.e., an int) and returns how many dates in the list are in the given month*)
fun number_in_month(ds : (int * int * int) list, m : int) =
    if null ds then 0
    else
	if #2 (hd ds) = m
	then 1 + number_in_month(tl ds, m)
	else
		number_in_month(tl ds, m)

(* #3 Takes a list of dates and a list of months (i.e., an int list)
and returns the number of dates in the list of dates that are in any of the months in the list of months.*)
fun number_in_months(ds : (int * int * int) list, ms : int list) =
    if null ms then 0
    else
	number_in_month(ds, hd ms) + number_in_months(ds, tl ms)

(* #4 Takes a list of dates and a month (i.e., an int) and returns a
list holding the dates from the argument list of dates that are in the month.*)
fun dates_in_month(ds : (int * int * int) list, ms : int) =
    if null ds then []
    else
	if #2 (hd ds) = ms
	then (hd ds) :: dates_in_month(tl ds, ms)
	else
		dates_in_month(tl ds, ms)

(* #5 Takes a list of dates and a list of months (i.e., an int list) and returns a list holding the dates from the argument list of dates that are in any of the months in the list of months.*)
fun dates_in_months(ds : (int * int * int) list, ms : int list) =
    if null ms
    then []
    else
	dates_in_month(ds, hd ms) @ dates_in_months(ds, tl ms)


(* #6 Takes a list of strings and an int n and returns the nth element of the list where the head of the list is 1st.*)
val count = 1;
fun get_nth(st : string list, n : int) =
    if count = n
    then hd st
    else
	get_nth(tl st, n - 1)

(* #7 Takes a date and returns a string of the form September-10-2015 (for example).*)
val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
fun date_to_string(date : (int * int * int)) =
    get_nth(months, #2 date) ^ "-" ^Int.toString(#3 date)^"-"^Int.toString(#1 date)

(* #8 Write a function number_before_reaching_sum that takes an int called sum and an int list and returns an int.
You should return an int n such that the first n elements of the list add to less than sum, but the first
n + 1 elements of the list add to sum or more. *)
fun number_before_reaching_sum(sum : int, numls : int list) =
    if (hd numls) >= sum
    then 0
    else
	1 + number_before_reaching_sum(sum - (hd numls), tl numls)

(* #9 Write a function what_month that takes a day of year (i.e., an int between 1 and 365) and returns
what month that day is in (1 for January, 2 for February, etc.).*)
val days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
fun what_month(day: int) =
    1 + number_before_reaching_sum(day, days_in_months)

(* #10 Write a function month_range that takes two days of the year day1 and day2 and returns an int list
[m1,m2,...,mn] where m1 is the month of day1, m2 is the month of day1+1, ..., and mn is the month
of day day2. *)
fun month_range(day1 : int, day2 : int) =
    if day2 < day1
    then []
    else
	what_month(day1)::month_range((day1+1), day2)

(* #11 Write a function oldest that takes a list of dates and evaluates to an (int*int*int) option. It
evaluates to NONE if the list has no dates else SOME d where the date d is the oldest date in the list. *)
fun oldest(dates : (int * int * int) list) =
    if null dates
    then NONE
    else
	let
		fun old(dates: (int*int*int)list)=
		    if null (tl dates)
		    then (hd dates)
		    else
			let
				val tail = old(tl dates) (*oldest*)
				val last = (hd dates) (*most recent*)
             		in
				if is_older(last, tail)
				then last
				else
					tail
			end
       	in
		SOME(old(dates))
	end

(* #12 Write a function cumulative_sum that takes a list of numbers and returns a list of the partial sums
of these numbers. For example, cumulative_sum [12,27,13] = [12,39,52]. *)
fun cumulative_sum(nums: int list) =
    let fun csum(nums: int list) =
    	if null nums then [0]
    	else
		let val tail = csum(tl nums)
		in (hd nums) + (hd tail) :: tail
		end

	fun helper(x1: int list, x2: int list) =
    	    if null x1
   	    then x2
   	    else
		helper(tl x1, hd x1:: x2)


    in tl(helper(csum(helper(nums, [])), []))
    end