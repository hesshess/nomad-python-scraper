import csv

def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    writter = csv.writer(file)
    writter.writerow(["Title", "Company","Reward", "Link"] )
    for job in jobs:
        writter.writerow(job.values())
    file.close()