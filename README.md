# Compiled programming language

*Version 0.0.2*

Shard is a very small programming language in active development. It uses Python and PLY to generate C code.

## Last changes
- Division by zero handling
- C code generation
- Float numbers support

## Features
- Arithmetic operations

## Running
Create your Shard program and type the following command:

```bash
python3 path/to/shard.py -c your_program.shd    # you can use --compile instead of -c
```

## Preview
**Shard program**
```
3 * 5;
8 + (9 - 2);
```

**Generated C code**
```c
int main() {
  (3 * 5);
  (8 + ((9 - 2)));
   return 0;
}
```

## Contribution
To see how to contribute to the project, check out [the contributing guide](CONTRIBUTING.md)!
Thanks to report any issue, bug and problem. Don't forget to tell us about your suggestions (if you have some)!