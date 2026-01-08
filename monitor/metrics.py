class APIMetrics:
    def __init__(self):
        self.total_checks = 0
        self.successful_checks = 0
        self.failure_streak = 0
        self.latencies = []

    def record(self, result: dict):
        self.total_checks += 1

        if result["success"]:
            self.successful_checks += 1
            self.failure_streak = 0
            if result["latency_ms"] is not None:
                self.latencies.append(result["latency_ms"])
        else:
            self.failure_streak += 1

    def uptime_percentage(self) -> float:
        if self.total_checks == 0:
            return 0.0
        return round((self.successful_checks / self.total_checks) * 100, 2)

    def average_latency(self):
        if not self.latencies:
            return None
        return round(sum(self.latencies) / len(self.latencies), 2)
