import csv





"""
@param rawSpriteFile:
	the unprocessed sprite file to be processed
@param outFile:
	the file to write the processed sprite data too
	Default: 'sprites.csv'
@return:
	Returns 1 on failure and 0 on success
"""
def preProcessSprites(rawSpriteFile, outFile="sprites.csv"):
	try: #Opening the file reader and writer
		spriteRawReader = open(rawSpriteFile,"rb")
		spriteReader = csv.DictReader(spriteRawReader)
		spriteWriter = open(outFile, "w")
	except:
		print "Sprite Processor Failed To Open File."
		print "Exiting Function With Value of 1."
		return 1
	#####Variables###########Description###########################
	project_id = 0  #the id of the current project.               #
	numSprites = 0  #the number of sprites in the current project #
	numScripts = 0  #thr numbrt of scripts in the current project #
	###############################################################
	
	
	spriteWriter.write("project_id,sprites,scripts\n")
	"""
	all sprites within a project are always next to each other row wise
	within an unprocessed sprite file so we can take advantage of this
	locality to avoid having to store all project information in a list
	before exporting to a csv file.
		
	Instead we can export a processed project's sprite information as
	soon as the project id changes and we will never need to worry
	about that project again.
	"""
	for sprite in spriteReader:
		if int(project_id) != 0 and int(sprite["project_id"]) != project_id:
			spriteWriter.write(str(project_id) +","+ str(numSprites) +","+ str(numScripts)+"\n")
			numSprites = 0
			numScripts = 0
		project_id = int(sprite["project_id"])
		numScripts += int(sprite["scripts"])
		numSprites += 1	
	#We need this line to write the final project's sprite information
	spriteWriter.write(str(project_id) +","+ str(numSprites) +","+ str(numScripts)+"\n")
	
	try: #Closing the file reader and writer
		spriteWriter.close()
		spriteRawReader.close()
	except:
		print "Sprite Processor Failed To Close File."
		print "Exiting Function With Value of 1."
		return 1
	return 0
		
		
		
preProcessSprites("spriteProcessTestInput.csv")
	
	
	
	