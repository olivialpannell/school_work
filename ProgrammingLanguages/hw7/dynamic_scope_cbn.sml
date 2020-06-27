(*  Concrete syntax
e :: x | n | true | false | succ | pred | iszero | if e then e else e
       | fn x => e | e e | (e) | let x = e in e

Abstract Syntax
datatype term = AST_ID of string 
  | AST_NUM of int 
  | AST_BOOL of bool
  | AST_SUCC 
  | AST_PRED 
  | AST_ISZERO 
  | AST_IF of (term * term * term)
  | AST_FUN of (string * term) 
  | AST_APP of (term * term)
  | AST_LET of (string * term * term)
  | AST_ERROR of string
*)

use "parser.sml";

datatype env = Env of (string -> term);
datatype result = 
  RES_ERROR of string 
  | RES_NUM of int
  | RES_BOOL  of bool
  | RES_SUCC 
  | RES_PRED 
  | RES_ISZERO 
  | RES_FUN of (string * term)
  | RES_CLOSURE of (envstat * (string * term)) and envstat = Env1 of (string -> (envstat * term))

exception UnboundID

fun emptyenvFun  (x : string) : term = raise UnboundID;
val emptyenv = Env emptyenvFun
fun update (Env e) (x : string) (ty : term) = fn y => if x = y then ty else e y

exception Not_implemented_yet
exception Error of string


fun interp (env, AST_ID i)          = let val Env e = env in interp(Env e, e i) end
  | interp (env, AST_NUM n)         = RES_NUM n
  | interp (env, AST_BOOL b)        = RES_BOOL b
  | interp (env, AST_FUN (i,e))     = RES_FUN (i,e)
  | interp (env, AST_APP (AST_APP (AST_ADD, e1), e2)) = 
        (case interp (env, e1) of
            RES_NUM n1 => (case interp (env, e2) of
                RES_NUM n2 => RES_NUM (n1+n2)
                    |  _         => raise (Error  "not a number"))
            |  _         => raise (Error "not a number")
        )
  | interp (env, AST_APP (AST_ADD, e1)) = raise (Error "not enough arguments for +")
  | interp (env, AST_APP (e1,e2))   = (case interp (env, e1) of
         RES_FUN (x, body) => interp (Env (update env x e2), body)
       | RES_SUCC =>  (case interp(env, e2) of
                  RES_NUM num => RES_NUM(num+1)
                  |_ => RES_ERROR "not a number in SUCC")
       | RES_PRED =>  let val v1 = interp(env, e2)
                in case v1 of
                  RES_NUM num => if num = 0 then RES_NUM(0) else RES_NUM(num - 1)
                  |_ => RES_ERROR "invalid number in PRED"
              end
       | RES_ISZERO => (case interp( env, e2) of
                    RES_NUM num => if num = 0 then RES_BOOL(true) else RES_BOOL(false)
                    | _ => RES_ERROR  "not a number ISZERO")
       | _ => RES_ERROR "can't apply non-function")
  | interp (env, AST_SUCC)          = RES_SUCC
  | interp (env, AST_PRED)          = RES_PRED
  | interp (env, AST_ISZERO)        = RES_ISZERO
  | interp (env, AST_IF (e1,e2,e3)) =  (case interp (env,e1) of
                                     RES_BOOL true  => interp (env,e2)
                                   | RES_BOOL false => interp (env,e3)
                                   | _              => raise Error  "case on non-bool")

  | interp (env, AST_LET (x,e1,e2)) = let val new_env = update env x e1
                          in interp(Env new_env, e2)
                        end
  | interp (env, AST_ERROR s)       = raise Error s

fun eval s = interp (emptyenv, parsestr s);


fun emptyenvFun2  (x : string) : (envstat * term) = raise UnboundID;
val emptyenv2 = Env1 emptyenvFun2
fun update2 (Env1 e) (x : string) (ty : (envstat * term)) = fn y => if x = y then ty else e y

