from tkinter import Label as tkLabel
from tkinter import StringVar

class Label(tkLabel):
  def __init__(self, master, text='', **kwargs):
    self._text = StringVar()
    self.updateText(text)
    super().__init__(master=master, textvariable=self._text, **kwargs)

  def updateText(self, newText):
    self._text.set(newText)
