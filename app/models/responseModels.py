
class Response:
    def __init__(self, status_code: int, message: str, data: any):
        self.status_code=status_code,
        self.message=message,
        self.data=data
    
    def toDict(self):
        return {
            "status": self.status_code,
            "message": self.message,
            "data": self.data
        }
        