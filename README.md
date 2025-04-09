# The Shard Programming Language

*Version 0.0.1*

Shard is a very small programming language in active development. It uses the C programming language and Flex & Bison.

## Installation
*The automatic installation support is only available on Linux-based systems.*

**Step 1**: clone this repository
```bash
git clone https://github.com/sharp-lang/sharp
```

**Step 2**: build the language
```bash
cd sharp
chmod +x build.sh
./build.sh
```

**Step 3**: complete the installation by running these commands as root
```bash
chmod +x install.sh
./install.sh
```

**Step 4**: create a program and run it!
```
59 + 12 * (-4 / 2);
```
```bash
sharp my_program.shd
```

## Features
Sharp...
- Handles different arithmetic operators: + - * and /
- Handles different arithmetic symbols: ( and )
- Handles negative expressions: -5
- Handles explicit positive expressions: +49
- Handles programs with several instructions: 1 + 1; 4* 2; 3 - 4;

## Contribution
To see how to contribute to the project, check out [the contributing guide](CONTRIBUTING.md)!
Thanks to report any issue, bug and problem. Don't forget to tell us about your suggestions (if you have some)!