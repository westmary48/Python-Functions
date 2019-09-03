def print_lyrics():
  print("I'm a lumberjack and I'm okay")
  print("I sleep all night and I work all day")

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

repeat_lyrics()


# The rjust() method returns the right-justified string within the given minimum width .
# If fillchar is defined, it fills the remaining space with the defined character.
def right_just(s):
    print(s.rjust(70))

right_just('monty')

def do_twice(f):
  print((f))
  print((f))

def print_spam():
  print('spam')

do_twice('print_spam')
