
# KaiInterface.py
# Main game loop connecting world, story, choices, memory
# Author: K. Hutton (Simon)

from Prototype.KaiWorldState import KaiWorldState
from Prototype.KaiStoryBrain import KaiStoryBrain
from Prototype.KaiChoiceBrain import KaiChoiceBrain
from Prototype.KaiMemoryEngine import KaiMemoryEngine

class KaiInterface:
    def __init__(self):
        self.world = KaiWorldState()
        self.story_brain = KaiStoryBrain()
        self.choice_brain = KaiChoiceBrain()
        self.memory = KaiMemoryEngine()

    def start_game(self):
        print("🌌 Welcome to Kai Engine V4 - AI-Driven Narrative Simulation 🌌\n")
        while True:
            # Present world summary
            self.display_world_state()

            # Ask player for a free-text action
            player_action = input("\nWhat would you like to do? > ").strip()

            # Log player action
            self.memory.log_event(f"Player action: {player_action}")

            # World reacts (basic simulation)
            self.world.advance_years(1)
            self.world.update_entropy(1)

            # Generate story based on action and world
            story = self.story_brain.generate_story(self.world, player_action)
            print(f"\n📝 Story: {story}\n")

            # Offer dynamic choices for next step
            dynamic_choices = self.choice_brain.generate_choices(self.world)
            print("Available actions:")
            for number, choice in dynamic_choices:
                print(f"[{number}] {choice}")

            # Ask player to select next action (optional)
            next_choice = input("\nChoose an option by number, or type your own action: ").strip()

            # If valid menu choice, inject it as next player action
            if next_choice in [num for num, _ in dynamic_choices]:
                player_action = dict(dynamic_choices)[next_choice]
                self.memory.log_event(f"Selected option: {player_action}")
                continue  # Loop continues naturally
            else:
                self.memory.log_event(f"Typed custom action: {next_choice}")

            # If typed something custom, treat it as free action
            if next_choice.lower() in ["quit", "exit"]:
                print("\n🌌 Thank you for playing Kai Engine V4. Simulation closed. 🌌")
                break

    def display_world_state(self):
        summary = self.world.summary()
        print("--- World State ---")
        for key, value in summary.items():
            print(f"{key}: {value}")
