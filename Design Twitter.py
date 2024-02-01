# Design Twitter
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
# code

class Twitter:
  def __init__(self):
    # Use itertools.count to generate a decreasing sequence of integers for tweets
    self.timer = itertools.count(step=-1)
    # Use defaultdict and deque to store tweets for each user
    self.tweets = collections.defaultdict(deque)
    # Use defaultdict and set to store followees for each user
    self.followees = collections.defaultdict(set)

  def postTweet(self, userId: int, tweetId: int) -> None:
    # Append the tweet to the left of the deque for the user, along with its timestamp
    self.tweets[userId].appendleft((next(self.timer), tweetId))
    # If the deque for the user has more than 10 tweets, remove the oldest tweet from the right
    if len(self.tweets[userId]) > 10:
      self.tweets[userId].pop()

  def getNewsFeed(self, userId: int) -> List[int]:
    # Merge the tweets of the user's followees (including the user) using heapq.merge
    tweets = list(heapq.merge(
        *(self.tweets[followee] for followee in self.followees[userId] | {userId})))
    # Return the tweet IDs of the 10 most recent tweets
    return [tweetId for _, tweetId in tweets[:10]]

  def follow(self, followerId: int, followeeId: int) -> None:
    # Add the followee to the set of followees for the follower
    self.followees[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    # Remove the followee from the set of followees for the follower (if the followee exists)
    self.followees[followerId].discard(followeeId)