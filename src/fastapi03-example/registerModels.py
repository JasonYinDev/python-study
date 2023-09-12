from pydantic import BaseModel,validator,Field

class UserSignUp(BaseModel):
  username:str=Field(...,example="jason")
  password:str=Field(...,example="123")
  repassword:str=Field(...,example="123")
  
  @validator("repassword")
  def tow_pass_match(cls,value,values):
    print(value!=values["password"])
    if value!=values["password"]:
      raise ValueError("password not match")
    
    return value