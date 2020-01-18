class TagQueue:
  def __init__(self):
    self._front = None
    self._back = None

  def push(self, tag):
    if self._back is None:
      self._front = TagNode(tag, self._back)
      self._back = self._front
    else:
      self._back.next = TagNode(tag, self._back)
      self._back = self._back.next

  def pop(self):
    if self._front is None:
      return None
    tag = self._front.tag
    temp = self._front
    self._front = self._front.next
    del temp
    return tag

  def isEmpty(self):
    return self._front is None


class TagNode:
  def __init__(self, value, next):
    self.next = next
    self.tag = value


