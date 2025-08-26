from enum import StrEnum


class AuthTopics(StrEnum):
    UserRegistered='user_registered'


class NotificationTopics(StrEnum):
    TelegramNotify='telegram_notify'