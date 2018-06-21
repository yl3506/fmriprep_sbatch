import os

main_directory = '/mindhive/saxelab3/anzellotti/forrest/forrest_bids/'
all_objects = ['face', 'scene', 'body', 'house', 'object', 'scramble']
# cd into subject file iteratively
os.chdir(main_directory)
for subject in ['sub-18']:
	os.chdir(main_directory + subject)
# create object_events/ directory for saving output data
	if not os.path.exists(main_directory+subject+'/object_events'):
		os.makedirs('object_events')
# cd into ses-localizer/func directory
	os.chdir('ses-localizer/func/')
# iterate through all files and read in file that contains "events"
	run_count = 0
	for file in os.listdir('.'):
		if 'events' in file:
			run_count += 1
			f = open(file, 'r')
			all_lines = f.readlines()
			last_line = all_lines[-1]
			for object_num in range(1, 7): # 6 objects in total
				cur_obj = all_objects[object_num - 1]
				out_file = open(main_directory+subject+'/object_events/run_'+str(run_count)+'_'+all_objects[object_num-1]+'.txt', 'w+')
				out_file = open(main_directory+subject+'/object_events/run_'+str(run_count)+'_'+all_objects[object_num-1]+'.txt', 'a')
				# initialize parameters
				prev_onset = 0
				onset = 0
				prev_dur = 0
				dur = 0
				flag = 0
				for line in all_lines: # read in each line
					if 'onset' in line.split('\t')[0]:
						continue # skip first line
					words = line.split('\t')
					onset = float(words[0])
					dur = float(words[1])
					flag = words[2]
					if cur_obj in flag:
						flag = 1
					else:
						flag = 0
					if flag == 1:
						out_file.write(str(prev_onset+prev_dur) + '    ' + str(onset-prev_onset-prev_dur) + '    0\n')
						prev_onset = onset
						prev_dur = dur
						out_file.write(str(onset)+'    '+str(dur)+'    '+str(flag)+'\n')
					elif line is last_line:
						out_file.write(str(prev_onset+prev_dur)+'    '+str(onset-prev_onset-prev_dur+dur)+'    '+str(flag)+'\n')