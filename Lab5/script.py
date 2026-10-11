lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

print("\nCelsius to Fahrenheit Conversion Table:\n")
print(f"{'Celsius':>10} | {'Fahrenheit':>12}")
print("-" * 25)

for celsius in range(lower_bound, upper_bound + 1):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:>10} | {fahrenheit:>12.1f}")
