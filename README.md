# Robot Circle Problem

## Solution logic
Since the robot can only turn in 90° parts, if the robot doesn't return to its origin in 1,2 or 4 executions of its command it is then deviating, and therefore cannot remain within a defined circle after infinity executions.

## Program logic
The script models the 2D environment and simulates the robots movements for up to 4 executions of its commands. If its simulated position returns to its origin (0,0) the program returns "YES" indicating that its path can be confined within a circle after infinity executions.

## Code
Pass a single command  string into the `isCircle` function: and it will return "YES" if it can be confined by a circle after infinity executions or "NO" if it can’t.

```python
command = "RLGGR"
output = isCircle(command)
print(output) # prints YES
```
