#!/usr/bin/paython3
"""BaseModel class script"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """base model class"""
    def __init__(self):
        """public instances attrs"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """prints readable presentaion"""
        Cname = self.__class__.__name__
        return "[{}] ({}) {}".format(Cname, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
          the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """return dictionary contents as key/value"""
        ins_diCt = self.__dict__.copy()
        ins_diCt["__class__"] = self.__class__.__name__
        ins_diCt["created_at"] = self.created_at.isoformat()
        ins_diCt["updated_at"] = self.updated_at.isoformat()
        return ins_diCt
