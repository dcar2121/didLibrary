# Transmission Signal Utility

import math
import time
import hashlib
from dataclasses import dataclass


class TransmissionSignalUtility:
    """Manage message counts and calculate transmission cost.

    The cost function is illustrative: a logarithmic factor times squared
    message_count to introduce diminishing/accelerating cost behavior.
    """
    def __init__(self):
        self.message_count = 0
        self.last_transmission_time = time.time()

    def calculate_cost(self) -> float:
        time_since_last = time.time() - self.last_transmission_time
        if self.message_count == 0:
            return 1.0
        return math.log(self.message_count + 1) * (self.message_count ** 2) / max(1.0, time_since_last)

    def transmit(self) -> float:
        cost = self.calculate_cost()
        self.message_count += 1
        self.last_transmission_time = time.time()
        return cost


def example_transmission():
    util = TransmissionSignalUtility()
    for _ in range(5):
        print("Cost:", util.transmit())


@dataclass
class SovereignSignal:
    """Simple wrapper for a sovereign seed/identity.

    Note: This module stores seeds in-memory only. Do NOT persist secrets
    to shared locations. Use HSM or secure keystores in production.
    """
    seed: str

    def id(self) -> str:
        """Derive a stable identifier from the seed (SHA256 hex)."""
        return hashlib.sha256(self.seed.encode("utf-8")).hexdigest()

    def verify_identity(self, claimant_seed: str) -> bool:
        """Verify a claimant by comparing derived identifiers.

        This is a placeholder for a cryptographic verification (e.g., sigs).
        """
        return self.id() == hashlib.sha256(claimant_seed.encode("utf-8")).hexdigest()


def example_sovereign():
    s = SovereignSignal(seed="example-seed-1234")
    print("Sovereign ID:", s.id())


if __name__ == "__main__":
    example_transmission()
    example_sovereign()
