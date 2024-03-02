"""User models"""

from pydantic import BaseModel, computed_field


class User(BaseModel):
    id: int
    name: str
    age: int


class UserWithAdult(User, BaseModel):
    """User with is_adult for response"""

    @computed_field
    @property
    def is_adult(self) -> bool:
        """User is adult"""
        return self.age >= 18
