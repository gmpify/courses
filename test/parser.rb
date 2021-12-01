require 'minitest/autorun'

class BookTest < Minitest::Test
  def test_to_s
    isbn = '123'
    title = 'xyz'
    author = 'abc'
    year = 2000
    assert_equal("ISBN: #{isbn}\tTitle: #{title}", Book.new(isbn, title, author, year).to_s)
  end
end

class Book
  attr_reader :isbn, :title, :author, :year
  def initialize(isbn, title, author, year)
    @isbn = isbn
    @title = title
    @author = author
    @year = year
  end

  def to_s
    "ISBN: #{@isbn}\tTitle: #{@title}"
  end
end

books = []
File.open('ids.txt', 'r').each do |line|
  data = line.split(';').map{|elem| elem.strip }
  books << Book.new(data[0], data[1], data[2], data[3])
end
