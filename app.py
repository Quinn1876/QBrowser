from tkinter import (
  Button,
  END,
  Frame,
  INSERT,
  Menu,
  Text,
  Tk
)

from api_instance import ApiInstance
from widgets.html_textbox import HtmlText
from widgets.search_bar import SearchBar

def donothing():
  pass

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
    self.searchBar = SearchBar(master=self, searchCommand=self.updateTextWithExample1)

    self._createMenuBar()

    self.searchBar.pack()
    self.htmlDisplay.pack(fill='both', expand=True)
    self.htmlText.pack(fill='both', expand=True)

  def updateText(self, htmlText: str) -> None:
    self.htmlText.clear()
    self.htmlText.insertHtml(htmlText)

  def updateTextWithExample1(self) -> None:
    """
    # updateTextWithExample1()
    clears the htmlText display and then gets the html from example1
    """
    self.htmlText.clear()
    ApiInstance.getExample1(lambda text: self.htmlText.insertHtml(text))

  def search(self, searchQuery: str) -> None:
    # TODO: Do more than just print the query result.
    print(ApiInstance.postSearch(searchQuery))

  def searchGoogle(self) -> None:
    print(ApiInstance.postSearch('www.google.com'))

  def _createMenuBar(self) -> None:
    """
    # _createMenuBar

    creates the menubar for the aplication
    """
    menuBar = Menu(self)
    filemenu = Menu(menuBar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    menuBar.add_cascade(label="File", menu=filemenu)
    self.configure(menu=menuBar)

Main.run()
