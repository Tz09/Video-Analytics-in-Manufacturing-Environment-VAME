import importlib
from server.service import _state

interfaces = ['login','register','logout']

URLs = []
for interface in interfaces:
    _interface = importlib.import_module(f'.{interface}', package=__name__)
    URL = getattr(_interface, 'url')
    URLs += URL
    for module, *urls in URL:
        locals().update({
            module: getattr(_interface, module)
        })
_state.URL += URLs