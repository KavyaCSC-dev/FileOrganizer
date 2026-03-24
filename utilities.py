import os #shows files
import json
from groq import Groq

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


