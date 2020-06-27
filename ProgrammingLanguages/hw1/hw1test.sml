use "hw1.sml";

(* Tests for #1 is_older function*)
val test1  = is_older ((2012, 12, 12), (2003,2,11)); (*False*)
val test2 = is_older ((2012, 12, 12), (2013, 2, 11)); (*True*)
val test3 = is_older ((2020, 11, 19), (2020, 11, 20)); (*True*)

(*Tests for #2 number_in_month function*)
val test4 = number_in_month([(2012,12,8),(2015,12,11), (2020, 12, 3)],12); (*3*)
val test5 = number_in_month([], 11); (*0*)
val test6 = number_in_month([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4)], 4); (*1*)

(*Tests for #3 number_in_months function*)
val test7 = number_in_months([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)], [4, 11]); (*3*)
val test8 = number_in_months([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)], [3, 11]); (*2*)
val test9 = number_in_months([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)], [3,12, 9]); (*0*)

(*Tests for #4 dates_in_month function*)
val test10 = dates_in_month([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)], 11); (*[(2020,11,4), (2020, 11, 19)]*)
val test11 = dates_in_month([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)], 3); (*[]*)

(*Tests for #5 dates_in_months function*)
val test12 = dates_in_months([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)], [4, 11]); (*[(2020, 4, 21), (2020,11,4), (2020, 11, 19)]*)
val test13 = dates_in_months([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)], [3, 5, 6]); (*[(2020,5,6)]*)

(*Tests for #6 get_nth function*)
val test14 = get_nth([("It"), ("is"), ("raining"), ("outside")], 3); (*Raining*)
val test15 = get_nth([("It"), ("is"), ("raining"), ("outside")], 4); (*Outside*)

(*Tests for #7 date_to_string function*)
val test16 = date_to_string (2020, 4, 6); (*April-6-2020*)
val test17 = date_to_string (2020, 11, 26); (*November-26-2020*)

(*Tests for #8 number_before_reaching_sum function*)
val test18 = number_before_reaching_sum (10, ([1, 3, 4, 1, 3, 5])); (*4*)
val test19 = number_before_reaching_sum (7, ([1, 3, 4, 1, 3, 5])); (*2*)

(*Tests for #9 what_month function*)
val test20 = what_month(5);
val test21 = what_month(32);
val test22 = what_month (363);

(*Tests for #10 month_range function*)
val test23 = month_range(59, 89); (*[2,3,3,3,3,...]*)
val test24 = month_range(31, 32); (*[1,2]*)

(*Test for #11 oldest function*)
val test25 = oldest([(2020, 4, 21), (2020, 5, 6), (2020, 11, 4),(2020, 11, 19)]); (*(2020,4,21)*)

(*Tests for #12 *)
val test26 = cumulative_sum([17, 21, 5]); (*17,38,43*)
