
from tag import Tag
import yaml

class ResultAccumulator:
    def __init__(self, tagFilePath: str) -> None:
        self.__parse_args(tagFilePath)
        self.valid_comp_ops = {"GELE", "GTLT", "GT", "GE", "LT", "LE", "EQ"}

    def submit_tag(tagId: str, value: any) -> bool:
        return

    def __parse_args(self, tagFilePath: str) -> None:
            self.tags = {}
            with open(tagFilePath) as f:
                tags_yaml = yaml.load(f, Loader=yaml.FullLoader)
                print(tags_yaml["PV001"]["description"])
                
                # for tag_id, tag_info in tags_yaml.items():
                    
                    
        
                     
            
            # if self.tag_id not in tags_yaml:
            #     raise Exception("Invalid Tag name: Can not be found in yaml")
            # else:
            #     print("Parsing Tag Parameters..")

            #     self.type = tags_yaml[self.tag_id]["type"]
            #     # self.value = sys.argv[2]
            #     try:
            #         self.value = eval(f"{self.type}({self.value})")
            #     except Exception as e:
            #         print(f"Error converting value to {self.type}: {e}")

            #     self.less_than = tags_yaml[self.tag_id]["lessThan"]
            #     self.greater_than = tags_yaml[self.tag_id]["greaterThan"]
            #     self.func_name = tags_yaml[self.tag_id]["function_name"]

ra = ResultAccumulator("./tags.yaml")