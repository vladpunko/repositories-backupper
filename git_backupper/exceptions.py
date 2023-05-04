# Copyright 2023 (c) Vladislav Punko <iam.vlad.punko@gmail.com>

__all__ = ["FileSystemError", "SettingsError"]


class FileSystemError(OSError):
    """The custom exception class to represent operating system or disk errors.

    This exception is used to represent all errors related to the operating system
    or input and output operations on the current working machine. This includes all
    system-level errors generated by failed system calls.
    """


class SettingsError(ValueError):
    """The custom exception class should include an error message that describes the
    issue that occurred while processing the settings.

    This exception should be raised when an error occurs that is related to the
    processing or validation of settings, such as when a required setting is missing
    or when a setting is invalid.
    """
