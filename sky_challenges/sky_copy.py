def dir_name(dir):
  if dir == "^":
    return "up"
  elif dir == "v":
    return "down"
  elif dir == "<":
    return "left"
  elif dir == ">":
    return "right"

def solution(S):
  freq = {}
  for direction in S:
    # creating a frequency vector with the firections
    direction_name = dir_name(direction)
    freq.setdefault(direction_name, 0)
    freq[direction_name] += 1

  # finding the most frequent direction 
  max_freq = max(freq, key=freq.get)
  # and remove it from the frequency vector
  del freq[max_freq]

  # counting the arrows to rotate 
  counter = 0
  for direction, frequency in freq.items():
    counter += frequency

  return counter



print(solution('^vv<v'))