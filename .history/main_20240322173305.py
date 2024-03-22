from extractors.berlin import extract_berlin_jobs
from filex import save_to_file

keyword = input("What kinds of jobs do you want to search?")

berlin = extract_berlin_jobs(keyword)

jobs = berlin

save_to_file(keyword, jobs)