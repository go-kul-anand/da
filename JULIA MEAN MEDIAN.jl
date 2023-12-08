using Statistics v = [1 2; 3 4]
println(mean!([1., 1.], v)) 
println(mean(1:20)) 
println(mean([1, missing, 3]))
println(median([1, 2, 3, 4]))
println(median(skipmissing([1, 2, missing, 4]))) 
println(middle(1:10))
