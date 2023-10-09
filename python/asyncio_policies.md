# First things first: Theory
- event loop policy is a global object used to get / set the current event loop
- by default, policy object get / set a separate event loop per context

# References:
- https://docs.python.org/3/library/asyncio-policy.html#custom-policies