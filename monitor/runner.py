import time
import logging
from monitor.checker import check_api
from monitor.metrics import APIMetrics
from monitor.config import load_config
from monitor.logger import setup_logger

def start_monitoring():
    setup_logger()
    config = load_config()

    poll_interval = config["poll_interval_seconds"]
    timeout = config["timeout_seconds"]
    alert_threshold = config["failure_alert_threshold"]

    api_metrics = {}

    logging.info("API monitoring started")

    while True:
        for api in config["apis"]:
            name = api["name"]
            url = api["url"]

            if name not in api_metrics:
                api_metrics[name] = APIMetrics()

            result = check_api(url, timeout)
            api_metrics[name].record(result)

            metrics = api_metrics[name]

            logging.info(
                f"{name} | success={result['success']} "
                f"latency={result['latency_ms']}ms "
                f"uptime={metrics.uptime_percentage()}%"
            )

            if metrics.failure_streak >= alert_threshold:
               logging.warning(
    f"[ALERT] {name} failed "
    f"{metrics.failure_streak} consecutive checks"
)

        time.sleep(poll_interval)
