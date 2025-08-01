from enum import StrEnum


class AuthTopics(StrEnum):
    NewUser='user.registered'
    LoginUser='user.logon'