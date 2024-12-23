from pydub import AudioSegment
import sys
import glob
import os


def convert(mp3_path: str, wav_path: str):
    """
    Convert an MP3 file to a WAV file.

    Args:
        mp3_path (str): The path to the MP3 file.
        wav_path (str): The path to save the WAV file.
    """
    # Load the MP3 file
    mp3 = AudioSegment.from_mp3(mp3_path)

    # Export the MP3 file as a WAV file
    mp3.export(wav_path, format="wav")
    print(f"Converted {mp3_path} to {wav_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_mp3_to_wav.py <mp3_path_folder> <wav_path_folder>")
        sys.exit(1)

    mp3_folder = sys.argv[1]
    wav_path_folder = sys.argv[2]
    print(f"Converting MP3 files in {mp3_folder} to WAV files in {wav_path_folder}")

    # Create output folder if it does not
    if not os.path.exists(wav_path_folder):
        os.makedirs(wav_path_folder)

    # Get all MP3 files in the given folder
    mp3_files = glob.glob(f"{mp3_folder}/*.mp3")

    for mp3_source in mp3_files:
        wav_destiny = f"{wav_path_folder}/{os.path.basename(mp3_source).replace('.mp3', '.wav')}"
        convert(mp3_source, wav_destiny)
    
    print(f"Conversion completed! {len(mp3_files)} files converted.")