from html.parser import HTMLParser as ParentParser
from html_parser.tag_stack import HtmlTagStack as Stack
from html_parser.tag import Tag

VALID_TAGS = {
  'body',
  'head',
  'html',
  'p',
  'a'
}

class HtmlParser(ParentParser):
  """
  # HtmlParser

  Currently implimented using a parser base class from html.parser
  TODO: Write my own implementation that does not depend on this base class
  """
  parseStack = Stack() # Parser Input
  root = None

  def handle_starttag(self, tag, attrs):
    if tag in VALID_TAGS:
      self.parseStack.push(Tag(tag, attrs))
    else:
      raise HtmlParserError('Invalid tag detected')

  def handle_endtag(self, tag):
    if tag == 'html':
      self.root = self.parseStack.top
    elif self.parseStack.top == tag:
      tag = self.parseStack.pop()
      self.parseStack.top.appendData(tag)
    else:
     raise HtmlParserError('Invalid html')

  def handle_data(self, data):
    self.parseStack.top.appendData(data.lstrip().lstrip('\t'))

class HtmlParserError(Exception):
  pass
