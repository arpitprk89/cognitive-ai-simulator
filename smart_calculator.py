# ============================================================
# Cognitive AI Simulator
# Author: Arpit Pareek | Shrimadhopur, Rajasthan, India
# GitHub: github.com/arpitprk89
#
# A rule-based system simulating three core aspects of
# human cognition:
#   1. Emotion Detection (sentiment analysis via keywords)
#   2. Memory Retention (context tracking across session)
#   3. Decision Analysis (response adaptation based on state)
# ============================================================

# ─────────────────────────────────────────────
# MODULE 1: EMOTION DETECTION
# Classifies user input as Positive, Negative, or Neutral
# using keyword-based sentiment mapping.
# ─────────────────────────────────────────────

POSITIVE_WORDS = [
    "happy", "great", "good", "love", "excited", "wonderful",
    "amazing", "fantastic", "joy", "excellent", "awesome",
    "glad", "cheerful", "motivated", "hopeful", "proud"
]

NEGATIVE_WORDS = [
    "sad", "bad", "hate", "angry", "frustrated", "terrible",
    "awful", "horrible", "depressed", "worried", "anxious",
    "upset", "stressed", "scared", "confused", "lost"
]

def detect_emotion(text):
    """
    Scans user input for sentiment keywords.
    Returns: emotion label and confidence score.
    """
    text_lower = text.lower()
    words = text_lower.split()

    positive_count = sum(1 for word in words if word in POSITIVE_WORDS)
    negative_count = sum(1 for word in words if word in NEGATIVE_WORDS)

    total = positive_count + negative_count

    if total == 0:
        return "Neutral", 0.5

    positive_ratio = positive_count / total

    if positive_ratio > 0.6:
        confidence = round(0.5 + (positive_ratio * 0.5), 2)
        return "Positive", confidence
    elif positive_ratio < 0.4:
        confidence = round(0.5 + ((1 - positive_ratio) * 0.5), 2)
        return "Negative", confidence
    else:
        return "Mixed", 0.5


# ─────────────────────────────────────────────
# MODULE 2: MEMORY RETENTION
# Tracks conversation history and user emotional
# patterns across the session.
# ─────────────────────────────────────────────

class SessionMemory:
    """
    Simulates short-term cognitive memory.
    Stores interaction history and detects emotional trends.
    """

    def __init__(self):
        self.history = []          # Full conversation log
        self.emotion_log = []      # Sequence of detected emotions
        self.user_name = None      # Remembered from first input

    def remember(self, user_input, emotion, response):
        self.history.append({
            "input": user_input,
            "emotion": emotion,
            "response": response
        })
        self.emotion_log.append(emotion)

    def get_dominant_emotion(self):
        """Returns the most frequent emotion in this session."""
        if not self.emotion_log:
            return "Neutral"
        return max(set(self.emotion_log), key=self.emotion_log.count)

    def get_turn_count(self):
        return len(self.history)

    def recall_last(self):
        """Returns the last interaction."""
        if self.history:
            return self.history[-1]
        return None

    def show_history(self):
        if not self.history:
            print("  No interactions recorded yet.")
            return
        print("\n  --- Session Memory Log ---")
        for i, entry in enumerate(self.history, 1):
            print(f"  [{i}] You: {entry['input']}")
            print(f"       Emotion: {entry['emotion']} | Response: {entry['response']}")
        print("  --------------------------\n")


# ─────────────────────────────────────────────
# MODULE 3: DECISION ANALYSIS
# Adapts system response based on detected emotion
# and session memory context — simulating basic
# human-like reasoning in response generation.
# ─────────────────────────────────────────────

def make_decision(emotion, memory):
    """
    Decision tree that selects a response strategy
    based on current emotion and past session context.
    """
    turn = memory.get_turn_count()
    dominant = memory.get_dominant_emotion()

    # Opening turn — no memory yet
    if turn == 0:
        if emotion == "Positive":
            return "You seem to be in a good state. Let's keep that going."
        elif emotion == "Negative":
            return "I notice some difficulty in what you've shared. I'm here to help."
        else:
            return "I'm listening. Tell me more about what's on your mind."

    # Subsequent turns — memory-aware decisions
    if emotion == "Positive":
        if dominant == "Negative":
            return "This is a shift — you seem better than earlier in our conversation."
        return "Consistent positive state detected. You're doing well."

    elif emotion == "Negative":
        if dominant == "Positive":
            return "Something seems to have changed. Earlier you seemed okay — what happened?"
        elif dominant == "Negative":
            return "You've been in a difficult state throughout. Consider talking to someone you trust."
        return "I can sense this is hard. Take your time."

    elif emotion == "Mixed":
        return "Your thoughts seem mixed right now. That's okay — complexity is part of thinking."

    else:
        return "Understood. I'm processing what you've shared."


# ─────────────────────────────────────────────
# MAIN INTERFACE
# Ties all three modules together into an
# interactive cognitive simulation loop.
# ─────────────────────────────────────────────

def display_header():
    print("\n" + "=" * 55)
    print("   COGNITIVE AI SIMULATOR — by Arpit Pareek")
    print("   Emotion Detection | Memory | Decision Analysis")
    print("=" * 55)
    print("  Type 'memory' to view session log")
    print("  Type 'status' to see your emotional pattern")
    print("  Type 'exit' to end the session")
    print("=" * 55 + "\n")


def main():
    display_header()
    memory = SessionMemory()

    # Greet and remember name
    name = input("  Before we begin — what's your name? ").strip()
    if name:
        memory.user_name = name
        print(f"\n  Hello, {name}. This system will track your emotional state")
        print("  and adapt its responses based on what you share.\n")

    while True:
        user_input = input(f"  {memory.user_name or 'You'}: ").strip()

        if not user_input:
            continue

        # Special commands
        if user_input.lower() == "exit":
            dominant = memory.get_dominant_emotion()
            print(f"\n  Session ended after {memory.get_turn_count()} interactions.")
            print(f"  Your dominant emotional state this session: {dominant}")
            print(f"  Thank you, {memory.user_name or 'friend'}. Take care.\n")
            break

        elif user_input.lower() == "memory":
            memory.show_history()
            continue

        elif user_input.lower() == "status":
            dominant = memory.get_dominant_emotion()
            turns = memory.get_turn_count()
            print(f"\n  Turns so far: {turns}")
            print(f"  Dominant emotion this session: {dominant}\n")
            continue

        # Core pipeline: Detect → Decide → Remember
        emotion, confidence = detect_emotion(user_input)
        response = make_decision(emotion, memory)
        memory.remember(user_input, emotion, response)

        # Output
        print(f"\n  [Emotion Detected: {emotion} | Confidence: {confidence}]")
        print(f"  System: {response}\n")


if __name__ == "__main__":
    main()
