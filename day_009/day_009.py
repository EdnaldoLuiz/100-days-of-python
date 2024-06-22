from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 0
    PENDING = 2

print(Status.ACTIVE)  
print(Status.ACTIVE.value)  

if Status.ACTIVE == Status(1):
    print("Status ativo!")

class HttpStatus(Enum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

    def is_success(self):
        return 200 <= self.value < 300

print(HttpStatus.OK.is_success()) 
print(HttpStatus.NOT_FOUND.is_success()) 
