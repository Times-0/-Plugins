from Plugins.IPlugin import IPlugin

class Example(IPlugin):
    """Example plugin.
    """

    requirements = list()
    name = 'ExamplePlugin'
    developer = 'Dote'

    def __init__(self, engine):
        super(Example, self).__init__(engine)
        
        print "Example Plugin!!"
