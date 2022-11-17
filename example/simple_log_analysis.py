'''
Simple ulog analysis script to show how pyulog can be used to analyze .ulg files.

This script will :
- Read and process the sample.ulg file and list first 10 names of logged topics
- 
'''
from pyulog import ULog

ulog_fname = 'Example_SITL.ulg'
ulog = ULog(ulog_fname)

# Fetch the data_list, which contains all the messages in the ulog
data_list = ulog.data_list

# Go through the data_list, each with specific message grouped together
print('<<Logged topic namest>>')
topics_counter = 0
for data_chunk in data_list:
    print(topics_counter, 'th topic :', data_chunk.name)
    topics_counter += 1
    if (topics_counter >= 10):
        print('... And so on..')
        break

