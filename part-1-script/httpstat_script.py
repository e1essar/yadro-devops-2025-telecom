#!/usr/bin/env python3
import requests
import sys
import logging
from requests.exceptions import RequestException, Timeout

logging.basicConfig(
    format = "[%(asctime)s] - %(levelname)s - %(message)s",
    level = logging.INFO
)

logger = logging.getLogger(__name__)

def main():
    code = None
    if len(sys.argv) > 1:
        try:
            code = int(sys.argv[1])
        except ValueError:
            logger.error("Argument of code is not integer.")
            sys.exit(1)
      
    default_codes = [101, 200, 300, 404, 500]
    if code is not None:
        codes = [code]
    else:
        codes = default_codes
        
    urls = [f"https://httpstat.us/{c}" for c in codes]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code // 100
            if status in (1,2,3):
                logger.info(f"URL: {url} | Status: {response.status_code} | Body: {response.text}")
            else:
                response.raise_for_status()
        except Timeout:
            logger.error(f"Request timeout {url}")
        except RequestException as e:
            logger.error(f"Exception error {url}: {e}")
            
if __name__ == "__main__":
    main()