import json

json_text=input("put some json text to validate...")

try:
	json_object=json.loads(json_text)
	print(json_object)
except ValueError :
	print("Not a valid json text")
	


