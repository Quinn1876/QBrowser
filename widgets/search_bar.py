from tkinter import Button, Text, Frame, Widget, LEFT, RIGHT

class SearchBar(Frame):
  def __init__(self, master: Widget, searchCommand: callable, **kwargs):
    super().__init__(master, **kwargs)
    self.searchButton = Button(master=self, text="Search", command=searchCommand)
    self.searchTextInput = Text(master=self, height='1')

    self.searchButton.pack(side=RIGHT)
    self.searchTextInput.pack(side=LEFT, fill='x')
