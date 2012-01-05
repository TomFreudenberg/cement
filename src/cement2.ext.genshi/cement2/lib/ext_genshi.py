"""Genshi Framework Extension Library."""

import sys
import pkgutil
from genshi.template import NewTextTemplate
from cement2.core import output, backend, exc

Log = backend.minimal_logger(__name__)
    
class GenshiOutputHandler(object):
    """
    This class implements the :ref:`IOutput <cement2.core.output>` 
    interface.  It provides text output from template and uses the 
    `Genshi Text Templating Language <http://genshi.edgewall.org/wiki/Documentation/text-templates.html>`_.  
    
    """
    class Meta:
        interface = output.IOutput
        label = 'genshi'
        
    def __init__(self):
        self.config = None
        
    def setup(self, config_obj):
        """
        Sets up the class for use by the framework.  Little is done here in
        this implementation.
        
        Required Arguments:
        
            config_obj
                The application configuration object.  This is a config object 
                that implements the :ref:`IConfig <cement2.core.config>` 
                interface and not a config dictionary, though some config 
                handler implementations may also function like a dict 
                (i.e. configobj).
                
        Returns: n/a
        
        """
        self.config = config_obj
        
    def render(self, data_dict, template):
        """
        Take a data dictionary and render it using the given template file.
        
        Required Arguments:
        
            data_dict
                The data dictionary to render.

            template
                This option is completely ignored.
                
        Returns: string
        
        """
        tmpl_module = self.config.get('genshi', 'template_module')
        Log.debug("genshi template module is '%s'" % tmpl_module)
        Log.debug("rendering output using '%s' as a template." % template)
        
        # get the template content
        tmpl_content = pkgutil.get_data(tmpl_module, template)
                
        if tmpl_content is None:  
            raise exc.CementRuntimeError(
                "Template file '%s' does not exist in module '%s'." % \
                (template, tmpl_module))
            res = ''
        else:
            tmpl = NewTextTemplate(tmpl_content)
            res = tmpl.generate(**data_dict).render()
            return res
            
        return res
