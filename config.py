from yacs.config import CfgNode as CN


_C = CN()

_C.AZURE_OPENAI = CN()
_C.AZURE_OPENAI.ENDPOINT_DOMAIN = 'vtomopenai0226.openai.azure.com'
_C.AZURE_OPENAI.KEY = 'e0d7fe7b8cd44da785f984782e882eb8'
_C.AZURE_OPENAI.DEPLOYMENT = 'gpt35turbo'

def get_cfg_defaults():
    """Get a yacs CfgNode object with default values for my_project."""
    # Return a clone so that the defaults will not be altered
    # This is for the "local variable" use pattern
    return _C.clone()

# Alternatively, provide a way to import the defaults as
# a global singleton:
# cfg = _C  # users can `from config import cfg`
