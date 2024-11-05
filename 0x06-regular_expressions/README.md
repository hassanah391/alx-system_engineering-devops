# Regular Expressions

This repository holds code that illustrates essential concepts of programming related to regular expressions.

## Resources

To learn more about regular expressions, check out these resources:

- [Rubular](http://rubular.com/)
- [Regex101](https://regex101.com/r/cO8lqs/2)
- [Blog post: Regex Tutorial - A Simple Cheatsheet by Examples](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)

## Environment

- Language: Ruby
- Operating System: Ubuntu 20.04 LTS
- Usage: Run each file with `./[filename] "pattern to test if match" | cat -e`
- Each file has the following format:

  ```ruby
  #!/usr/bin/env ruby
  puts ARGV[0].scan(/ regex here /).join
  