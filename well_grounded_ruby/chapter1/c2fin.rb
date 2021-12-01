puts "Reading Celsius temperature value from data file..."
num = File.read("temp.dat")
celsius = num.to_i
fahrenehit = (celsius * 9 / 5) + 32
puts "The result is "
puts fahrenehit
puts "."
