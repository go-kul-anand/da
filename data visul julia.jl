import Pkg 
Pkg.add("Plots") 
using Plots
# 10 points of random data, in two columns 
x = 1:10;
y = rand(10, 2);
plot(x, y, title = "Two Lines", label = ["Line 1" "Line 2"], marker = ([:hex :d], 8), lw
= 3)
xlabel!("My x label")
