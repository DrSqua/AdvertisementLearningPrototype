from typing import Union


class FeatureContainer:
    def __init__(self, startingDict=None) -> None:
        """
        features is a dictionary holding all specified features with corresponding values for a given object
        """
        if startingDict is None:
            startingDict = {}
        self.featureDict: dict[str, int] = startingDict

    def __str__(self) -> str:
        featureContainerString: str = "FeatureContainer: "
        for key in list(self.featureDict.keys()):
            featureContainerString += str(key) + ", "
        return featureContainerString

    def __iter__(self) -> iter:
        return FeatureContainerIter(list(self.featureDict.keys()))

    def push_back(self, featureName: str, featureValue: Union[bool, int]) -> None:
        """

        :param featureName:
        :param featureValue:
        # 'Union[a, b]' is equal to 'a | b', in other words 'a or b'
        """
        self.featureDict[featureName] = int(featureValue)
        # TODO Optimize storage
        # 1) Us a type of hashtable to convert featurename as str to ID
        # 2) Differentiate between bool and int? Might have no use

    def at(self, featureName: str) -> int:
        return self.featureDict.get(featureName)


class FeatureContainerIter:
    def __init__(self, featureContainerKeys: list[str]):
        self.featureContainerKeys: list[str] = featureContainerKeys
        self.featureIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.featureIndex < len(self.featureContainerKeys):
            self.featureIndex += 1
            return self.featureContainerKeys[self.featureIndex - 1]  # We use -1 because python has no ++i operator
        raise StopIteration
