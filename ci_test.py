from random import randrange

class CITest(object):
  average_test_time = 5
  test_flake_rate = 0.001

  def __init__(self, env, build_tracker, name, ci_worker):
    self.env = env
    self.name = name
    self.build_tracker = build_tracker
    self.ci_worker = ci_worker

    self.action = env.process(self.run())

  def run(self):
    with self.ci_worker.request() as req:
      yield req
      yield self.env.timeout(self.average_test_time)

      if self.coin_flip(self.test_flake_rate):
        self.build_tracker.passed()
      else:
        self.build_tracker.failed()

      self.build_tracker.test_finished()

  def coin_flip(self, odds):
    flip = randrange(1000)

    return flip >= (odds * 1000)

