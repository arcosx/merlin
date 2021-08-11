# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from client.configuration import Configuration


class Project(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'mlflow_tracking_url': 'str',
        'administrators': 'list[str]',
        'readers': 'list[str]',
        'team': 'str',
        'stream': 'str',
        'labels': 'list[Label]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mlflow_tracking_url': 'mlflow_tracking_url',
        'administrators': 'administrators',
        'readers': 'readers',
        'team': 'team',
        'stream': 'stream',
        'labels': 'labels',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, mlflow_tracking_url=None, administrators=None, readers=None, team=None, stream=None, labels=None, created_at=None, updated_at=None, _configuration=None):  # noqa: E501
        """Project - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._mlflow_tracking_url = None
        self._administrators = None
        self._readers = None
        self._team = None
        self._stream = None
        self._labels = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if mlflow_tracking_url is not None:
            self.mlflow_tracking_url = mlflow_tracking_url
        if administrators is not None:
            self.administrators = administrators
        if readers is not None:
            self.readers = readers
        if team is not None:
            self.team = team
        if stream is not None:
            self.stream = stream
        if labels is not None:
            self.labels = labels
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def mlflow_tracking_url(self):
        """Gets the mlflow_tracking_url of this Project.  # noqa: E501


        :return: The mlflow_tracking_url of this Project.  # noqa: E501
        :rtype: str
        """
        return self._mlflow_tracking_url

    @mlflow_tracking_url.setter
    def mlflow_tracking_url(self, mlflow_tracking_url):
        """Sets the mlflow_tracking_url of this Project.


        :param mlflow_tracking_url: The mlflow_tracking_url of this Project.  # noqa: E501
        :type: str
        """

        self._mlflow_tracking_url = mlflow_tracking_url

    @property
    def administrators(self):
        """Gets the administrators of this Project.  # noqa: E501


        :return: The administrators of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._administrators

    @administrators.setter
    def administrators(self, administrators):
        """Sets the administrators of this Project.


        :param administrators: The administrators of this Project.  # noqa: E501
        :type: list[str]
        """

        self._administrators = administrators

    @property
    def readers(self):
        """Gets the readers of this Project.  # noqa: E501


        :return: The readers of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._readers

    @readers.setter
    def readers(self, readers):
        """Sets the readers of this Project.


        :param readers: The readers of this Project.  # noqa: E501
        :type: list[str]
        """

        self._readers = readers

    @property
    def team(self):
        """Gets the team of this Project.  # noqa: E501


        :return: The team of this Project.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Project.


        :param team: The team of this Project.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def stream(self):
        """Gets the stream of this Project.  # noqa: E501


        :return: The stream of this Project.  # noqa: E501
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this Project.


        :param stream: The stream of this Project.  # noqa: E501
        :type: str
        """

        self._stream = stream

    @property
    def labels(self):
        """Gets the labels of this Project.  # noqa: E501


        :return: The labels of this Project.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Project.


        :param labels: The labels of this Project.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501


        :return: The created_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.


        :param created_at: The created_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Project.  # noqa: E501


        :return: The updated_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Project.


        :param updated_at: The updated_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Project, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
