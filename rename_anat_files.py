# rearrange name of data in anat directories,
# delete repeated task-name pattern, add missing pattern
import os
# change to main directory
main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids/'
#main_directory = '/Users/chloe/Documents/test10/'
os.chdir(main_directory)
# get all subject folders in main directory
all_folder_names = os.listdir(main_directory)
# iterate through all subjects to arrange files
for sub in all_folder_names:
	if sub == '.DS_Store' or sub == 'dataset_description.json' or sub == '.bidsignore' :
		continue
	os.chdir(main_directory+sub+'/ses-localizer/anat')
	list_of_anat = os.listdir('.')
	for anat_file in list_of_anat:
		if 'defacemask' in anat_file:
			os.rename(anat_file, main_directory+sub+'/ses-localizer/anat/'+sub+'_ses-localizer_mod-T1w_defacemask.nii.gz')
			print('RENAME SUCCESS: '+ anat_file)
	
	os.chdir(main_directory+sub+'/ses-movie/anat')
	list_of_anat2 = os.listdir('.')
	for anat_file2 in list_of_anat2:
		if 'defacemask' in anat_file2:
			print(anat_file2+' FOUND')
			os.rename(anat_file2, main_directory+sub+'/ses-movie/anat/'+sub+'_ses-movie_mod-T1w_defacemask.nii.gz')
			print('RENAME SUCCESS: ' + anat_file2)