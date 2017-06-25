import json


def extract():
	assigned_to_file_json_root_key = 'assigned_to'
	component_file_json_root_key = 'component'

	assigned_to_file = open('../Dataset/JSON/assigned_to.json')
	assigned_to = json.loads(assigned_to_file.read())[assigned_to_file_json_root_key]

	component_file = open('../Dataset/JSON/component.json')
	component = json.loads(component_file.read())[component_file_json_root_key]

	output_file = open("OutputFiles/toss_data", "a")
	for bug_id, assignments in assigned_to.items():
		assignments_len = len(assignments)
		components_len = len(component[bug_id])

		line = ""
		count = 0
		for i in range(0, assignments_len, 1):
			for j in range(0, components_len, 1):
				if assignments[i]["when"] == component[bug_id][j]["when"] and assignments[i]["what"] is not None and \
								component[bug_id][j]["what"] in (
						"UI", "Core", "Text", "Debug", "APT", "Doc"):

					if count != 0:
						line += " , "
					line += (assignments[i]["what"])
					count += 1
		if count >= 2:
			line += "\n"
			output_file.write(line.encode('utf-8'))

	assigned_to_file.close()
	component_file.close()
	output_file.close()
