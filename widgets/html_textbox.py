from tkinter import INSERT, LEFT, Text
from html_parser.html_parser import HtmlParser
from html_parser.tag import Tag


class HtmlText(Text):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.bind("<Key>", lambda e: "break")
    self.tag_config('p', justify=LEFT)

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

  def writeTag(self, parent):
    for data in parent.data:
      if type(data) is str:
        tag = parent.tag
        self.insert(INSERT, data, tag)
      elif type(data) is Tag:
        self.writeTag(data)

  def clear(self):
    self.replace('1.0', 'end', '')

if __name__ == "__main__":
  from api_instance import ApiInstance
  text = HtmlText(master=None)
  ApiInstance.getExample1(text.insertHtml)
