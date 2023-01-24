import time

from DataStructures.FeatureContainer import FeatureContainer
from Agent.AdvertisementSelectorAgent import AdvertisementSelectorAgent
from Utility.MostInCommonUtility import MostInCommonUtility


if __name__ == '__main__':
    """
    A list of possible features
    Lid, Gedoopt, Student, FTI, Ingenium Schacht
    """
    saved_time: list = [time.time()]

    print("Setting up variables ...")
    person1 = FeatureContainer({"Lid": 1, "Gedoopt": 1})  # Non-FTI maar wel bij ons gedoopt
    person2 = FeatureContainer({"Student": 1, "FTI": 1})  # Standaard FTI, niet van Ingenium
    person3 = FeatureContainer({"Lid": 1, "Student": 1, "Ingenium_Schacht": 1, "Gedoopt": 1})  # Schacht
    personList = [person1, person2, person3]

    print("    Set up person1 as: " + str(person1))
    print("    Set up person2 as: " + str(person2))

    advertisement1 = FeatureContainer({"Lid": 1, "Gedoopt": 1, "Ingenium_Schacht": 1})  # Cantus
    advertisement2 = FeatureContainer({"Student": 1, "FTI": 1})  # Pitchavond
    advertisement3 = FeatureContainer({"Lid": 1, "Gedoopt": 1, "Student": 1})  # TD
    advertisement4 = FeatureContainer({"Lid": 1, "Student": 1, "Gedoopt": 1})  # Café Avond
    advertisement5 = FeatureContainer({"Student": 1, "FTI": 1})  # Study sessie
    advertisementList = [advertisement1, advertisement2, advertisement3, advertisement4, advertisement5]

    print("    Set up advertisement1 as: " + str(advertisement1))
    print("    Set up advertisement2 as: " + str(advertisement2))

    print("    Setting up utility function ... ", end="")
    utility = MostInCommonUtility()

    print("Done!")

    print("    Setting up AdvertisementSelectorAgent ... ", end="")
    advertisementSelectorAgent = AdvertisementSelectorAgent(utility)
    print("Done!")
    print("Finished setup!" + "\n"*2)

    for person in personList:
        n: int = 2
        print(f"Running algorithm for {n} ads adjusted to {person} ...")

        print("    Selecting advertisements with n = " + str(n) + " ... ", end="")
        selectedAdvertisements = advertisementSelectorAgent.calculate_advertisement_order_by_copy(2, person1, advertisementList)

        saved_time.append(time.time())
        print(f"Done! {saved_time[-1] - saved_time[-2]}")

        print("    Printing top " + str(n) + " selected algorithms:")
        for ad in selectedAdvertisements:
            print("    " + str(ad))

        print("Finished running algorithm!" + "\n" * 2)
