class AdmissionError(Exception):
    """Base exception for all admission-related errors."""


class InvalidInputError(AdmissionError):
    """Raised when input data fails validation."""
