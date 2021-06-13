# Contributing to this repository <!-- omit in toc -->

## Getting started <!-- omit in toc -->

Before you begin:
- Check out the [existing issues](https://github.com/grapeJUICE1/python-mini-projects/issues) ...

### Ready to make a change? Fork the repo

Fork using GitHub Desktop:

- [Getting started with GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop) will guide you through setting up Desktop.
- Once Desktop is set up, you can use it to [fork the repo](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop)!

Fork using the command line:

- [Fork the repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository) so that you can make your changes without affecting the original project until you're ready to merge them.

Fork with [GitHub Codespaces](https://github.com/features/codespaces):

- [Fork, edit, and preview](https://docs.github.com/en/free-pro-team@latest/github/developing-online-with-codespaces/creating-a-codespace) using [GitHub Codespaces](https://github.com/features/codespaces) without having to install and run the project locally.

### Make your update:
Make your changes to the file(s) you'd like to update.
  - Are you contributing to markdown? We use [GitHub Markdown](contributing/content-markup-reference.md).

### Open a pull request
When you're done making changes and you'd like to propose them for review, use the [pull request template](#pull-request-template) to open your PR (pull request).

### Submit your PR & get it reviewed
- Once you submit your PR, others from the Docs community will review it with you. The first thing you're going to want to do is a [self review](#self-review).
- After that, we may have questions, check back on your PR to keep up with the conversation.
- Did you have an issue, like a merge conflict? Check out  [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) on how to resolve merge conflicts and other issues.

### Your PR is merged!
Congratulations! The whole GitHub community thanks you. :sparkles:

Once your PR is merged, you will be proudly listed as a contributor in the [contributor chart](https://github.com/grapeJUICE1/python-mini-projects/graphs/contributors).

## Starting with an issue
You can browse existing issues to find something that needs help!

## Opening a pull request
You can use the GitHub user interface :pencil2: for some small changes, like fixing a typo or updating a readme. You can also fork the repo and then clone it locally, to view changes and run your tests on your machine.

### Self review
You should always review your own PR first.

For content changes, make sure that you:
- [ ] Confirm that the changes meet the user experience and goals outlined in the content design plan (if there is one).
- [ ] Compare your pull request's source changes to staging to confirm that the output matches the source and that everything is rendering as expected. This helps spot issues like typos, content that doesn't follow the style guide, or content that isn't rendering due to versioning problems. Remember that lists and tables can be tricky.
- [ ] Review the content for technical accuracy.

### Pull request template
When you open a pull request, you must fill out the "Ready for review" template before we can review your PR. This template helps reviewers understand your changes and the purpose of your pull request.

## Windows

This site can be developed on Windows, however a few potential gotchas need to be kept in mind:

1. Regular Expressions: Windows uses `\r\n` for line endings, while Unix based systems use `\n`. Therefore when working on Regular Expressions, use `\r?\n` instead of `\n` in order to support both environments. The Node.js [`os.EOL`](https://nodejs.org/api/os.html#os_os_eol) property can be used to get an OS-specific end-of-line marker.
1. Paths: Windows systems use `\` for the path separator, which would be returned by `path.join` and others. You could use `path.posix`, `path.posix.join` etc and the [slash](https://ghub.io/slash) module, if you need forward slashes - like for constructing URLs - or ensure your code works with either.
1. Bash: Not every Windows developer has a terminal that fully supports Bash, so it's generally preferred to write [scripts](/script) in JavaScript instead of Bash.
