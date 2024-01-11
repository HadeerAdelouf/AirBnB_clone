#!/usr/bin/paython3
"""BaseModel class script"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """base model class"""
    def __init__(self, *args, **kwargs):
        """
        public instances attrs

        Args:
            *args:list of arguments
            **kwargs (dict): Key/value pairs of attributes.
        """

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, t_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
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
