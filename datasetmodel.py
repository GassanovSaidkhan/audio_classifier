import os
import librosa
import numpy as np
import torch.utils.data as data


class RAVDESSDataset(data.Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform

        self.audio_files = []
        self.labels = []

        for subdir, _, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.wav'):
                    self.audio_files.append(os.path.join(subdir, file))
                    self.labels.append(int(file[7:8]) - 1)  # Get emotion label

    def __len__(self):
        return len(self.audio_files)

    def __getitem__(self, idx):
        audio_path = self.audio_files[idx]
        waveform, sample_rate = librosa.load(audio_path, sr=None, mono=True)

        # Extract features
        mfcc = librosa.feature.mfcc(waveform, sample_rate, n_mfcc=13)
        spectral_centroid = librosa.feature.spectral_centroid(waveform, sample_rate)
        spectral_rolloff = librosa.feature.spectral_rolloff(waveform, sample_rate)
        chroma = librosa.feature.chroma_stft(waveform, sample_rate)

        features = np.concatenate((mfcc.flatten(), spectral_centroid.flatten(),
                                   spectral_rolloff.flatten(), chroma.flatten()))

        # Convert label to tensor
        label = torch.tensor(self.labels[idx], dtype=torch.long)

        if self.transform:
            features = self.transform(features)

        return features, label
