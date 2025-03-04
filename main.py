from src.pipeline.stage_01_data_ingestion import *
from src import logger

if __name__ == '__main__':
    try:
        logger.info(f'{STAGE_NAME} started')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'{STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e