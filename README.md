# loggly-restsfdc
A wrapper around the simple-salesforce module to ease making REST API calls to SFDC
##Create a client by instantiating a restsfdc client
sf = sfdcrest.sfdcrestClient()
###Note: It expects a file with all the required SFDC credentials in the folder /etc/analytics/sfdcrest.conf. 
###The other option is to put it in the conf dolder of the directory structure. Take a look at the sameple file structure
##to get an idea of how the config file should look like


##To Read an Opportunity by a custom field
sf.execute('get-opportunity',<custom-field-name>,<custom-field-name-value>)

## To update an Opportunity using an id
sf.execute('update-opportunity',<Opportunity-ID>,<data-dict>):
