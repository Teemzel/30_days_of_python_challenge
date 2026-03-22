# Explain the difference between map, filter, and reduce.
Map () = # Transforms each item in a list to a new value, producing a new array with the same length.
# Example: [1, 2, 3] -> multiply by 2 -> [2, 4, 6].
Filter (Condition) = # Evaluates a condition for each element, creating a new array with only the elements that return true.
# Example: [1, 2, 3] -> keep > 1 -> [2, 3].
Reduce (Accumulator) = # Applies a function against an accumulator and each element to reduce it to a single value.

# Explain the difference between higher order function, closure and decorator
# ``` Higher-order function (HOF) is a general programming concept where a function takes one or more functions as arguments or returns a function as its result. Examples include map, filter, and reduce.
Closure is a specific technical mechanism where a nested function remembers and accesses variables from its enclosing scope, even after the outer function has finished executing.
Decorator is a design pattern (and specific Python syntax using @) that uses both HOFs and closures to wrap another function or class and modify its behavior without permanently changing its source code.#````