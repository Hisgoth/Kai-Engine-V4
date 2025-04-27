
# KaiChoiceBrain.py
# AI-driven dynamic choice generation for Kai Engine V4
# Author: K. Hutton (Simon)

import random

class KaiChoiceBrain:
    def __init__(self):
        self.themes = {
            "collapse": [
                "Reinforce the east airlock before full collapse.",
                "Abandon unstable sectors to preserve oxygen.",
                "Send a distress signal into deep orbit.",
                "Lead an exodus toward uncharted zones."
            ],
            "betrayal": [
                "Confront your party about rising tensions.",
                "Assign secret watchers to monitor loyalty.",
                "Offer desperate incentives for loyalty."
            ],
            "hostility": [
                "Organize a strike against enemy factions.",
                "Negotiate under threat of complete collapse.",
                "Sabotage rival supply lines covertly."
            ],
            "struggle": [
                "Scavenge hidden tunnels for forgotten supplies.",
                "Strengthen defenses against the coming storm.",
                "Seek out lost allies among scattered settlers."
            ]
        }

    def pick_theme(self, entropy, loyalty, reputation):
        """Choose the world crisis theme based on tension."""
        if entropy >= 70:
            return "collapse"
        elif loyalty <= 30:
            return "betrayal"
        elif reputation <= 20:
            return "hostility"
        else:
            return "struggle"

    def generate_choices(self, world_state):
        """Generate 2-4 dynamic next actions based on current world tension."""
        theme = self.pick_theme(
            world_state.entropy,
            world_state.party_loyalty,
            world_state.faction_reputation
        )

        possible_actions = self.themes.get(theme, [])
        if not possible_actions:
            return []

        selected_actions = random.sample(possible_actions, k=min(3, len(possible_actions)))

        option_list = []
        for idx, action in enumerate(selected_actions, start=1):
            option_list.append((str(idx), action))

        return option_list
