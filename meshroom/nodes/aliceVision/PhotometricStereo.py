__version__ = "3.0"

from meshroom.core import desc

class PhotometricStereo(desc.CommandLineNode):
    commandLine = 'aliceVision_photometricStereo {allParams}'
    category = 'Photometry'
    documentation = '''
TODO.
'''

    inputs = [
        desc.File(
            name='inputPath',
            label='SfmData',
            description='Input file. Coulb be SfMData file or folder.',
            value='',
            uid=[0],
        ),
        desc.File(
            name='maskPath',
            label='Mask folder path',
            description='Mask folder path',
            value='',
            uid=[0],
        ),
        desc.File(
            name='pathToJSONLightFile',
            label='Lights Folder',
            description='Folder containing lighting information.',
            value='',
            uid=[0]
        )
    ]

    outputs = [
        desc.File(
            name='outputSfmData',
            label='SfmData',
            description='Path to the output folder',
            value=desc.Node.internalFolder + '/sfmData.sfm',
            uid=[],
            group='', # remove from command line
        ),
        desc.File(
            name='outputPath',
            label='Output Folder',
            description='Path to the output folder',
            value=desc.Node.internalFolder,
            uid=[],
        ),
    ]
