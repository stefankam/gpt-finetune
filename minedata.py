import requests
contents = ""
response = requests.get('https://www.international.gc.ca/world-monde/issues_development-enjeux_developpement/response_conflict-reponse_conflits/crisis-crises/ukraine-fact-fait.aspx?lang=eng#dataset-filter')
contents=response.text
fromhere=0
with open("/Users/stefankam/Downloads/data.txt", "w") as f:
    while "Posted" in contents[fromhere:]:
        pos1 = fromhere + contents[fromhere:].find("Posted")
        pos2 = pos1 + contents[pos1 + 1:].find("false claim:")
        pos3 = pos2 + contents[pos2 + 1:].find("Posted")
        if pos1==pos2:
            break
        area1 = contents[pos1:pos2-15]
        area2 = contents[pos2-14:pos3]
        fromhere = pos3 + 1
        f.write("\n")
        f.write('{"prompt":'+f'"{area1}"'+', "completion":'+f'"{area2}"'+'}')
