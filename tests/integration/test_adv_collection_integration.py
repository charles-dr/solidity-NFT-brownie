from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_integration():
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    advanced_collectible, tx = deploy_and_create()
    print("Waiting...")
    time.sleep(60)
    # requestId = creation_tx.events["requestedCollectible"]["requestId"]
    # print(f"[requestId] {requestId} [address] {advanced_collectible.address}")
    # random_number = 777
    # tx = get_contract("vrf_coordinator").callBackWithRandomness(
    #     requestId, random_number, advanced_collectible.address, {"from": get_account()}
    # )
    print(f"TokenCounter: {advanced_collectible.tokenCounter()}")
    # Assert
    assert advanced_collectible.tokenCounter() > 0
    # assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
