class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('локатор поиска', 'что-то передаю')

print(search.loc, search.text)

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

frame = Button('локатор рамки', 'какой-то текст')

print(frame.loc, frame.text)

class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

letter_1 = Title('локатор буквы', 'ещё текст')

print(letter_1.loc, letter_1.text)

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

line = Link('локатор линии', 'больше текста')

print(line.loc, line.text)