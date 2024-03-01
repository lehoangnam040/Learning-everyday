from datetime import datetime
from pydantic.datetime_parse import from_unix_seconds
from pydantic import BaseModel


class UnixSecondsToDatetimeField(datetime):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            description="epoch timestamp",
            type="number",
            examples=[1709298399.0],
        )

    @classmethod
    def validate(cls, v):
        if not isinstance(v, (int, float)):
            raise TypeError("epoch timestamp required")
        return from_unix_seconds(v)
    

class DatetimeToUnixSecondsField(float):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            description="epoch timestamp",
            type="number",
            examples=[1709298399.0],
        )

    @classmethod
    def validate(cls, v):
        print("validate")
        # comment this check number to see error in fastapi response
        if isinstance(v, (int, float)):
            return v
        elif not isinstance(v, datetime):
            raise TypeError("required datetime")
        return v.timestamp()
    

class ModelReq(BaseModel):
    dt: UnixSecondsToDatetimeField

    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp()   # pydantic 1.10.14, it's not working
        }

class ModelDto(BaseModel):
    dt: DatetimeToUnixSecondsField


m = ModelReq.parse_obj({"dt": 1715298399})
print(m)

print(m.dict())

m_dto = ModelDto.parse_obj(m)
print(m_dto)