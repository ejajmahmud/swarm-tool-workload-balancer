"""Tests for WorkloadBalancer."""
import unittest
from swarm_tool_workload_balancer.core import WorkloadBalancer

class TestWorkloadBalancer(unittest.TestCase):
    def test_least_connection_distribution(self):
        wb = WorkloadBalancer()
        wb.register_worker("w1", capacity=5)
        wb.register_worker("w2", capacity=5)

        s1 = wb.select_worker()
        s2 = wb.select_worker()
        self.assertNotEqual(s1, s2)  # Should balance across both

    def test_unhealthy_worker_skip(self):
        wb = WorkloadBalancer()
        wb.register_worker("w1", capacity=5)
        wb.mark_unhealthy("w1")
        self.assertIsNone(wb.select_worker())
