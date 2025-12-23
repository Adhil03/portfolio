from fasthtml.common import *

app, rt = fast_app(live=True, hdrs=(picolink))


@rt("/")
def get():
    return (Titled("Adhil's Portfolio"),)


serve()
