class Restangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        print(self.x * self.y)

    def perimeter(self):
        print(2 * (self.x + self.y))

quadr1 = Restangle(5, 5)

quadr2 = Restangle(2, 4)

quadr1.square()
quadr1.perimeter()
quadr2.square()
quadr2.perimeter()


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

random = Math(3, 4)

random.addition()
random.multiplication()
random.division()
random.subtraction()

print('\n')

class Button:

    def __init__(self, text, locator='', type='кнопка'):
        self.text = text
        self.type = type
        self.locator = locator

    def click(self):
       return "Клик по кнопке" + "{" + self.text + "}"

text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio button')
web_tables = Button('Web tables')
buttons = Button('Buttons')
links = Button('Links')
br_links_im = Button('Broken links - Images')
up_and_down = Button('Upload and download')
dyn_prop = Button('Dynamic Properties')

print(text_box.text)
print(text_box.click())

print('\n')

print(check_box.text)
print(check_box.click())

print('\n')

print(radio_button.text)
print(radio_button.click())

print('\n')

print(web_tables.text)
print(web_tables.click())

print('\n')

print(buttons.text)
print(buttons.click())

print('\n')

print(links.text)
print(links.click())

print('\n')

print(br_links_im.text)
print(br_links_im.click())

print('\n')

print(up_and_down.text)
print(up_and_down.click())

print('\n')

print(dyn_prop.text)
print(dyn_prop.click())

print('\n')