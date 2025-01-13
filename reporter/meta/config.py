from pathlib import Path

from reporter.utils import read_env_var

# Mounted Paths
PATH_ARTIFACTS = Path("/artifacts")
PATH_REPO = Path("/repo")

# Project
PLATFORM = read_env_var("PLATFORM", "gitlab")
DOMAIN = read_env_var("DOMAIN", "https://gitlab.com")
OWNER = read_env_var("OWNER")
REPO = read_env_var("REPO")
URL_RUNNER = read_env_var("URL_RUNNER", "google.com")

# Comparing branches
HASH_MAIN = read_env_var("HASH_MAIN")
HASH_FEAT = read_env_var("HASH_FEAT")

# Configuration
PLOTS = read_env_var("PLOTS")

PATH_CONFIG = read_env_var("PATH_CONFIG")

# Do some checks on mounted paths
if not PATH_ARTIFACTS.exists():
    msg = f"Path '{PATH_ARTIFACTS}' must be mounted."
    raise OSError(msg)
needed_subdir = [
    "feat/benchmarks",
    "feat/results",
    "feat/logs",
    "feat/.snakemake/log",
    "main/benchmarks",
    "main/results",
    "main/logs",
    "main/.snakemake/log",
]
if not all((PATH_ARTIFACTS / subdir).exists() for subdir in needed_subdir):
    msg = f"Path '{PATH_ARTIFACTS}' must contain subdirectories: {needed_subdir}"
    raise OSError(msg)

if not PATH_REPO.exists():
    msg = f"Path '{PATH_REPO}' must be mounted."
    raise OSError(msg)
