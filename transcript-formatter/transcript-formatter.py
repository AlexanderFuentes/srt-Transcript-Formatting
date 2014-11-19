#to do: combine duplicate timestamp items
#import regular expressions
import re

#define variables
time_code =''
time_text_list= []

#read and sort the old_file
with open("text.txt") as old_file:
        for line in old_file:
                #define items to find and use regular expression for recognition of time and numbers
                stripped_line = line.strip()
                find_time =re.match(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9]', stripped_line)
                find_number = re.match(r'[0-9]', stripped_line)
                
                if find_time:
                    time_code = stripped_line
                elif not find_time and not find_number:
                    text_addition = stripped_line
                    time_text_list_item = [[time_code, text_addition]]
                    time_text_list.extend(time_text_list_item)
#loop to remove empty lines
for item in time_text_list:
    for subitem in item:
        if subitem == '':
            time_text_list.remove(item)
#write list of time codes and text to a new file
with open('new_text.txt','w') as new_file:
    for item in time_text_list:   
#Convert the timecode which displays a time span to a single time stamp. 
#Write only the first 8 digits of the time code; the milliseconds and second time stamp are removed.
            new_file.write("%s" % item[0][:8])
            new_file.write("    %s\n" % item[1])
with open('new_text.txt', 'r') as new_file:
    print new_file.read()
