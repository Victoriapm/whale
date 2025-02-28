# Getting started

## Installation

### Mac OS

```text
brew install dataframehq/tap/whale
```

### All others

All other systems should \(a\) clone the whale repository and run \(b\)**`make && make install`** in the base directory of the repo:

```text
git clone https://github.com/dataframehq/whale.git
cd whale/
make && make install
```

The Makefile commands don't explicitly add an alias for the `whale` binary, so you'll want to add the following alias to your `.bash_profile` or `.zshrc` file.

```text
alias wh=~/.whale/bin/whale
```

This method is generally preferred for development as well, as the virtual environment is exposed and modifiable in `~/.whale/libexec/env`.

### Advanced syntax highlighting

We highly recommend installing [`bat`](https://github.com/sharkdp/bat) to enable advanced syntax highlighting \(once detected, whale will use `bat` over `cat` automatically\).

## Quick start \(local usage\)

Start by running:

```text
wh init
```

This will assist you in:

* Setting up the necessary file structure in `~/.whale`.
* Setting up your warehouse connection credentials.
* Registering a cron job in your `crontab`, so whale can periodically scrape metadata.

Once that is complete, either wait for the cron job to run, or run `wh pull &` to manually kick off a job in the background, if you're feeling impatient.

**If you instead want to use a git server like github to back your catalog, see** [**Git setup**](setup/getting-started-for-teams.md)**.**

## Basic usage

To obtain a list of available commands, run:

```text
wh -h
```

To run whale's search engine, run:

```text
wh
```

