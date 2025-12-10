def sanitize_ids(number_pair):
    """Parse a number range string into first and last integers."""
    first_number, last_number = tuple(number_pair.split("-"))
    return int(first_number), int(last_number)


# ============= PART 1 =============

def is_sequence_repeated_twice(n):
    """Check if a number is a sequence repeated exactly twice."""
    s = str(n)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half


def sum_invalid_ids_part1(first: int, last: int):
    """Sum all invalid IDs (sequences repeated exactly twice) in range."""
    numbers = range(first, last + 1)
    invalid_ids = filter(is_sequence_repeated_twice, numbers)
    return sum(invalid_ids)


# ============= PART 2 =============

def is_repeating_sequence(n):
    """Check if a number is a sequence repeated at least twice."""
    s = str(n)
    length = len(s)
    
    for seq_length in range(1, length // 2 + 1):
        if length % seq_length == 0:
            sequence = s[:seq_length]
            repetitions = length // seq_length
            
            if sequence * repetitions == s:
                return True
    
    return False


def sum_invalid_ids_part2(first: int, last: int):
    """Sum all invalid IDs (repeating sequences at least twice) in range."""
    numbers = range(first, last + 1)
    invalid_ids = filter(is_repeating_sequence, numbers)
    return sum(invalid_ids)


# ============= MAIN =============

def solve_part1(filename='input.txt'):
    """Solve part 1 of the puzzle."""
    with open(filename, 'r') as f:
        numbers_range = f.read().strip().split(",")
    
    total_sum = 0
    for number_pair in numbers_range:
        first, last = sanitize_ids(number_pair)
        range_sum = sum_invalid_ids_part1(first, last)
        total_sum += range_sum
    
    return total_sum


def solve_part2(filename='input.txt'):
    """Solve part 2 of the puzzle."""
    with open(filename, 'r') as f:
        numbers_range = f.read().strip().split(",")
    
    total_sum = 0
    for number_pair in numbers_range:
        first, last = sanitize_ids(number_pair)
        range_sum = sum_invalid_ids_part2(first, last)
        total_sum += range_sum
    
    return total_sum


def main():
    """Main function to solve both parts"""
    print("=" * 50)
    print("PART 1: Sequences repeated exactly twice")
    print("=" * 50)
    part1_result = solve_part1()
    print(f"Part 1 Answer: {part1_result}")
    
    print("\n" + "=" * 50)
    print("PART 2: Sequences repeated at least twice")
    print("=" * 50)
    part2_result = solve_part2()
    print(f"Part 2 Answer: {part2_result}")


if __name__ == '__main__':
    main()
