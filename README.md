Example for demoing a bokeh server with Binder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/panel-demos/bird_migration/master?urlpath=/proxy/5006/app

Create a `app_no_temp.py` in the repo. This is the application that will be served.

This repo contains:

- `environment.yml` installing bokeh and nbserverproxy
- a custom serverextension (`bokehserverextension.py`) that launches bokeh server
- a `postBuild` script to enable the server extensions and install the local one
  (this last step would go away if the local extension became a proper package)
- A [panel](https://github.com/pyviz/panel) based app which visualizes migration patterns of bird species in the Americas
