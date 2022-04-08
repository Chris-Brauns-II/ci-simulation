import simpy

from random import randrange

from ci_test import CITest

class CIBuild(object):
  number_of_tests_to_run = 1000
  ci_workers = 1
  flakey_retry_rate = 0.5

  def __init__(self, env):
    self.env = env
    self.passes = 0
    self.failures = 0
    self.rebases = 0
    self.tests_finished = 0
    self.resource = simpy.Resource(self.env, capacity=self.ci_workers)
  
  def failed(self):
    self.failures += 1

  def passed(self):
    self.passes += 1

  def stats(self, now):
    # print("Passes: %d, Failures: %d" % (self.passes, self.failures))
    f = open("data.csv", "a")
    pass_rate = self.passes / (self.failures + self.passes)
    f.write("%f,%d,%f\n" % (pass_rate, self.rebases, now))
    f.close()

  def test_finished(self):
    self.tests_finished +=1 

    if self.tests_finished == self.number_of_tests_to_run:
      if self.failures > 0:
        if self.coin_flip(self.flakey_retry_rate):
          self.rebases += 1
          # self.passes = 0
          # self.failures = 0
          self.tests_finished = 0
          self.run()


  def run(self):
    for i in range(self.number_of_tests_to_run):
      CITest(self.env, self, 'Test %d' % (i), self.resource)

  def coin_flip(self, odds):
    flip = randrange(1000)

    return flip >= (odds * 1000)


