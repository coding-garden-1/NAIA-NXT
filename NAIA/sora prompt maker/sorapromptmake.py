
import openai 
from openai import OpenAI

with open("openai_key.txt",'r') as file:
    key = file.read().strip()

client = OpenAI(
    api_key=key,
)

def llm_call(transcript):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": """
             

             
Your job is to create an uplifting scene 
that would make the individual feel more empowered
about whatever negative emotion or situation they are going through.

The scene has to be incredibly specific to resolving their issue.

You must word it in a way that a video making AI understands:

like First person perspective POV sitting in a cafe excitedly writing ideas on a whiteboard with marker.

(input: negative emotions; 
output: video prompt for uplifting scene). 

Please be as specific as you can be with the scene.

Please format it in a way that a video AI can understand 

(so it shouldn't be too long, too short, or too vague).

One sentence max.

You must always include the words first person perspective, and never use the users name.


             """
             
             },
            {"role": "user", "content": transcript}
        ]
    )
    generated_message = completion.choices[0].message.content
    return generated_message


