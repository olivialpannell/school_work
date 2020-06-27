(* Dan Grossman, CSE341, HW3 Provided Code *)

exception NoAnswer

datatype pattern = WildcardP
                 | VariableP of string
                 | UnitP
                 | ConstantP of int
                 | ConstructorP of string * pattern
                 | TupleP of pattern list

datatype valu = Constant of int
              | Unit
              | Constructor of string * valu
              | Tuple of valu list

fun g f1 f2 p =
    let
        val r = g f1 f2
    in
        case p of
            WildcardP         => f1 ()
          | VariableP x       => f2 x
          | ConstructorP(_,p) => r p
          | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
          | _                 => 0
    end

(**** you can put all your code here ****)
(* #1 takes a string list and returns a string list that has only the strings in the argument that start with an lowercase letter. Assume all strings have at least 1 character. Use List.filter, Char.isLower, and String.sub *)
val only_lowercase=
    List.filter(fn s => Char.isLower(String.sub(s, 0)));


(*#2 takes a string list and returns the longest string in the list. If the list is empty, return "". In the case of a tie, return the string closest to the beginning of the list.*)
val longest_string1=
    foldl(fn(str1, str2)=> if (String.size(str1)) <= (String.size(str2)) then str2 else str1) "";


(*#3 exactly like longest_string1 except in the case of ties
it returns the string closest to the end of the list.*)
val longest_string2 =
    foldl( fn(str1, str2) => if (String.size (str1)) < (String.size (str2)) then str2 else str1) "";

(*#4 longest_string3 has the same behavior as longest_string1 and longest_string4 has the
same behavior as longest_string2. longest_string_helper will look a lot like longest_string1 and longest_string2
but is more general because it takes a function as an argument. If longest_string_helper is passed a function
that behaves like > (so it returns true exactly when its first argument is stricly greater than its second),
then the function returned has the same behavior as longest_string1.*)
fun longest_string_helper(sign) =
    foldl( fn(str1, str2)=> if sign(String.size(str2), String.size(str1)) then str1 else str2) "";

val longest_string3 = longest_string_helper(fn (str1, str2) => str2 > str1);

val longest_string4 = longest_string_helper(fn (str1, str2) => str1 <= str2);


(*#5 takes a string list and returns the longest string in the
list that begins with an lowercase letter, or "" if there are no such strings. Assume all strings have at
least 1 character.*)
val longest_lowercase = longest_string1 o only_lowercase;

(*#6 takes a string and returns the string that is like the
input except every letter is capitalized and every “x” or “X” is removed (e.g., “aBxXXxDdx” becomes
“ABDD”).*)
val caps_no_X_string = String.implode
    		     o List.filter(fn(str) => Char.toString(str) <> "x")
		     o List.filter(fn(str) => Char.toString(str) <> "X")
		     o List.map(fn(str) => Char.toUpper(str))
		     o String.explode;

(*#7  The first argument should be applied to elements of the second argument in order until the first time it returns SOME v
for some v and then v is the result of the call to first_answer. If the first argument returns NONE for all list elements,
then first_answer should raise the exception NoAnswer.*)
fun first_answer (x, ls) = case ls of
    [] => raise NoAnswer
    | s ::ls' => case x s of
      	  	      NONE => first_answer(x, ls')
		      | SOME v => v

(*#8 first argument should be applied to elements of the second
argument. If it returns NONE for any element, then the result for all_answers is NONE. Else the
calls to the first argument will have produced SOME lst1, SOME lst2, ... SOME lstn and the result of
all_answers is SOME lst where lst is lst1, lst2, ..., lstn appended together.*)
fun all_answers (x, ls) =
    let
	fun help(accum, lst)= case lst of
	    [] => SOME accum
	    | s :: ls' => case x s of
	      	       	       NONE => NONE
			       | SOME v => help((accum @ v), ls')
     in
	help([], ls)
     end


(*#9a The arguments are curried arguments, function 1 with an empty list of bindings, function 2 which holds one element (string), and a pattern of the given datatype pattern.
The function g basically computes which pattern is given because it returns something specific to that type such as a WildcardP returns () and VariableP returns an x.
*)

(*#9b takes a pattern and returns how many WildcardP patterns it contains. *)
val count_wildcards = g (fn() => 1) (fn(str) => 0)

(*#9c returns the number of Wildcard patterns it contains plus the sum of the string lengths of all the
variables in the variable patterns it contains. *)
val count_wild_and_variable_lengths= g(fn() =>1) (fn(str)=>String.size(str))

(*#9d Use g to define a function count_a_var that takes a string and a pattern (as a pair) and returns
the number of times the string appears as a variable in the pattern. *)
fun count_a_var(s, pat)=
    g(fn()=> 0) (fn(str) => if str = s then 1 else 0)pat

(*#10 Write a function check_pat that takes a pattern and returns true if and only if all the variables
appearing in the pattern are distinct from each other (i.e., use different strings). The constructor
names are not relevant.*)
fun check_pat(p) =
    let
	fun help1(pat) = case pat of
	    VariableP v => [v]
	    | TupleP tp => foldl(fn(pat, accum) => (help1(pat) @ accum))[]tp
	    | _ => []
	fun help2(sl) = case sl of
	    [] => false
	    | str :: sl' => if List.exists(fn (s) => s = str) sl' then true else help2(sl')
    in
	not(help2(help1(p)))
    end


(*#11 Write a function match that takes a valu * pattern and returns a (string * valu) list option,
namely NONE if the pattern does not match and SOME lst where lst is the list of bindings if it does.
Note that if the value matches but the pattern has no patterns of the form VariableP s, then the
result is SOME [].*)
fun match(v, pat) = case (v, pat) of
   (_,  WildcardP) => SOME []
   | (_, VariableP s) => SOME [(v, s)]
   | (Unit, UnitP) => SOME []
   | (Constant cv, ConstantP cp) => if (cv = cp) then SOME [] else NONE
   | (Constructor(str1, v1), ConstructorP(str2, p)) => if str1 = str2 then match (v, pat) else NONE
   | (Tuple t1, TupleP t2) => if List.length(t2) = List.length(t1) then all_answers(match, (ListPair.zip(t1, t2))) else NONE
   | _ => NONE


(*#12  Write a function first_match that takes a value and a list of patterns and returns a
(string * valu) list option, namely NONE if no pattern in the list matches or SOME lst where
lst is the list of bindings for the first pattern in the list that matches. Use first_answer and a handle-expression. *)

fun first_match (v, pl) =
    SOME(first_answer(fn(pat) => match(v, pat),  pl)) handle NoAnswer => NONE;
