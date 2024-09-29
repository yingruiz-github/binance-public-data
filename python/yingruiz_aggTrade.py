"""
down load aggTrade trade data
"""
import subprocess
from yingruiz_config import TARGET_PARIS, gcp_logger,CONDA_ENV_NAME
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
        run_report[pair] = {
                "monthly":{"time":None, "output":None, "error":None}, 
                "daily":{"time":None, "output":None, "error":None}
                }
            
        # monthly 
        #print("runned")
        monthly_cmd = f"conda run -n {CONDA_ENV_NAME} python download-aggTrade.py -t spot -s {pair} -c 1 -skip-daily 1".split() # {CONDA_RUN_PREFIX} 
        start_time = time.time()
        temp_result = subprocess.run(monthly_cmd, capture_output = True, text = True)
        run_report[pair]["monthly"]["output"] = temp_result.stdout
        run_report[pair]["monthly"]["error"] = temp_result.stderr
        run_report[pair]["monthly"]["time"] = time.time() - start_time

        # daily
        #print("runned") # {CONDA_RUN_PREFIX} 
        daily_cmd = f"conda run -n {CONDA_ENV_NAME} python download-aggTrade.py -t spot -s {pair} -c 1 -skip-monthly 1 -startDate \
            {datetime.date(year = year, month = month, day = 1)}".split()
        start_time = time.time()
        temp_result = subprocess.run(daily_cmd, capture_output = True, text = True)
        run_report[pair]["daily"]["output"] = temp_result.stdout
        run_report[pair]["daily"]["error"] = temp_result.stderr
        run_report[pair]["daily"]["time"] = time.time() - start_time
    
    total_time = time.time() - total_start_time
    
    # delete later
    #print(TARGET_PARIS, CONDA_ENV_NAME)
    logs = []
    errors = []
    for pair_name, pair in run_report.items():
        errors.append(pair["monthly"]["error"])
        errors.append(pair["daily"]["error"])
        logs.append(pair["monthly"]["output"])
        logs.append(pair["daily"]["output"])
    logs_string = "".join(logs)
    errors_string = "".join(errors)
    with open("aggTrade_logs.log", "w") as f:
        f.write(logs_string)
        f.writelines([str(total_time)])
    with open("aggTrade_erros.txt", "w") as f:
        f.write(errors_string)
        
    return
    # delete later end


if __name__ == "__main__":
    main()
    