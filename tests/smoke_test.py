"""Check that basic features work.

Catch cases where e.g. files are missing so the import doesn't work. It is
recommended to check that e.g. assets are included."""

from trusted_publishing_examples import hello

message = hello(101)
if message == "Hello 5050!":
    print("Smoke test succeeded")
else:
    raise RuntimeError(message)
