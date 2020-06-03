import os
import re
print('Selected Directory:', os.getcwd())
user_input = input('Do You Want To Proceed?(y/n) ')
if user_input.capitalize() == 'Y':
    string = input('Enter The Name You Want To Give To Each File: ')
    no = 0
    replace_name = ''
    for file_names in os.listdir():
        if file_names == 'renamer.py' or file_names == 'renamer.exe':
            continue
        extension_finder = re.compile(r'\..+$')            # this will catch extensions such as .pdf , .mp4 , .jpg  etc
        ext = extension_finder.search(file_names)
        no += 1                                            # no variable will increement each time the loop runs 
        try:
            replace_name = f'{string}-{no}{file_names[ext.start():ext.end()]}'     # .start() will return starting index and .end() will return ending index of the extension string
        except AttributeError:                                                     # for renaming multiple directories
            replace_name = f'{string}-{no}'
        os.rename(file_names, replace_name)
    print('Process Completed!!')

else:
    print('Process Aborted!!')
