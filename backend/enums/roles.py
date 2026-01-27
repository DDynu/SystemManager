from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    MANAGER = "manager"

def checkRole(role):
    match role:
        case "admin":
            return Role.ADMIN
        case "user":
            return Role.USER
        case "manager":
            return Role.MANAGER
