"""This module has interesting methods to make check
    of information data found.
    
    Author:
        jazzrelax
    """


from os import mkdir
from pathlib import Path
from os.path import isfile, isdir
from urllib.parse import urlparse


# PATH UTILITIES ----------------------------------------------------


def initialpath() -> str:
    """It returns to project root directory, no matter
    where it be.

    Returns:
        str: root path.
    """
    path = Path(__file__).parent.absolute().__str__()
    path = backdirs(ndir=2, dire=path)
    return path


def backdirs(ndir=0, dire='') -> str:
    """This functions backs levels from a path.

    Args:
        ndir (int, optional): number of levels to come back. Defaults to 0.
        dire (str, optional): path to analyze. Defaults to ''.

    Returns:
        str: requested path.
    """
    # rever to dire and become tuple
    dire = list(dire)
    dire.reverse()
    dire = tuple(dire)
    # testing dirs level to change
    for n in range(ndir):
        dire = dire[dire.index('/')+1:]
    else:
        # list, reverse and become generator
        dire = list(dire)
        dire.reverse()
        dire = (n for n in dire)
        # returning path
        return ''.join(n for n in dire)


def joindirfile(pathfile: str) -> str:
    """This method can join file or dir or both.

    Args:
        pathfile (str): file or dir.

    Returns:
        str: joined file or dir.
    """
    pathfile = intialpath() + f'/{pathfile}' \
        if pathfile[0] != '/' else intialpath() + f'{pathfile}'
    return pathfile


def isitfile(file: str) -> bool:
    """This method checks if a pathfile is a file.

    Args:
        file (str): path and file str.

    Returns:
        bool: True if it's file.
    """
    return isfile(file)


def isitdir(dir: str) -> bool:
    """This method checks if a path is a directory.

    Args:
        dir (str): path str.

    Returns:
        bool: True if it's file.
    """
    return isdir(dir)


def createdir(path: str, dir: str):
    """This method is just to create a new directory.

    Args:
        path (str): path initial.
        dir (str): directory to create.
    """
    if isitdir(dir=path+f'/{dir}'):
        return
    mkdir(path+f'/{dir}')


# PATH UTILITIES ----------------------------------------------------

# STR UTILITIES -----------------------------------------------------


def strinanotherstr(str1='', str2='') -> bool:
    """This method checks if a str is in another str.

    Args:
        str1 (str, optional): str to compare - part. Defaults to ''.
        str2 (str, optional): str to compare - whole. Defaults to ''.

    Returns:
        bool: True if str1 in str2 else False.
    """
    slen = str1.__len__()
    str2 = str2[:slen]
    for idx in range(slen):
        if str1[idx] != str2[idx]:
            return False
    else:
        return True


# STR UTILITIES -----------------------------------------------------

# HTML UTILITIES ----------------------------------------------------


def takesfromclosedtag(tag='<tag>', content='') -> str:
    """This method take off text inside a closed tag.

    Args:
        tag (str, optional): html tag open. Defaults to '<tag>'.
        content (str, optional): content with info to removes html tag. 
        Defaults to ''

    Returns:
        str: text inside closed tag.
    """
    tag_cl = f'{tag[0]}/{tag[1:]}'
    op_id = cl_id = len_op = len_cl = 0
    len_op = tag.__len__()
    len_cl = tag_cl.__len__()
    len_content = content.__len__()
    try:
        for i in range(len_content):
            if content[i:i+len_op] == tag:
                op_id = i+len_op
                break
        for i in range(len_content):
            if content[i:i+len_cl] == tag_cl:
                cl_id = i+len_cl
                break
        content = content[op_id:cl_id]
        cl_id = len_cl
        return content[:-cl_id]
    except IndexError:
        content = op_id = cl_id = None
        return ''
    finally:
        tag = tag_cl = len_op = len_cl = len_content = None


def takeparam(content: str, param: str, endid='>') -> str:
    """This method can take param content from a html tag.

    Args:
        content (str): content to analyze.
        param (str): param to find.
        endid (str, optional): param end from content. Defaults to '>'.

    Returns:
        str: param and content -> param="{content}"
    """
    plen = param.__len__()
    clen = content.__len__()
    try:
        for idx in range(clen):
            if param == content[idx:idx+plen]:
                content = content[idx:]
                break
        else:
            return ''
        return content[:content.index(endid)]
    except IndexError:
        return ''


def takeparamcontent(content=(), tag='>', end='', *params):
    """This function makes a generator of wished params at
    a html tag.

    Args:
        content (tuple, optional): data to analyze. Defaults to ().
        tag (str, optional): html tag. Defaults to ''.
        end (str, optional): end param char. Defaults to '>'.

    Returns:
        generator: wished param content.
    """
    content = list(line for line in content if tag in line)
    indexes, idx = [], 0
    for line in content:
        for param in params:
            if not param in line:
                indexes.append(idx)
        idx += 1
    else:
        for idx in indexes:
            del content[idx]
        else:
            indexes, idx = [], 0
    for line in content:
        for idx in params:
            indexes.append(takeparam(content=line, param=idx, endid=end))
    indexes = (line for line in indexes)
    content = (line for line in indexes)
    return content


# HTML UTILITIES ----------------------------------------------------

# URL UTILITIES -----------------------------------------------------


def urlchecker(urlink: str) -> bool:
    """This method is for checks a url link.

    Args:
        urlink (str): url link.

    Returns:
        bool: True if urlink is valid else False.
    """
    try:
        result = urlparse(url=urlink)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False


def urlfilename(urlink: str) -> str:
    """This method takes a file name from an URL.

    Args:
        urlink (str): URL to take name.

    Returns:
        str: file name from URL.
    """
    urlink = list(urlink)
    urlink.reverse()
    urlink = urlink[:urlink.index('/')]
    urlink.reverse()
    return ''.join(f for f in urlink)

# URL UTILITIES -----------------------------------------------------
