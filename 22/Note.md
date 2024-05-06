### Backtrack

- The idea is to add `')'` only after valid `'('`
- We use two integer variables `left` & `right` to see how many `'('` & `')'` are in the current string
- If `left < n` then we can add `'('` to the current string
- If `right < left` then we can add `')'` to the current string