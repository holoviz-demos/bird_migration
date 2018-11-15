from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the app.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "app_no_temp.py", "--allow-websocket-origin=*"])
