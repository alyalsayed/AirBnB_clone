def calculate_sum(numbers):
    # Calculate the sum of a list of numbers.
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    # Main function to test `calculate_sum`.
    nums = [1, 2, 3, 4, 5]
    print(f"The sum of {nums} is {calculate_sum(nums)}.")

if __name__ == "__main__":
    main()
