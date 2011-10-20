"""Cement core plugins module."""

from cement2.core import backend, exc, interface

Log = backend.minimal_logger(__name__)

def plugin_validator(klass, obj):
    """Validates an handler implementation against the IPlugin interface."""
    
    members = [
        'setup',
        'load_plugin',
        'load_plugins',
        'loaded_plugins',
        ]
    interface.validate(IPlugin, obj, members)
    
class IPlugin(interface.Interface):
    """
    This class defines the Plugin Handler Interface.  Classes that 
    implement this handler must provide the methods and attributes defined 
    below.
    
    Implementations do *not* subclass from interfaces.
    
    Usage:
    
    .. code-block:: python
    
        from cement2.core import plugin
        
        class MyPluginHandler(object):
            class meta:
                interface = plugin.IPlugin
                label = 'my_plugin_handler'
            ...
    
    """
    class imeta:
        label = 'plugin'
        validator = plugin_validator
    
    # Must be provided by the implementation
    meta = interface.Attribute('Handler meta-data')
    loaded_plugins = interface.Attribute('List of loaded plugins')
    enabled_plugins = interface.Attribute('List of enabled plugins')
    disabled_plugins = interface.Attribute('List of disabled plugins')
    
    def setup(config_obj):
        """
        The setup function is called during application initialization and
        must 'setup' the handler object making it ready for the framework
        or the application to make further calls to it.
        
        Required Arguments:
        
            config_obj
                The application configuration object.  This is a config object 
                that implements the :ref:`IConfig` <cement2.core.config>` 
                interface and not a config dictionary, though some config 
                handler implementations may also function like a dict 
                (i.e. configobj).
                
        Returns: n/a
        
        """
    
    def load_plugin(self, plugin_name):
        """
        Load a plugin whose name is 'plugin_name'.
        
        Required Arguments:
        
            plugin_name
                The name of the plugin to load.
                
        """
        
    def load_plugins(self, plugin_list):
        """
        Load all plugins from plugin_list.
        
        Required Arguments:
        
            plugin_list
                A list of plugin names to load.
        
        """
        