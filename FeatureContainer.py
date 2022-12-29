from typing import Union


class FeatureContainer:
    def __init__(self, startingDict=None):
        """
        features is a dictionary holding all specified features with corresponding values for a given object
        """
        if startingDict is None:
            startingDict = {}
        self.featureDict: dict[str, int] = startingDict

        # For making class iterable
        self.feature_index: int = 0

    def __str__(self):
        featureContainerString: str = "FeatureContainer: "
        for key in list(self.featureDict.keys()):
            featureContainerString += str(key) + ", "
        return featureContainerString

    def __iter__(self):
        return FeatureContainerIter(list(self.featureDict.keys()))

    def push_back(self, featureName: str, featureValue: Union[bool, int]):
        """

        :param featureName:
        :param featureValue:
        # 'Union[a, b]' is equal to 'a | b', in other words 'a or b'
        """
        self.featureDict[featureName] = int(featureValue)
        # TODO Optimize storage (differentiate between 0 or 1 and int)

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
            return self.featureContainerKeys[self.featureIndex]
        raise StopIteration