# **header42**

42 (Paris)

### **Description**

42 standard header rewritten as a python script 
and working with stdin/stdout so I can use it as 
a custom formatter chain in Helix editor.

![42 header](img/42header.jpg)

### **UNIX Setup**

#### Option 1: export USER and MAIL in your shell configuration file

Add in `~/.zshrc` your:

+ `USER`
+ `MAIL`

### **Usage**

```bash
$ nix-build -E 'with import <nixpkgs> {}; callPackage ./default.nix {}'

$ nix-shell -p $(readlink -f result)

$ cat <filename> | header42 <filename>
```

### **Credits**

[@zazard](https://github.com/zazard) - creator  
[@alexandregv](https://github.com/alexandregv) - contributor  
[@mjacq42](https://github.com/mjacq42) - contributor  
[@sungmcho](https://github.com/lordtomi0325) - contributor  
[@jukefr](https://github.com/jukefr) - python rewrite

### **License**

This work is published under the terms of **[42 Unlicense](https://github.com/gcamerli/42unlicense)**.
