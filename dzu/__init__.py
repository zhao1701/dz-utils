import sys
from pathlib import Path

import git


def find_repo_dir(add_to_sys_path=True):
    repo_dir = git.Repo(search_parent_directories=True).working_dir
    sys.path.append(repo_dir)
    return Path(repo_dir)
