(define (over-or-under num1 num2) 'YOUR-CODE-HERE)

; ;; Tests
(expect (over-or-under 1 2) -1)

(expect (over-or-under 2 1) 1)

(expect (over-or-under 1 1) 0)

(expect (over-or-under -10 10) -1)

(expect (over-or-under 5 4) 1)

(define (sum-of-squares x y) 'YOUR-CODE-HERE)

; ;; Tests
(expect (sum-of-squares 3 4) 25)

(expect (sum-of-squares -1 0) 1)

(expect (sum-of-squares 1 -100) 10001)

(define (make-adder num) 'YOUR-CODE-HERE)

; ;; Tests
(define adder (make-adder 5))

(expect (adder 8) 13)

(define (composed f g) 'YOUR-CODE-HERE)

(define lst 'YOUR-CODE-HERE)

(define (remove item lst) 'YOUR-CODE-HERE)

; ;; Tests
(expect (remove 3 nil) ())

(expect (remove 3 '(1 3 5)) (1 5))

(expect (remove 5 '(5 3 5 5 1 4 5 4)) (3 1 4 4))
