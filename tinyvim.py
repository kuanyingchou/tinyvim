class TextCpn:

  def __init__(self):
    self.content = [[]]
    self.showLineNumber = True
    self.cursor_x = 0
    self.cursor_y = 0
  
  def __str__(self):
    prefix = ''
    no = 1
    res = ''
    for line in self.content:
      if self.showLineNumber:
        res = res + str(no) + '. '
      for char in line:
         res = res + char
      res = res + '\n'
      no = no + 1
    return res;
  
  def insert(self, c):
    current_line = self.content[self.cursor_y]
    if c == '\n':
      self.content[self.cursor_y] = current_line[:self.cursor_x]
      self.content.insert(self.cursor_y + 1, current_line[self.cursor_x:])
      self.move_down()
    else:
      current_line.insert(self.cursor_x, c)
      self.move_right()
    
  #def new_line(self):
  #  self.content.append([''])
  
  def move_right(self):
    current_line = self.content[self.cursor_y]
    if self.cursor_x < len(current_line):
      self.cursor_x = self.cursor_x + 1

  def move_left(self):
    if self.cursor_x > 0:
      self.cursor_x = self.cursor_x - 1

  def move_down(self):
    self.cursor_y = self.cursor_y + 1
if __name__ == '__main__':
  txt = TextCpn()
  txt.insert('h')
  txt.insert('e')
  txt.insert('l')
  txt.insert('l')
  txt.insert('o')
  txt.insert('\n')
  txt.insert('b')
  txt.insert('y')
  txt.insert('e')
  print(txt)
