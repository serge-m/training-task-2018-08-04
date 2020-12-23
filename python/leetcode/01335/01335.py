"""
1335. Minimum Difficulty of a Job Schedule


t = 50min
c = hard

1. cur job depends on all previos
2. at least 1 task per day
3. diff(schedule) = sum of difficulty(day)
4. diff(day) = max(diff(jobs of that day))

find minimum difficulty of a schedule
or return -1 if one cannot find a schedule

"""
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # return find(jobDifficulty, len(jobDifficulty), d)
        no_schedule = -1
        jobs = jobDifficulty
        n = len(jobs)
        t = [
            [no_schedule for _ in range(n + 1)]
            for _ in range(d + 1)
        ]

        t[0][0] = 0
        for di in range(1, d + 1):
            for num_jobs in range(1, n + 1):
                cost_schedule_best = no_schedule
                cost_today = None
                for jobs_to_take_today in range(1, num_jobs + 1):
                    cur_job_cost = jobs[num_jobs - jobs_to_take_today]
                    if cost_today is None or cur_job_cost > cost_today:
                        cost_today = cur_job_cost

                    jobs_left = num_jobs - jobs_to_take_today
                    if jobs_left < 0:
                        continue
                    cost_prev = t[di - 1][jobs_left]

                    if cost_prev == no_schedule:
                        continue  # no schedule

                    cost_schedule = cost_today + cost_prev
                    if cost_schedule_best == no_schedule or cost_schedule_best > cost_schedule:
                        cost_schedule_best = cost_schedule
                t[di][num_jobs] = cost_schedule_best

        return t[d][n]


def test_1():
    assert Solution().minDifficulty([186, 398, 479, 206, 885, 423, 805, 112, 925, 656, 16, 932, 740, 292, 671, 360], 4) == 1803