fun find (Env1 f) i = f i

fun interp_static (envstat, AST_ID i) = interp_static(find envstat i)(*let val Env1 e = envstat in interp_static(Env1 e, e i) end*) 
  | interp_static (envstat, AST_NUM n) = RES_NUM n
  | interp_static(envstat, AST_BOOL b) = RES_BOOL b
  | interp_static (envstat, AST_FUN (i,e)) = RES_CLOSURE(envstat, (i,e))
  | interp_static (envstat, AST_APP (AST_APP (AST_ADD, e1), e2)) = 
        (case interp_static (envstat, e1) of
            RES_NUM n1 => (case interp_static (envstat, e2) of
                RES_NUM n2 => RES_NUM (n1+n2)
                    |  _         => raise Error  "not a number")
            |  _         => raise Error "not a number"
        )
  | interp_static (envstat, AST_APP (AST_ADD, e1)) = raise (Error "not enough arguments for +")
  | interp_static (envstat, AST_APP (e1,e2))   =  (case interp_static (envstat, e1) of
       (*  RES_FUN (v, body) => let val new_env = update2 envstat v (envstat, e2)
                                   in interp_static(Env1 new_env, body)
                                  end*)
       RES_SUCC => let val n = interp_static(envstat, e2)
                in case n of
                  RES_NUM(0) => RES_NUM(0)
                  | RES_NUM num => RES_NUM(num+1)
                  |_ => RES_ERROR "Not a number"
              end 
       | RES_PRED => let val v1 = interp_static(envstat, e2)
                in case v1 of
                  RES_NUM num => if num = 0 then RES_NUM(0) else RES_NUM(num - 1)
                  |_ => RES_ERROR "Invalid number"
              end
       | RES_ISZERO => let val v1 = interp_static( envstat, e2)
                  in case v1 of
                    RES_NUM num => if num = 0 then RES_BOOL(true) else RES_BOOL(false)
                    | _ => RES_ERROR "not a number"
                end
       | RES_CLOSURE(env1, (x, x2)) => let val new_env = update2 env1 x (envstat, e1) 
                              in interp_static(Env1 new_env, x2)
                          end
       |_ => RES_ERROR "Error with application." )
  | interp_static (envstat, AST_SUCC)          = RES_SUCC
  | interp_static (envstat, AST_PRED)          = RES_PRED
  | interp_static (envstat, AST_ISZERO)        = RES_ISZERO
  | interp_static (envstat, AST_IF (e1,e2,e3)) = (case interp_static (envstat,e1) of
            RES_BOOL true => interp_static (envstat,e2)
            | RES_BOOL false => interp_static (envstat,e3)
            | _              => RES_ERROR "if condition non-bool!")
  | interp_static (envstat, AST_LET (x,e1,e2)) = let val new_env = update2 envstat x (envstat, e1)
                          in interp_static(Env1 new_env, e2)
                        end
  | interp_static (envstat, AST_ERROR s)       = raise (Error s)

fun interp_s s = interp_static (emptyenv2, parsestr s)
                     handle (Error z) => RES_ERROR z ;

interp(emptyenv,parsestr ("(fn x => 34) (iszero true)"));
(*val it = RES_ERROR "some complaint about applying true to iszero..." : result*)

(*But in a call-by-name, or call-by-need interpreter:*)

interp_static(emptyenv2,parsestr ("(fn x => 34) (iszero true)"));
(*val it = RES_NUM 34 : result*)

(*************************  #4  **********************************)
(*Briefly discuss what you would change in your interpreters if the input 
  to the interpreter had been type- checked before its invocation.

  If the input to the interpreter was type checked before, I wouldn't 
  need the RES_ERROR in result or AST_ERROR in term because there in 
  theory there would be no errors thrown at this point so I would have
  to change my IF, and nearly all of APPs conditionals so that it only 
  pattern match for any the possible working cases instead of the 
  wildcard at the end.


*)
(******************************************************************)




