# Nothing to actually run, just explore these things.

# What is ASGI

# WSGI
def request(environ, start_response):
    r = start_response(environ)
    # ...
    return r


# ASGI
async def app(scope, receive, send):
    r = await receive(scope)
    # ...
    return await send(r, scope)


# Resources
# https://github.com/florimondmanca/awesome-asgi


# Server
# uvicorn - https://www.uvicorn.org/
