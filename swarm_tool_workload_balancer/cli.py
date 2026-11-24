"""CLI for Workload Balancer."""
import argparse
from .core import WorkloadBalancer

def main():
    parser = argparse.ArgumentParser(description="Swarm Tool Workload Balancer CLI")
    parser.add_argument("--demo", action="store_true", help="Run load balancer demo")
    args = parser.parse_args()

    wb = WorkloadBalancer()
    wb.register_worker("worker-1", 5)
    wb.register_worker("worker-2", 5)

    w_a = wb.select_worker()
    w_b = wb.select_worker()
    print(f"Dispatched job 1 to {w_a}, job 2 to {w_b}")

if __name__ == "__main__":
    main()
