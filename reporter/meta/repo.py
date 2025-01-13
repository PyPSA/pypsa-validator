"""
Module to retrieve repository information.

Provides:
    - BRANCH_FEAT: Feature branch name.
    - BRANCH_MAIN: Main branch name.
    - DIFF_CONFIG: Difference between feature and main branch for the snakemake config
      file.
    - AHEAD_COUNT: Number of commits ahead of the main branch.
    - BEHIND_COUNT: Number of commits behind the main branch.
"""

from pathlib import Path

import git
import yaml

from reporter.meta.config import HASH_FEAT, HASH_MAIN, PATH_CONFIG, PATH_REPO

repo = git.Repo(PATH_REPO)

try:
    repo.git.fetch("--all")
except git.exc.GitCommandError:
    print("Failed to fetch all branches.")

try:
    BRANCH_FEAT = repo.commit(HASH_FEAT).name_rev.split(" ")[-1].split("/")[-1]
    HASH_FEAT_SHORT = HASH_FEAT[:7]
except git.exc.GitCommandError:
    msg = f"Failed to checkout feature branch with hash {HASH_FEAT}."
    raise ValueError(msg)

try:
    BRANCH_MAIN = repo.commit(HASH_MAIN).name_rev.split(" ")[-1].split("/")[-1]
    HASH_MAIN_SHORT = HASH_MAIN[:7]
except git.exc.GitCommandError:
    msg = f"Failed to checkout main branch with hash {HASH_MAIN}."
    raise ValueError(msg)


DIFF_CONFIG = repo.git.diff(HASH_MAIN, HASH_FEAT, PATH_CONFIG)
AHEAD_COUNT = len(
    list(
        repo.iter_commits(
            f"{HASH_FEAT}...{HASH_MAIN}",
            left_only=True,
        )
    )
)
BEHIND_COUNT = len(
    list(
        repo.iter_commits(
            f"{HASH_FEAT}...{HASH_MAIN}",
            right_only=True,
        )
    )
)

# Read in hash specific config
file_blob = repo.commit(HASH_MAIN).tree / str(PATH_CONFIG)
CONFIG_MAIN = yaml.safe_load(file_blob.data_stream.read().decode("utf-8"))
file_blob = repo.commit(HASH_FEAT).tree / str(PATH_CONFIG)
CONFIG_FEAT = yaml.safe_load(file_blob.data_stream.read().decode("utf-8"))


PATH_MAIN_RESULTS = (
    Path("main")
    / "results"
    / CONFIG_MAIN.get("run", {}).get("prefix", "")
    / CONFIG_MAIN.get("run", {}).get("name", "")
)
PATH_FEAT_RESULTS = (
    Path("feat")
    / "results"
    / CONFIG_FEAT.get("run", {}).get("prefix", "")
    / CONFIG_FEAT.get("run", {}).get("name", "")
)
