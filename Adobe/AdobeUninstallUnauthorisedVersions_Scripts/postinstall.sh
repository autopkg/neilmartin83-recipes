#!/bin/bash
logFile="/Library/Logs/Adobe/UninstallUnauthorizedVersions-$(/bin/date +%F-%T).log"

/private/tmp/AdobeCCUninstaller | /usr/bin/tee "$logFile"
/bin/echo "$(/bin/cat $logFile)"