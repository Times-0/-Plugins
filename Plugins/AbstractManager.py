from abc import ABCMeta

class Abstraction:
    loaded_plugins = list()

    @classmethod
    def PluginExists(cls, _id):
        for plugin in Abstraction.loaded_plugins:
            if plugin[0] == _id:
                return True
        
        return False
    
    @classmethod
    def getPlugin(cls, _id):
        for plugin in Abstraction.loaded_plugins:
            if plugin[0] == _id:
                return plugin[1]
        
        return None
    
    @classmethod
    def getAllPlugins(cls):
        return list(p[1] for p in Abstraction.loaded_plugins)

    @classmethod
    def getAllPluginsByDeveloper(cls, dev):
        plugins = list()
        for plugin in Abstraction.getAllPlugins():
            if plugin.developer == dev:
                plugins.append(plugin)

        return plugins

class AbstractManager(object):
    """
    AbstractManager: base type for any plugin
    """

    def __new__ (cls, *args, **kwargs):
        instance = super(AbstractManager, cls).__new__(cls, *args, **kwargs)
        _id = instance.code

        Abstraction.loaded_plugins.append((_id, instance))
        return instance

    pass