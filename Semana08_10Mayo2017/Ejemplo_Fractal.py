import turtle

def copoNieve(lado, n):
    if n == 0:
        turtle.forward(lado)
    else:
        lado = lado / 3
        copoNieve(lado, n-1)
        turtle.left(60)
        copoNieve(lado, n-1)
        turtle.right(120)
        copoNieve(lado, n-1)
        turtle.left(60)
        copoNieve(lado, n-1)

copoNieve(300, 5)
turtle.done()