import requests
contents = ""
response = requests.get('https://www.understandingwar.org/backgrounder/ukraine-conflict-updates')
contents=response.text
fromhere=0
with open("/Users/stefankam/Downloads/data_isw.txt", "w") as f:
    while "Key Takeaways" in contents[fromhere:]:
        pos1 = fromhere + contents[fromhere:].find("Key Takeaways")
        pos2 = pos1 + contents[pos1 + 1:].find("Russian Offensive")
        if pos1>=pos2:
            break
        area = contents[pos1:pos2]
        area1=''.join(i for i in area if i not in '"').replace('“',"").replace('”',"")
        area1=str.join(" ", area1.splitlines())
        fromhere = pos2 + 1
        f.write("\n")
        f.write('{"prompt":'+f'"{area1}"'+', "completion":'+'""'+'}')
