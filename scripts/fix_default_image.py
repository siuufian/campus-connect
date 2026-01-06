import base64
import os

# This is a minimal 1x1 gray JPEG image encoded in base64
jpeg_data = base64.b64decode(
    '/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsK'
    'CwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQU'
    'FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAABAAEDASIA'
    'AhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEB'
    'AQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCwAB//2Q=='
)

media_path = 'C:\\Users\\abusu\\Downloads\\Diagram\\campus-connect-main\\media'
os.makedirs(media_path, exist_ok=True)

with open(os.path.join(media_path, 'default.jpg'), 'wb') as f:
    f.write(jpeg_data)

print("Created minimal valid JPEG image")
