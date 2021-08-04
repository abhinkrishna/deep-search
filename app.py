# *************** Algorithm ****************
# a func to search for keyword on a given folder
# read search phrase, let say s = 'abc'
# let n = no of folders in current directory
# for i in range(0,n):
#   1. create a new process
#   2. call search function with i th folder name as parameter
# if found append to result list with,
#   1. file name
#   2. process number
#   print 1,2
#
# after all process ended
#   1. print "search complete"
#   2. display all 
#   

import time
import os
from multiprocessing import Process, current_process

def deep_scan(directory, keyword):
    # displaying the directory of search
    process_id = os.getpid()
    process_name = current_process().name
    print('Process [{}:{}] : Searching on {} folder'.format(process_id, process_name, directory))
    # getting all file in dir
    path = os.listdir(path='.')
    root = '.\\{}\\'.format(directory)
    # all_files_in_dir -> getting all files locations in that folder
    all_files_in_dir = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            all_files_in_dir.append(os.path.join(path, name))
    # print('All files {}'.format(all_files_in_dir))
    # afile -> single file [ iteration through all files ]
    for afile in all_files_in_dir:
        # to skip this app.py file [this file]
        if(afile == './app.py'):
            continue
        try:
            f = open(afile,'r',encoding = 'utf-8')
            content = f.read()    
            if keyword in content:
                #Search Element Found
                fname = afile
                print('[match found] [{}] from {} : {}\n'.format(process_id, directory, fname))
                log = '[{}] -> {}\n'.format(process_name, fname)
                print(log)
                with open("result.txt", "a") as savefile:
                    savefile.write(log)
                savefile.close()
            else:
                print('[included] [{}] : {}'.format(process_name, afile))
        except:
            print("[excluded] [{}] : {}".format(process_name, afile))
        finally:
            f.close() 

if __name__ == "__main__":
    # getting path and number of folders on current dir
    def get_folders():
        path = os.listdir(path='.')
        root = './'
        directory = []
        for x in os.listdir(root):
            if(os.path.isdir(x)):
                directory.append(x)
        return directory

    # Read keyword.ini
    key_file = 'deep_scan_keyword.ini'
    try:
        key = open(key_file,'r',encoding = 'utf-8')
        keyword = key.read()
        if(keyword == ""):
            exit(self)
        print("Searching for '{}'".format(keyword))
        key.close()
    except:
        f = open(key_file, 'w')
        f.close()
        print('deep_scan_keyword.ini not available [now created recommended using it]')
        keyword = input('Enter keyword directly : ')

    # used to calculate total execution time
    start_time = time.time()
    if os.path.exists("result.txt"):
        os.remove("result.txt")
    # Displaying No. of folders found (should create that much threads)
    folders = get_folders()
    print("No. of folders  : {}".format(len(folders)))
    print("Folders founded : {}\n".format(folders))

    processes = []

    # for search in all sub dirs
    for i in folders:
        process = Process(target=deep_scan, args=(i, keyword))
        processes.append(process)
        process.start()

    finish_status = False
    for process in processes:
        process.join()
        finish_status = True
    if(finish_status):
        # Printing results
        res = os.path.exists("result.txt")
        if(res):
            print('\n**************** Results ****************\n')
            results = open('result.txt','r')
            line = results.readline()
            num = 0
            while line:
                num+=1
                print('{} : file -> {}\n'.format(num, line.strip()))
                line = results.readline()
            results.close()
        else:
            print('\n********* No Match Found *********')
            

    end_time = time.time()
    timetaken = "{} seconds".format(round(end_time - start_time, 2))
    print('\nTotal time taken {}'.format(timetaken))
    with open("result.txt", "a") as savefile:
        savefile.write("100% Completed in {}".format(timetaken))
    savefile.close()
    input('press enter to exit...')
