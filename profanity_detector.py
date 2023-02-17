import re

def calculate_profanity(tweet, racial_slurs):
    # Count the number of racial slurs in the tweet
    num_slurs = sum(1 for slur in racial_slurs if re.search(r"\b" + slur + r"\b", tweet, re.IGNORECASE))
    
    # Calculate the degree of profanity as a percentage of racial slurs in the tweet
    profanity_degree = (num_slurs / len(tweet.split())) * 100
    
    return profanity_degree

def main():
    # Load the set of racial slurs from a file
    with open("racial_slurs.txt", "r") as f:
        racial_slurs = set(line.strip() for line in f)
    
    # Read the tweets from a file and calculate the degree of profanity for each tweet
    with open("tweets.txt", "r") as f:
        for tweet in f:
            profanity_degree = calculate_profanity(tweet, racial_slurs)
            print(f"Tweet: {tweet.strip()} | Profanity degree: {profanity_degree}%")

if __name__ == "__main__":
    main()
    
