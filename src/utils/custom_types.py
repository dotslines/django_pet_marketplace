from dataclasses import dataclass
from typing import Union


@dataclass
class Owner:
    id: Union[int, str]
    email: str


@dataclass
class ModelWithOwnerFK:
    owner: Owner
