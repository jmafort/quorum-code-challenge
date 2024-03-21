import os


APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = os.getenv("APP_PORT", 8000)

LEGISLATORS_DATA_LOCATION = ("data/legislators_(2).csv")
BILLS_DATA_LOCATION = ("data/bills_(2).csv")
VOTES_DATA_LOCATION = ("data/votes_(2).csv")
VOTE_RESULTS_DATA_LOCATION = ("data/vote_results_(2).csv")
