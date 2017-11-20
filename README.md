# -Plugins
An extensible, flexible plugin system written in Python

# Example usage, with requirements
```py
from Plugins.IPlugin import IPlugin, IPluginAbstractMeta
from Example import Example

class TestPlugin(IPlugin):

    requirements = [
        {
            "name" : "ExamplePlugin",
            "code" : "",
            "developer" : "Dote",
            "version" : 0
        }
    ]

    name = "Test Plugin"

    def __init__(self, engine):
        super(TestPlugin, self).__init__(engine)

MyPlugin = TestPlugin(None)
```

# Example usgae, with extensibility
```py
om Plugins.IPlugin import IPlugin, IPluginAbstractMeta
from Plugins.Abstract import ExtensibleObject
from Plugins import extend
from Example import Example

class Extensible(ExtensibleObject):

    extend = True

class Test(IPlugin):

    __metaclass__ = IPluginAbstractMeta

    @classmethod
    def onBuild(cls):
        print Receiver.__bases__
        extend(Extensible, cls)
        extend(Receiver, cls)

    def cool(self):
        print 'cool'

# test
a = Extensible()
a.cool()
```
