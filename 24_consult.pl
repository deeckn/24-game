/* RPN = Reverse Polish notation */

% Define a list of valid operators
operator(add).
operator(sub).
operator(mul).
operator(div).

% Perform the specified operation on the given operands and return the result in the fourth argument
doop(add, A, B, C) :- C = A + B.
doop(sub, A, B, C) :- C = A - B.
doop(mul, A, B, C) :- C = A * B.
doop(div, A, B, C) :- B1 is B, B1 \= 0, C = A / B.

% Convert an RPN expression (given as a list of integers and operators)
% into an infix expression
% Stack: list of operands
% Prog: list of integers and operators
% Result: the result of the RPN expression
% Expr: the resulting infix expression

% Base case: if the stack has a single element, it is the result of the RPN expression
rpn2exp([X], [], X).

% If the current element is an integer, push it onto the stack
rpn2exp(Stack, [Head|Tail], Res) :-
	integer(Head),
	rpn2exp([Head|Stack], Tail, Res).

% If the current element is an operator, pop the top two elements from the stack
% perform the operation, and push the result back onto the stack
rpn2exp([X,Y|Others], [Head|Tail], Res) :-
	operator(Head),
	doop(Head, Y, X, X1),
	rpn2exp([X1|Others], Tail, Res).


% Evaluate an RPN expression by first converting it to an infix expression and then evaluating the infix expression
eval_rpn(Prog, Res) :- rpn2exp([], Prog, Exp), Res is Exp.

% Generate all possible combinations of the given list of integers and check if any of them can be evaluated to 24
try_prog([A, B, C, D], [A, B, X, C, Y, D, Z], N) :- eval_rpn([A, B, X, C, Y, D, Z], N).
try_prog([A, B, C, D], [A, B, X, C, D, Y, Z], N) :- eval_rpn([A, B, X, C, D, Y, Z], N).
try_prog([A, B, C, D], [A, B, C, X, D, Y, Z], N) :- eval_rpn([A, B, C, X, D, Y, Z], N).
try_prog([A, B, C, D], [A, B, C, X, Y, D, Z], N) :- eval_rpn([A, B, C, X, Y, D, Z], N).
try_prog([A, B, C, D], [A, B, C, D, X, Y, Z], N) :- eval_rpn([A, B, C, D, X, Y, Z], N).
solve24order(Numbers, Prog) :- try_prog(Numbers, Prog, 24).
solve24order(Numbers, Prog) :- try_prog(Numbers, Prog, 24.0).
solve24(Numbers, Prog) :- setof(T, lists:perm(Numbers, T), Bag), lists:member(T1, Bag), solve24order(T1, Prog), rpn2exp([], Prog, E), write(E), nl, fail.

% If the given list of integer can be evaluated to 24 return true
is_input_valid(Prog) :- eval_rpn(Prog, 24).
