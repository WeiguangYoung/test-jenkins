import base64

authorization = "Basic eWFuZzoxMjM0NTY="


def check_basic_auth(basic_auth):
    auth_info = basic_auth.replace("Basic ", "")
    auth_info = base64.b64decode(auth_info)
    auth_info = auth_info.decode()
    login_info = auth_info.split(":")
    if len(login_info) != 2:
        return None
    username, password = login_info
    return login_info


print(check_basic_auth(authorization))
