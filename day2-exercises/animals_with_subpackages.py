# Import classes from your brand new package

# can do it for example like this:

import animal.harmless
import animal.dangerous

harmless_birds =  animal.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animal.dangerous.Fish()
dangerous_fish.printMembers()

dangerous_mammals = animal.dangerous.Mammals()
dangerous_mammals.printMembers()
###############3

# or like this

from animal import harmless, dangerous

harmless_birds =  harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = dangerous.Fish()
dangerous_fish.printMembers()
