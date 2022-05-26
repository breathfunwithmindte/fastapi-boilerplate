from typing import Union
from pydantic import BaseModel

class UserFormstate(BaseModel):
    username: str
    description: Union[str, None] = None
    short_description: Union[str, None] = "Hello world i am using this app."
    age: int