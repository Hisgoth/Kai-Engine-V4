
# KaiMemoryEngine.py
# Tracks player actions and key world events for evolving narrative memory
# Author: K. Hutton (Simon)

class KaiMemoryEngine:
    def __init__(self):
        self.memory_log = []  # Stores chronological record of major events
        self.traits_drift = {}  # Optional: stores historical trait changes
        self.major_flags = {}   # Stores major turning points ("Betrayal Risk", "Colony Collapse Imminent")

    def log_event(self, event_description):
        """Adds an event description to the memory log."""
        self.memory_log.append(event_description)

    def log_trait_shift(self, trait_name, old_value, new_value):
        """Record major trait drift if needed for future narrative references."""
        if trait_name not in self.traits_drift:
            self.traits_drift[trait_name] = []
        self.traits_drift[trait_name].append((old_value, new_value))

    def set_major_flag(self, flag_name, value=True):
        """Set a major world or character turning point."""
        self.major_flags[flag_name] = value

    def get_summary(self):
        """Returns a snapshot of memory for story engine reference."""
        return {
            "Memory Log": self.memory_log,
            "Trait Drift": self.traits_drift,
            "Major Flags": self.major_flags
        }
