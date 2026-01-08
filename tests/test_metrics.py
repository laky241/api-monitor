from monitor.metrics import APIMetrics

def test_uptime_calculation():
    m = APIMetrics()
    m.record({"success": True, "latency_ms": 100})
    m.record({"success": False, "latency_ms": None})

    assert m.uptime_percentage() == 50.0

def test_failure_streak():
    m = APIMetrics()
    m.record({"success": False, "latency_ms": None})
    m.record({"success": False, "latency_ms": None})

    assert m.failure_streak == 2
