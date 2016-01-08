__author__ = 'ssinha'
__version__= '0.1'

from conman import load_config, ConfigLoadError
from os.path import dirname, join

SFDC_CONF = '/etc/analytics/sfdcrest.conf'
CONF_DIR = join( dirname( dirname( __file__ ) ), 'conf' )

try:
    sfdcconfig = load_config( SFDC_CONF )
except ConfigLoadError:
    sfdcconfig = load_config( join( CONF_DIR, 'sfdc.test.conf' ) )