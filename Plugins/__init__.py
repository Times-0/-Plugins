from Plugins.IPlugin import IPlugin

PermissionError = type('PermissionError', (Exception,), {})

def extend(base, plugin):
    if not hasattr(base, 'extend'):
        raise NotImplementedError("Unable to extend object - {}".format(base))

    if not base.extend:
        raise PermissionError("Extend feature disabled for  - {}".format(base))

    if not issubclass(plugin, IPlugin):
        raise TypeError("Extend allowed only for IPlugin children")

    if not issubclass(base, object):
        raise TypeError("Can extend only new-styled classes deriving objects")

    bases = tuple(base.__bases__)
    if not plugin in bases:
        bases += (plugin,)

    base.__bases__ = bases