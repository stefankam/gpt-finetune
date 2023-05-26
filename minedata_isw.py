import requests
from io import StringIO
from html.parser import HTMLParser
from datetime import datetime

contents = ""
response = requests.get('https://www.understandingwar.org/backgrounder/ukraine-conflict-updates')
contents=response.text
fromhere=0

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


with open("/Users/stefanbehfar/Downloads/data_isw.txt", "w") as f:
    while "Key Takeaways" in contents[fromhere:]:
        pos0 = fromhere + contents[fromhere:].find("Russian Offensive Campaign Assessment")
        pos1 = fromhere + contents[fromhere:].find("Key Takeaways")
        pos2 = pos1 + contents[pos1 + 1:].find("Russian Offensive")
        if pos1>=pos2:
            break
        area0 = contents[pos0:pos0+56]
        #fmt = "%B %d, %Y"
        #day = datetime.strptime(strip_tags(area0[-20:]), fmt)
        area = contents[pos1:pos2]
        area1=''.join(i for i in area if i not in '"').replace('“',"").replace('”',"")
        area1=str.join(" ", area1.splitlines())
        fromhere = pos2 + 1
        f.write("\n")
        f.write('{"prompt":'+f' "{strip_tags(area0)+strip_tags(area1)}"'+', "completion":'+'"the facts"'+'}')