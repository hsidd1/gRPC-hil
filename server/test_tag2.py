"""
Tests individual tag

"""
import pytest
import sys
import yaml


class Tag:
    def __init__(self, tag_name: str, value: any) -> None:
        self.tag_name = tag_name
        self.value = value
        self.__parse_args()
        self.run_tests()

    def test_less_than(self):
        return self.value < self.less_than

    def test_greater_than(self):
        return self.value > self.greater_than

    def __parse_args(self):
        # if len(sys.argv) < 1:
        #     raise Exception("Tag and value argument not specified")
        # if len(sys.argv) < 2:
        #     raise Exception("Value argument not specified")

        # tag_name = sys.argv[1]

        with open("server/tags.yml") as f:
            tags_yaml = yaml.load(f, Loader=yaml.FullLoader)
            print(tags_yaml)
        if self.tag_name not in tags_yaml:
            raise Exception("Invalid Tag name: Can not be found in yaml")
        else:
            print("Parsing Tag Parameters..")

            self.type = tags_yaml[self.tag_name]["type"]
            # self.value = sys.argv[2]
            try:
                self.value = eval(f"{self.type}({self.value})")
            except Exception as e:
                print(f"Error converting value to {self.type}: {e}")

            self.less_than = tags_yaml[self.tag_name]["lessThan"]
            self.greater_than = tags_yaml[self.tag_name]["greaterThan"]
            self.func_name = tags_yaml[self.tag_name]["function_name"]

    def run_tests(self):
        # pytest.main()
        self.test_greater_than()
        self.test_less_than()

    def __str__(self) -> str:
        return f"""
            Tag Name: {self.tag_name}
            Value: {self.value}
            Less Than: {self.less_than}
            Greater Than: {self.greater_than}
            Function Name: {self.func_name}
        """


if __name__ == "__main__":
    t = Tag("PV001", 10)
    print(t)
    pytest.main(["-v", "-s", "server/test_tag2.py"])
