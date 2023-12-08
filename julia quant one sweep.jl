using FLoops
@floop for (x, y) in zip(1:3, 1:2:6)
a = x + y
b = x - y
@reduce(s += a, t += b) end
(s, t)
