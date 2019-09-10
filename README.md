# Knuth-Bendix algorithm for monoids

Small utility for computing word rewriting systems for a given monoid presentation.

Based on [wikipedia article on Knuth-Bendix in monoids](https://en.wikipedia.org/wiki/Knuth%E2%80%93Bendix_completion_algorithm)

## Usage
Running
```
python knuth_bendix.py $INPUT_FILE
```
will produce a list of rules to standard output. Rules are read from left to right.

There is also a utility for generating Coxeter presentation of $S_n$. Running
```
python generate_Sn_presentation.py $DIM
```
will produce a
```
S{$DIM}_presentation.json
```
file with appropriate description.


## Examples

Example input file, for $S_5$ as a Coxeter group:
```json
{
    "N": 5, 
    "relations": 
    [
        [[0, 0], []],
        [[1, 1], []],
        [[2, 2], []],
        [[3, 3], []],
        [[4, 4], []],
        [[3, 1], [1, 3]],
        [[4, 1], [1, 4]],
        [[4, 2], [2, 4]],
        [[1, 2, 1], [2, 1, 2]],
        [[2, 3, 2], [3, 2, 3]],
        [[3, 4, 3], [4, 3, 4]]
    ]
}
```

Examples are in the `examples/` directory:
  - `S5_presentation.json` - the file above.
  - `two_element_monoid.json` - representation of a monoid given by
  ```<x,y, xxx=yyy=xyxyxy=1>```, from the wikipedia article. The system of rewriting rules is:
    ```
    yyy -> 1
    xxx -> 1
    yxyx -> xxyy
    xyxy -> yyxx
    ```
  - `free_abelian_presentation_terminating.json` - as the name says
  - `free_abelian_presentation_nonterminating.json` - an example on how order on words can make Knuth-Bendix fail to terminate.
  
