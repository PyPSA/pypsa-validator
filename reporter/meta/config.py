from reporter.utils import read_env_var

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
