use "hw3.sml";

(* #1 *)
val test1 = only_lowercase([("Testing"), ("CAPITALS"), ("iN"), ("ThiS"), ("string")]) = ([("iN"), ("string")])

(* #2 *)
val test2 = longest_string1([("long"), ("longboy"), ("shorttt"), ("sho")]) = ("longboy");
val test3 = longest_string1([("long"), ("shorttt"), ("longboy"), ("sho")]) = ("shorttt");

(* #3 *)
val testt = longest_string2(["yes", "no"])= ("yes")
val test4 = longest_string2([("long"), ("longboy"), ("shorttt"), ("sho")]) = ("shorttt");
val test5 = longest_string2([("long"), ("shorttt"), ("longboy"), ("sho")]) = ("longboy");

(* #4 *)
val test6 = longest_string3([("long"), ("longboy"), ("shorttt"), ("sho")]) = ("longboy");
val test7 = longest_string3([("long"), ("shorttt"), ("longboy"), ("sho")]) = ("shorttt");
val test8 = longest_string4([("long"), ("longboy"), ("shorttt"), ("sho")]) = ("shorttt");
val test9 = longest_string4([("long"), ("shorttt"), ("longboy"), ("sho")]) = ("longboy");

(* #5 *)
val test10 = longest_lowercase([("Long"), ("Longboy"), ("Shorttt"), ("sho")]) = ("sho");
val test11 = longest_lowercase([("long"), ("shorttt"), ("longboy"), ("Sho")]) = ("shorttt");

(* #6 *)
val test12 = caps_no_X_string("lxOng") = ("LONG");
val test13 = caps_no_X_string("XXsXhoXrTtXtX") = ("SHORTTT");

(* #7 *)
val test14 = first_answer((fn(v) => SOME v), [1, 2, 3, 4]) = 1;

(* #8 *)
val test15 = all_answers((fn(v) => SOME [v]), [1, 2, 3, 4]);

(* #9b *)
val test16 = count_wildcards(TupleP [WildcardP, WildcardP]) = 2;
val test17 = count_wildcards(VariableP "a") = 0;

(* #9c *)
val test18 = count_wild_and_variable_lengths(VariableP "a") = 1;

(* #9d *)
val test19 = count_a_var("a", VariableP "b") = 0;
val test20 = count_a_var("a", VariableP "a") = 1;

(* #10 *)
val test21 = check_pat(TupleP [VariableP "b", VariableP "a"]) = true;
val test22 = check_pat(TupleP [VariableP "a", VariableP "a"]) = false;

(* #11 *)
val test23 = match(Constant 44, VariableP "a");
val test24 = match(Constant 4, TupleP [ConstantP 1]) = NONE;

(* #12 *)
first_match(Unit , [UnitP]) = SOME [];


(*
fun g f1 f2 p = case p of
      WildcardP         => f1 ()
    | VariableP x       => f2 x
    | ConstructorP(_,p) => (g f1 f2) p
    | TupleP ps         => List.foldl (fn (p,i) => ((g f1 f2) p) + i) 0 ps
    | _                 => 0
*)
