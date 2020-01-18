from tkinter import LEFT, Text
from html_parser.html_parser import HtmlParser

class HtmlText(Text):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)

    self.tag_config('p', justify=LEFT)

  def insertHtml(self, html):
    parser = HtmlParser()
    parser.feed(html)

    htmlTag = parser.root
    if not htmlTag is None:
      bodyNode = filter(HtmlText.bodyFilter, htmlTag.data)
      if not bodyNode is None:
        for node in bodyNode:
          print(str(node))

  @staticmethod
  def bodyFilter(tag):
    if hasattr(tag, 'tag'):
      return tag.tag == 'body'
    return False

if __name__ == "__main__":
  from api_instance import ApiInstance
  text = HtmlText(master=None)
  ApiInstance.getExample1(text.insertHtml)
