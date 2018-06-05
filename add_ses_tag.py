# add session tag in each file name from anat folder
import os, json, fnmatch, shutil

# change to main directory
main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids'
os.chdir(main_directory)
# get all subject folders in main directory
all_folder_names = os.listdir(main_directory)
# iterate through all subjects to arrange files
for name in all_folder_names:
	# enter current subject folder
	os.chdir(main_directory+'/'+name)
	# cd to sub/ses-movie/anat
	os.chdir(main_directory+'/'+name+'/ses-movie/anat')
	# change name of all files to ses-movie
	list_anat = os.listdir('.')
	for anat in list_anat:
		cur_name = anat
		new_name = cur_name.replace("T1w-defacemask", "ses-movie_T1w-defacemask")
		os.rename(anat, main_directory+'/'+name+'/ses-movie/anat/'+new_name)
	
	# cd to sub/ses-localizer/anat
	os.chdir(main_directory+'/'+name+'/ses-localizer/anat')
	list_anat = os.listdir('.')
	# change name of all files to ses-movie
	for anat in list_anat:
		cur_name = anat
		if not cur_name.contains("ses-localizer"):
			
			new_name = cur_name.replace("T1w-defacemask", "ses-localizer_T1w-defacemask")
			os.rename(anat, main_directory+'/'+name+'/ses-localizer/anat/'+new_name)