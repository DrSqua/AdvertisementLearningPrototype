import time

from FeatureContainer import FeatureContainer
from AdvertisementSelectorAgent import AdvertisementSelectorAgent
from ReinforcedLearning.RandIntUtility import RandIntUtility


if __name__ == '__main__':
    saved_time: list = [time.time()]

    print("Setting up variables ...")
    person1 = FeatureContainer({"Lid": 1, "Gedoopt": 1})  # Non-FTI maar wel bij ons gedoopt
    person2 = FeatureContainer({"Student": 1, "FTI": 1})  # Standaard FTI, niet van Ingenium

    print("    Set up person1 as: " + str(person1))
    print("    Set up person2 as: " + str(person2))

    advertisement1 = FeatureContainer({"Lid": 1, "Gedoopt": 1})  # Cantus
    advertisement2 = FeatureContainer({"Student": 1, "FTI": 1})  # Pitchavond
    advertisementList = [advertisement1, advertisement2]

    print("    Set up advertisement1 as: " + str(advertisement1))
    print("    Set up advertisement2 as: " + str(advertisement2))

    print("    Setting up utility function ... ", end="")
    utility = RandIntUtility()

    print("Done!")

    print("    Setting up AdvertisementSelectorAgent ... ", end="")
    advertisementSelectorAgent = AdvertisementSelectorAgent(utility)
    print("Done!")
    print("Finished setup!" + "\n"*2)


    print("Running algorithm ...")
    n: int = 2
    print("    Selecting advertisements with n = " + str(n) + " ... ", end="")
    selectedAdvertisements = advertisementSelectorAgent.calculate_advertisement_order(2, person1, advertisementList)

    saved_time.append(time.time())
    print(f"Done! {saved_time[-1] - saved_time[-2]}")
    print("Finished running algorithm!" + "\n"*2)

    print("Printing top " + str(n) + " selected algorithms:")
    for ad in selectedAdvertisements:
        print(ad)
