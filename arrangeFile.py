# this script is to rearrange data files in 
# forrest dataset to allign with BIDS format
import os, json, fnmatch

# change to main directory
main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids'
os.chdir(main_directory)

# write dataset description in json
data = {}
data['Name'] = "A studyforrest extension, simultaneous fMRI and eye gaze recordings during prolonged natural stimulation,"
data['License'] = "https://www.nature.com/articles/sdata201692#abstract,"
data['BIDSVersion'] = "1.0.0"
data['ReferencesAndLinks'] = "http://dx.doi.org/10.1038/sdata.2016.92"
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
	# create new subfolder ses-movie/func, anat (TBD)
	os.chdir(main_directory+'/'+name+'/ses-movie')
	if not os.path.exists('func'):
		os.mkdir('func')
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

	# cd to previous level anat folder
	os.chdir(main_directory+'/'+name+'/anat')	
	for anat in os.listdir('.'):
		# check if exists T1w_defacemask file
		if fnmatch.fnmatch(anat, '*T1w_defacemask.*'):
			# if so, change name to T12-defacemask
			anat_name = name+'_T1w-defacemask.nii.gz'
			os.rename(anat, main_directory+'/'+name+'/anat/'+anat_name)
	# change name to ses-loc/movie (TBD)
	
	# cd to main directory
	# copy sub/anat to sub/ses-movie
	# move file sub/anat to sub/ses-loc
	# cd to sub/ses-movie
	# change name of all files to ses-movie