import kurt
import hairball
from hairball import Hairball
from hairball import KurtCache
from hairball import plugins
#from hairball.plugins import BlockCounts
#help(hairball)
#print "Begin Test"



#option wrapper class needed to run hairball
class optionWrapper(object):
    def __init__(self, project):
        self.kurt_plugin = {"kurt"}
        self.quiet = False
        self.plugin = {"blocks.BlockCounts", "blocks.DeadCode", "checks.Animation", "checks.BroadcastReceive"
            , "checks.SaySoundSync", "duplicate.DuplicateScripts", "initialization.VariableInitialization"
            , "initialization.AttributeInitialization"}





cacheFolder = "CACHE"
#inFile = {"CACHE/testFile1.sb2", "tests/testFile1.sb2"}
scratchFile = "CACHE/testFile1.sb2"
project = kurt.Project.load(scratchFile)





#creates  a KurtCache object from hairball. essentially the folder where scratch programs you want annalized are
#myKurtCache = KurtCache(cacheFolder)
#print "KurtCache Initialized"
options = optionWrapper(project)
myHairball = Hairball(options,cacheFolder)
myHairball.initialize_plugins()
myHairball.process()
#hairball.main("-p",)








#myHairball = Hairball(project,inFile)

#myHairball.main()
#print "Done"
