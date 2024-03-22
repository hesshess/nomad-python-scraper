from extractors.wanted import extract_wanted_jobs
from file import save_to_file

keyword = input("What kinds of jobs do you want to search?")

wanted = extract_wanted_jobs(keyword)

jobs = wanted

save_to_file(keyword, jobs)