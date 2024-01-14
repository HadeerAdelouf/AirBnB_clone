#!/usr/bin/paython3
"""BaseModel class script"""
from datetime import datetime
from uuid import uuid4
from models import storage
import models

class BaseModel:
    """base model class"""
    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """prints readable presentaion"""
        Cname = self.__class__.__name__
        return "[{}] ({}) {}".format(Cname, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
          the current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """return dictionary contents as key/value"""
        ins_diCt = self.__dict__.copy()
        ins_diCt["__class__"] = self.__class__.__name__
        ins_diCt["created_at"] = self.created_at.isoformat()
        ins_diCt["updated_at"] = self.updated_at.isoformat()
        return ins_diCt
