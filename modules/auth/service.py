class AuthService:
    """Service layer for handling authentication and user account operations."""

    def __init__(self) -> None:
        """Initialize the AuthService instance."""
        pass

    def login(self):
        """Authenticate a user and return tokens."""
        pass

    def register(self):
        """Register a new user and return tokens."""
        pass

    def reset_password(self):
        """Initiate password reset process by sending a reset link."""
        pass

    def reset_password_confirm(self):
        """Confirm password reset using a provided token."""
        pass

    def refresh_token(self):
        """Refresh access and refresh tokens using a valid refresh token."""
        pass

    def current_user(self):
        """Retrieve the currently authenticated user."""
        pass

    def change_password(self):
        """Change the current user's password."""
        pass
