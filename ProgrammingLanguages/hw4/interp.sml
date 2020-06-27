(*  Concrete syntax 
e :: x | n | true | false | succ | pred | iszero | if e then e else e 
       | fn x => e | e e | (e) | let x = e in e 

Ambiguous
 - How do you parse e f g  === (e f) g (x) 
 - How do you parse fn f = f 0  ===  fn f = (f 0) 

Abstract syntax tree :
datatype term = AST_ID of string 
	| AST_NUM of int 
	| AST_BOOL of bool
  	| AST_SUCC 
  	| AST_PRED 
  	| AST_ISZERO 
  	| AST_ADD 
  	| AST_IF of (term * term * term)
  	| AST_FUN of (string * term) 
  	| AST_APP of (term * term) 
  	| AST_LET of (string * term * term) 
  	| AST_ERROR of string
*)

use "parser.sml";

datatype result = RES_ERROR of string 
	| RES_NUM of int
	| RES_BOOL  of bool
    | RES_SUCC 
    | RES_PRED 
    | RES_ISZERO 
    | RES_FUN of (string * term)
    | RES_CLOSURE of (env * (string * term)) and env = Env of (string -> result);


(*  An environment is a function string -> result  *)

exception UnboundID
exception Error of string

(*datatype env = Env of (string -> result)*)

fun emptyenvFun  (x : string) : result = raise UnboundID;
val emptyenv = Env emptyenvFun

(*  update : env -> string -> result -> string -> result  *)
fun update (Env e) (x : string) (ty : result) = fn y => if x = y then ty else e y

fun interp (env, AST_ID i) = let val Env e = env in e i end 
  | interp (env, AST_NUM n) = RES_NUM n
  | interp(env, AST_BOOL b) = RES_BOOL b
  | interp (env, AST_FUN (i,e)) = RES_FUN (i,e)
  | interp (env, AST_APP (AST_APP (AST_ADD, e1), e2)) = 
        (case interp (env, e1) of
            RES_NUM n1 => (case interp (env, e2) of
                RES_NUM n2 => RES_NUM (n1+n2)
                    |  _         => raise (Error  "not a number"))
            |  _         => raise (Error "not a number")
        )
  | interp (env, AST_APP (AST_ADD, e1)) = raise (Error "not enough arguments for +")
  | interp (env, AST_APP (e1,e2))   =  (case interp (env, e1) of
         RES_FUN (v, body) => let val v2 = interp (env,e2)
                               in let val new_env = update env v v2
                                   in interp (Env new_env, body)
                                   end
                              end  
       | RES_SUCC => let val n = interp(env, e2)
       					in case n of
       						RES_NUM num => RES_NUM(num+1)
       						|_ => raise (Error "not a number")
       				end 
       | RES_PRED => let val v1 = interp(env, e2)
       					in case v1 of
       						RES_NUM num => if num = 0 then RES_NUM(0) else RES_NUM(num - 1)
       						|_ => raise (Error "invalid number")
       				end
       | RES_ISZERO => let val v1 = interp( env, e2)
       						in case v1 of
       							RES_NUM num => if num = 0 then RES_BOOL(true) else RES_BOOL(false)
       							| _ => raise (Error "not a number")
       					end
       |_ => raise (Error "Error with function.") )
  | interp (env, AST_SUCC)          = RES_SUCC
  | interp (env, AST_PRED)          = RES_PRED
  | interp (env, AST_ISZERO)        = RES_ISZERO
  | interp (env, AST_IF (e1,e2,e3)) = (case interp (env,e1) of
            RES_BOOL true => interp (env,e2)
            | RES_BOOL false => interp (env,e3)
            | _              => raise (Error "if condition non-bool!") )
  | interp (env, AST_LET (x,e1,e2)) = let val v1 = interp(env, e1)
  										in let val new_env = update env x v1
  												in interp(Env new_env, e2)
  											end
  										end
  | interp (env, AST_ERROR s)       = raise (Error s)

fun interp_dynamic s = interp (emptyenv, parsestr s)
                     handle (Error z) => RES_ERROR z ;














fun interp_static (env, AST_ID i) = let val Env e = env in e i end 
  | interp_static (env, AST_NUM n) = RES_NUM n
  | interp_static(env, AST_BOOL b) = RES_BOOL b
  | interp_static (env, AST_FUN (i,e)) = RES_CLOSURE(env, (i,e))
  | interp_static (env, AST_APP (AST_APP (AST_ADD, e1), e2)) = 
        (case interp_static (env, e1) of
            RES_NUM n1 => (case interp_static (env, e2) of
                RES_NUM n2 => RES_NUM (n1+n2)
                    |  _         => raise (Error  "not a number"))
            |  _         => raise (Error "not a number")
        )
  | interp_static (env, AST_APP (AST_ADD, e1)) = raise (Error "not enough arguments for +")
  | interp_static (env, AST_APP (e1,e2))   =  (case interp_static (env, e1) of
         RES_FUN (v, body) => let val v2 = interp_static (env,e2)
                               in let val new_env = update env v v2
                                   in interp_static(Env new_env, body)
                                   end
                              end  
       | RES_SUCC => let val n = interp_static(env, e2)
       					in case n of
       						RES_NUM num => RES_NUM(num+1)
       						|_ => raise (Error "not a number")
       				end 
       | RES_PRED => let val v1 = interp_static(env, e2)
       					in case v1 of
       						RES_NUM num => if num = 0 then RES_NUM(0) else RES_NUM(num - 1)
       						|_ => raise (Error "invalid number")
       				end
       | RES_ISZERO => let val v1 = interp_static( env, e2)
       						in case v1 of
       							RES_NUM num => if num = 0 then RES_BOOL(true) else RES_BOOL(false)
       							| _ => raise (Error "not a number")
       					end
       | RES_CLOSURE(env1, (x, x2)) => let val v1 = interp_static(env, e2)
		       								in let val new_env = update env1 x v1 
		       								  	in interp_static(Env new_env, x2)
		       								end
		       							end
       |_ => raise (Error "Error with application.") )
  | interp_static (env, AST_SUCC)          = RES_SUCC
  | interp_static (env, AST_PRED)          = RES_PRED
  | interp_static (env, AST_ISZERO)        = RES_ISZERO
  | interp_static (env, AST_IF (e1,e2,e3)) = (case interp_static (env,e1) of
            RES_BOOL true => interp_static (env,e2)
            | RES_BOOL false => interp_static (env,e3)
            | _              => raise (Error "if condition non-bool!") )
  | interp_static (env, AST_LET (x,e1,e2)) = let val v1 = interp_static(env, e1)
  										in let val new_env = update env x v1
  												in interp_static(Env new_env, e2)
  											end
  										end
  | interp_static (env, AST_ERROR s)       = raise (Error s)

fun interp_s s = interp_static (emptyenv, parsestr s)
                     handle (Error z) => RES_ERROR z ;

parsestr "succ(pred 5)";
parsestr "if 7 then true else 5";
parsestr "fn a => f a a";

