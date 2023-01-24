from Utility.AdvertisementUtility import AdvertisementUtility
from DataStructures.FeatureContainer import FeatureContainer


class MostInCommonUtility(AdvertisementUtility):
    def calculate_utility(self, person: FeatureContainer, advertisement: FeatureContainer):
        adScore: float = 0.0
        for adFeature in advertisement:
            if adFeature in person:
                adScore += 1.0
            else:
                adScore -= 0.2
        return adScore
