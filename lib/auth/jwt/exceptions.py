class JwtTokenException(Exception):
    pass


class TokenMissingException(JwtTokenException):
    pass


class AccessTokenMissingException(TokenMissingException):
    def __str__(self):
        return 'Access token missing'
    

class RefreshTokenMissingException(TokenMissingException):
    def __str__(self):
        return 'Refresh token missing'
    