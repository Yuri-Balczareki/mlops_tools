import logging 
from omegaconf import DictConfig, OmegaConf
import hydra 
from hydra.utils import get_original_cwd, to_absolute_path

logger = logging.getLogger(__name__)

@hydra.main(config_path="configs", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))
    logger.info("Some info message")
    logger.debug("Some debug message")

if __name__ == "__main__": 
    main()