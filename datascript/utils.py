import json

def save_json(data, target, prettify=True):
	indent = 4 if prettify else None
	with open(target, "w", encoding="utf-8") as targetfile:
		json.dump(data, targetfile, ensure_ascii=False, indent=indent)

def load_json(source):
	with open(source, "r", encoding="utf-8") as sourcefile:
		data = json.load(sourcefile)
	return data 