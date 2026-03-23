import os #shows files
import shutil #actions
import  sys #CLI
import json
from groq import Groq

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
def unknown_file(ext):
    api=os.getenv("GROQ_API_KEY")
    groq = Groq(api_key=api)

    response = groq.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "identify extintion of file and organize the file with folder name."},
            {
                "role": "user",
                "content":f"prvode folder name to thise exstintion{ext}.no fancy name keep understandable name",
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "file_extintion",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "exstintion": {"type": "string"},
                        "folder_name": {"type": "string"},
                    },
                    "required": ["exstintion", "folder_name"],
                    "additionalProperties": False
                }
            }
        }
    )

    result = json.loads(response.choices[0].message.content or "{}")
    #print(json.dumps(result, indent=2))
    return {result["exstintion"]: result["folder_name"]}


def already_existing_file(file,destination_path):
    name,ext=os.path.splitext(file)
    new_path=os.path.join(destination_path,name+ext)
    i=1
    while os.path.exists(new_path):
        new_path=os.path.join(destination_path,f"{name}({i}){ext}")
        i+=1
    return new_path

#print(files) its Working gave me list of files i have
def organize_files(folder_path):
    files=os.listdir(folder_path) #getting list of files
    ext_map = {

        # Documents
        ".pdf": "documents", ".docx": "documents", ".doc": "documents",
        ".odt": "documents", ".ott": "documents", ".rtf": "documents",
        ".txt": "documents", ".md": "documents", ".markdown": "documents",
        ".rst": "documents", ".tex": "documents", ".wpd": "documents",
        ".wps": "documents", ".pages": "documents", ".epub": "documents",
        ".mobi": "documents", ".azw": "documents", ".azw3": "documents",
        ".djvu": "documents", ".xps": "documents", ".oxps": "documents",
        ".abw": "documents", ".hwp": "documents", ".sxw": "documents",

        # Spreadsheets
        ".xlsx": "spreadsheets", ".xls": "spreadsheets", ".xlsm": "spreadsheets",
        ".xlsb": "spreadsheets", ".xltx": "spreadsheets", ".ods": "spreadsheets",
        ".ots": "spreadsheets", ".csv": "spreadsheets", ".tsv": "spreadsheets",
        ".numbers": "spreadsheets", ".dif": "spreadsheets", ".slk": "spreadsheets",

        # Presentations
        ".pptx": "presentations", ".ppt": "presentations", ".pptm": "presentations",
        ".ppsx": "presentations", ".pps": "presentations", ".odp": "presentations",
        ".otp": "presentations", ".key": "presentations",

        # Images
        ".jpg": "images", ".jpeg": "images", ".png": "images",
        ".gif": "images", ".bmp": "images", ".tif": "images",
        ".tiff": "images", ".webp": "images", ".svg": "images",
        ".svgz": "images", ".ico": "images", ".avif": "images",
        ".heic": "images", ".heif": "images", ".raw": "images",
        ".cr2": "images", ".cr3": "images", ".nef": "images",
        ".nrw": "images", ".arw": "images", ".dng": "images",
        ".orf": "images", ".rw2": "images", ".pef": "images",
        ".psd": "images", ".psb": "images", ".ai": "images",
        ".eps": "images", ".xcf": "images", ".tga": "images",
        ".exr": "images", ".hdr": "images", ".pcx": "images",
        ".ppm": "images", ".pgm": "images", ".pbm": "images",
        ".jfif": "images", ".xbm": "images", ".xpm": "images",

        # Audio
        ".mp3": "audio", ".wav": "audio", ".flac": "audio",
        ".aac": "audio", ".ogg": "audio", ".opus": "audio",
        ".m4a": "audio", ".wma": "audio", ".aiff": "audio",
        ".aif": "audio", ".mid": "audio", ".midi": "audio",
        ".amr": "audio", ".ape": "audio", ".wv": "audio",
        ".mka": "audio", ".ac3": "audio", ".dts": "audio",
        ".caf": "audio", ".tta": "audio", ".spx": "audio",
        ".ra": "audio", ".dsf": "audio", ".dff": "audio",

        # Video
        ".mp4": "video", ".mkv": "video", ".avi": "video",
        ".mov": "video", ".wmv": "video", ".flv": "video",
        ".webm": "video", ".m4v": "video", ".mpg": "video",
        ".mpeg": "video", ".m2v": "video", ".mts": "video",
        ".m2ts": "video", ".3gp": "video", ".3g2": "video",
        ".ogv": "video", ".vob": "video", ".rmvb": "video",
        ".asf": "video", ".f4v": "video", ".mxf": "video",
        ".divx": "video", ".xvid": "video",

        # Archives
        ".zip": "archives", ".rar": "archives", ".7z": "archives",
        ".tar": "archives", ".gz": "archives", ".bz2": "archives",
        ".xz": "archives", ".zst": "archives", ".tgz": "archives",
        ".tbz2": "archives", ".txz": "archives", ".cab": "archives",
        ".iso": "archives", ".dmg": "archives", ".deb": "archives",
        ".rpm": "archives", ".apk": "archives", ".jar": "archives",
        ".war": "archives", ".ace": "archives", ".arj": "archives",
        ".lzh": "archives", ".wim": "archives", ".z": "archives",

        # Code
        ".html": "code", ".htm": "code", ".xhtml": "code",
        ".css": "code", ".scss": "code", ".sass": "code",
        ".less": "code", ".js": "code", ".jsx": "code",
        ".ts": "code", ".tsx": "code", ".vue": "code",
        ".svelte": "code", ".py": "code", ".pyw": "code",
        ".rb": "code", ".java": "code", ".c": "code",
        ".h": "code", ".cpp": "code", ".cc": "code",
        ".hpp": "code", ".cs": "code", ".vb": "code",
        ".go": "code", ".rs": "code", ".swift": "code",
        ".kt": "code", ".dart": "code", ".scala": "code",
        ".ex": "code", ".exs": "code", ".erl": "code",
        ".hs": "code", ".jl": "code", ".lua": "code",
        ".r": "code", ".pl": "code", ".php": "code",
        ".nim": "code", ".zig": "code", ".sol": "code",
        ".groovy": "code", ".f90": "code", ".asm": "code",
        ".cob": "code", ".pas": "code", ".ada": "code",
        ".coffee": "code", ".clj": "code", ".ml": "code",
        ".tcl": "code", ".wasm": "code",

        # Scripts
        ".sh": "scripts", ".bash": "scripts", ".zsh": "scripts",
        ".fish": "scripts", ".ksh": "scripts", ".bat": "scripts",
        ".cmd": "scripts", ".ps1": "scripts", ".vbs": "scripts",
        ".ahk": "scripts", ".wsf": "scripts",

        # Data / Config
        ".json": "data", ".jsonl": "data", ".xml": "data",
        ".yaml": "data", ".yml": "data", ".toml": "data",
        ".ini": "data", ".cfg": "data", ".conf": "data",
        ".env": "data", ".plist": "data", ".csv": "data",
        ".parquet": "data", ".avro": "data", ".pkl": "data",
        ".hdf5": "data", ".h5": "data", ".proto": "data",
        ".graphql": "data", ".bson": "data",

        # Database
        ".sql": "database", ".db": "database",
        ".sqlite": "database", ".sqlite3": "database",
        ".mdb": "database", ".accdb": "database",
        ".dbf": "database",

        # Fonts
        ".ttf": "fonts", ".otf": "fonts", ".woff": "fonts",
        ".woff2": "fonts", ".eot": "fonts", ".fon": "fonts",

        # 3D / CAD
        ".obj": "3d", ".fbx": "3d", ".stl": "3d",
        ".blend": "3d", ".glb": "3d", ".gltf": "3d",
        ".usdz": "3d", ".dae": "3d", ".3ds": "3d",
        ".dwg": "3d", ".dxf": "3d", ".step": "3d",
        ".skp": "3d", ".3mf": "3d", ".ply": "3d",

        # Executables
        ".exe": "executables", ".msi": "executables",
        ".dll": "executables", ".so": "executables",
        ".dylib": "executables", ".app": "executables",
        ".bin": "executables", ".pyc": "executables",
        ".class": "executables", ".dex": "executables",

        # Subtitles
        ".srt": "subtitles", ".vtt": "subtitles",
        ".ass": "subtitles", ".sub": "subtitles",
        ".sbv": "subtitles", ".ttml": "subtitles",

        # GIS
        ".shp": "gis", ".geojson": "gis",
        ".gpx": "gis", ".kml": "gis",
        ".kmz": "gis", ".osm": "gis",

        # Certificates
        ".pem": "certificates", ".crt": "certificates",
        ".cer": "certificates", ".p12": "certificates",
        ".pfx": "certificates", ".gpg": "certificates",
        ".csr": "certificates",

        # ML models
        ".pt": "ml_models", ".pth": "ml_models",
        ".onnx": "ml_models", ".tflite": "ml_models",
        ".gguf": "ml_models", ".safetensors": "ml_models",
        ".keras": "ml_models",

        # Shortcuts
        ".lnk": "shortcuts",
        ".url": "shortcuts",
        ".webloc": "shortcuts",

        # Logs
        ".log": "logs",
        ".trace": "logs",
        ".evtx": "logs",

    } #mapping generated from claude ai
    #if ".xyz" in ext_map: i tried it by adding a new file in desktop named test.xyz it created new folder named xyz and placed file there but when i checked dictionary there is no key name .xyz
    #    print("Key exists")
    with open('log.txt', 'a') as log:  # fully tested and debugged working fine
      for file in files:       #loop to organize files
          source_path = os.path.join(folder_path, file)
          if not os.path.isfile(source_path):#check it is file or folder and skips folders
              continue
          moved=False
          ext=os.path.splitext(file)[1].lower()#its still complex using os plits the dictionary and fisnd the file using exstintion its like i have dictonary like {"image":".jpeg"} it take index 1 of that means ".jpeg"
          folder_name=ext_map.get(ext)

          if folder_name is None: #uses to unknow type of files to add them with help of ai
              new_exti=unknown_file(ext) #returns {".xyz":"others"} like something
              for k,v in new_exti.items(): #separate the both as k (exstintion) v (file_name)
                  ext_map[k]=v #add to exsisting dict
              log.write(f'unknown file extintion:{file} added to dict\n ') #logging important to debugging
              folder_name=v # get new file name and send to next process i mean it will see if folder exisist or create new one


          destination_path = os.path.join(folder_path, folder_name)#it means folder path i mean c:\\user\\image(created itself or uses exisisting)

          if not os.path.exists(destination_path):
              os.makedirs(destination_path)
          final_destination_path = os.path.join(destination_path, file)

          if os.path.exists(final_destination_path):
              new_path=already_existing_file(file,destination_path)
              shutil.move(source_path,new_path)
              log.write(f'Already Exisist:{file} moved as {new_path}\n')
          else:
              shutil.move(source_path, final_destination_path)
              log.write(f"{file} Moved to {destination_path}\n")






           ###Works But Slow and eats memory while using loop
          #for folder_name,extension in file_types.items():
          #    if file.lower().endswith(tuple(extension)):
          #        destination_path = os.path.join(folder_path, folder_name)
          #        if not os.path.exists(destination_path):
          #            os.mkdir(destination_path)
          #        final_destination_path = os.path.join(destination_path, file)
          #        shutil.move(source_path, final_destination_path)
#
          #        moved=True
          #        break





##

organize_files(folder_path)
#Understanding 'for' loop to dictionary
#dictonary={
#    "NAME":"Test",
#    "age":20
#}
#
#
#for k,v in dictonary.items():
#    print(k)
#    print(v)

