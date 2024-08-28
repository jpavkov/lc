# https://leetcode.com/problems/video-stitching/description/

class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:

        movies = [-1] * time
        count = 0

        for clip in clips:
            for i in range(clip[0], clip[1]):
                if i < time:
                    movies[i] = max(clip[1], movies[i])

        location = 0

        while location != -1 and location < time:
            location = movies[location]
            count += 1

        if location >= time:
            return count

        return -1

        # print(list(range(0, time)))
        # print(movies)


sol = Solution()
clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
time = 10
print(sol.videoStitching(clips, time))

clips = [[0, 1], [1, 2]]
time = 5
print(sol.videoStitching(clips, time))

clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [
    1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]]
time = 9
print(sol.videoStitching(clips, time))
