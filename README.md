# Terminal Fun

Yes, it is terminal.

Inspired by: https://github.com/dustinkirkland/hollywood

Uses this tools:

- cmatrix https://github.com/abishekvashok/cmatrix
- asciiquarium https://github.com/nothub/asciiquarium
- pipes.sh https://github.com/pipeseroni/pipes.sh
- cbonsai https://gitlab.com/jallbrit/cbonsai
- jp2a
- cowsay
- lolcat
- cowfortune https://github.com/anthraxx/cowfortune
- lavat https://github.com/AngelJumbo/lavat


## build image

```bash
podman build --tag terminal-fun --file ./Containerfile
```

## enter container

```bash
podman run -it terminal-fun
```

## remove container and image

```bash
podman stop terminal-fun
podman rm cli
podman rmi "$(podman images terminal-fun --all --quiet)"
```

## To Do

- publish to dockerhub
- create a gif to demonstrate
- fix a jp2a display bug
- make a more serious mode