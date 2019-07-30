README:

to get blockCount file run getNumBlocksByProject.py





Basic Steps Flow Chart:

-usrProj has a list of project ids and associated user ids
-the other starter csv files hold various project data


#########   ########    ########    ########
#usrProj#   #blocks#    #sprite#    #stacks# //raw csv files
#########   ########    ########    ########
    |           |           |           |
    |       *******************************
    |       *       preProcess.py         * //preprocesses csv files
    |       *******************************
    |           |           |           |
    |       #########    ##########   #########
    |       #pBlocks#    #pSprites#   #pStacks# //preprocessed csv files
    |       #########    ##########   #########
    |           |           |           |
    |       *******************************
    |       *    generateProjectFile.py   * //combine into single csv file
    |       *******************************
    V           |
#########   ##########
#usrProj#   #projects#
#########   ##########___
    |           |        |
***********************  |
* generateUserFile.py *  | //remove projects entries in usrProj not in projects
***********************  |
        |                V
################    ##########
#synchedUsrProj#    #projects# //now both files should be synced by project id
################    ##########
        |                |
    ************************
    *  buildTimeSeries.py  * //build time series dataset
    ************************
        |
        V
    #####################
    #Time Series Dataset# //save the time series dataset (provided functions
    ##################### //use cpickle)

Use-age:
This software is designed such that once you complete a steps (on the
diagram these are the .py programs with the asterisks as a border)
you shouldn't need to run it again.


1.
In preProcess.py, the goal is to take the block, sprite, and stack file
and create a preprocessed version of each of these files which in a given row
will contain the project id and fields from dr. scratch obtained from the
unprocessed files. (fields: Abstraction, Parallelism, User Interactivity, Flow
Control, Logic, Data Representation, and synchronization)

2. In generateProjectFile.py, the goal is to combine all of the preprocessed
files generated in step 1 and combine them into a single file. This can either
be done all at once or in stages as the resulting file can be used as an
argument in the function used to create it. Always use the preprocessed
blocks file or the output file which used blocks as its head file as the head
file as certain of the preprocessed files get the order of projects jumbled
based on how python orders dictionaries.

3. In generateUserFile.py, the goal is to generate a modified user file which
only contains the project ids listed within the project file created in step 2
such that if one begins reading line by line within both files at the beginning,
the project ids will always match.

4. Having a guaranteed synchronized project id between the project file and
the user file allows us to save significant time and heap space in building
a time series but this does not autosave. Save functions are included but you
will need to call them yourselves. (That said, with the current optimizations
the time series building function only takes a few seconds to run due to
having most of the work done in the previous steps so if you forget to save,
you don't need to wait too long)
