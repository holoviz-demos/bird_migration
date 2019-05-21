from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the app.py directory with bokeh server"""
    Popen(["panel", "serve", "app.py", "--allow-websocket-origin=*"])
