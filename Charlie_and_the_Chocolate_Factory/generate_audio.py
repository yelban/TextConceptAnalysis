"""
Generate audio files for Charlie and the Chocolate Factory script.
Uses OpenAI TTS API with different voices for different characters.

Usage:
    export OPENAI_API_KEY=your-key
    uv run generate_audio.py
"""

from openai import OpenAI
from pathlib import Path

client = OpenAI()

# All script lines with character assignments
# Text is modified to be more expressive for children's theater style
LINES = [
    {"id": "01", "character": "both", "text": "A pleasant day, EVERYONE!"},
    {"id": "02", "character": "archie", "text": "My name is... ARCHIE!"},
    {"id": "03", "character": "mera", "text": "And MY name is... MERA!"},
    {
        "id": "04",
        "character": "archie",
        "text": "That was AMAZING! Grade 1 gave us shakes and wiggles this morning!",
    },
    {
        "id": "05",
        "character": "mera",
        "text": "YES, you're RIGHT, Archie! That was ENERGY!",
    },
    {
        "id": "06",
        "character": "archie",
        "text": "Well... to conclude this event, we will celebrate... one of Roald Dahl's FAMOUS children's books!",
    },
    {
        "id": "07",
        "character": "mera",
        "text": "And we will witness, on stage... the story of a young boy, who BELIEVES...",
    },
    {"id": "08", "character": "both", "text": "Nothing is IMPOSSIBLE!"},
    {
        "id": "09",
        "character": "mera",
        "text": "Ladies and gentlemen... we are PROUDLY present...",
    },
    {
        "id": "10",
        "character": "archie",
        "text": "Grades 4, 5, and 6... in the story of...",
    },
    {"id": "11", "character": "both", "text": "CHARLIE... and the CHOCOLATE FACTORY!"},
]

# Voice mapping for each character type
VOICES = {
    "archie": "echo",  # Young male voice (suitable for elementary school boy)
    "mera": "nova",  # Lively female voice
    "both": "alloy",  # Neutral voice for duet lines
}


def main():
    # Create audio directory
    audio_dir = Path("audio")
    audio_dir.mkdir(exist_ok=True)

    print("Generating audio files...")
    print("-" * 50)

    for line in LINES:
        voice = VOICES[line["character"]]
        output_path = audio_dir / f"{line['id']}.mp3"

        print(f"[{line['id']}] {line['character']:8} -> {voice:6} : {line['text'][:50]}...")

        response = client.audio.speech.create(
            model="tts-1-hd",
            voice=voice,
            input=line["text"],
            speed=0.9,  # Slightly slower for children's theater
        )
        response.stream_to_file(str(output_path))

    print("-" * 50)
    print(f"Done! Generated {len(LINES)} audio files in {audio_dir}/")


if __name__ == "__main__":
    main()
