from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(default= 123, validate_default=True)

user = User()
print(user)