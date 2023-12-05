#!/usr/bin/python3

"""
This is the base model of the project, where other classes
will inherit from
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This class is the base model of the project, where other classes
    will inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Initialisation

        args:
            ... - ...
        """

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at":
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if key == "updated_at":
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """

        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with
        the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance:
        by using self.__dict__, only instance attributes
        set will be returned
        a key __class__ must be added to this dictionary
        with the class name of the object
        created_at and updated_at must be converted to string
        object in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        you can use isoformat() of datetime object
        This method will be the first piece of the
        serialization/deserialization process:
        create a dictionary representation with “simple object type”
        of our BaseModel
        """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return (new_dict)
