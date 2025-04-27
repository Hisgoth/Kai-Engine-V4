
# KaiStoryBrain.py
# AI-driven dynamic story generation for Kai Engine V4
# Author: K. Hutton (Simon)

import random

class KaiStoryBrain:
    def __init__(self):
        # Optional setup if needed
        pass

    def generate_story(self, world_state, player_action):
        """Generates a story paragraph based on current world state and player action."""
        entropy = world_state.entropy
        loyalty = world_state.party_loyalty
        reputation = world_state.faction_reputation
        traits = world_state.player_traits

        # Build basic story structure
        intro = self.pick_intro(entropy, loyalty, reputation)
        middle = self.describe_action(player_action, traits)
        twist = self.pick_twist(entropy, loyalty)

        story_paragraph = f"{intro} {middle} {twist}"
        return story_paragraph

    def pick_intro(self, entropy, loyalty, reputation):
        """Create the atmospheric start based on world tension."""
        if entropy > 80:
            return "The colony trembles under collapsing infrastructure."
        elif reputation < 20:
            return "Hostile murmurs ripple across the broken settlement."
        elif loyalty < 30:
            return "Tension gnaws between the remaining survivors."
        else:
            return "The stale air carries the weight of forgotten hopes."

    def describe_action(self, player_action, traits):
        """Describe the player's chosen action with emotional tone."""
        empathy = traits.get("empathy", 50)
        resilience = traits.get("resilience", 50)

        if "search" in player_action.lower() or "explore" in player_action.lower():
            if resilience > 60:
                return "You push deeper into the abandoned sectors, unfazed by the cold silence."
            else:
                return "Every step into the ruins feels heavier, the dark pressing closer."
        elif "negotiate" in player_action.lower() or "talk" in player_action.lower():
            if empathy > 60:
                return "You choose your words carefully, hoping to salvage trust from wary eyes."
            else:
                return "Your offers sound hollow even to your own ears."
        elif "retreat" in player_action.lower() or "hide" in player_action.lower():
            return "You withdraw into the sheltering corridors, ears straining for pursuit."
        else:
            return "You act on instinct, driven by forces you barely understand."

    def pick_twist(self, entropy, loyalty):
        """Add a small final twist depending on current decay."""
        if entropy > 90:
            return "Somewhere in the shadows, something old and waiting stirs."
        elif loyalty < 25:
            return "Behind you, whispered doubts grow louder."
        else:
            return "The world holds its breath, waiting for your next move."
