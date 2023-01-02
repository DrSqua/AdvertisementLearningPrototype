from DataStructures.FeatureContainer import FeatureContainer
from Utility.AdvertisementUtility import AdvertisementUtility


class AdvertisementSelectorAgent:
    def __init__(self, utility: AdvertisementUtility):
        self.utility = utility

    def calculate_advertisement_order(self, n: int, person: FeatureContainer,
                                      advertisementList: list[FeatureContainer]) -> list[FeatureContainer]:
        """
        :param n: Count of advertisement indices which will be returned
        :param person:
        :param advertisementList:
        :return: indices of advertisements
        """

        # Error checking
        if len(advertisementList) < n:
            raise "Fuck you"

        # Generating the score for each advertisement
        adValues: list[float] = [self.calculate_advertisement_score(person, advertisement) for advertisement in advertisementList]

        # Super inefficient, but can be optimized later
        sortedAd = [ad for _, ad in sorted(zip(adValues, advertisementList), reverse=True, key=lambda pair: pair[0])]
        return sortedAd[:n]

    def calculate_advertisement_score(self, person: FeatureContainer, advertisement: FeatureContainer) -> float:
        return self.utility.calculate_utility(person=person, advertisement=advertisement)
