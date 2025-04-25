import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

class MusicRecommender:
    def __init__(self):
        
        self.music_data = {
            'song_id': range(1, 11),
            'title': [
                'Shape of You', 'Blinding Lights', 'Dance Monkey', 
                'Sunflower', 'Bad Guy', 'Watermelon Sugar', 
                'Don\'t Start Now', 'Circles', 'Someone You Loved',
                'Memories'
            ],
            'artist': [
                'Ed Sheeran', 'The Weeknd', 'Tones and I',
                'Post Malone', 'Billie Eilish', 'Harry Styles',
                'Dua Lipa', 'Post Malone', 'Lewis Capaldi',
                'Maroon 5'
            ],
            'genre': [
                'pop', 'synth-pop', 'dance-pop',
                'hip-hop', 'electropop', 'pop',
                'disco', 'hip-hop', 'pop',
                'pop'
            ],
            'popularity': [
                95, 90, 85, 88, 87, 89, 86, 84, 88, 82
            ],
            'energy': [
                0.825, 0.730, 0.859, 0.522, 0.701, 0.548,
                0.793, 0.695, 0.405, 0.615
            ],
            'danceability': [
                0.931, 0.514, 0.824, 0.755, 0.701, 0.548,
                0.793, 0.695, 0.405, 0.615
            ]
        }
        
        self.df = pd.DataFrame(self.music_data)
        self.feature_columns = ['popularity', 'energy', 'danceability']
        
        
        scaler = MinMaxScaler()
        self.df[self.feature_columns] = scaler.fit_transform(self.df[self.feature_columns])
        
        
        self.similarity_matrix = cosine_similarity(self.df[self.feature_columns])

    def get_recommendations(self, song_title, n_recommendations=3):
        """
        Get music recommendations based on a song title
        """
        try:
            
            idx = self.df[self.df['title'].str.lower() == song_title.lower()].index[0]
            
            
            similarity_scores = list(enumerate(self.similarity_matrix[idx]))
            
            
            similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
            
            
            similar_songs = similarity_scores[1:n_recommendations+1]
            
            recommendations = []
            for i, score in similar_songs:
                recommendations.append({
                    'title': self.df.iloc[i]['title'],
                    'artist': self.df.iloc[i]['artist'],
                    'genre': self.df.iloc[i]['genre'],
                    'similarity_score': round(score * 100, 2)
                })
            
            return recommendations
        
        except IndexError:
            return f"Song '{song_title}' not found in the database."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def add_song(self, title, artist, genre, popularity, energy, danceability):
        """
        Add a new song to the dataset
        """
        new_song = {
            'song_id': max(self.df['song_id']) + 1,
            'title': title,
            'artist': artist,
            'genre': genre,
            'popularity': popularity,
            'energy': energy,
            'danceability': danceability
        }
        
        self.df = pd.concat([self.df, pd.DataFrame([new_song])], ignore_index=True)
        
        
        scaler = MinMaxScaler()
        self.df[self.feature_columns] = scaler.fit_transform(self.df[self.feature_columns])
        self.similarity_matrix = cosine_similarity(self.df[self.feature_columns])
        
        return "Song added successfully!"

    def get_all_songs(self):
        """
        Get all songs in the database
        """
        return self.df[['title', 'artist', 'genre']].to_dict('records') 