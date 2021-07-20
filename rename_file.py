# this prgoram is for rename the file in windows
# because windows does not support with the bash shell

# -> made on 20-7-2021

import os
import pathlib

def renameFile(dir_path = None, out_path = None):

    # to 2get the filelist of the current inputing dir
    file_paths = os.listdir(dir_path)
    file_lens = len(file_paths)

    print("file_len:",file_lens)

    # set the output file if None:
    if out_path == None:
        out_path = str(dir_path) + '/outdir'

    print("out_path",out_path)
    # dir_path = os.path.join('C:\\Users\\User\\Desktop', timestr)
    os.mkdir(out_path)

    for k in range(0,file_lens):
        file_format,file_extension = os.path.splitext(file_paths[k])
        out_file_name = out_path + "/" + str(k+1) + str(file_extension)
        print("out_file_name",out_file_name)
        f1 = open(file_paths[k], mode='r', encoding='utf-8')
        f2 = open(out_file_name, mode='w+', encoding='utf-8')
        f2.write(f1.read())
        f1.close()
        f2.close()



    

if __name__ == "__main__":

    #
    # mode -> 0, get the path here and make the outpath
    # mode -> 1, get the inpath and outpath
    #

    mode = 0

    # to get the curpath if need
    if mode == 0:
        curPath = pathlib.Path(__file__).parent.resolve()
        renameFile(curPath)

    # print(curPath)
