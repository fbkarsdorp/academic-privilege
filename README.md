# Academic Privilege

[![Build Status](https://travis-ci.com/fbkarsdorp/academic-privilege.svg?token=6szGZirW7A2kgxnJVg7g&branch=master)](https://travis-ci.com/fbkarsdorp/academic-privilege)

## Description

Description of the project and this repository...

## File format

The folder `questions` contains question files in different languages (e.g.,
`questions-en.yml` for English). Files are written in YAML format (see https://yaml.org/
for detailed documentation). Each file consists of a series of questions, which should
adhere to the following schema:

``` yaml
- id: the id of the question as an integer, e.g.: 1
  question: The actual question presented to the participants
  categories: a list of categories this question belongs to, e.g., [sexuality, language, education]
  weight: a weight on a scale of 1 to 5 reflecting the importance of this question
  active: true or false
  privilege answer: yes or no
```

## Contributing

There are many ways to contribute to this project, with the most common ones being the
construction of code or adding / editing questions and documentation.

### Submitting a question or feature request

We use GitHub issues to track all questions and feature requests; feel free to open an
issue if you have a question or wish to see a question changed/added.

### Contributing or editing questions

The preferred way to contribute to this repository is to fork the repository, and
subsequently, submit a so-called "Pull Request" (PR). These are the steps to do that:

1. Create an account on GitHub (if you don't already have one);
2. Fork the project repository: click on the 'Fork' button near the top right of the
   screen. This will create a copy (a fork) of the project in your own GitHub account.
3. Create a new branch in your local copy. GitHub provides an easy way to make a new
   branch. Click on the button "Branch: master". Type the name of your new branch, e.g.,
   `feature/new-question` and create the branch.
4. In the new branch, make any changes you like. Please mind the schema outlined above
   when submitting or editing questions. When you're done, commit the changes.
5. Finally, follow
![these](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) to
create a pull request from your work. This will send a message to the maintainers of the
repository, who will review the PR. When the PR is accepted, it will be merged into the
project.

## Code of Conduct

We abide by the principles of openness, respect, and consideration of others of the ...

## Credits

