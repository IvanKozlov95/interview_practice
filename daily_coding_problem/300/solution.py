from heapq import heappush, heapify

class FraudException(Exception):
  pass

class Candidate:
  def __init__(self, id):
    self._id = id
    self.votes = 0

  def __eq__(self, other):
    return self.votes == other.votes
  
  def __lt__(self, other):
    return self.votes < other.votes
  
  def __qt__(self, other):
    return self.votes > other.votes

class VotingMachine:
  def __init__(self):
    self.leaderboard = list()
    self.candidates = dict()
    self.voters = set()

  def add_vote(self, voter_id, candidate_id):
    if voter_id in self.voters:
      raise FraudException('Fraud by voter {}'.format(voter_id))
    self.voters.add(voter_id)

    if candidate_id not in self.candidates:
      candidate = Candidate(candidate_id)
      heappush(self.leaderboard, candidate)
      self.candidates[candidate_id] = candidate
    candidate = self.candidates[candidate_id]
    candidate.votes += 1

  def top(self):
    return [x._id for x in self.leaderboard[-3:]]

  def process_votes(self, votes):
    for (voter_id, candidate_id) in votes:
      self.add_vote(voter_id, candidate_id)

def process_all_votes(votes):
  vm = VotingMachine()
  vm.process_votes(votes)
  return vm.top()

solution = process_all_votes
testcase1 = {
  'input': {
    'votes': [
      (0, 0),
      (1, 1),
      (2, 0),
      (3, 1),
      (4, 2),
      (5, 2),
      (6, 2),
    ],
  },
  'expected': [2, 0, 1],
}
testcases = [testcase1]
