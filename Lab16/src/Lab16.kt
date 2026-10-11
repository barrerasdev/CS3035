fun add(a: Int, b: Int): Int = a + b
fun subtract(a: Int, b: Int): Int = a - b
fun multiply(a: Int, b: Int): Int = a * b

fun mathOperation(a: Int, b: Int, operation: (Int, Int) -> Int): Int {
    return operation(a, b)
}

fun mathOperation(operation: (Int, Int) -> Int): (Int, Int) -> Int {
    return operation
}

fun main() {
    println("\nFunction as Input")
    println("Add: " + mathOperation(5, 3, ::add))
    println("Subtract: " + mathOperation(5, 3, ::subtract))
    println("Multiply: " + mathOperation(5, 3, ::multiply))

    println("\nReturning a Function")
    val addFunction = mathOperation(::add)
    val resultAdd = addFunction(5, 3)
    println("Result of addFunction(5, 3): $resultAdd")
}