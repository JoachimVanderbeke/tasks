from typing import Optional

from pydantic_settings import BaseSettings


# uses BaseSettings which reads environment variables by default and
# sets them to instance attributes having the same names.
# So, we'll have to set a TABLE_NAME environment variable in the Lambda
class Config(BaseSettings):
    TABLE_NAME: str = ""
    DYNAMODB_URL: Optional[str] = None
