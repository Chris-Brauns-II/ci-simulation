import simpy

number_of_simulations_to_run = 1

ci_workers = 1
number_of_tests_to_run = 1000

failure_rebase_rate = 0.2

global total_failures
global total_passes

f = open("data.csv", "w")
f.write("Pass Rate,Wall Clock Time\n")

def ci_test(env, name, ci_worker):
  passed = False

  with ci_worker.request() as req:
    yield req
    yield env.timeout(average_test_time)

    passed = coin_flip(test_flake_rate)
    if passed == True:
      global total_passes
      print("Test passed")
      total_passes += 1
    else:
      global total_failures
      total_failures += 1

def run_build():
  env = simpy.Environment()
  ci_worker = simpy.Resource(env, capacity=ci_workers)

  global total_passes
  global total_failures
  total_passes = 0
  total_failures = 0

  for i in range(number_of_tests_to_run):
    env.process(ci_test(env, 'Test %d' % i, ci_worker))
  env.run()

  pass_rate = (float(total_passes) / float(total_passes + total_failures))
  f.write("%f,%d\n" % (pass_rate, env.now))

def run_sim():
  run_build()

for i in range(number_of_simulations_to_run):
  run_build()



