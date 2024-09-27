import hydra 
from omegaconf import DictConfig
from hydra.utils import instantiate 
import torch 

class MyClass: 
    def __init__(self, name:str) -> None:
        self.name = name 

    def say_hello(self) -> None: 
        print(f"Hello, {self.name}")

def main() -> None: 
    my_class = MyClass(name="Yuri") 
    my_class.say_hello()

if __name__ == "__name__": 
    main()