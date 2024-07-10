import os
import json
import instructor
from pydantic import BaseModel, ConfigDict
from openai import OpenAI


# Define your desired output structure
class UserInfo(BaseModel):
   name :str
   age :int
class Userinfo_list(BaseModel):
    '''stores list of name and age'''
    users:list[UserInfo]

os.environ["OPENAI_API_KEY"] = " YOUR _ API _ KEY "
# Patch the OpenAI client
client = instructor.from_openai(OpenAI())

# Extract structured data from natural language
user_info = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=Userinfo_list,
    messages=[{"role": "user", "content": " Mugilan is at the age of 19 and Nelson is at the age of 28"}],
)



with open('outcome.json','w') as f:
    json_data = (json.dumps(user_info.dict(), indent =3))
    f.write(json_data)
