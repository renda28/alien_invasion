class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings, store):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # Initialize all time high score if it exists.
        self.store = store
        try:
            high_score = store.read_high_score()
        except FileNotFoundError:
            print("File not found")
            self.high_score = 0
        else:
            self.high_score = int(high_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
