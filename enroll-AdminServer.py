import os
import java

#=======================================================================================
# Get WebLogic home
#=======================================================================================        
def getWeblogicHome():
   return str(java.lang.System.getProperty('pineapple.weblogic.home.path'))

   
#=======================================================================================
# Get domain directory
#=======================================================================================
def getDomainDirectory():
    return domainsDirectory + '/' + domainName
        
#=======================================================================================
# Get node manager home
#=======================================================================================
def getNmHomeDirectory():
    return getWeblogicHome() + '/common/nodemanager'

#=======================================================================================
# start and connect to adm server outside node manager process
#=======================================================================================
def startAdmServer():
    url = 't3://' + adminListenAddress + ':' + adminListenPort
    block = 'true'
    timeout = 60000
    startServer(serverName, domainName, url, systemUser, systemPassword, getDomainDirectory(), block, timeout)
    connect(systemUser, systemPassword, url)

def main():   

    try:

        # BUG, if domainName is used then is NONE by the time nmConnect is invoked??
        name=domainName
        domainDirectory=getDomainDirectory() 

        # start amdserver
        startAdmServer()

        # enroll server
        nmEnroll(domainDirectory, getNmHomeDirectory())

        # shutdown adm server outside node manager process
        shutdown()

        # connect to node manager
        nmConnect(nmUserName,nmPassword,adminListenAddress,nmPort,name,domainDirectory)

        # start amdserver in nm process
        nmStart(adminServerName, domainDirectory)

    except:
        dumpStack()

main()
exit()