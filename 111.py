__author__ = 'админ'
from drawman import *
2 from time import sleep
3

4

5 def f(x):
6     return x*x
7

8 print(drawman_scale)
9 drawman_scale(100)
10 x = -5.0
11 to_point(x, f(x))
12 pen_down()
13 while x <= 5:
14     to_point(x, f(x))
15     x += 0.1
16 pen_up()
17

18 sleep(10)

