from jwt import encode, decode
import datetime as dt

def validate_jwt(jwt_token):
    decoded_payload = decode(jwt_token, "kmwcj2g091v3is8a", algorithms=["HS256"])
    current_date = dt.datetime.now()
    jwt_date = dt.datetime.strptime(decoded_payload.get('Time'), "%d-%m-%Y %H:%M:%S")
    jwt_expiry = 60*60*2
    if (current_date-jwt_date).seconds > jwt_expiry:
        raise Exception('Session Expired! Kindly Login Again')
    return decoded_payload

# Creating JWT Token during Login for specific user types
def generate_user_token(user):
    payload = {'User': user}
    payload['Time'] = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    jwt_token = encode(payload, "kmwcj2g091v3is8a", algorithm="HS256")
    return jwt_token
