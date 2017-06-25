import json


def format_input():
	assigned_to_file_json_root_key = 'assigned_to'
	component_file_json_root_key = 'component'
	short_desc_file_json_root_key = 'short_desc'

	assigned_to_file = open('../Dataset/JSON/assigned_to.json')
	assigned_to = json.loads(assigned_to_file.read())[assigned_to_file_json_root_key]

	component_file = open('../Dataset/JSON/component.json')
	component = json.loads(component_file.read())[component_file_json_root_key]

	short_desc_file = open('../Dataset/JSON/short_desc.json')
	short_desc = json.loads(short_desc_file.read())[short_desc_file_json_root_key]

	output_file = open("OutputFiles/formatted_input", "a")
	count = 1

	for bug_id, assignments in assigned_to.items():
		assignments_len = len(assignments)
		components_len = len(component[bug_id])
		short_desc_len = len(short_desc[bug_id])
		for i in range(0, assignments_len, 1):
			for j in range(0, components_len, 1):
				for k in range(0, short_desc_len, 1):
					if assignments[i]["when"] == component[bug_id][j]["when"] == short_desc[bug_id][k]["when"] and \
									assignments[i]["what"] is not None and \
									component[bug_id][j]["what"] in ("UI", "Core", "Text", "Debug", "APT", 'Doc'):
						count += 1
						val = (short_desc[bug_id][k]["what"] + "  " + component[bug_id][j]["what"] + " , " + assignments[i]["what"] + "\n")
						output_file.write(val.encode('utf-8'))

	assigned_to_file.close()
	component_file.close()
	short_desc_file.close()
	output_file.close()
