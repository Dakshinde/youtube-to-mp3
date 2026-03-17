import librosa
import os
import shutil

def sort_by_bpm(source_dir, workout_dir, study_dir):
    for file in os.listdir(source_dir):
        if file.endswith(".mp3"):
            path = os.path.join(source_dir, file)
            # Load the audio file
            y, sr = librosa.load(path)
            # AI detects the tempo (BPM)
            tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
            
            print(f"Song: {file} | Detected BPM: {tempo:.2f}")
            
            # Categorize based on energy level
            if tempo > 120:
                shutil.move(path, os.path.join(workout_dir, file))
            else:
                shutil.move(path, os.path.join(study_dir, file))

if __name__ == "__main__":
    os.makedirs("music/workout", exist_ok=True)
    os.makedirs("music/study", exist_ok=True)
    sort_by_bpm("music/raw", "music/workout", "music/study")