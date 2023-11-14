from typing import List


class StudentRecord:
    def __init__(self, id: int, score: int):
        self.id = id
        self.score = score

    def __gt__(self, other):
        if other.score > self.score:
            return False
        if other.score == self.score:
            return self.id < other.id
        return True

    def __repr__(self):
        return f"{self.id}"


def feedback_counter(student_id: int, positive, negative, report: str) -> StudentRecord:
    student = StudentRecord(student_id, 0)
    report_words = report.split(" ")
    for word in report_words:
        if word in positive:
            student.score += 3
        if word in negative:
            student.score -= 1
    return student


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:

        positive = set(positive_feedback)
        negative = set(negative_feedback)

        results = []
        for report, student_id in zip(report, student_id):
            score = feedback_counter(student_id, positive, negative, report)
            results.append(score)
        results.sort(reverse=True)
        return [
            r.id for r in results[:k]
        ]


if __name__ == '__main__':
    result = Solution().topStudents(["smart","brilliant","studious"], ["not"], ["this student is not studious","the student is smart"], [1, 2], 2)
    print(result)