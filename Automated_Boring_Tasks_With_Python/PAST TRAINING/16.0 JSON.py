import json

# Starting with JSON loads() fun

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue

# Starting wit JSON dumps() fun

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData