import random


def generate_random_numbers(n, output_file):
    with open(output_file, "w") as file:
        for _ in range(n):
            file.write(f"{random.randint(1, 100)}\n")


# Example usage
n = 10  # Replace with desired number of random numbers
num = int(input("N: "))
generate_random_numbers(num, "output.txt")
