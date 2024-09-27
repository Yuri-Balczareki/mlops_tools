from omegaconf import DictConfig, OmegaConf 

def main() -> None: 
    config = OmegaConf.create({
        "some_key": "some_value", 
        "list_of_items": [1, "2", {"nested_dict_key": "nested_dict_value", }]
    })
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__": 
    main()