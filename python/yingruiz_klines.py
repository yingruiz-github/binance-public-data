"""
1. attempt to download all monthly files
2. then attempt to download all daily files for the current month
3. scan through the files and check their checksum, recrod a list of wrong checksum files. stop if the list is empty
4. delete all files and its checksum files, then download them again
5. go back to step 2 and repeat
"""
import subprocess
from yingruiz_config import TARGET_INTERVALS, TARGET_PARIS, CONDA_RUN_PREFIX, gcp_logger
import datetime
import time
import os
from pathlib import Path


def main():
    
    year = datetime.datetime.utcnow().year
    month = datetime.datetime.utcnow().month
    # day = datetime.datetime.utcnow().day

    current_file:Path = Path(__file__).resolve()
    python_dir = current_file.parent
    os.chdir(python_dir)

    run_report = {}
    total_start_time = time.time()
    
    for pair in TARGET_PARIS:
        run_report[pair] = {}
        for interval in TARGET_INTERVALS:
            run_report[pair][interval] = {
                "monthly":{"time":None, "output":None}, 
                "daily":{"time":None, "output":None}
                }
            
            # monthly 
            monthly_cmd = f"{CONDA_RUN_PREFIX} python download-kline.py -t spot -s {pair} -i {interval} -c 1 -skip-daily 1".split()
            start_time = time.time()
            run_report[pair][interval]["monthly"]["output"] = subprocess.run(monthly_cmd, capture_output = True, text = True)
            run_report[pair][interval]["monthly"]["time"] = time.time() - start_time

            # daily
            daily_cmd = f"{CONDA_RUN_PREFIX} python download-kline.py -t spot -s {pair} -i {interval} -c 1 -skip-monthly 1 -startDate \
                {datetime.date(year = year, month = month, day = 1)}".split()
            start_time = time.time()
            run_report[pair][interval]["daily"]["output"] = subprocess.run(daily_cmd, capture_output = True, text = True)
            run_report[pair][interval]["daily"]["time"] = time.time() - start_time
    
    total_time = time.time() - total_start_time
    
    # delete later
    logs = []
    for pair_name, pair in run_report:
        for interval_name, interval in pair:
            logs.append(interval["monthly"]["output"])
            logs.append(interval["daily"]["output"])
    logs_string = "".join(logs)
    with open("logs.log", "w") as f:
        f.write(logs_string)
        f.writelines([str(total_time)])
        
    return
    # delete later end
    
    # process the download metrics
    # outputs = []
    # for pair_name, pair in run_report:
    #     for interval_name, interval in pair:
    #         labels = {:}
    #         gcp_logger.log_v1(message=str(interval), file_path=current_file, folder=gcp_logger.__class__.LOG_DIR.TEST_DIR, labels=)
            # outputs.extend(v["monthly"]["output"].splitlines())
            # outputs.extend(v["daily"]["output"].splitlines())
            
    # gcp_logger.log_v1(message:str, file_path:str, machine_ip:str = "", folder:LOG_DIR = LOG_DIR.DEFAULT_DIR, 
    #            labels:dict = {}, level:LOG_SEVERITY = LOG_SEVERITY.INFO):
    # log_v1(self, message:str, file_path:str, machine_ip:str = "", folder:LOG_DIR = LOG_DIR.DEFAULT_DIR, 
    #            labels:dict = {}, level:LOG_SEVERITY = LOG_SEVERITY.INFO):
        
            
            
            


    # for pair in TARGET_PARIS:
    #     run_report[pair] = {}
    #     for interval in TARGET_INTERVALS:
    #         temp_cmd = f"{CONDA_RUN_PREFIX} python download-kline.py -t spot -s {pair} -i {interval} -c 1 -skip-daily 1".split()
    #         run_report[pair][interval] = subprocess.run(temp_cmd,  capture_output = True, text = True)
    
    # # attempt to download all monthly files
    # for pair in TARGET_PARIS:
    #     run_report[pair] = {}
    #     for interval in TARGET_INTERVALS:
    #         temp_cmd = f"{CONDA_RUN_PREFIX} python download-kline.py -t spot -s {pair} -i {interval} -c 1 -skip-monthly 1 -startDate {datetime.date(year = year, month = month, day = 1)}".split()
    #         subprocess.run(temp_cmd)
    # return
    

    

if __name__ == "__main__":
    main()
    