class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


command = input()

while command != "End":
    current_email = command
    if "@" not in current_email:
        raise MustContainAtSymbolError("Email must contain @")

    name, *_ = current_email.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    *_, domain = current_email.split(".")

    if domain != "com" and domain != "bg" and domain != "net" and domain != "org":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    command = input()
