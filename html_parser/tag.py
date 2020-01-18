class Tag:
  def __init__(self, tag, attrs):
    self.__tag = tag
    self.__attrs = attrs
    self.__data = []

  def __eq__(self, other):
    return other == self.__tag

  def __str__(self):
    return f"""
    tag: {self.__tag}
    attrs: {self.__attrs}
    data: {self.__data}
    """

  @property
  def tag(self):
    return self.__tag

  @property
  def attrs(self):
    return self.__attrs

  @property
  def data(self):
    return self.__data

  def appendData(self, data):
    self.__data.append(data)
