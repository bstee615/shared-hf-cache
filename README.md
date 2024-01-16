# Shared HuggingFace cache

This is how we set up a shared HuggingFace cache.

# Set it up

Run `bash setup_shared_cache.sh`. It requires sudo permissions.

# Test it out

You can test it out by running the test program with two users at the same time.
When the model weights are downloading, user B will receive a file lock error (in order to avoid concurrency issues).
After user A downloaded the weights, user B can use them at the same time.

```bash
pip install -r requirements.txt
# Logged in as user A
python test_shared_cache.py
# In another terminal at the same time, logged in as user B
python test_shared_cache.py
```
