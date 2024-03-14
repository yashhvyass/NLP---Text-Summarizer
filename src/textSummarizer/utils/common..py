# Those functions which we will use repeatedly -  utility functions.
import os
from box.exceptions import BoxValueError
import yaml
import textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import AnyStr


# reading any yaml file and print all the contents in it
# returns config box to access the keys directly from dictionary.
# whenver you're passing datatype it is best to make a decorator ensure annotations so that you'll get error while passing wrong value.
@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): Path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    Args:
        path_to_directories(list): list of path of directories to create
        ignore_log(bool, optional): ignore if multiple directories is to be created. Defaults to False
        """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory at: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB
    Args: 
        path (Path): path to file
    returns: 
        str: size in KB
    
    size_in_kb (str): round(os.path.getsize(path)/1024)
    return f"~ {size in kb} KB"
    """