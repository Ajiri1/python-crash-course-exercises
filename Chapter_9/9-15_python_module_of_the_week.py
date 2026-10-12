"""Explore a standard-library module; this example uses statistics."""
import statistics

numbers = [12, 15, 15, 18, 20, 20, 20, 25]
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Mode:", statistics.mode(numbers))
