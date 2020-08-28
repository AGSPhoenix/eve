#Eve config file

logToStdout = False #False for status display, True for debug logs
stdoutLogLevel = "INFO"
logToFile = True
logFile = "eve.log"

boardUpdateDelay = 120
imageDir = "./boards"
ratelimitRate = 1

downloadMedia = False
downloadThumbs = True

#Database conection info
host='localhost'
user='root'
passwd=''
db='eve'

checkArchive = True
checkArchivePercentage = 80

boards = [
         "bant",
         "c",
         "e",
         "n",
         "news",
         "out",
         "p",
         "toy",
         "vip",
         "vp",
         "w",
         "wg",
         "wsr",
         ]