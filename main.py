from ci_build import CIBuild
import simpy

f = open("data.csv", "w")
f.write("Pass Rate,Rebases,Wall Clock Time\n")
f.close()

def run_sim():
  for _ in range(1000):
    env = simpy.Environment()

    build = CIBuild(env)
    build.run()

    env.run()
    build.stats(env.now)

run_sim()



