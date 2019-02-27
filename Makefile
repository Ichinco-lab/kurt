CACHEDIR = CACHE/
BLOCK = -p blocks.DeadCode -p duplicate.DuplicateScripts -p blocks.BlockCounts -p checks.Animation
CHECK = -p checks.Animation -p checks.BroadcastReceive -p checks.SaySoundSync
ATTR = -p initialization.AttributeInitialization -p initialization.VariableInitialization
OUTPUT = output.txt


RUNHAIRBALLTOSCREEN:
		hairball $(BLOCK) $(CHECK) $(CACHEDIR)

RUNHAIRBALL:
		hairball $(BLOCK) $(CHECK) $(CACHEDIR) > $(OUTPUT)
