"""User registration and authentication services."""

# pylint: disable=import-error
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    """Raised when supplied user data is invalid."""


class AuthenticationError(Exception):
    """Raised when user authentication fails."""


class UserService:
    """Validate user input and coordinate repository operations."""

    def __init__(self, user_repository=default_user_repository):
        """Create a service backed by the given user repository."""
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        """Return the matching user or raise an authentication error."""
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        """Validate and create a user."""
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        """Raise an input error if registration data is invalid."""
        if not username or not password:
            raise UserInputError("Username and password are required")

        if password != password_confirmation:
            raise UserInputError("Passwords do not match")

        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")

        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already in use")


user_service = UserService()
