class RoyaltyTracker:
    def __init__(self):
        self.creators = {}
        self.royalties = {}

    def add_creator(self, creator_name):
        self.creators[creator_name] = 0
        self.royalties[creator_name] = []

    def record_sale(self, creator_name, amount):
        if creator_name in self.creators:
            self.creators[creator_name] += amount
            self.royalties[creator_name].append(amount)
        else:
            raise ValueError("Creator not found.")

    def get_total_royalties(self, creator_name):
        if creator_name in self.creators:
            return self.creators[creator_name]
        else:
            raise ValueError("Creator not found.")

    def get_royalty_history(self, creator_name):
        if creator_name in self.royalties:
            return self.royalties[creator_name]
        else:
            raise ValueError("Creator not found.")

# Example usage
tracker = RoyaltyTracker()
tracker.add_creator("Alice")
tracker.record_sale("Alice", 100)
tracker.record_sale("Alice", 150)

print("Total royalties for Alice:", tracker.get_total_royalties("Alice"))
print("Royalty history for Alice:", tracker.get_royalty_history("Alice"))
