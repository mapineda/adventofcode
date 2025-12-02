def crack_safe_part1(rotations):
  """
    Calculate how many times the dial points to 0 after rotations.
    
    Args:
        rotations: List of rotation strings (e.g., ['L68', 'R48'])
    
    Returns:
        Number of times the dial points to 0
  """
  position = 50
  zero_count = 0

  for rotation in rotations:
    direction = rotation[0] # L or R
    distance = int(rotation[1:]) # grab numbers after L or R prefix, cast as int

    if direction == "L":
      position = (position - distance) % 100

    else: # direction is R
      position = (position + distance) % 100

    if position == 0:
      zero_count += 1
  
  return zero_count

def crack_safe_part2(rotations):
  """
    Calculate how many times the dial points to 0 including during rotations.
    
    Args:
        rotations: List of rotation strings (e.g., ['L68', 'R48'])
    
    Returns:
        Number of times the dial points to 0 (including during rotation)
  """
  position = 50
  zero_count = 0

  for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
          
    for _ in range(distance):
      if direction == 'L':
        position = (position - 1) % 100
      else:  # direction == 'R'
        position = (position + 1) % 100
        
      if position == 0:
          zero_count += 1
      
  return zero_count


def main():
  """Main function to solve the puzzle"""
  with open('input.txt', 'r') as f:
      rotations = f.read().strip().split("\n")
  
  password = crack_safe_part1(rotations)
  print(f"The password is: {password}")

  second_password = crack_safe_part2(rotations)
  print(f"The second password is: {second_password}")


if __name__ == '__main__':
  main()
