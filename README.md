# Sticklight Python SDK

The official Python SDK for [Sticklight](https://sticklight.io).

## Installation

```sh
pip install sticklight
# OR
uv add sticklight
```

## Quick Start

```python
import sticklight as sl

# Authenticate with your API key
sl.init("your-api-key")

# Publish an event
sl.capture(
    "user_sent_message",
    user_id="user_123",
    message="I need help with your new feature",
)
```

## Authentication

You'll need a Sticklight API key to use this SDK. You can either:

1. Set it as an environment variable:
   ```sh
   export STICKLIGHT_API_KEY="your-api-key"
   ```

2. Use `init` to authenticate at the start of your application:
   ```python
   sl.init("your-api-key")
   ```

To get your API key, go to the [Sticklight Platform] and create a new key.

## Requirements

- Python 3.11 or higher

## About Sticklight

Sticklight provides precise and actionable analytics for AI-powered products, giving product managers and developers deep insights into how users interact with their AI features. Our platform helps you:

- Understand user patterns and behaviors in LLM interactions
- Identify where users struggle and detect critical issues in real-time
- Make data-driven decisions for your AI product roadmap

Think of it as product analytics, but specifically designed for the unique challenges of AI applications. Whether you're running a support chatbot, internal agentic architecture, or any other LLM-oriented product, Sticklight instills deep confidence and clarity in your product decisions.

## Development

```sh
# Clone the repository
git clone https://github.com/sticklight-io/sticklight-python.git
cd sticklight-python

# Install dependencies
uv sync --dev

# Run tests
uv run scripts/test

# Publish to PyPI
uv run scripts/manual-publish
```

## License

Apache 2.0

## Support

- Documentation: [docs.sticklight.io](https://docs.sticklight.io)
- Issues: [GitHub Issues](https://github.com/sticklight-io/sticklight-python/issues)
- Email: support@sticklight.io
- [Book a demo](https://calendly.com/matan-sticklight/30min)

[Sticklight Platform]: https://platform.sticklight.io
