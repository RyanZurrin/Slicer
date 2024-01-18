import slicer
from slicer import slicervolumerenderingtestdatapaths as datapath

filepath = f"{datapath.input}/VolumeRendering_CTAbdomen_AppleTutorial.xml"
testUtility = slicer.app.testingUtility()
success = testUtility.playTests(filepath)
if not success:
    raise Exception("Failed to finished properly the play back !")
