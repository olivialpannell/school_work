(* CSE 341, HW2 Provided Code *)

(* main datatype definition we will use throughout the assignment *)
datatype json =
         Num of real (* real is what SML calls floating point numbers *)
       | String of string
       | False
       | True
       | Null
       | Array of json list
       | Object of (string * json) list

(* some examples of values of type json *)
val json_pi    = Num 3.14159
val json_hello = String "hello"
val json_false = False
val json_array = Array [Num 1.0, String "world", Null]
val json_obj   = Object [("foo", json_pi), ("bar", json_array), ("ok", True)]

(* some provided one-liners that use the standard library and/or some features
   we have not learned yet. (Only) the challenge problem will need more
   standard-library functions. *)

(* dedup : string list -> string list -- it removes duplicates *)
fun dedup xs = ListMergeSort.uniqueSort String.compare xs

(* strcmp : string * string -> order compares strings alphabetically
   where datatype order = LESS | EQUAL | GREATER *)
val strcmp = String.compare                                        
                        
(* convert an int to a real *)
val int_to_real = Real.fromInt

(* absolute value of a real *)
val real_abs = Real.abs

(* convert a real to a string *)
val real_to_string = Real.toString

(* return true if a real is negative : real -> bool *)
val real_is_negative = Real.signBit

(* We now load 3 files with police data represented as values of type json.
   Each file binds one variable: small_incident_reports (10 reports), 
   medium_incident_reports (100 reports), and large_incident_reports 
   (1000 reports) respectively.

   However, the large file is commented out for now because it will take 
   about 15 seconds to load, which is too long while you are debugging
   earlier problems.  In string format, we have ~10000 records -- if you
   do the challenge problem, you will be able to read in all 10000 quickly --
   it's the "trick" of giving you large SML values that is slow.
*)

(* Make SML print a little less while we load a bunch of data. *)
       ; (* this semicolon is important -- it ends the previous binding *)
Control.Print.printDepth := 3;
Control.Print.printLength := 3;

use "parsed_small_police.sml";
(*use "parsed_medium_police.sml";*)

(* uncomment when you are ready to do the problems needing the large report*)
use "parsed_large_police.sml"; 

val large_incident_reports_list =
    case large_incident_reports of
        Array js => js
      | _ => raise (Fail "expected large_incident_reports to be an array")


