from mypackage.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mypackage.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline
from mypackage.pipeline.stage_03_model_training import ModelTrainingPipeline
from mypackage import logger


STAGE_NAME = "DATA INGESTION"
try:
    logger.info(f'{STAGE_NAME} started')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'{STAGE_NAME} completed')
except Exception as e:
    logger.exception(e)
    raise e
    


STAGE_NAME = "PREPARE BASE MODEL"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "TRAIN MODEL"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e