from extractors.wanted import extract_wanted_jobs
from filex import save_to_file

keyword = input("What kinds of jobs do you want to search?")

wanted = extract_wanted_jobs(keyword)

jobs = wanted

print(len(jobs))
save_to_file(keyword, jobs)