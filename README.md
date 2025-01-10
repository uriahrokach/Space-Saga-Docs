# Space Saga Documentation

Documentation of lore and technical details in **Space Saga** LARP.
You can access the documentation [here](uriahrokach.github.io/space-saga-docs).

## Contributing

This documentation is using the [material plugin for mkdocs](https://squidfunk.github.io/mkdocs-material/)
In order to generate beautiful documentation, with some extra custom `HTML` and `CSS`. 

### Prerequisites

* docker

### Setting up a dev environment

Clone the repository:

```shell 
git clone https://github.com/uriahrokach/Space-Saga-Docs.git
```

And then run the development env with docker (in powershell/bash):

```shell
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

This should create a test environemnt which reloads automatically on port `8000`.

### Publishing your results

After you are done, commit your changes to your own repository, and open a new pull request.

Happy Hacking!
