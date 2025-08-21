from infix_to_postfix import infix_to_postfix

expressions = [
    "5 + ( 6 - 2 ) * 9",
    "( 1 + 2 ) * ( 3 + 4 )",
    "( 1 + 2 ) * 3"
]

for expr in expressions:
    postfix = infix_to_postfix(expr)
    print(f"Infix: {expr}")
    print(f"Postfix: {postfix}\n")
