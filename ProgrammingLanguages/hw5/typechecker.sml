use "type.sml";

Control.Print.printDepth:= 100;

(* A term datatype with typed function arguments to allow type checking *)
datatype term
  = AST_ID of string
  | AST_NUM of int
  | AST_BOOL of bool
  | AST_FUN of (string * typ * term)
  | AST_SUCC
  | AST_PRED
  | AST_ISZERO
  | AST_IF of (term * term * term)
  | AST_APP of (term * term)
  | AST_LET of (string * term * term)

exception Unimplemented;
exception TypeError;

(* typeOf : env -> term -> typ *)
fun typeOf (Env env) (AST_ID s)          = env s
  | typeOf env (AST_NUM n)         = INT
  | typeOf env (AST_BOOL b)        = BOOL
  | typeOf env (AST_FUN (i,t,e))   = let val new_env = update env i t
                                        in let val v2 = typeOf (Env new_env) e
                                            in ARROW(t, v2)
                                          end
                                      end 
  | typeOf env AST_SUCC            = ARROW (INT, INT)
  | typeOf env AST_PRED            = ARROW (INT, INT)
  | typeOf env AST_ISZERO          = ARROW (INT,BOOL)
  | typeOf env (AST_IF (e1,e2,e3)) =
    let val t1 = typeOf env e1
        val t2 = typeOf env e2
        val t3 = typeOf env e3
    in
        case (t1 = BOOL) andalso (t2 = t3) of
            true => t3
          | false => raise TypeError
    end
  | typeOf env (AST_APP (e1,e2))   = 
    let val t1 = typeOf env e1
        val t2 = typeOf env e2
        in case t1 of 
          ARROW(v1,v2) => v2
          | _ => raise TypeError
    end
  | typeOf env (AST_LET (x,e1,e2)) = (*raise Unimplemented*)
    let val t1 = typeOf env e1
        in let val new_env = update env x t1
            in typeOf (Env new_env) e2
        end
      end

(*
Some sample functions translated into abstract syntax for you to test
your typechecker on:
*)

(*val fun1 = fn (f : a -> a) => fn (x : a) => f (f x);*)

val test1 = AST_FUN("f", ARROW(VAR "a", VAR "a"),
                AST_FUN("x", VAR "a",
                    AST_APP(AST_ID "f",
                        AST_APP(AST_ID "f", AST_ID "x"))));


(* val fun2 = fn (f : 'b -> 'c) => fn (g : 'a -> 'b) => fn (x : 'a) => f (g x); *)
val test2 = AST_FUN("f", ARROW(VAR "b", VAR "c"),
                AST_FUN("g", ARROW(VAR "a", VAR "b"),
                    AST_FUN("x", VAR "a",
                        AST_APP(AST_ID "f",
                            AST_APP(AST_ID "g", AST_ID "x")))));

(*val fun3 = fn (b : bool) => if b then 1 else 0 *)
val test3 = AST_FUN("b", BOOL,
                AST_IF(AST_ID "b", AST_NUM 1, AST_NUM 0));


(* feel free to write your own test expressions! *)
val res1 = typ2str( typeOf emptyenv test1);
val res2 = typ2str(typeOf emptyenv test2);
val res3 = typ2str(typeOf emptyenv test3);
