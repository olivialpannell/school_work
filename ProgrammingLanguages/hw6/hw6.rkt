#lang racket

; this is a comment

; 1
(define (sequence spacing low high)
  (if (<= low high)
      (cons low (sequence spacing (+ low spacing) high))
      null))

; 2
(define (list-nth-mod xs n)
  (cond [(negative? n)
         (error "list-nth-mod: negative number")]
        [(null? xs)
         (error "list-nth-mod: empty list")]
        [(positive? n)
         (car (list-tail xs (remainder n (length xs))))]
      ))


;;;;;;;;;;;; stream just for testing
(define ones (lambda () (cons 1 ones)))

;3
(define (stream-for-k-steps s k)
  (if (positive? k) ; checks for k < 0
      (cons (car (s)) (stream-for-k-steps (cdr (s)) (- k 1)))
      null))
      
;4
(define (funny-number-stream)
  (letrec ([help (lambda (n)
              (cond [(zero? (remainder n 6))
                     (cons (* -1 n) (lambda () (help (+ n 1))))] ;if multiple of 6 change it to negative
                    [#t (cons n (lambda () (help (+ n 1))))]))])
    (help 1))) 
                     
  
;5
(define (vector-assoc v vec)
  (letrec ([l (vector-length vec)]
           [help (lambda (x) (if (<= l x)
                                 #f
                                 (let ([w (vector-ref vec x)])
                                       (if (and (equal? v (car w)) (pair? w) ) ;pair? w
                                          w
                                          (help (+ x 1))))))])
    (help 0)))


;6
(define (caching-assoc xs n)
  (let* ([f (make-vector n (cons #f #f))]
         [i 0]
         [f2 (lambda (vec)
                      (if (vector-assoc vec f)
                          (vector-assoc vec f)
                            (if (assoc vec xs)
                                (begin
                                  (vector-set! f (remainder i n) (assoc vec xs)) (assoc vec xs))
                            #f)))])
  f2))

;7
(define-syntax while-greater
  (syntax-rules (do)
    [(while-greater e1 do e2)
     (letrec ([i e1]
              [help (lambda ()
                     (let ([x e2])
                       (if (<= x i)
                           #t
                           (begin (help)))))])
       (help))]))

;8
(define (TR e)
  (cond
    [(number? e) e] ;return itself
    [(equal? (car e) `+)  `(* ,(TR (cadr e)) ,(TR (caddr e)))]
    [(equal? (car e) `*)  `(+ ,(TR (cadr e)) ,(TR (caddr e)))]
    [#t  (error "Error: Not a valid E term")]))