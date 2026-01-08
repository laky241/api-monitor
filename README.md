# API Failure & Latency Monitoring Tool

## TL;DR
A lightweight API monitoring system that tracks uptime, latency,
and failure streaks, with structured logging and alerting.

## Why this exists
Modern systems depend on third-party APIs. This tool simulates
how backend teams monitor reliability and detect outages early.

## Features
- API uptime percentage
- Response latency tracking
- Failure streak detection
- Config-driven monitoring
- Structured logging
- Live dashboard

## Architecture
- `monitor/` → core monitoring logic
- `dashboard/` → visualization
- `tests/` → deterministic tests

### Design decisions
- Config-based APIs
- In-memory metrics for simplicity
- Threshold-based alerts to avoid noise
- Logging-first observability

### Limitations
- Metrics are not persisted
- Single-process monitoring
- Not a replacement for Prometheus or Datadog

## Future improvements
- Persistent storage
- Email / Slack alerts
- Visualization charts

## How to run
```bash
pip install -r requirements.txt
pytest
python -c "from monitor.runner import start_monitoring; start_monitoring()"
streamlit run dashboard/app.py

