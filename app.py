from tkinter import (
  Button,
  END,
  Frame,
  INSERT,
  Text,
  Tk,
)

from label import Label
from api_instance import ApiInstance

import time

class Main(Tk):
  @classmethod
  def run(cls):
    main = cls()
    main.geometry("800x600")
    main.title("Py Browser")
    main.mainloop()

  def __init__(self):
    super().__init__()
    self.htmlDisplay = Frame(master=self)
    self.htmlLabel = Label(master=self.htmlDisplay, text="Hello World", background="#FFFFFF")
    self.htmlText = Text(master=self.htmlDisplay)
    self.searchButton = Button(master=self, text="Search", command=self.updateText)

    self.searchButton.pack()
    self.htmlDisplay.pack(fill='both', expand=True)
    # self.htmlLabel.pack(fill='both', expand=True)
    self.htmlText.pack(fill='both', expand=True)


  def updateLabel(self):
    ApiInstance.getHome(self.htmlLabel.updateText)

  def updateText(self):
    ApiInstance.getHome(lambda text: self.htmlText.replace('1.0', END, text))

  def search(self):
    print(ApiInstance.postSearch('www.google.com'))

Main.run()
