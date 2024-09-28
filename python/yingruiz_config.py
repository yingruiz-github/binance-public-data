from pathlib import Path
from gcp_module.module.cloud_logging.cloud_logging import CloudLoggingWrapper

API_PUBLIC_KEY="gEm27MHfMknISWTDGAxprCz0DXa1p54tEnXkZDVutcGyPWcRSZxIDoevbhW9L5O5"
API_PRIVATE_KEY="OWoz9YsodSkOAp86zma2lBX8eRoCrrSnByvicmxD4AzeRBciC1su7JOQZkg2bBVJ"

# PYTHON_DIR = Path(__file__).resolve().parent

KLINE_COLUMN_NAMES = [
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",	
    "close_time",	
    "quote_volume",
    "count",	
    "taker_buy_volume",
    "taker_buy_quote_volume",
    "ignore"
]

TARGET_PARIS = [
    "SUNUSDT",
    "BNBUSDT",
    "RAREUSDT",
    "ALPACAUSDT",
    "BAKEUSDT",
    "NULSUSDT",
    "RAYUSDT",
    "PROSUSDT",
    "VOXELUSDT",
    "IOUSDT",
    "BANANAUSDT",
    "FLUXUSDT",
    "SAGAUSDT",
    "SOLUSDT",
    "BTCUSDT",
    "ETHUSDT",
    "PEPEUSDT",
    "XRPUSDT",
    "WIFUSDT",
    "TRXUSDT",
    "FLUXUSDT",
    "LQTYUSDT",
    "EDUUSDT",
    "DATAUSDT",
    "BTTCUSDT",
    "VIDTUSDT",
    "GHSTUSDT",
    "UFTUSDT",
    "JSTUSDT"
]

TARGET_PARIS = [
    "SUNUSDT",
    "BNBUSDT"
]

TARGET_INTERVALS = [
    "1m",
     "3m",
      "5m",
       "15m",
        "30m",
         "1h",
          "2h",
           "4h",
            "1d",
            "1w"
]

CONDA_ENV_NAME = "trading_data_download"
CONDA_RUN_PREFIX = f"conda run -n {CONDA_ENV_NAME}"

gcp_logger = CloudLoggingWrapper()