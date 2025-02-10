# Sticklight Python SDK

The official Python SDK for [Sticklight](https://sticklight.io) - the <...>

## Installation

```bash
pip install sticklight-python
```

## Quick Start

```python
import sticklight_python as sl

# Publish an event
sl.capture({
    "event": "user_message",
    "user_id": "user_123",
    "message": "Help me with <...>",
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

To get your API key, go to the [Sticklight dashboard](https://app.sticklight.io/settings/api-keys) and create a new key.

## Requirements

- Python 3.11 or higher

## About Sticklight

Sticklight provides <...> for <...>, giving product managers and developers <value prop>. Our platform helps you:

- <...>
- <...>
- <...>

## License

MIT

## Support

- Documentation: [docs.sticklight.io](https://docs.sticklight.io)
- Issues: [GitHub Issues](https://github.com/sticklight/sticklight-python/issues)
- Email: support@sticklight.io
