# Sticklight Python SDK

The official Python SDK for [Sticklight](https://sticklight.io) - the analytics platform built for LLM-powered applications.

## Installation

```bash
pip install sticklight-python
```

## Quick Start

```python
import sticklight_python as sl

# Publish an event
sl.capture({
    "event": "llm_response",
    "model": "gpt-4",
    "prompt_tokens": 150,
    "completion_tokens": 50,
    "latency_ms": 2500,
    "user_id": "user_123"
})
```

## Authentication

You'll need a Sticklight API key to use this SDK. You can either:

1. Set it as an environment variable:
   ```bash
   export STICKLIGHT_API_KEY="your-api-key"
   ```

2. Pass it directly to the capture function:
   ```python
   sl.capture(data, sticklight_api_key="your-api-key")
   ```

## Requirements

- Python 3.11 or higher
- `requests` library (automatically installed)

## About Sticklight

Sticklight provides analytics and monitoring for LLM-powered applications, giving product managers and developers the insights they need to build better AI products. Our platform helps you:

- Track and analyze LLM usage patterns
- Monitor performance and costs
- Understand user interactions
- Make data-driven decisions about your AI features

## License

MIT

## Support

- Documentation: [docs.sticklight.io](https://docs.sticklight.io)
- Issues: [GitHub Issues](https://github.com/sticklight/sticklight-python/issues)
- Email: support@sticklight.io
