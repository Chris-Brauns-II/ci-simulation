from random import randrange

class CITest(object):
  average_test_time = 5
  test_flake_rate = 0.001

  def __init__(self, env, ci_worker):
    self.env = env
    self.ci_worker = ci_worker

    self.action = env.process(self.run())

  def run(self):
    passed = False

    with self.ci_worker.request() as req:
      yield req
      yield self.env.timeout(average_test_time)

      passed = self.coin_flip(test_flake_rate)
      if passed == True:
        global total_passes
        print("Test passed")
        total_passes += 1
      else:
        global total_failures
        total_failures += 1

  def coin_flip(odds):
    flip = randrange(1000)

    print("Flip: %d, Odds: %d, Result: %d" % (flip, odds, (flip >= (odds * 1000))))
    flip >= (odds * 1000)