(* Now make SML print more again so that we can see what we're working with. *)
; Control.Print.printDepth := 20;
Control.Print.printLength := 20;

(**** PUT PROBLEMS 1-8 HERE ****)


(*Write a function make_silly_json that takes an int i and returns a json. The result should represent a JSON array of JSON objects where every object in the array has two fields, "n" and "b". Every object’s "b" field should hold true (i.e., True). The first object in the array should have a "n" field holding the JSON number i.0, the next object should have an "n" field holding ((i − 1).0 and so on where the last object in the array has an "n" field holding 1.0.*)
fun make_silly_json (i: int)=
    let
	fun help(i :int)=
	    if i = 0 then []
	    else
		Object[("n", Num (int_to_real(i))), ("b", True)] :: help(i-1)
     in
	Array(help(i))
     end

(*Write a function assoc of type ’’a * (’’a * ’b) list -> ’b option that takes two arguments k
and xs. It should return SOME v1 if (k1,v1) is the pair in the list closest to the beginning of the list
for which k and k1 are equal.*)

fun assoc (k, xs) = case xs of
    [] => NONE
    | (k1, v1) :: xs' => if (k1 = k)
      	       	      	 then SOME v1
      	       	      	 else
				assoc(k, xs')

(* Write a function dot that takes a json (call it j) and a string (call it f) and returns a json option.
If j is an object that has a field named f, then return SOME v where v is the contents of that field. If j is not an object or does not contain a field f, then return NONE.*)
fun dot (j: json, f: string) = case j of
    Object(v) => assoc(f, v)
    |  _ => NONE

(* Write a function one_fields that takes a json and returns a string list. If the argument is an
object, then return a list holding all of its field names (not field contents). Else return the empty list. Use a tail-recursive, locally defined helper function. It is easiest to have the result have the strings in reverse order from how they appear in the object and this reverse order is fine/expected.*)
fun one_fields(j: json) = case j of
    Object(v) => let
			fun help(v,strs)= case v of
			    [] => strs
			    | (str, _) :: v1 => help(v1, str::strs)
		in
			help(v, [])
		end
    | _ => []

(* Write a function no_repeats that takes a string list and returns a bool that is true if and only
if no string appears more than once in the input.*)
fun no_repeats(str: string list)=
    if length(str) = length(dedup(str))
    then true
    else false

(* Write a function recursive_no_field_repeats that takes a json and returns a bool that is true
if and only if no object anywhere “inside” (arbitrarily nested) the json argument has repeated field
2 names. (Notice the proper answer for a json value like False is true. Also note that it is not relevant
that different objects may have field names in common.) In addition to using some of your previous
functions, you will want two locally defined helper functions for processing the elements of a JSON
array and the contents of a JSON object’s fields. By defining these helper functions locally, they can
call recursive_no_field_repeats in addition to calling themselves recursively. Sample solution is 16
lines.*)
fun recursive_no_field_repeats (j : json)= case j of
    Array arr => let
			fun arrhelp(js, a) = case a of
			    [] => true
			    | js :: a' => recursive_no_field_repeats (js) andalso arrhelp(js, a')
		in
			arrhelp(j, arr)
		end
    |Object ob => let
			fun obhelp(js, os) = case os of
			    []=> true
			    | (_, js):: os'=> recursive_no_field_repeats(js) andalso obhelp(js, os') 
    	       	  in
			no_repeats(one_fields(Object ob)) andalso obhelp(j, ob)
		  end
     | _ => true

(* Write a function count_occurrences of type string list * exn -> (string * int) list. If the
string list argument is sorted (in terms of the ordering implied by the strcmp function we provided
you), then the function should return a list where each string is paired with the number of times it
occurs. (The order in the output list does not matter.) If the list is not sorted, then raise the exn
argument. Your implementation should make a single pass over the string list argument, primarily
using a tail-recursive helper function. You will want the helper function to take a few arguments,
including the “current” string and its “current” count.*)

val rc = 1; (*used to reset count*)
fun count_occurrences(strs: string list, e: exn) = case strs of
    [] => []
    | currentstr :: strs' =>
      		let
		    fun help(strs, cstr, count, accum, ef) = case strs of
	    	    	[] => ((cstr, count) :: accum)
	    	    	| newstr :: strs' => if newstr = cstr then help(strs',cstr,count + 1, accum, ef)
			  	    	     else if
					     	  strcmp(newstr, cstr) = ef
				             orelse
						ef = strcmp("", "")
					     then
						help(strs', newstr, rc, ((cstr, count) :: accum), strcmp(newstr, cstr))
					     else
						raise e
		in
			help(strs', currentstr, rc, [], strcmp("","")) (*using example null strcmp that is true to compare*)
		end

(* Write a function string_values_for_field of type string * (json list) -> string list (the
parentheses in this type are optional, so the REPL won’t print them). For any object in the json list
that has a field equal to the string and has contents that are a JSON string (e.g., String "hi") put
the contents string (e.g., "hi") in the output list (order does not matter; the output should have
duplicates when appropriate). Assume no single object has repeated field names. Sample solution is 6
lines thanks to dot. *)
fun string_values_for_field(str: string, jsl: json list)= case jsl of
    [] => []
    | j::jsl' => let
			fun help(str, jsl, jop: json option) = case jop of
			    SOME (String(s)) => s :: string_values_for_field(str,jsl')
			    | _=>string_values_for_field(str,jsl')
		in
			help(str, jsl, dot(j, str))
		end
    
(* histogram and historgram_for_field are provided, but they use your 
   count_occurrences and string_values_for_field, so uncomment them 
   after doing earlier problems *)

(* histogram_for_field takes a field name f and a list of objects js and 
   returns counts for how often a string is the contents of f in js. *)

exception SortIsBroken

fun histogram (xs : string list) : (string * int) list =
  let
    fun compare_strings (s1 : string, s2 : string) : bool = s1 > s2

    val sorted_xs = ListMergeSort.sort compare_strings xs
    val counts = count_occurrences (sorted_xs,SortIsBroken)

    fun compare_counts ((s1 : string, n1 : int), (s2 : string, n2 : int)) : bool =
      n1 < n2 orelse (n1 = n2 andalso s1 < s2)
  in
    ListMergeSort.sort compare_counts counts
  end

fun histogram_for_field (f,js) =
  histogram (string_values_for_field (f, js))


(**** PUT PROBLEMS 9-11 HERE ****)

(*Write a function filter_field_value of type string * string * json list -> json list. The
output should be a subset of the third argument, containing exactly those elements of the input list
that have a field with name equal to the first string argument and that field’s contents are a JSON
string equal to the second string argument. Sample solution uses dot and is less than 10 lines*)
fun filter_field_value(str1: string, str2: string, jsl: json list)= case jsl of
    [] => []
    | j::jsl' => let
			fun help(str1, str2, jsl, j, jop) = case jop of
			    SOME (String(s)) => if strcmp(s, str2) = EQUAL
			    	 	     	then (j :: filter_field_value(str1, str2, jsl'))
						else
							filter_field_value(str1, str2, jsl')
			    | _=>filter_field_value(str1, str2, jsl')
		in
			help(str1, str2, jsl, j, dot(j, str1))
		end
		
(*Bind to the variable large_event_clearance_description_histogram a histogram (using
histogram_for_field) of the objects in large_incident_reports_list based on the
"event_clearance_description" field.*)
val large_event_clearance_description_histogram = histogram_for_field("event_clearance_description", large_incident_reports_list);

(*Bind to the variable large_hundred_block_location_histogram a histogram (using
histogram_for_field) of the objects in large_incident_reports_list based on the
"hundred_block_location" field.*)
val large_hundred_block_location_histogram = histogram_for_field("hundred_block_location", large_incident_reports_list);


;Control.Print.printDepth := 3;
Control.Print.printLength := 3;

(**** PUT PROBLEMS 12-15 HERE ****)
(*Bind to the variable forty_third_and_the_ave_reports a json list containing the elements of
large_incident_reports_list whose "hundred_block_location" field contains the JSON string
"43XX BLOCK OF UNIVERSITY WAY NE".*)
val forty_third_and_the_ave_reports = filter_field_value("hundred_block_location", "43XX BLOCK OF UNIVERSITY WAY NE", large_incident_reports_list);


(*13. Bind to the variable forty_third_and_the_ave_event_clearance_description_histogram a histogram based on the "event_clearance_description" field (like in problem 10), but considering only
the objects whose "hundred_block_location" field contains "43XX BLOCK OF UNIVERSITY WAY NE"
(as in problem 12).*)
val forty_third_and_the_ave_event_clearance_description_histogram = histogram_for_field("event_clearance_description", forty_third_and_the_ave_reports);


(*14. Bind to the variable nineteenth_and_forty_fifth_reports a json list containing the elements
of large_incident_reports_list whose "hundred_block_location" field contains the JSON string
"45XX BLOCK OF 19TH AVE NE".*)
val nineteenth_and_forty_fifth_reports = filter_field_value("hundred_block_location", "45XX BLOCK OF 19TH AVE NE", large_incident_reports_list); 

(*15. Bind to the variable nineteenth_and_forty_fifth_event_clearance_description_histogram a
histogram based on the "event_clearance_description" field (like in problem 10), but considering
only the objects whose "hundred_block_location" field contains "45XX BLOCK OF 19TH AVE NE" (as
in problem 14).*)
val nineteenth_and_forty_fifth_event_clearance_description_histogram= histogram_for_field("event_clearance_description", nineteenth_and_forty_fifth_reports);

;Control.Print.printDepth := 20;
Control.Print.printLength := 20;

(**** PUT PROBLEMS 16-19 HERE ****)
(*16. Write a function concat_with that takes a separator string and a list of strings, and returns the string
that consists of all the strings in the list concatenated together, separated by the separator. The
separator should be only between elements, not at the beginning or end. Use ML’s ^ operator for
concatenation (e.g., "hello" ^ "world" evaluates to "helloworld"). Sample solution is 5 lines.*)
fun concat_with(sep: string, strs: string list)= case strs of 
    [] => ""
    |str::[] => str
    |str1::(str2:: strs')=> str1 ^ sep ^ concat_with(sep, str2 :: strs')
    

(*17. Write a function quote_string that takes a string and returns a string that is the same except
there is an additional " character at the beginning and end. Sample solution is 1 line.*)
fun quote_string(str: string) =
    concat_with(str, ["\"", "\""])

(*18. Write a function real_to_string_for_json that takes a real and returns a string. You can’t quite
just use the real_to_string function we provided because in ML negative numbers start with ~, but
we want the more common - character. But we also provided real_abs. Sample solution is 1–2 lines.*)

fun real_to_string_for_json(rl)=
    if real_is_negative(rl)
    then "-" ^ real_to_string(real_abs(rl))
    else real_to_string(rl)


(*19. Write a function json_to_string that converts a json into the proper string encoding in terms of the
syntax described on the first page of this assignment. The three previous problems are all helpful, but
you will also want local helper functions for processing arrays and objects (hint: in both cases, create
a string list that you then pass to concat_with). Sample solution is 25 lines.*)

fun json_to_string(js: json) = case js of
	Num rl => real_to_string_for_json(rl)
	| String str => "\"" ^ str ^ "\""
	| False => "false"
	| True => "true"
	| Null => "null"
	| Array arr => let
				fun arrhelp(a) = case a of
			    	    [] => []
			    	    |t::a' => json_to_string(t)::arrhelp(a')
			in 
				 "[" ^ concat_with(", ", arrhelp arr) ^ "]" 
			end
	| Object ob => let
			fun obhelp(ob) = case ob of
			    []=>[]
			    | (str, js)::ob' =>("\"" ^ str ^ "\"" ^ " : " ^ json_to_string(js)) :: obhelp(ob')
			in
			    "{" ^ concat_with(", ", obhelp(ob)) ^"}"
			end
