import os
import time

from loguru import logger

def run():
    param = os.environ.get("BATCH_PARAM")
    logger.info(f"run batch with parama {param}")
    logger.info(f"start: {time.time()}")
    time.sleep(2)
    logger.info(f"end. : {time.time()}")

if __name__ == "__main__":
    run()