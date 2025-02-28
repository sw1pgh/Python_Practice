# Learning 'match' statement <-> Similar to `switch` statement in other programming languages

def http_status(status):
    match status:
        case 200:
            return 'OK'
        case 404:
            return 'NOT FOUND'
        case 500:
            return 'INTERNAL SERVER ERROR'
        case _:
            return 'UNKNOWN STATUS'
    
# Usage
print(http_status(200)) # Prints 200 
print(http_status(404)) # Prints Not Found 
print(http_status(500)) # Prints Internal Server Error
print(http_status(1000)) # Prints Unknown Status 