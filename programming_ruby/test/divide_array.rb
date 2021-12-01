a = [3, 2, 1]

last_part = a.dup
first_part = Array.new(0)

while element = last_part.shift
  first_part.push(element)

  break if first_part.inject(:+) == last_part.inject(:+)
end

p first_part
p last_part
