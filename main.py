import os #shows files
import shutil #actions
import  sys #CLI
import json
from utilities import unknown_file
from utilities import already_existing_file

#functions of os i know listdir==to get list of files
#os.path.isfile==it checks the selection is file or not
#os.path.join==it helps to define correct path
#os.path.exists==y

#folders_path=sys.argv[1] #path defined
#
#if not folders_path:    Not working trying another
#    print("Enter folder Path!")
#
try:
    folder_path = sys.argv[1]
except IndexError:
    print("Folder path not provided")
    sys.exit()


if not os.path.exists(folder_path):
    sys.exit("Folder Path Not Found")


def organize_files(folder_path):
    files=os.listdir(folder_path) #getting list of files

    with open('log.txt', 'a') as log:
     with open('data.json', 'r+') as Ex_file:
      ext_map = json.load(Ex_file)
      for file in files:
          source_path = os.path.join(folder_path, file)
          if not os.path.isfile(source_path):
              continue
          moved=False
          ext=os.path.splitext(file)[1].lower()
          folder_name=ext_map.get(ext)

          if folder_name is None:
              new_exti=unknown_file(ext)

              for k,v in new_exti.items():
                  ext_map[k]=v

              Ex_file.seek(0)
              json.dump(ext_map, Ex_file)
              Ex_file.truncate()
              log.write(f'unknown file extintion:{file} added to dict\n ')
              folder_name=v

          destination_path = os.path.join(folder_path, folder_name)

          if not os.path.exists(destination_path):
              os.makedirs(destination_path)
          final_destination_path = os.path.join(destination_path, file)

          if os.path.exists(final_destination_path):
              new_path=already_existing_file(file,destination_path)
              try:
                  os.rename(source_path,new_path)
              except OSError:
                  shutil.move(source_path,new_path)
              log.write(f'Already Exisist:{file} moved as {new_path}\n')
          else:
              try:
                  os.rename(source_path,final_destination_path)
              except OSError:
                  shutil.move(source_path, final_destination_path)

              log.write(f"{file} Moved to {destination_path}\n")


organize_files(folder_path)

