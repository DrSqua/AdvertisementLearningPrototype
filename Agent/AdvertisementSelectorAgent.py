from DataStructures.FeatureContainer import FeatureContainer
from Utility.AdvertisementUtility import AdvertisementUtility


class AdvertisementSelectorAgent:
    def __init__(self, utility: AdvertisementUtility):
        self.utility = utility

    def calculate_advertisement_order_by_copy(self, n: int, baseFeatureContainer: FeatureContainer,
                                              featureContainerList: list[FeatureContainer]) -> list[FeatureContainer]:
        """
        Function takes in a first featureContainer, a list of featureContainers and a size n
        Then selects the n best fitting featureContainers
        :param n: Count of advertisement indices which will be returned
        :param baseFeatureContainer:
        :param featureContainerList:
        :return: indices of advertisements
        """

        # Error checking
        if len(featureContainerList) < n:
            raise ValueError("Requested top n advertisements can not be larger than len of input advertisementList")

        # Generating the score for each advertisement
        adValues: list[float] = [self.calculate_advertisement_score(baseFeatureContainer, advertisement) for advertisement in featureContainerList]

        # A little inefficient, but can be optimized later <- Then again, why bother
        sortedAd = [ad for _, ad in sorted(zip(adValues, featureContainerList), reverse=True, key=lambda pair: pair[0])]
        return sortedAd[:n]

    def calculate_advertisement_score(self, person: FeatureContainer, advertisement: FeatureContainer) -> float:
        return self.utility.calculate_utility(person=person, advertisement=advertisement)
