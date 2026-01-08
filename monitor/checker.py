import time
import requests
import logging

def check_api(url: str, timeout: int) -> dict:
    start = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        latency = round((time.time() - start) * 1000, 2)

        success = response.status_code == 200

        return {
            "success": success,
            "status_code": response.status_code,
            "latency_ms": latency,
        }

    except requests.RequestException as e:
        logging.error(f"Request failed for {url}: {e}")
        return {
            "success": False,
            "status_code": None,
            "latency_ms": None,
        }
