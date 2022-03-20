from brownie import AdvancedCollectible

def main():
  advanced_collectible = AdvancedCollectible[-1]
  number_of_advanced_collectibles = advanced_collectible.tokenCounter()
  print(f"You have created {number_of_advanced_collectibles} collectibles")
  pass
