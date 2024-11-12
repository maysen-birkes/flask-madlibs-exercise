"""Madlibs Stories"""

class Story:
    """Madlibs story.
    
    Make a story, pass in a code, a title, a list of questions/prompts, and the text of the story template.

    >>> s = Story(
        ...     "short",
        ...     "A Short and Sweet Story",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, token, title, words, text):
        """Create story with words and template text."""

        self.token = token
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text
    

    # Stories

story1 = Story(
    "adventure",
    "A Day in the Life of a Superhero",
    ["adjective", "name", "verb", "place", "villain_name", "object", "superpower", "action_verb", "small_gift", "emotion", "verb_2"],
    """Today was a(n) {adjective} day for {name}. As soon as they woke up, they knew they had to {verb} to save the {place} from the evil {villain_name}! With their trusty {object} in hand, they raced to the scene.
    
    When they arrived, {name} used their incredible {superpower} to {action_verb} the villain's plan. The citizens of {place} cheered and thanked {name}, and one little child even gave them a {small_gift} as a token of appreciation.

    At the end of the day, {name} returned home, feeling {emotion} and ready to {verb_2} again tomorrow."""
)

story2 = Story(
    "vacation",
    "The Wild Vacation",
    ["name", "friend_name", "adjective", "place", "number", "plural_noun", "verb", "famous_landmark", "food", "adjective_2", "animal", "emotion", "object", "number_2", "adjective_3", "noun"],
    """Last summer, {name} and their best friend {friend_name} decided to take a(n) {adjective} vacation to {place}. They packed their bags with {number} pairs of {plural_noun} and set off early in the morning.

    When they arrived, the first thing they did was {verb} at the {famous_landmark}. Afterward, they tried some local {food} that tasted {adjective_2}!

    One of the most exciting parts of the trip was when {name} and {friend_name} encountered a {animal}. They were so {emotion} that they almost dropped their {object}!

    By the end of the vacation, they had collected {number_2} souvenirs, including a(n) {adjective_3} {noun} to remember their adventure. They couldn’t wait to tell everyone about their incredible trip to {place}!"""
)

stories = {s.token: s for s in [story1, story2]}