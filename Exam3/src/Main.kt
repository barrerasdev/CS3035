import kotlin.math.log2
import kotlin.math.floor

fun main() {
    val numbers = listOf(32, -5, 64, 0, 7, -10, 15, 1, -1, 100)
    val positiveNumbers = numbers.filter { it > 0 }
    val log2Values = positiveNumbers.map { log2(it.toFloat()) }
    val bitsNeeded = log2Values.map { floor(it).toInt() + 1 }

    println("Original numbers: $numbers")
    println("Positive numbers: $positiveNumbers")
    println("Log2 values: $log2Values")
    println("Bits needed: $bitsNeeded")
}
