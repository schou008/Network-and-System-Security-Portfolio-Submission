import random
import time

TOTAL_HOSTS = 30

def propagate(attempts_per_cycle=3):
    infected = set([0])  # worm starts at host 0
    cycle = 0

    print("=== Worm Propagation Simulation ===\\n")
    print("Starting infection at host 0\\n")

    while len(infected) < TOTAL_HOSTS:
        new_infected = set()
        cycle += 1

        print(f"--- Cycle {cycle} ---")

        for host in sorted(infected):
            for _ in range(attempts_per_cycle):
                target = random.randint(0, TOTAL_HOSTS - 1)
                if target not in infected and target not in new_infected:
                    # simulate a vulnerable host found with 50% success
                    if random.random() < 0.5:
                        new_infected.add(target)

        infected.update(new_infected)

        print(f"Infected after cycle {cycle}: {sorted(infected)}\\n")
        time.sleep(0.5)

    print("All hosts infected.")

if __name__ == "__main__":
    propagate()