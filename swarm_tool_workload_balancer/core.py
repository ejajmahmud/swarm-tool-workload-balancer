"""Core Workload Balancer implementation."""
from typing import Dict, List, Optional

class WorkerNode:
    def __init__(self, worker_id: str, capacity: int = 10):
        self.worker_id = worker_id
        self.capacity = capacity
        self.active_jobs = 0
        self.healthy = True

class WorkloadBalancer:
    def __init__(self):
        self.workers: Dict[str, WorkerNode] = {}

    def register_worker(self, worker_id: str, capacity: int = 10):
        self.workers[worker_id] = WorkerNode(worker_id, capacity)

    def select_worker(self) -> Optional[str]:
        available = [w for w in self.workers.values() if w.healthy and w.active_jobs < w.capacity]
        if not available:
            return None
        # Least connection selection
        chosen = min(available, key=lambda w: w.active_jobs)
        chosen.active_jobs += 1
        return chosen.worker_id

    def release_worker(self, worker_id: str):
        if worker_id in self.workers and self.workers[worker_id].active_jobs > 0:
            self.workers[worker_id].active_jobs -= 1

    def mark_unhealthy(self, worker_id: str):
        if worker_id in self.workers:
            self.workers[worker_id].healthy = False
