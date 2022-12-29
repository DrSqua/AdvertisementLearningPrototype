from random import randint

from .AdvertisementUtility import AdvertisementUtility
from FeatureContainer import FeatureContainer


class RandIntUtility(AdvertisementUtility):
    def calculate_utility(self, person: FeatureContainer, advertisement: FeatureContainer):
        return randint(0, 10)
