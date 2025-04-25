from music_recommender import MusicRecommender

def main():
    
    recommender = MusicRecommender()
    
    
    print("Available songs in the database:")
    all_songs = recommender.get_all_songs()
    for song in all_songs:
        print(f"- {song['title']} by {song['artist']} ({song['genre']})")
    
    print("\n=== Music Recommendation Demo ===")
    
    

    user_input=input("enter the song name")
    song_title = user_input
    print(f"\nGetting recommendations for '{song_title}':")
    recommendations = recommender.get_recommendations(song_title, n_recommendations=3)
    
    if isinstance(recommendations, list):
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['title']} by {rec['artist']}")
            print(f"   Genre: {rec['genre']}")
            print(f"   Similarity Score: {rec['similarity_score']}%")
    else:
        print(recommendations)
    
    
    print("\nAdding a new song to the database...")
    result = recommender.add_song(
        title="New Song",
        artist="New Artist",
        genre="pop",
        popularity=85,
        energy=0.7,
        danceability=0.8
    )
    print(result)
    
    
    print("\nGetting recommendations for the new song:")
    recommendations = recommender.get_recommendations("New Song", n_recommendations=3)
    
    if isinstance(recommendations, list):
        for i, rec in enumerate(recommendations, 1):
            print(f"\n{i}. {rec['title']} by {rec['artist']}")
            print(f"   Genre: {rec['genre']}")
            print(f"   Similarity Score: {rec['similarity_score']}%")
    else:
        print(recommendations)

if __name__ == "__main__":
    main() 