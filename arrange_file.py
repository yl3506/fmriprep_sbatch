# this script is to rearrange data files in 
# forrest dataset to allign with BIDS format
import os, json, fnmatch, shutil

# change to main directory
main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids'
os.chdir(main_directory)

# write dataset description in json
data = {}
data['Name'] = "A studyforrest extension, simultaneous fMRI and eye gaze recordings during prolonged natural stimulation,"
data['License'] = "https://www.nature.com/articles/sdata201692#abstract,"
data['BIDSVersion'] = "1.0.0"
data['ReferencesAndLinks'] = []
data['ReferencesAndLinks'].append("http://dx.doi.org/10.1038/sdata.2016.92")
with open('dataset_description.json', 'w') as out_file:
	json.dump(data, out_file)

# get all subject folders in main directory
all_folder_names = os.listdir(main_directory)
# iterate through all subjects to arrange files
for name in all_folder_names:
	if name == '.DS_Store' or name == 'dataset_description.json':
		continue
	# enter current subject folder
	os.chdir(main_directory+'/'+name)
	# create new folders ses-localizer and ses-movie
	if not os.path.exists('ses-localizer'):
		os.mkdir('ses-localizer')
	if not os.path.exists('ses-movie'):
		os.mkdir('ses-movie')
	# create new subfolder ses-localizer/func, anat (TBD)
	os.chdir('ses-localizer')
	if not os.path.exists('func'):
		os.mkdir('func')
	if not os.path.exists('anat'):
		os.mkdir('anat')
	# create new subfolder ses-movie/func, anat (TBD)
	os.chdir(main_directory+'/'+name+'/ses-movie')
	if not os.path.exists('func'):
		os.mkdir('func')
	if not os.path.exists('anat'):
		os.mkdir('anat')
	if os.path.exists(main_directory+'/'+name+'/func'):
		# enter sub/func folder
		os.chdir(main_directory+'/'+name+'/func')
		# iterate through all files in func 
		all_func = os.listdir('.')
		for func in all_func:
			# move correspond files to ses-loc/func
			if fnmatch.fnmatch(func, '*ses-localizer*.*.*') or fnmatch.fnmatch(func, '*ses-localizer*.*'):
				os.rename(func, main_directory+'/'+name+'/ses-localizer/func/'+func)
			# move correspond files to ses-movie/func
			if fnmatch.fnmatch(func, '*ses-movie*.*.*') or fnmatch.fnmatch(func, '*ses-movie*.*'):
				os.rename(func, main_directory+'/'+name+'/ses-movie/func/'+func)
	# finish sub/func, delete the func folder
	os.chdir(main_directory+'/'+name)
	if os.path.exists('func'):
		# if func folder is empty, delete
		if os.listdir('func') == []:
			os.rmdir('func')

	# cd to previous level anat folder
	if os.path.exists(main_directory+'/'+name+'/anat'):
		os.chdir(main_directory+'/'+name+'/anat')	
		for anat in os.listdir('.'):
			# check if exists T1w_defacemask file
			if fnmatch.fnmatch(anat, '*T1w_defacemask.*'):
				# if so, change name to T12-defacemask
				anat_name = name+'_T1w-defacemask.nii.gz'
				os.rename(anat, main_directory+'/'+name+'/anat/'+anat_name)
		# cd to sub
		os.chdir(main_directory+'/'+name)
		# copy sub/anat to sub/ses-movie/anat and sub/ses-loc/anat
		for anat in os.listdir('anat'):
			shutil.copyfile('anat/'+anat, main_directory+'/'+name+'/ses-localizer/anat/'+anat)
			os.rename('anat/'+anat, main_directory+'/'+name+'/ses-movie/anat/'+anat)
		# delete sub/anat file if empty
		if os.path.exists('anat'):
			if os.listdir('anat') == []:
				os.rmdir('anat')

	# cd to sub/ses-movie/anat
	os.chdir(main_directory+'/'+name+'/ses-movie/anat')
	# change name of all files to ses-movie
	list_anat = os.listdir('.')
	for anat in list_anat:
		cur_name = anat
		new_name = cur_name.replace("T1w-defacemask", "ses-movie_T1w-defacemask")
		new_name = cur_name.replace("T1w.", "ses-movie_T1w.")
		os.rename(anat, main_directory+'/'+name+'/ses-movie/anat/'+new_name)
	# cd to sub/ses-localizer/anat
	os.chdir(main_directory+'/'+name+'/ses-localizer/anat')
	# change name of all files to ses-movie
	for anat in list_anat:
		cur_name = anat
		new_name = cur_name.replace("T1w-defacemask", "ses-localizer_T1w-defacemask")
		new_name = cur_name.replace("T1w.", "ses-localizer_T1w.")
		os.rename(anat, main_directory+'/'+name+'/ses-localizer/anat/'+new_name)
	