import Pkg 
Pkg.add("Optim")
using Optim
f(x) = (1.0 - x[1])^2 + 100.0 * (x[2] - x[1]^2)^2 
x_iv = [0.0, 0.0]
results = optimize(f, x_iv)
println("Results before changing the algorithm: ",results) 
results = optimize(f, x_iv, LBFGS())
println("Results after changing the algorithm: ",results)
