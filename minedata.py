import requests
from io import StringIO
from html.parser import HTMLParser
import re, datetime

contents = ""
response = requests.get('https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/response_conflict-reponse_conflits/crisis-crises/ukraine-fact-fait.aspx?lang=eng#dataset-filter')
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

with open("/Users/stefanbehfar/Downloads/data.txt", "w") as f:
    while "Posted" in contents[fromhere:]:
        pos1 = fromhere + contents[fromhere:].find("Posted")
        pos2 = pos1 + contents[pos1 + 1:].find("false claim:")
        pos3 = pos2 + contents[pos2 + 1:].find("Posted")
        if pos1==pos2:
            break
        area1 = contents[pos1+10:pos2-15]
        area1 = ''.join(i for i in area1 if i not in '"').replace('“',"").replace('”',"")
        day = re.search('\d{4}-\d{2}-\d{2}', area1)
        date = datetime.datetime.strptime(day.group(), '%Y-%m-%d').date()
        area2 = contents[pos2-14:pos3]
        area2 = ''.join(i for i in area2 if i not in '"').replace('“',"").replace('”',"")
        fromhere = pos3 + 1
        f.write("\n")
        f.write('{"prompt":'+f'"{strip_tags(area1)}"'+', "completion":'+'"the facts"'+'}')
        f.write("\n")
        f.write('{"prompt":'+f'"{str(date)+strip_tags(area2)}"'+', "completion":'+'"false claims"'+'}')