# loggly-restsfdc
A wrapper around the simple-salesforce module to ease making REST API calls to SFDC

####Import from the class object

```sh
from logglyrestsfdc  import sfdcrest
```

####Create a client by instantiating a rest based SFDC client

```sh
sf = sfdcrest.sfdcrestClient()
```
Note: It expects a file with all the required SFDC credentials in the folder /etc/analytics/sfdcrest.conf. 
The other option is to put it in the conf dolder of the directory structure. Take a look at the sameple file structure
to get an idea of how the config file should look like


####To Read an Opportunity by a custom field
```sh
sf.execute('get-opportunity',<custom-field-name>,<custom-field-name-value>)
```

#### To update an Opportunity using an id
```sh
sf.execute('update-opportunity',<Opportunity-ID>,<data-dict>):
```
