# add RepetitionTime and TaskName in the json file in each subject session
# and change old RepetitionTime to RepetitionTime_2
import os, json, fnmatch
# change to main directory
main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids/'
#main_directory = '/Users/chloe/Documents/test11/'
os.chdir(main_directory)
# get all subject folders in main directory
all_folder_names = os.listdir(main_directory)
# iterate through all subjects to arrange files
for sub in all_folder_names:
	# ignore files with certain names
	if sub == '.DS_Store' or sub == 'dataset_description.json' or sub == '.bidsignore' :
		continue
	# cd to ses-localizer/func
	os.chdir(main_directory+sub+'/ses-localizer/func/')
	# iterate through all files in func and find json files
	all_func_files = os.listdir('.')
	for func_file in all_func_files:
		if fnmatch.fnmatch(func_file, '*.json'):
			# if find json file, open and modify
			with open(main_directory+sub+'/ses-localizer/func/'+func_file) as json_file:
				print(func_file)
				json_string = json_file.read()
				json_string = json_string.replace('"RepetitionTime":', '"RepetitionTime_2":')		
				print("replaced repetitiontime2")
				data = json.loads(json_string)
				#print(json_string)
				#print(type(json_string))
				old_repetition_time = data['global']['const']['RepetitionTime_2']
				new_repetition_time = old_repetition_time / 1000
				data['RepetitionTime'] = round(new_repetition_time, 3)
				if 'movielocalizer' in func_file:
					data['TaskName'] = "task-movielocalizer"
				elif 'objectcategories' in func_file:
					data['TaskName'] = "task-objectcategories"
				elif 'retmapccw' in func_file:
					data['TaskName'] = "task-retmapccw"
				elif 'retmapclw' in func_file:
					data['TaskName'] = "task-retmapclw"
				elif 'retmapexpcon' in func_file:
					data['TaskName'] = "task-retmapexpcon"
				elif 'retmapexp' in func_file:
					data['TaskName'] = "task-retmapexp"
			with open(func_file, 'w') as f:
				f.write(json.dumps(data, indent=4))

	# cd to ses-movie/func
	os.chdir(main_directory+sub+'/ses-movie/func/')
	# iterate through all files in func and find json files
	all_func_files2 = os.listdir('.')
	for func_file2 in all_func_files2:
		if fnmatch.fnmatch(func_file2, '*.json'):
			# if find json file, open and modify
			with open(main_directory+sub+'/ses-movie/func/'+func_file2) as json_file2:
				print(func_file2)
				json_string2 = json_file2.read()	
				print("movie read")	
				json_string2 = json_string2.replace('"RepetitionTime":', '"RepetitionTime_2":')
				print("movie replaced")
				data2 = json.loads(json_string2)

				old_repetition_time2 = data2['global']['const']['RepetitionTime_2']
				new_repetition_time2 = old_repetition_time2 / 1000
				data2['RepetitionTime'] = round(new_repetition_time2, 3)
				if 'task-movie' in func_file2:
					data2['TaskName'] = "task-movie"
			with open(func_file2, 'w') as f2:
				f2.write(json.dumps(data2, indent=4))