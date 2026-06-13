from pydantic import BaseModel,Field

class ResponseModel(BaseModel):
    message:str= Field(description="Response from the model")
