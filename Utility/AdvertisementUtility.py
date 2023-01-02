from abc import ABC

from DataStructures.FeatureContainer import FeatureContainer


class AdvertisementUtility(ABC):
    """
    Base class for Utility Class
    defines calculate_utility function

    Deriving from ABC metaclass means that all classes which inherit from this class
    are force to overwrite all member functions
    """
    def calculate_utility(self, person: FeatureContainer, advertisement: FeatureContainer):
        pass
