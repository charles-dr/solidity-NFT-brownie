from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path

def main():
  advanced_collectible = AdvancedCollectible[-1]
  number_of_advanced_collectibles = advanced_collectible.tokenCounter()
  print(f"You have created {number_of_advanced_collectibles} collectibles")
  for token_id in range(number_of_advanced_collectibles):
    breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
    collectible_metadata = metadata_template
    if Path(metadata_file_name).exists():
      print(f"{metadata_file_name} already exists! Delete it to overwrite")
    else:
      print(f"Creating metadata file: {metadata_file_name}")
      collectible_metadata.name = breed
      collectible_metadata.description = f"An adorable {breed} pup(by BW)!"


