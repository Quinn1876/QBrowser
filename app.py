from tkinter import (
  Button,
  END,
  Frame,
  INSERT,
  Text,
  Tk,
)

from api_instance import ApiInstance
from widgets.html_textbox import HtmlText


class Main(Tk):
  @classmethod
  def run(cls):
    main = cls()
    main.geometry("800x600")
    main.title("QBrowser")
    main.mainloop()

  def __init__(self):
    super().__init__()
    self.htmlDisplay = Frame(master=self)
    self.htmlText = HtmlText(master=self.htmlDisplay)
    self.searchButton = Button(master=self, text="Search", command=self.updateText)

    self.searchButton.pack()
    self.htmlDisplay.pack(fill='both', expand=True)
    self.htmlText.pack(fill='both', expand=True)


  def updateText(self):
    """
    # updateText
    clears the htmlText display and then gets the html from example1
    """
    self.htmlText.clear()
    ApiInstance.getExample1(lambda text: self.htmlText.insertHtml(text))

  def search(self):
    print(ApiInstance.postSearch('www.google.com'))

Main.run()
