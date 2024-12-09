def fibonacci_sequence(n_terms):
    """Print Fibonacci sequence up to n terms."""
    if n_terms <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize the first two terms
    n1, n2 = 0, 1
    count = 0

    print(f"Fibonacci sequence up to {n_terms} terms:")
    while count < n_terms:
        print(n1, end=" ")
        # Update values
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# Input the number of terms
try:
    terms = int(input("Enter the number of terms: "))
    fibonacci_sequence(terms)
except ValueError:
    print("Invalid input! Please enter an integer.")

input("")
