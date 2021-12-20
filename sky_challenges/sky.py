
# Use verbal naming for directions

up = '^'
down = 'v'
left = '<'
right = '>'

def dir_name(dir):
  if dir == "^":
    return up
  elif dir == "v":
    return down
  elif dir == "<":
    return left
  elif dir == ">":
    return right

def rotation_count(main_direction, dir_to_count):
  # if main_direction == dir_to_count:
  if main_direction == up:
    if dir_to_count == down:
      return 2
    elif dir_to_count == left or dir_to_count == right:
      return 1

  elif main_direction == down:
    if dir_to_count == up:
      return 2
    elif dir_to_count == left or dir_to_count == right:
      return 1

  elif main_direction == left:
    if dir_to_count == right:
      return 2
    elif dir_to_count == up or dir_to_count == down:
      return 1
  
  elif main_direction == right:
    if dir_to_count == left:
      return 2
    elif dir_to_count == up or dir_to_count == down:
      return 1


def solution(S):
  freq = {}
  for direction in S:
    direction_name = dir_name(direction)
    freq.setdefault(direction_name, 0)
    freq[direction_name] += 1

  # find most frequent direction 
  max_freq = dir_name(max(freq, key=freq.get))
  # and remove it from the frequency vector
  del freq[max_freq]
  print(freq)

  counter = 0
  for direction, frequency in freq.items():
    print(direction,frequency, rotation_count(max_freq, direction))
    counter += ( rotation_count(max_freq, direction) * frequency)

  return counter



print(solution('^vv<v'))