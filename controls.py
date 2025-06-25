import turtle

class Key():
  def __init__(self, key):
    # Default settings of a 'Key' object.
    self.key = key
    self.down = False

    # Sets an event listener to the binded key.
    turtle.onkeypress(self.press, key)
    turtle.onkeyrelease(self.release, key)
  
  # Changes the key's status to being currently pressed/held.
  def press(self):
    self.down = True
  
  # Changes the key's status to not being currently pressed/held.
  def release(self):
    self.down = False