__version__ = "1.0"

from meshroom.core import desc


class ExportMaya(desc.AVCommandLineNode):
    commandLine = 'aliceVision_exportMeshroomMaya {allParams}'

    category = 'Export'
    documentation = '''
Export a scene for Autodesk Maya, with an Alembic file describing the SfM: cameras and 3D points.
It will export half-size undistorted images to use as image planes for cameras and also export thumbnails.
Use the MeshroomMaya plugin, to load the ABC file. It will recognize the file structure and will setup the scene.
MeshroomMaya contains a user interface to browse all cameras.
'''

    inputs = [
        desc.File(
            name="input",
            label="Input SfMData",
            description="Input SfMData file.",
            value="",
            uid=[0],
        ),
        desc.ChoiceParam(
            name="verboseLevel",
            label="Verbose Level",
            description="Verbosity level (fatal, error, warning, info, debug, trace).",
            value="info",
            values=["fatal", "error", "warning", "info", "debug", "trace"],
            exclusive=True,
            uid=[],
        ),
    ]
    
    outputs = [
        desc.File(
            name="output",
            label="Folder",
            description="Folder for MeshroomMaya outputs: undistorted images and thumbnails.",
            value=desc.Node.internalFolder,
            uid=[],
        ),
    ]
