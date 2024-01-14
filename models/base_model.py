#!/usr/bin/paython3
"""BaseModel class script"""
from datetime import datetime
from uuid import uuid4
from models import storage
import models
import uuid


class BaseModel:
    """base model class"""
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
