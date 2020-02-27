class HtmlTagStack:
  """
  # HtmlTagStack
  """
  def __init__(self):
    self._stack = []

  def pop(self):
    return self._stack.pop()

  def push(self, item):
    self._stack.append(item)

  @property
  def top(self):
    return self._stack[len(self._stack) - 1]
