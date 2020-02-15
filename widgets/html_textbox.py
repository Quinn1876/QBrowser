from tkinter import INSERT, LEFT, Text
from html_parser.html_parser import HtmlParser
from html_parser.tag import Tag


class HtmlText(Text):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.bind("<Key>", lambda e: "break")
    self.tag_config('p', justify=LEFT)

    self.tag_config("a", foreground="blue", underline=1)
    self.tag_bind("a", "<Enter>", self._enter)
    self.tag_bind("a", "<Leave>", self._leave)
    self.tag_bind("a", "<Button-1>", self._click)

  def insertHtml(self, html):
    parser = HtmlParser()
    parser.feed(html)

    htmlTag = parser.root
    if not htmlTag is None:
      bodyNode = next(filter(HtmlText.bodyFilter, htmlTag.data))
      if not bodyNode is None:
          self.writeTag(bodyNode)

  @staticmethod
  def bodyFilter(tag):
    if hasattr(tag, 'tag'):
      return tag.tag == 'body'
    return False

  def writeTag(self, parent: Tag) -> None:
    for data in parent.data:
      if type(data) is str:
        tag = parent.tag
        self.insert(INSERT, data, tag)
      elif type(data) is Tag:
        self.writeTag(data)

  def clear(self):
    self.replace('1.0', 'end', '')

  def _enter(self, event):
    """
    Determines what happens when the Mouse enters
    link area
    """
    self.config(cursor="hand2")

  def _leave(self, event):
    """
    Determines what happens when the mouse leaves link area
    """
    self.config(cursor="")

  def _click(self, event):
    """
    Determines what happens when the link is clicked
    """
    raise NotImplementedError

if __name__ == "__main__":
  from api_instance import ApiInstance
  text = HtmlText(master=None)
  ApiInstance.getExample1(text.insertHtml)
